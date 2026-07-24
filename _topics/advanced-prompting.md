---
title: Advanced Prompting Techniques
slug: advanced-prompting
category: ai
description: Four moves that turn good prompts into great ones. No coding needed.
video_url: ''
parts:
- title: Show an example (few-shot)
  blocks:
  - type: lesson
    title: Hand it a finished sample
    body: |
      In "Prompting Fundamentals" you learned RTCF. For many jobs that is all you need. These four techniques go a step further when you want more polish.

      The first one has a technical name, **few-shot prompting**, but the idea is simple: before you ask for what you want, show the AI an example of exactly what good looks like.

      It works like training a new employee. Instead of describing the job in the abstract, you hand them a finished example and say, "Do one like this for the new situation." The AI picks up the pattern, the tone, and the level of detail.

      **In your work, this means:** when you write an email or summary that lands really well, save it. It becomes your example the next time you need something similar. The AI learns from your best work.
- title: Ask it to reason (chain-of-thought)
  blocks:
  - type: lesson
    title: Make it think before it answers
    body: |
      A standard prompt asks for an answer. A chain-of-thought prompt asks the model to work through the problem step by step first. One instruction does it:

      > "Think through this step by step before you answer."

      This reliably improves anything that involves reasoning, planning, or a few moving parts. And there is a bonus: you can read the reasoning and catch a wrong assumption before you rely on the answer. A plain answer gives you a result you cannot question. A reasoned one you can check.
- title: Give it a persona and limits
  blocks:
  - type: lesson
    title: Who it is, and what to avoid
    body: |
      RTCF's Role sets who the AI is writing for. You can go further by giving it a clear identity (a persona) and firm boundaries (constraints).

      The pattern is easy to remember:

      - **Persona:** "You are a friendly front-desk coordinator at a busy clinic."
      - **Constraints:** "Never give medical advice. Always offer a callback option. Keep it under 4 sentences."

      Naming what the AI should *never* do is often more useful than naming what it should do.
  - type: activity
    title: Run a three-round test
    body: |
      Pick a task from your field, like drafting a reply to an upset customer. Run all three rounds in the same chat, so the AI builds on what came before.

      1. **Round 1:** Type a plain, casual request, the kind you would have written before this course.
      2. **Round 2:** Rewrite it using full RTCF.
      3. **Round 3:** Add a persona and two constraints, and ask it to think step by step.

      After each round, save the output. Then answer the real question: which version would I actually use at work?
- title: Refine in cycles
  blocks:
  - type: lesson
    title: The draft is the start, not the end
    body: |
      The biggest mistake new users make is treating every prompt like a one-shot deal: one prompt, one answer, done. Professionals use AI the way a good editor uses a draft. They cycle.

      1. Generate a first draft.
      2. Read it and decide what works and what does not.
      3. Send a short follow-up that targets exactly what to change.
      4. Repeat until it is right.

      Because the AI remembers the conversation, your follow-ups can be short. "Warmer." "Cut the third paragraph." "Add a line about the refund." What matters is that each cycle is deliberate. You know what you are improving and why.
  - type: lesson
    title: Know when to step in yourself
    body: |
      These techniques make AI more powerful, which makes it more important to know where it should not be your tool at all. Final decisions about a person, anything with legal weight, and work that carries real risk if it is wrong all belong to you.

      Employers are starting to look for exactly this judgment. Not just "can this person use AI," but "does this person know when not to."
  - type: quiz
    title: Quick check
    body: |
      The quiz covers the four techniques: examples, step-by-step reasoning, persona with limits, and refining in cycles.

      I'll add the quiz link here soon. It opens in a new tab.
    quiz_url: ''
    quiz_label: Open the quiz
---
