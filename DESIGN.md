# DESIGN.md — Tutorial Hub Design System

This is the single source of truth for how the site looks and behaves. Every new
topic page and every future build session should pull from these tokens instead
of inventing new values, so the site stays consistent as it grows. When you make
a notable design decision, record it here.

Format is inspired by Google's DESIGN.md / DTCG token spec: named tokens, grouped,
with the concrete value and (where relevant) the WCAG contrast note.

---

## 1. Design principles

1. **Well-funded edtech, not a school handout.** Closer to Stripe / Linear / Notion /
   DeepLearning.AI than a Bootstrap template. Real type hierarchy, real color system,
   generous whitespace, purposeful motion.
2. **Accessibility is a feature, not a checkbox.** WCAG 2.1 AA minimum. Large base
   font for older adults. Full keyboard operation, including the mega menu. Never rely
   on color alone — pair it with a label and an icon.
3. **Calm, not busy.** Motion is subtle and fast. Nothing blinks, bounces, or slows a
   page down. All motion is disabled under `prefers-reduced-motion`.
4. **Scales by data, not by code.** Navigation is driven by `_data/topics.yml`. Page
   content is driven by front matter in `_topics/*.md`. Adding a topic is a content
   change, editable from the `/admin` CMS.

---

## 2. Color tokens

All foreground/background pairs below meet or exceed WCAG AA (4.5:1 for body text,
3:1 for large text and UI borders). Contrast ratios are noted against the surface
they sit on.

### Brand & neutrals
| Token | Value | Notes |
|---|---|---|
| `--ink` | `#1a1d29` | Primary text on white. Contrast 15.8:1. |
| `--ink-soft` | `#4a4f60` | Secondary text on white. Contrast 8.0:1. |
| `--ink-faint` | `#6b7280` | Muted captions on white. Contrast 5.1:1. |
| `--surface` | `#ffffff` | Page background / cards. |
| `--surface-alt` | `#f6f7fb` | Section bands, subtle panels. |
| `--surface-sunken` | `#eef0f7` | Insets, code, footer top. |
| `--border` | `#e2e5ef` | Hairlines, card outlines. |
| `--border-strong` | `#c9cede` | Stronger dividers, focus rings on light. |

### Primary (interactive)
| Token | Value | Notes |
|---|---|---|
| `--brand` | `#4338ca` | Indigo-700. Links/buttons on white. Contrast 8.3:1. |
| `--brand-hover` | `#372fb0` | Hover/active. |
| `--brand-tint` | `#eef0ff` | Soft brand background. |
| `--brand-ink` | `#312a94` | Brand text on `--brand-tint`. Contrast 8.6:1. |

### Accent (delight, used sparingly)
| Token | Value | Notes |
|---|---|---|
| `--accent` | `#e0611a` | Warm coral-amber. Hero underline, highlights. Large text only. |
| `--accent-ink` | `#9a3d0c` | Coral text on white for small text. Contrast 5.9:1. |

### Content-block system (Section 5 of the brief)
Each block type is distinguished by **color + label + icon**, never color alone.

| Type | `--*-tint` (bg) | `--*-accent` (bar/icon) | `--*-ink` (label text on tint) | Icon | Label |
|---|---|---|---|---|---|
| Lesson | `#eef3ff` | `#1d4ed8` (blue-700) | `#1a3a8f` (7.6:1) | book | "Lesson" |
| Activity | `#e9f9f0` | `#047857` (emerald-700) | `#0a5a3f` (6.9:1) | pencil/hand | "Activity — try it" |
| Quiz | `#f4efff` | `#6d28d9` (violet-700) | `#4a1f9e` (8.1:1) | check-badge | "Check your understanding" |

### Status / feedback
| Token | Value | Notes |
|---|---|---|
| `--focus` | `#1d4ed8` | 3px focus ring, 2px offset. Contrast vs white 6.3:1. |
| `--success` | `#047857` | |
| `--warn-ink` | `#8a5a00` | Amber note text on white, 4.9:1. |

---

## 3. Typography

- **Display / headings:** `Fraunces` (variable serif, optical size, a little character).
  Used for the wordmark, hero, and page/section titles (`h1`, `.section-title`).
