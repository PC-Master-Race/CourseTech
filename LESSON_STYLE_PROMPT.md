# Lesson Formatting Prompt (Tutorial Hub house style)

Paste everything below the line into an AI assistant, then attach or paste your
source document (a Word doc, PDF, or notes). The AI will turn it into a finished
lesson file that drops straight into the site's `_topics/` folder.

Word documents (.docx) work better than PDFs, since PDFs often scramble tables
and repeat page headers.

---

You are formatting raw course material into a finished lesson for my educational
website. Follow these rules exactly. The goal is a lesson that is faithful to my
source, warm and readable for a beginner, and ready to publish.

## 1. Fidelity to the source (most important)

- **Preserve everything.** Keep every section, definition, example, case study,
  table, list, and recommended-reading link from the source. Do not drop content
  to save space. Do not summarize away detail.
- **Reword, do not invent.** Rewrite for voice and clarity, but never add facts,
  statistics, tools, or claims that are not in the source. If the source has a
  number or a citation, keep it. If it has no source for a claim, do not add one.
- Keep every table as a Markdown table. Keep every case study and its takeaway.
- If the source has a "recommended reading" list, keep it as a bulleted list.
- **Flag anything that looks out of date** rather than silently repeating it,
  especially software steps, menu names, version numbers, and device models.

## 2. Voice and writing rules

- Write in the **first person**, as me (the instructor) talking directly to one
  student. "Let's open Excel together," not "Users should open the application."
- 8th-to-9th-grade reading level. Define any technical term in plain language the
  first time it appears.
- Prefer **bullet points, numbered steps, and tables** over long paragraphs.
- **No em dashes anywhere.** Use commas, periods, or restructure the sentence.
- Avoid AI-writing tells: no "delve," "leverage," "unlock," "landscape,"
  "tapestry," "realm," "seamless," "elevate," no forced rule-of-three lists, and
  no paragraphs that are all the same length. Vary the rhythm.
- Warm and direct, like an instructor who wants the student to succeed.
- Never use a complicated word where a simple one does the job. Plain language is
  the whole point of this site.

## 3. Remove classroom framing

This is a public website read by people all over the world, alone, at their own
pace. Cut or reword anything that assumes the reader is in a room with me or on a
schedule:

- Remove: "share with the class," "your partner," "groups of three," "raise your
  hand," "the board," "volunteers," "discussion," references to Week 1 / Day 2 /
  Thursday / "next class," estimated class times, "graded," and any submission
  instructions (Canvas, email addresses, exit tickets, office hours).
- **Remove class-prep checklists entirely.** Source guides often open with a
  "before you begin, check these things" list: your device is charged, your
  glasses are on, this handout is open in front of you, tell me if something is
  wrong. None of that makes sense to someone reading online by themselves.
  Replace it with a short, genuinely useful setup note if one is needed (for
  example, which software version the steps assume), or cut it and start teaching.
- Remove anything implying I am physically present and can help in the moment:
  "let me know right away," "come find me," "we will wait for everyone."
- Keep the activities themselves, but reword them for a solo learner: "jot this
  down," "think about," "reflect on," "try this on your own."
- Turn "yesterday / today / this week" into neutral wording, or reference another
  lesson by name.

## 4. Structure

Break the lesson into **parts** (which become the on-page table of contents), and
break each part into **blocks**. There are three block types:

- **lesson** — the core teaching. Most blocks are this type.
- **activity** — a hands-on task the student does. Keep at least one per lesson.
- **quiz** — a short "check your understanding" block at the very end. Leave the
  quiz link blank (I add it later); just write a sentence about what it covers.

Every lesson opens with a single short **lead-in**: one first-person paragraph
saying, in plain terms, what the student will learn and why it matters. Like a
good textbook chapter opener.

Use short definition callouts with a Markdown blockquote:
`> **Term:** plain-language definition.`

## 5. Bloom's taxonomy: build the ladder

Do not let a lesson stop at "read it" or "follow my steps." Each lesson should
climb from lower-order to higher-order thinking:

- Lesson blocks handle **Remember** and **Understand**.
- The main activity should reach **Apply** (do the thing).
- End the main activity with a short paragraph starting `**Go further.**` that
  pushes into **Analyze**, **Evaluate**, or **Create**: judge the output, defend a
  choice, compare two options, adapt it to their own situation, build something
  reusable, or explain it to someone else in their own words.
- Keep it concrete and doable in a few minutes. Never use the words "Bloom's" or
  the level names in student-facing text. The student should just experience it as
  a natural next step.

## 6. Output format

Output ONE file, exactly in this format (the site's front-matter schema). Use a
literal block scalar (`|`) for every `body` so the Markdown is preserved:

```
---
title: The lesson title
slug: url-friendly-slug-with-dashes
category: ai
lead_in: One first-person paragraph on what they'll learn and why it matters. No em dashes.
description: One sentence shown under the title and on cards.
video_url: ''
parts:
- title: First part title
  intro: Optional one-line setup for this part.
  blocks:
  - type: lesson
    title: Block heading
    body: |
      The teaching text as Markdown. Use bullets, numbered steps, tables,
      and `> **Term:** definition` callouts. No em dashes.
  - type: activity
    title: Activity heading
    body: |
      A hands-on task, reworded for a solo learner.

      **Go further.** The higher-order extension: judge, compare, adapt, or create.
- title: Second part title
  blocks:
  - type: lesson
    title: ...
    body: |
      ...
  - type: quiz
    title: Quick check
    body: |
      One or two sentences on what the quiz covers, then:
      "I'll add the quiz link here once it is built. It opens in a new tab."
    quiz_url: ''
    quiz_label: Open the quiz
---
```

Notes on the format:
- `category` is one of my course ids: `ai`, `software`, or `devices`.
- `slug` must be lowercase letters, numbers, and dashes only. It becomes the web
  address, so keep it short and clear.
- Indentation matters: parts are a list under `parts:`, blocks are a list under
  each part's `blocks:`, and each `body: |` block's text is indented beneath it.
- If a title or blurb contains a colon, wrap the whole value in quotes.

## 7. Before you finish, self-check

Confirm all of these, and fix anything that fails:

- [ ] Every section, table, example, and reading link from the source is present.
- [ ] Zero em dashes anywhere.
- [ ] No AI-tell words (delve, leverage, unlock, landscape, tapestry, etc.).
- [ ] No classroom framing, no class-prep checklist, no scheduling references.
- [ ] First person throughout; a lead-in at the top; at least one activity with a
      "Go further" step; a quiz block at the end.
- [ ] Nothing invented that is not in the source, and anything possibly outdated
      is flagged to me rather than stated as current fact.

Now format the source material I am giving you into one lesson file in exactly
this style.
