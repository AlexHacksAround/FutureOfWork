/* ============================================================
   The Office of 2035 — The Listening Cave
   Experience logic: landing → guided tour → free roam.
   No dependencies beyond the global `pannellum`.
   ============================================================ */
(function () {
  "use strict";

  var $ = function (id) { return document.getElementById(id); };

  var els = {
    landing: $("landing"),
    experience: $("experience"),
    enter: $("enter"),
    langLanding: $("lang-toggle"),
    langHud: $("lang-toggle-hud"),
    narration: $("narration"),
    narrationName: $("narration-name"),
    narrationText: $("narration-text"),
    narrationOk: $("narration-ok"),
    hotspotCard: $("hotspot-card"),
    hotspotTitle: $("hotspot-title"),
    hotspotBody: $("hotspot-body"),
    hotspotClose: $("hotspot-close"),
    menuToggle: $("menu-toggle"),
    sceneLabel: $("scene-label"),
    nextScene: $("next-scene"),
    soundToggle: $("sound-toggle"),
    menu: $("menu"),
    menuList: $("menu-list"),
    menuOutro: $("menu-outro")
  };

  var state = {
    lang: (navigator.language || "en").toLowerCase().indexOf("de") === 0 ? "de" : "en",
    mode: "tour",          // 'tour' | 'roam'
    index: 0,              // current scene index
    content: null,
    visited: new Set(),
    soundOn: true,
    entered: false,
    narrationVisible: false,
    openHotspot: null      // { scene: i, spot: j } while hotspot card is up
  };

  var viewer = null;
  var reducedMotion = window.matchMedia &&
    window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---------------------------------------------------------
     Audio — narration voiceover + ambience loop.
     Files may not exist yet: every failure degrades silently.
     --------------------------------------------------------- */

  var narrationAudio = new Audio();
  narrationAudio.preload = "none";
  var ambienceAudio = new Audio();
  ambienceAudio.preload = "none";
  ambienceAudio.loop = true;
  ambienceAudio.volume = 0.25;
  narrationAudio.addEventListener("error", function () { /* ignore */ });
  ambienceAudio.addEventListener("error", function () { /* ignore */ });

  function tryPlay(el) {
    var p = el.play();
    if (p && typeof p.catch === "function") p.catch(function () { /* ignore */ });
  }

  function fadeTo(el, target, done) {
    if (el._fade) clearInterval(el._fade);
    if (reducedMotion) {
      el.volume = target;
      if (done) done();
      return;
    }
    el._fade = setInterval(function () {
      var d = target - el.volume;
      if (Math.abs(d) <= 0.03) {
        el.volume = target;
        clearInterval(el._fade);
        el._fade = null;
        if (done) done();
      } else {
        el.volume = Math.min(1, Math.max(0, el.volume + (d > 0 ? 0.03 : -0.03)));
      }
    }, 50);
  }

  function stopNarrationAudio() {
    narrationAudio.pause();
    narrationAudio.removeAttribute("src");
  }

  function playNarrationAudio(scene) {
    stopNarrationAudio();
    var src = scene.audio && scene.audio.narration && scene.audio.narration[state.lang];
    if (src && state.soundOn) {
      narrationAudio.src = src;
      tryPlay(narrationAudio);
    }
  }

  function updateAmbience(scene) {
    var src = scene.audio && scene.audio.ambience;
    var abs = src ? new URL(src, window.location.href).href : "";
    if (abs && ambienceAudio.src === abs) {
      if (state.soundOn) tryPlay(ambienceAudio);
      return;
    }
    var start = function () {
      if (!abs) { ambienceAudio.pause(); ambienceAudio.removeAttribute("src"); return; }
      ambienceAudio.src = abs;
      if (state.soundOn) {
        ambienceAudio.volume = 0;
        tryPlay(ambienceAudio);
        fadeTo(ambienceAudio, 0.25);
      } else {
        ambienceAudio.volume = 0.25;
      }
    };
    if (!ambienceAudio.paused) {
      fadeTo(ambienceAudio, 0, function () { ambienceAudio.pause(); start(); });
    } else {
      start();
    }
  }

  function setSound(on) {
    state.soundOn = on;
    els.soundToggle.setAttribute("aria-pressed", String(on));
    els.soundToggle.textContent = uiString(on ? "soundOn" : "soundOff");
    if (!on) {
      narrationAudio.pause();
      ambienceAudio.pause();
    } else {
      if (narrationAudio.getAttribute("src") && !narrationAudio.ended) tryPlay(narrationAudio);
      if (ambienceAudio.getAttribute("src")) tryPlay(ambienceAudio);
    }
  }

  /* ---------------------------------------------------------
     Strings — "title", "subtitle", "thesis" live in meta,
     everything else in ui: resolve as (ui[key] ?? meta[key]).
     --------------------------------------------------------- */

  function uiString(key) {
    var c = state.content;
    if (!c) return "";
    var entry = (c.ui && c.ui[key]) || (c.meta && c.meta[key]);
    return (entry && entry[state.lang]) || "";
  }

  function scenes() { return state.content.scenes; }

  function applyLang() {
    document.documentElement.lang = state.lang;
    document.querySelectorAll("[data-ui]").forEach(function (el) {
      el.textContent = uiString(el.getAttribute("data-ui"));
    });
    var other = (state.lang === "en" ? "de" : "en").toUpperCase();
    els.langLanding.textContent = other;
    els.langHud.textContent = other;
    els.soundToggle.textContent = uiString(state.soundOn ? "soundOn" : "soundOff");
    els.menuOutro.textContent = uiString("outro");
    if (!state.content) return;
    buildMenu();
    updateHud();
    if (state.narrationVisible) renderNarration();
    if (state.openHotspot) renderHotspot();
  }

  function toggleLang() {
    state.lang = state.lang === "en" ? "de" : "en";
    // Mid-scene language switch: stop the voiceover, don't replay.
    stopNarrationAudio();
    applyLang();
  }

  /* ---------------------------------------------------------
     Cards
     --------------------------------------------------------- */

  function renderNarration() {
    var s = scenes()[state.index];
    els.narrationName.textContent = s.name[state.lang];
    els.narrationText.textContent = s.narration[state.lang];
  }

  function showNarration() {
    closeHotspot();
    renderNarration();
    els.narration.hidden = false;
    state.narrationVisible = true;
  }

  function hideNarration() {
    els.narration.hidden = true;
    state.narrationVisible = false;
  }

  function renderHotspot() {
    var h = scenes()[state.openHotspot.scene].hotspots[state.openHotspot.spot];
    els.hotspotTitle.textContent = h.title[state.lang];
    els.hotspotBody.textContent = h.body[state.lang];
  }

  function openHotspot(sceneIdx, spotIdx) {
    hideNarration(); // cards are exclusive
    state.openHotspot = { scene: sceneIdx, spot: spotIdx };
    renderHotspot();
    els.hotspotCard.hidden = false;
  }

  function closeHotspot() {
    els.hotspotCard.hidden = true;
    state.openHotspot = null;
  }

  /* ---------------------------------------------------------
     Menu (free roam)
     --------------------------------------------------------- */

  function buildMenu() {
    els.menuList.innerHTML = "";
    scenes().forEach(function (s, i) {
      var li = document.createElement("li");
      var b = document.createElement("button");
      b.type = "button";
      b.setAttribute("data-scene", String(i));
      b.textContent = s.name[state.lang];
      li.appendChild(b);
      els.menuList.appendChild(li);
    });
  }

  function openMenu(withOutro) {
    els.menuOutro.hidden = !withOutro;
    els.menu.hidden = false;
    els.menuToggle.setAttribute("aria-expanded", "true");
  }

  function closeMenu() {
    els.menu.hidden = true;
    els.menuToggle.setAttribute("aria-expanded", "false");
  }

  function toggleMenu() {
    if (els.menu.hidden) openMenu(false);
    else closeMenu();
  }

  /* ---------------------------------------------------------
     Scenes
     --------------------------------------------------------- */

  function updateHud() {
    if (!state.content) return;
    var list = scenes();
    var s = list[state.index];
    els.sceneLabel.textContent =
      (state.index + 1) + " / " + list.length + " · " + s.name[state.lang];
    els.nextScene.textContent =
      uiString(state.index === list.length - 1 ? "finish" : "continue");
  }

  function showScene(i) {
    var list = scenes();
    if (i < 0 || i >= list.length) return;
    state.index = i;
    var scene = list[i];
    if (viewer && viewer.getScene() !== scene.id) viewer.loadScene(scene.id);
    closeHotspot();
    if (!state.visited.has(scene.id)) {
      // First visit: narration card + voiceover. Revisits (free roam)
      // never auto-show the narration again.
      state.visited.add(scene.id);
      showNarration();
      playNarrationAudio(scene);
    } else {
      hideNarration();
      stopNarrationAudio();
    }
    updateAmbience(scene);
    updateHud();
  }

  function onContinue() {
    if (!state.entered || !els.menu.hidden) return;
    if (state.index >= scenes().length - 1) {
      // Finish: open the menu with the closing line.
      hideNarration();
      closeHotspot();
      openMenu(true);
    } else {
      showScene(state.index + 1);
    }
  }

  /* ---------------------------------------------------------
     Pannellum
     --------------------------------------------------------- */

  function initViewer() {
    var sceneConfigs = {};
    scenes().forEach(function (s, i) {
      sceneConfigs[s.id] = {
        type: "equirectangular",
        panorama: s.pano,
        preview: s.preview,
        hotSpots: s.hotspots.map(function (h, j) {
          return {
            pitch: h.pitch,
            yaw: h.yaw,
            cssClass: "hotspot-ember", // tooltip-less ember dot; the card carries the text
            clickHandlerFunc: function (e, args) { openHotspot(args.scene, args.spot); },
            clickHandlerArgs: { scene: i, spot: j }
          };
        })
      };
    });
    viewer = window.pannellum.viewer("viewer", {
      "default": {
        firstScene: scenes()[0].id,
        sceneFadeDuration: 800,
        autoLoad: true,
        autoRotate: reducedMotion ? 0 : -2, // slow pan; Pannellum stops it on drag
        hfov: 100,
        compass: false
      },
      scenes: sceneConfigs
    });
  }

  /* ---------------------------------------------------------
     Wiring
     --------------------------------------------------------- */

  function enterExperience() {
    if (state.entered) return;
    state.entered = true;
    els.landing.hidden = true;
    els.experience.hidden = false;
    initViewer(); // init after the container is visible so it sizes correctly
    showScene(0);
  }

  function wireEvents() {
    els.enter.addEventListener("click", enterExperience);
    els.langLanding.addEventListener("click", toggleLang);
    els.langHud.addEventListener("click", toggleLang);
    els.narrationOk.addEventListener("click", hideNarration);
    els.hotspotClose.addEventListener("click", closeHotspot);
    els.nextScene.addEventListener("click", onContinue);
    els.menuToggle.addEventListener("click", toggleMenu);
    els.soundToggle.addEventListener("click", function () { setSound(!state.soundOn); });

    // Menu: scene entries jump; anywhere else on the overlay closes it.
    els.menu.addEventListener("click", function (e) {
      var btn = e.target.closest ? e.target.closest("#menu-list button") : null;
      if (btn) {
        state.mode = "roam";
        closeMenu();
        showScene(Number(btn.getAttribute("data-scene")));
      } else {
        closeMenu();
      }
    });

    document.addEventListener("keydown", function (e) {
      if (!state.entered || els.experience.hidden) return;
      if (e.defaultPrevented) return; // e.g. Pannellum panning with arrow keys
      if (e.key === "Escape") {
        if (!els.menu.hidden) closeMenu();
        else { closeHotspot(); hideNarration(); }
      } else if (e.key === "m" || e.key === "M") {
        toggleMenu();
      } else if (e.key === "ArrowRight" || e.key === " ") {
        // Let a focused button keep its native Space behavior.
        if (e.key === " " && e.target && e.target.tagName === "BUTTON") return;
        e.preventDefault();
        onContinue();
      }
    });
  }

  fetch("content.json")
    .then(function (r) {
      if (!r.ok) throw new Error("content.json: HTTP " + r.status);
      return r.json();
    })
    .then(function (content) {
      state.content = content;
      wireEvents();
      applyLang();
    })
    .catch(function (err) {
      console.error("The Listening Cave could not load its content:", err);
    });
}());
