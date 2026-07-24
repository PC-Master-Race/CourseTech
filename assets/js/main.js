/* Tutorial Hub — interaction: accessible mega menu, scroll reveal, TOC highlight */
(function () {
  "use strict";
  var isDesktop = function () { return window.matchMedia("(min-width: 960px)").matches; };

  /* ---------- Mega menu ---------- */
  var toggle = document.getElementById("megaToggle");
  var panel = document.getElementById("megaPanel");
  var overlay = document.getElementById("megaOverlay");

  if (toggle && panel) {
    var open = function () {
      panel.hidden = false;
      if (overlay) { overlay.hidden = false; }
      // allow the browser to register the un-hide before animating
      requestAnimationFrame(function () {
        panel.setAttribute("data-open", "true");
        if (overlay) { overlay.setAttribute("data-open", "true"); }
      });
      toggle.setAttribute("aria-expanded", "true");
      document.addEventListener("keydown", onKey);
      document.addEventListener("click", onOutside, true);
    };
    var close = function (returnFocus) {
      panel.setAttribute("data-open", "false");
      if (overlay) { overlay.setAttribute("data-open", "false"); }
      toggle.setAttribute("aria-expanded", "false");
      document.removeEventListener("keydown", onKey);
      document.removeEventListener("click", onOutside, true);
      var done = function () {
        panel.hidden = true;
        if (overlay) { overlay.hidden = true; }
        panel.removeEventListener("transitionend", done);
      };
      if (isDesktop()) { panel.addEventListener("transitionend", done); }
      else { panel.hidden = true; if (overlay) { overlay.hidden = true; } }
      if (returnFocus) { toggle.focus(); }
    };
    var onKey = function (e) {
      if (e.key === "Escape") { close(true); }
    };
    var onOutside = function (e) {
      if (!panel.contains(e.target) && !toggle.contains(e.target)) { close(false); }
    };
    toggle.addEventListener("click", function () {
      if (toggle.getAttribute("aria-expanded") === "true") { close(false); } else { open(); }
    });
    if (overlay) { overlay.addEventListener("click", function () { close(false); }); }

    // First link inside panel gets focus for keyboard users when opened via keyboard.
    toggle.addEventListener("keyup", function (e) {
      if ((e.key === "Enter" || e.key === " ") && toggle.getAttribute("aria-expanded") === "true") {
        var first = panel.querySelector("a.mega__link");
        if (first) { first.focus(); }
      }
    });
    // Reset state on resize between desktop/mobile.
    window.addEventListener("resize", function () {
      if (!isDesktop()) { panel.hidden = false; }
    });
  }

  /* ---------- Scroll reveal ---------- */
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var revealEls = document.querySelectorAll(".reveal");
  if (reduce || !("IntersectionObserver" in window)) {
    revealEls.forEach(function (el) { el.classList.add("is-in"); });
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add("is-in"); io.unobserve(en.target); }
      });
    }, { threshold: 0.12, rootMargin: "0px 0px -8% 0px" });
    revealEls.forEach(function (el) { io.observe(el); });
  }

  /* ---------- TOC active state ---------- */
  var tocLinks = Array.prototype.slice.call(document.querySelectorAll(".toc a[href^='#']"));
  if (tocLinks.length && "IntersectionObserver" in window) {
    var map = {};
    tocLinks.forEach(function (l) {
      var id = l.getAttribute("href").slice(1);
      var sec = document.getElementById(id);
      if (sec) { map[id] = l; }
    });
    var spy = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) {
          tocLinks.forEach(function (l) { l.classList.remove("is-active"); l.removeAttribute("aria-current"); });
          var active = map[en.target.id];
          if (active) { active.classList.add("is-active"); active.setAttribute("aria-current", "true"); }
        }
      });
    }, { rootMargin: "-30% 0px -60% 0px", threshold: 0 });
    Object.keys(map).forEach(function (id) { spy.observe(document.getElementById(id)); });
  }
})();
