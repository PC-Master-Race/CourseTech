# Build Prompt: Student Tutorial Hub (Mega Menu Edition)

Paste this whole document into a fresh Claude Code session (Opus 4.8 or similar) to kick off the build. It is written so the building AI can act on it directly.

---

**Important, read this first:** I am stepping away after handing you this prompt. You will be making every remaining decision on this project without me checking in along the way, I'll only be providing source content as I have it. That does not lower the bar, it raises it. This site cannot look mediocre, unfinished, or like a default AI-generated template. It has to look genuinely professional and modern (Section 3), stay fully accessible (Section 4), and every page's content has to be formatted cleanly, consistently, and readably (Section 6). If you're ever choosing between shipping something fast and shipping something polished, choose polished.

---

## 0. Before you start

If you are running in Claude Code and have plugin install access, check for and install these skills first, then use them for this project:

- `humanizer` (github.com/blader/humanizer): strips AI-writing tells from generated copy. Run page text through this before finalizing.
- `claude-design`: governs the design process itself (scoping the brief, gathering context, producing variants, verifying a local HTML artifact, avoiding generic AI-design slop). Use this to drive the initial visual design pass.
- `popular-web-designs`: 54 ready-to-paste design systems (exact colors, typography, components, CSS values) for real sites like Stripe, Linear, Vercel, Notion, Airbnb. Pair with `claude-design` if I ask for a look styled after one of those.
- `design-md`: Google's DESIGN.md spec format for authoring a formal, persistent, machine-readable design-token file (colors, type, spacing, WCAG contrast checking, Tailwind/DTCG export) that lives in the repo. Since this site will keep growing with new topic pages over a long period, set one up early so every future page pulls from the same token file instead of drifting.

Typical composition: `claude-design` drives the process and taste, `popular-web-designs` supplies the visual vocabulary if I want a known-brand look, and `design-md` is where the resulting decisions get written down as a persistent spec other build sessions can consume later.

If these are not available in this environment, follow Sections 3 and 6 below as a manual substitute for what they'd otherwise provide. Do not tell me you used a skill you did not actually load.

I will not be available to answer questions once the build starts. Where this prompt leaves something ambiguous, make the call yourself using the judgment of a senior product designer and engineer, and default to the higher-quality option whenever you're unsure. Document notable decisions (e.g. in the DESIGN.md file above) so the site stays consistent as you build out more of it.

---

## 1. What this project is

I am an adjunct technology instructor teaching vocational re-entry courses (Excel, basic computing, mobile tech, AI for the workplace). I am building a standalone website to hold all of my own instructional content, separate from my school's Canvas LMS. Canvas pages will link out to or embed this site, but the content itself needs to stay mine.

This is a **new, standalone repository**, separate from any other GitHub Pages project I have. Set it up as its own GitHub Pages site from scratch.

Audience: adult students, many with little to no computer background. Some are older adults, some have disabilities. Assume near-zero technical literacy when writing content, and design for accessibility from the start.

---

## 2. Tech stack

