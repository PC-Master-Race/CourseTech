# Lesson Formatting Prompt (Tutorial Hub house style)

Paste everything below the line into an AI assistant, then attach or paste your
source document (a Word doc, PDF, or notes). The AI will turn it into a finished
lesson file that drops straight into the site's `_topics/` folder.

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
- If the source cites sources or has a "recommended reading" list, keep it as a
  bulleted list at the end.

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

## 3. Remove classroom framing

This is a public website, not my in-person class. Cut or reword anything that
assumes the reader is in a room with me or on a schedule:

- Remove: "share with the class," "your partner," "groups of three," "raise your
  hand," "the board," "volunteers," "discussion," references to Week 1 / Day 2 /
  Thursday / "next class," estimated class times, "graded," and any submission
  instructions (Canvas, email address, exit tickets, office hours).
- Keep the activities themselves, but reword them for a solo online learner:
  "jot this down," "think about," "reflect on," "try this on your own."
- Turn "yesterday / today / this week" into neutral wording, or reference another
  lesson by name.

## 4. Structure

Break the lesson into **parts** (which become the on-page table of contents), and
break each part into **blocks**. There are three block types:

- **lesson** — the core teaching. Most blocks are this type.
- **activity** — a hands-on task the student does. Keep at least one per lesson.
- **quiz** — a short "check your understanding" block at the very end. Leave the
  quiz link blank (I add it later); just write a sentence about what the quiz
  covers.

Every lesson opens with a single short **lead-in**: one first-person paragraph
that says, in plain terms, what the student will learn and why it matters. Like a
good textbook chapter opener.

Use short definition callouts with a Markdown blockquote, like:
`> **Term:** plain-language definition.`

## 5. Output format

Output ONE file, exactly in this format (this is the site's front-matter schema).
Use a literal block scalar (`|`) for every `body` so the Markdown is preserved:

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
- `slug` must be lowercase letters, numbers, and dashes only, and it becomes the
  page's web address, so keep it short and clear.
- Indentation matters: parts are a list under `parts:`, blocks are a list under
  each part's `blocks:`, and each `body: |` block's text is indented beneath it.

## 6. Before you finish, self-check

Confirm all of these, and fix anything that fails:

- [ ] Every section, table, example, and reading link from the source is present.
- [ ] Zero em dashes anywhere.
- [ ] No AI-tell words (delve, leverage, unlock, landscape, tapestry, etc.).
- [ ] No classroom or scheduling references.
- [ ] First person throughout; a lead-in at the top; at least one activity; a quiz
      block at the end.
- [ ] Nothing invented that is not in the source.

Now format the source material I am giving you into one lesson file in exactly
this style.
