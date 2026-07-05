#!/usr/bin/env python3
"""Generate narration voiceovers for the Office of the Future walkthrough.

Reads scene narrations (en + de) from site/content.json and synthesizes one
MP3 per scene per language via the ElevenLabs text-to-speech API, writing to
the exact paths referenced by each scene's audio.narration entry
(site/audio/<scene-id>-<lang>.mp3).

Key resolution: ELEVENLABS_API_KEY env var, else /home/af/api_keys/11labs.
The key is only ever sent as the xi-api-key header — never printed or logged.

Usage:
    python3 tools/make_voiceovers.py            # all scenes, both languages
    python3 tools/make_voiceovers.py --only den # a single scene, both languages
"""

import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.request

# Voice: "George" — ElevenLabs premade narrative voice. Warm, calm, middle-aged
# British narrator with a documentary register; renders cleanly in both English
# and German under eleven_multilingual_v2. (The provided key lacks the
# voices_read permission, so this premade ID is pinned rather than discovered
# via GET /v1/voices.)
VOICE_ID = "JBFqnCBsd6RMkjVDRZzb"

MODEL_ID = "eleven_multilingual_v2"
VOICE_SETTINGS = {
    "stability": 0.55,
    "similarity_boost": 0.75,
    "style": 0.2,
}

API_URL = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
KEY_FILE = "/home/af/api_keys/11labs"
LANGUAGES = ("en", "de")

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE_DIR = os.path.join(REPO_ROOT, "site")
CONTENT_JSON = os.path.join(SITE_DIR, "content.json")


def resolve_api_key():
    key = os.environ.get("ELEVENLABS_API_KEY", "").strip()
    if key:
        return key
    try:
        with open(KEY_FILE, encoding="utf-8") as f:
            key = f.read().strip()
        if key:
            return key
    except OSError:
        pass
    return None


def synthesize(api_key, text, out_path):
    """POST one TTS request; write MP3 to out_path. Returns True on success."""
    payload = json.dumps(
        {
            "text": text,
            "model_id": MODEL_ID,
            "voice_settings": VOICE_SETTINGS,
        }
    ).encode("utf-8")
    req = urllib.request.Request(
        API_URL,
        data=payload,
        headers={
            "xi-api-key": api_key,
            "Content-Type": "application/json",
            "Accept": "audio/mpeg",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            audio = resp.read()
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        print(f"  ERROR: HTTP {e.code} for {out_path}\n  {body}", file=sys.stderr)
        return False
    except urllib.error.URLError as e:
        print(f"  ERROR: request failed for {out_path}: {e.reason}", file=sys.stderr)
        return False

    with open(out_path, "wb") as f:
        f.write(audio)
    print(f"  wrote {out_path} ({len(audio):,} bytes)")
    return True


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--only", metavar="SCENE_ID", help="generate clips for a single scene id")
    args = parser.parse_args()

    api_key = resolve_api_key()
    if not api_key:
        print(
            "No ElevenLabs API key found — nothing generated (this is not an error).\n"
            "Provide a key one of two ways, then re-run this script:\n"
            "  1. export ELEVENLABS_API_KEY=<your key>\n"
            f"  2. put the key (one line) in {KEY_FILE}\n"
        )
        return 0

    with open(CONTENT_JSON, encoding="utf-8") as f:
        content = json.load(f)

    scenes = content["scenes"]
    if args.only:
        scenes = [s for s in scenes if s["id"] == args.only]
        if not scenes:
            known = ", ".join(s["id"] for s in content["scenes"])
            print(f"Unknown scene id {args.only!r}. Known: {known}", file=sys.stderr)
            return 1

    # Build the clip list from the audio.narration paths in content.json so the
    # files land exactly where the site expects them.
    clips = []  # (scene_id, lang, text, absolute output path)
    for scene in scenes:
        narration_paths = scene["audio"]["narration"]
        narration_text = scene["narration"]
        for lang in LANGUAGES:
            rel = narration_paths[lang]  # e.g. "audio/approach-en.mp3"
            clips.append((scene["id"], lang, narration_text[lang], os.path.join(SITE_DIR, rel)))

    os.makedirs(os.path.join(SITE_DIR, "audio"), exist_ok=True)

    failures = 0
    for i, (scene_id, lang, text, out_path) in enumerate(clips):
        print(f"[{i + 1}/{len(clips)}] {scene_id} ({lang}) — {len(text)} chars")
        if not synthesize(api_key, text, out_path):
            failures += 1
        if i < len(clips) - 1:
            time.sleep(0.5)  # rate-limit courtesy

    if failures:
        print(f"\n{failures} of {len(clips)} clips failed.", file=sys.stderr)
        return 1
    print(f"\nAll {len(clips)} clips generated.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