- Static site, hosted on GitHub Pages, built with Jekyll (same general approach I've used before: a single YAML data file driving navigation, e.g. `_data/topics.yml`, so adding a topic is a data change, not a template rewrite)
- No server-side backend, since GitHub Pages does not run one
- Content authored in Markdown with front matter, one file per topic page (or per part, if a topic has multiple parts, see Section 5)

### Editing mechanism

Wire up **Decap CMS** (formerly Netlify CMS) as an admin panel:
- Accessible at `/admin` on the deployed site
- Authenticated via GitHub (I'll use my own GitHub login, no separate user system needed)
- Configured so I can, through a form-based UI: edit page text, reorder/add sections within a topic, upload and add images (with a required alt-text field, do not let an image be saved without one), add or change the YouTube video embed URL for a page, and add new topics or parts
- All edits commit directly to this repo, no separate database

Set up the `config.yml` for Decap CMS with clear, labeled fields matching the page structure in Section 5, not a raw Markdown textbox, so I don't need to hand-edit YAML front matter to make routine changes.

---

## 3. Visual design direction

Goal: modern, polished, and a little bit delightful, the opposite of a generic AI-generated template or a plain "student built this in an afternoon" site. Look and feel should be closer to a well-funded edtech product than a school handout.

Reference points: pull visual language from real, well-designed modern sites (clean SaaS/product sites like Stripe, Linear, Notion, or well-designed learning platforms like DeepLearning.AI) rather than defaulting to generic Bootstrap-looking components. If you have the `popular-web-designs` skill loaded, use it here.

Concretely:
- Real typographic hierarchy, not just bigger/bolder headings. A distinctive display font for headlines is welcome.
- Subtle, purposeful motion: hover states, menu transitions, scroll-triggered reveals. Nothing gimmicky or distracting, and nothing that meaningfully slows the page down.
- Generous whitespace, a real color system (not just blue links and black text), and consistent spacing/rhythm across pages.
- Avoid: default form-builder aesthetics, stock "AI app" gradients-and-glassmorphism-everywhere clichés, cookie-cutter card grids with no visual identity.

### Mega menu

Model the primary navigation on GCF LearnFree's mega menu: a top nav item that expands into a full-width panel organized by topic, letting a student see the whole topic list (all ~17 topics, currently covering things like AI basics, Excel, and digital literacy) at a glance and jump directly into any one. Keep it keyboard-navigable and screen-reader friendly (see Section 4).

---

## 4. Accessibility requirements (non-negotiable)

- Meet WCAG 2.1 AA at minimum: real color contrast, semantic HTML, proper heading hierarchy, visible focus states, full keyboard navigation (including the mega menu).
- Every image requires alt text. Enforce this at the CMS level (Section 2), not just as a content guideline.
- Base body font size larger than a typical marketing site, comfortably readable for older adults. Let users not need to zoom.
- Favor bullet points and tables over dense paragraphs wherever content allows it. See Section 6 for the writing rules this implies.
- Don't rely on color alone to convey meaning (the color-coded sections in Section 5 should also have a label/icon, not just a color).

---

## 5. Topic page template

Every topic gets its own landing page, broken into parts. Structure each page as follows, top to bottom:

1. **Header**: topic title, one-line description
2. **Video**: YouTube embed near the top of the page. Support this as a simple field (video URL) that can be empty/placeholder if I haven't recorded one yet, don't require it to render the page.
3. **Parts/sections**: a topic can have multiple parts (e.g. "Part 1: Getting Started," "Part 2: Formulas"). Each part is its own block or sub-page, and should be reachable from a within-page table of contents or sub-navigation, not just an infinite scroll.
4. **Content blocks within each part**, visually and semantically distinguished by type using color + label/icon (not color alone):
   - **Lesson content**: the core instructional text
   - **Activity**: a hands-on task for the student to do
   - **Quiz**: links out to a Gemini-built quiz (a clearly labeled button/link that opens the quiz in a new tab is the simplest reliable pattern, an embedded iframe is a fallback only if a button clearly isn't enough)
5. **Images**: support multiple images per page/part, each with required alt text, similar to how GCF LearnFree illustrates steps inline with screenshots.

Build this as a reusable Jekyll layout/include so adding a new topic or part is mostly a content/data change, not new template code.

---

## 6. Content and voice rules

All page copy is written **in first person, as me speaking directly to the student**, not third person or generic instructional copy. Examples:

- Yes: "Let's open Excel and take a look at the ribbon together."
- No: "Users should navigate to the ribbon menu."

Additional writing rules:
- 8th-9th grade reading level. No unexplained jargon. If a technical term is necessary, define it in plain language the first time it's used.
- Prefer bullet points, numbered steps, and tables over paragraphs when explaining a process.
- No em dashes, anywhere, in any generated copy.
- Avoid generic AI-writing tells: no "delve," "leverage," "tapestry," "landscape," "unlock," forced rule-of-three lists, or uniform paragraph lengths that feel templated. Vary sentence rhythm. If the `humanizer` skill is available, run generated page copy through it before finalizing. If not, self-check against this list before presenting a draft.
- Warm and direct tone, like an instructor who wants the student to succeed, not a corporate manual.

I will supply source documents (Word docs, existing handouts, slides) for you to adapt into this format and voice. Don't invent instructional content wholesale, work from what I provide, and ask me for source material on a topic if you don't have it yet.

---

## 7. Build process

1. Scaffold the new repo: Jekyll structure, `_data/topics.yml`, base layouts (home, mega menu nav, topic page template, admin panel entry point).
2. Set up Decap CMS per Section 2.
3. Build out the design system per Section 3 (colors, type, spacing, motion) as reusable includes/partials before building individual pages, so every page is consistent.
4. Once the shell is working end to end (nav, one fully-built sample topic page, admin panel editable and committing correctly), keep going and build out the rest without pausing for my review, I will not be checking in mid-build. Hold every page to the same design and accessibility bar as that first sample, not just the first one.
5. I'll provide source documents topic by topic as I have them, for you to adapt into pages in the voice and format from Section 6. Use your judgment on how to fold each one in without waiting for approval.

---

## 8. Decisions left to your judgment

I won't be around to weigh in on these, so decide them yourself and keep moving. Stay within the design and accessibility bar set in Sections 3 and 4, and log the choices in DESIGN.md so later pages stay consistent with earlier ones:

- Final list and order of topics, built out as I provide content for each (currently around 17, expect more over time)
- Exact color palette for the lesson/activity/quiz distinction, staying within WCAG AA contrast
- Whether the mega menu needs sub-categories within topics, or a flat topic list is enough
- GitHub repo name, and whether GitHub Pages serves from a custom domain or the default `github.io` URL