- **UI / body:** `Inter`. Used for `h2`–`h6`, body copy, nav, buttons, tables.
- **Mono:** `ui-monospace, "SF Mono", Menlo, Consolas, monospace` for prompt examples.

Fonts load from Google Fonts with `display=swap`; system fallbacks are declared so
text is readable before fonts arrive.

### Scale (base 18px for readability by older adults)
| Token | Size | Line height | Use |
|---|---|---|---|
| `--fs-hero` | clamp(2.6rem, 5vw, 4rem) | 1.05 | Home hero |
| `--fs-h1` | clamp(2.1rem, 3.5vw, 3rem) | 1.1 | Page title |
| `--fs-h2` | 1.7rem | 1.2 | Part titles |
| `--fs-h3` | 1.3rem | 1.3 | Block titles |
| `--fs-body` | 1.125rem (18px) | 1.7 | Body copy |
| `--fs-lead` | 1.3rem | 1.6 | Intro / lead |
| `--fs-small` | 1rem | 1.6 | Captions, meta |

Body copy max width ~68ch for comfortable reading.

---

## 4. Spacing, radius, shadow

- **Space scale (4px base):** `--s-1` 4, `--s-2` 8, `--s-3` 12, `--s-4` 16, `--s-5` 24,
  `--s-6` 32, `--s-7` 48, `--s-8` 64, `--s-9` 96.
- **Radius:** `--r-sm` 8px (buttons, tags), `--r-md` 14px (cards, blocks), `--r-lg` 22px
  (hero, feature panels), `--r-pill` 999px.
- **Shadow:** `--shadow-sm` soft 1px/2px; `--shadow-md` layered card lift;
  `--shadow-lg` mega-menu / hover lift. All low-opacity, cool-gray, never harsh black.

---

## 5. Motion

- Duration: `--t-fast` 140ms, `--t` 200ms, `--t-slow` 320ms. Easing `cubic-bezier(.2,.6,.2,1)`.
- Hover: cards and buttons lift 2px + shadow step. Links get an animated underline.
- Mega menu: fade + 6px slide-down on open.
- Scroll reveal: sections fade/rise in via IntersectionObserver.
- **All of the above collapse to no motion under `prefers-reduced-motion: reduce`.**

---

## 6. Components (canonical patterns)

- **Buttons:** `.btn` (primary, filled brand), `.btn--ghost` (outline), `.btn--quiz`
  (violet, opens in new tab with an external-link icon + "opens in a new tab" for SR).
- **Content block:** `.block.block--lesson|activity|quiz` — colored left bar, tint
  background, an icon chip, and a visible text label. Renders markdown body via
  `markdownify`.
- **Cards:** `.topic-card` used on home and category listings.
- **Tables:** full-width, zebra-free, strong header row, generous cell padding.
- **Mega menu:** `<button aria-expanded aria-controls>` toggles a `role="region"`
  full-width panel grouped by category. Esc closes and returns focus to the button.

---

## 7. Layout / breakpoints

- Content container max-width 1140px, gutter 24px (20px on small screens).
- Reading column (topic body) max-width 760px.
- Breakpoints: `>=960px` desktop mega menu; `<960px` collapses to an accessible
  disclosure list.

---

## 8. Decisions log

- **2026-07: Topic catalog & order.** Three categories to start: *AI at Work*,
  *Everyday Software* (Excel), *Devices & Digital Life* (mobile, Windows basics).
  Order set in `_data/topics.yml`. ~17 topics expected over time; the data file and
  CMS scale to more without template changes.
- **2026-07: Block palette.** Lesson = blue, Activity = green, Quiz = violet, each with
  icon + text label so meaning never depends on color (Section 4).
- **2026-07: Mega menu = flat topic list grouped by category** (no third-level
  sub-categories yet). Revisit if any category exceeds ~8 topics.
- **2026-07: Hosting.** Default `github.io` project URL (`/CourseTech/`) via
  `baseurl`. Swap to a custom domain later by setting `url`/`baseurl` and adding a
  `CNAME` file.
- **2026-07: Fonts.** Fraunces (display) + Inter (UI). Base body 18px.
