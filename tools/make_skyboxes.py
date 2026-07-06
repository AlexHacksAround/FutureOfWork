#!/usr/bin/env python3
"""Generate the five 360-degree scene panoramas via the Blockade Labs Skybox API.

Reads the Main/Negative prompt pairs from panoramas/prompts.md, submits each
scene to POST /skybox, polls GET /imagine/requests/{id} until complete, and
writes the equirectangular result to site/panos/<id>.jpg (converting PNG to
JPG and recompressing to stay under ~2.5 MB while preserving resolution).

Credentials: /home/af/api_keys/skybox, a text file with "key:" and "secret:"
lines. The key is only ever sent as the x-api-key header — never printed or
logged. If the file is missing, the script prints instructions and exits 0.

Usage:
    python3 tools/make_skyboxes.py                 # all five scenes
    python3 tools/make_skyboxes.py --only den      # a single scene
    python3 tools/make_skyboxes.py --list-styles   # print styles, no generation
    python3 tools/make_skyboxes.py --style-id 112  # override the default style
"""

import argparse
import io
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request

API_BASE = "https://backend.blockadelabs.com/api/v1"
CREDS_FILE = "/home/af/api_keys/skybox"

# Default style: 67 "M3 Photoreal" (Model 3). Chosen from the live
# GET /skybox/styles list as the most photorealistic Model 3 option for
# interiors: its description is "Photographic realism with a high degree of
# flexibility and good visual fidelity", it is non-premium/non-experimental,
# and it accepts our full prompts (600-char main / 410-char negative limits).
# The alternatives lose out: "M3 Cinematic Realism" (102) bakes in dark filmic
# grading that fights the warm-daylight brief, "M3 UHD Render" (68) and
# "M3 Detailed Render" (147) are CGI-render looks rather than photographic,
# and the Model 2 "Interiors"/"Realism" presets are older-generation. For
# maximum manual control there is "M3 Advanced (photo/render)" (112) via
# --style-id.
DEFAULT_STYLE_ID = 67

SCENE_IDS = ("approach", "hearth", "painted-wall", "den", "loom")
POLL_INTERVAL = 4.0  # seconds between GET /imagine/requests/{id} polls
POLL_TIMEOUT = 300.0  # give up on a scene after 5 minutes
TARGET_BYTES = int(2.5 * 1024 * 1024)  # resave at quality=82 above this
FAILED_STATUSES = {"error", "abort", "failed"}

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROMPTS_MD = os.path.join(REPO_ROOT, "panoramas", "prompts.md")
PANOS_DIR = os.path.join(REPO_ROOT, "site", "panos")


def load_credentials():
    """Parse key:/secret: lines. Returns dict or None if the file is missing."""
    try:
        with open(CREDS_FILE, encoding="utf-8") as f:
            lines = f.read().splitlines()
    except OSError:
        return None
    creds = {}
    for line in lines:
        if ":" in line:
            name, value = line.split(":", 1)
            creds[name.strip().lower()] = value.strip()
    if not creds.get("key"):
        return None
    return creds


def parse_prompts(path):
    """Extract {scene_id: (main, negative)} from the prompts.md blockquotes.

    Each scene section starts with "## N. The <Name>" and contains
    "**Main prompt:**" and "**Negative prompt:**" headings, each followed by
    a Markdown blockquote (consecutive "> " lines) holding the prompt text.
    """
    with open(path, encoding="utf-8") as f:
        text = f.read()

    scenes = {}
    # heading may carry a parenthesized role suffix, e.g. "## 2. The Hearth (Interaction room)"
    section_re = re.compile(r"^## \d+\. The (.+?)(?:\s*\(.*\))?\s*$", re.MULTILINE)
    matches = list(section_re.finditer(text))
    for i, m in enumerate(matches):
        body = text[m.end(): matches[i + 1].start() if i + 1 < len(matches) else len(text)]
        scene_id = m.group(1).strip().lower().replace(" ", "-")

        def blockquote_after(heading):
            hm = re.search(re.escape(heading), body)
            if not hm:
                return None
            lines = []
            for line in body[hm.end():].splitlines():
                stripped = line.strip()
                if stripped.startswith(">"):
                    lines.append(stripped.lstrip("> ").strip())
                elif lines and stripped == "":
                    break  # blank line ends the blockquote once it has begun
                elif lines:
                    break
            joined = " ".join(l for l in lines if l)
            return re.sub(r"\s+", " ", joined).strip() or None

        main = blockquote_after("**Main prompt:**")
        negative = blockquote_after("**Negative prompt:**")
        if main and negative:
            scenes[scene_id] = (main, negative)
    return scenes


def api_request(api_key, method, path, payload=None):
    """One JSON API call. Returns (data, None) or (None, 'status body') on error."""
    data = json.dumps(payload).encode("utf-8") if payload is not None else None
    req = urllib.request.Request(
        API_BASE + path,
        data=data,
        headers={
            "x-api-key": api_key,
            "Content-Type": "application/json",
            "Accept": "application/json",
        },
        method=method,
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            return json.loads(resp.read().decode("utf-8")), None
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        return None, f"HTTP {e.code}: {body[:1000]}"
    except (urllib.error.URLError, OSError, ValueError) as e:
        return None, f"request failed: {e!r}"


def fetch_styles(api_key):
    styles, err = api_request(api_key, "GET", "/skybox/styles")
    if err:
        print(f"ERROR fetching styles: {err}", file=sys.stderr)
        return None
    return styles


def print_styles_table(styles):
    print(f"{'id':>5}  {'model':<8} {'max-char':>8} {'neg-max':>7}  name")
    for s in styles:
        print(f"{s['id']:>5}  {s.get('model', '?'):<8} {s.get('max-char', '?'):>8} "
              f"{s.get('negative-text-max-char', '?'):>7}  {s['name']}")


def truncate(text, limit, label):
    if limit and len(text) > limit:
        cut = text[:limit].rsplit(",", 1)[0].rstrip(", ")
        print(f"  note: {label} truncated {len(text)} -> {len(cut)} chars (style limit {limit})")
        return cut
    return text


def unwrap_imagine(data):
    """Poll responses arrive as {"request": {...}}; POST /skybox returns the
    object directly. Accept both."""
    if isinstance(data, dict) and isinstance(data.get("request"), dict):
        return data["request"]
    return data


def generate_scene(api_key, scene_id, main, negative, style):
    """Generate one scene and write site/panos/<id>.jpg. Returns True on success."""
    main = truncate(main, style.get("max-char"), "main prompt")
    negative = truncate(negative, style.get("negative-text-max-char"), "negative prompt")

    payload = {
        "prompt": main,
        "negative_text": negative,
        "skybox_style_id": style["id"],
    }
    data, err = api_request(api_key, "POST", "/skybox", payload)
    if err:
        print(f"  ERROR submitting {scene_id}: {err}", file=sys.stderr)
        return False
    data = unwrap_imagine(data)
    request_id = data.get("id")
    if request_id is None:
        print(f"  ERROR: no request id in response: {json.dumps(data)[:500]}", file=sys.stderr)
        return False
    print(f"  request id {request_id} (status: {data.get('status')})")

    deadline = time.monotonic() + POLL_TIMEOUT
    file_url = None
    while True:
        status = data.get("status")
        if status == "complete":
            file_url = data.get("file_url")
            break
        if status in FAILED_STATUSES:
            print(f"  ERROR: generation {status}: {data.get('error_message')}", file=sys.stderr)
            return False
        if time.monotonic() > deadline:
            print(f"  ERROR: timed out after {POLL_TIMEOUT:.0f}s (last status: {status})",
                  file=sys.stderr)
            return False
        time.sleep(POLL_INTERVAL)
        data, err = api_request(api_key, "GET", f"/imagine/requests/{request_id}")
        if err:
            print(f"  ERROR polling {scene_id}: {err}", file=sys.stderr)
            return False
        data = unwrap_imagine(data)

    if not file_url:
        print(f"  ERROR: complete but no file_url: {json.dumps(data)[:500]}", file=sys.stderr)
        return False

    try:
        with urllib.request.urlopen(file_url, timeout=120) as resp:
            raw = resp.read()
    except (urllib.error.URLError, OSError) as e:
        print(f"  ERROR downloading {scene_id}: {e!r}", file=sys.stderr)
        return False

    out_path = os.path.join(PANOS_DIR, f"{scene_id}.jpg")
    try:
        from PIL import Image
        img = Image.open(io.BytesIO(raw))
        width, height = img.size
        if img.format == "JPEG" and len(raw) <= TARGET_BYTES:
            with open(out_path, "wb") as f:
                f.write(raw)
        else:
            # PNG -> JPG conversion and/or recompression; keep full resolution.
            img.convert("RGB").save(out_path, "JPEG", quality=82, optimize=True)
    except Exception as e:
        print(f"  ERROR processing image for {scene_id}: {e!r}", file=sys.stderr)
        return False

    size = os.path.getsize(out_path)
    print(f"  wrote {out_path}: {width}x{height}, {size:,} bytes")
    return True


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0],
                                     allow_abbrev=False)
    parser.add_argument("--list-styles", action="store_true",
                        help="print the styles table and exit (no generation)")
    parser.add_argument("--style-id", type=int, default=DEFAULT_STYLE_ID,
                        help=f"skybox style id (default {DEFAULT_STYLE_ID}: M3 Photoreal)")
    parser.add_argument("--only", metavar="SCENE_ID", choices=SCENE_IDS,
                        help=f"generate a single scene ({', '.join(SCENE_IDS)})")
    args = parser.parse_args()

    creds = load_credentials()
    if creds is None:
        print(
            "No Blockade Labs credentials found — nothing generated (not an error).\n"
            f"Put them in {CREDS_FILE} as two lines, then re-run this script:\n"
            "  key: <your api key>\n"
            "  secret: <your api secret>\n"
        )
        return 0
    api_key = creds["key"]

    styles = fetch_styles(api_key)
    if styles is None:
        return 1

    if args.list_styles:
        print_styles_table(styles)
        return 0

    style = next((s for s in styles if s["id"] == args.style_id), None)
    if style is None:
        print(f"Unknown style id {args.style_id}; see --list-styles.", file=sys.stderr)
        return 1
    print(f"Style: {style['id']} \"{style['name']}\" ({style.get('model')})")

    prompts = parse_prompts(PROMPTS_MD)
    missing = [s for s in SCENE_IDS if s not in prompts]
    if missing:
        print(f"ERROR: prompts not found in {PROMPTS_MD} for: {', '.join(missing)}",
              file=sys.stderr)
        return 1

    scene_ids = [args.only] if args.only else list(SCENE_IDS)
    os.makedirs(PANOS_DIR, exist_ok=True)

    failures = 0
    for i, scene_id in enumerate(scene_ids):
        main_prompt, negative_prompt = prompts[scene_id]
        print(f"[{i + 1}/{len(scene_ids)}] {scene_id} "
              f"(main {len(main_prompt)} chars, negative {len(negative_prompt)} chars)")
        if not generate_scene(api_key, scene_id, main_prompt, negative_prompt, style):
            failures += 1

    if failures:
        print(f"\n{failures} of {len(scene_ids)} scenes failed.", file=sys.stderr)
        return 1
    print(f"\nAll {len(scene_ids)} scenes generated.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
