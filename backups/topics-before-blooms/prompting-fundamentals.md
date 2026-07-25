---
title: Prompting Fundamentals
slug: prompting-fundamentals
category: ai
description: The foundational skill everything else builds on. Learn to ask an AI tool for exactly what you need.
lead_in: If I could only teach you one skill in this whole course, this would be it. In this lesson you will learn how to ask an AI tool for exactly what you want, using a simple four-part checklist I call RTCF. The same tool hands one person junk and another person gold, and the difference is almost always the prompt. Let me show you how to be that second person.
video_url: ''
parts:
- title: The single skill that changes everything
  intro: 'Estimated time: 30 to 35 minutes. Format: read and practice. Tools: ChatGPT or Gemini.'
  blocks:
  - type: lesson
    title: Why the same tool gives different results
    body: |
      Here is something that surprises almost every student. Two people can use the exact same AI tool, on the same day, for the same task, and get completely different results. One walks away with a polished, useful output. The other walks away frustrated, sure the AI simply "doesn't work."

      The difference is almost never the tool. The difference is the prompt.

      **Prompt engineering** is the skill of writing effective instructions for AI models, and it is the single most practical thing you will learn in this course. You do not need to write code. You do not need to understand how neural networks work. You need to communicate clearly and strategically with an AI system, and that is something every professional can do.

      This topic gives you the framework. The activity at the end gives you the practice.
- title: 'Why prompting matters: same tool, different world'
  intro: Before the framework, let's make the problem concrete. Look at these two prompts and what they produce.
  blocks:
  - type: lesson
    title: Vague versus strategic
    body: |
      | Vague prompt | Strategic prompt (RTCF) |
      |---|---|
      | "Write me an email." | "You are a medical office coordinator. Write a 3-sentence email to a patient reminding them of their 2 PM appointment tomorrow. Use a warm, professional tone, and include a note about arriving 10 minutes early for check-in." |
      | **Result:** a generic, bland email with no context, no tone, and no useful details. Could apply to anything, to anyone, in any industry. | **Result:** a polished, warm, professional patient message, ready to copy, paste, and send after one quick review. |

      The tool did not change. The input did. That is the entire lesson of prompting in one sentence. When you give an AI model more to work with, more context, more clarity, a defined role, a set format, it has more to draw on. Better input almost always produces better output.
- title: The RTCF framework, your prompting blueprint
  intro: 'Every strong prompt for a workplace task can be built from four parts. Together they spell RTCF: Role, Task, Context, and Format. Think of it as a checklist you run before sending any prompt that matters.'
  blocks:
  - type: lesson
    title: The four parts
    body: |
      | Part | What it does | Workplace example |
      |---|---|---|
      | **R, Role** | Tell the AI who to act as. This frames how it reads your request and the voice it uses. | "You are an experienced HR coordinator at a mid-size healthcare organization." |
      | **T, Task** | State exactly what you want done. Use active verbs: write, summarize, compare, list, rewrite, translate, evaluate. Vague tasks produce vague output. | "Write a 5-bullet summary of the attached onboarding checklist for new warehouse staff." |
      | **C, Context** | Give the details that shape the output: audience, purpose, constraints, background. Context is what separates generic from genuinely useful. | "The audience is first-day employees who may not know the safety rules. Keep the language simple and skip the jargon." |
      | **F, Format** | Say how you want the answer laid out: bullet list, numbered steps, a professional email, one paragraph, a table, a word count, a tone. | "Format it as a numbered list. Use plain language. Keep each item to one sentence." |

      You do not always need all four. A quick, low-stakes request can be shorter. But for anything you would put in front of a supervisor, send to a client, or use with a patient, run the full RTCF checklist. The few seconds it takes will save you far more time in rewrites.
  - type: lesson
    title: RTCF quick reference card
    body: |
      Keep this handy.

      - **Role:** Who should the AI act as? ("You are a bilingual customer service representative...")
      - **Task:** What exactly should it do? Use a strong verb: write, summarize, compare, translate, reformat, evaluate, list.
      - **Context:** What details does it need? Who is the audience? What are the constraints or background?
      - **Format:** How should the output look? (bullet list, numbered steps, formal email, one paragraph, under 200 words)

      Pro tip: write your RTCF prompt as one flowing paragraph. You do not need to label each section out loud. The goal is to make sure all four are present, not to format them as a checklist.
- title: RTCF in action, a full worked example
  intro: Let's build one complete prompt, piece by piece, so you can see how each part adds value.
  blocks:
  - type: lesson
    title: Watch it get stronger
    body: |
      | What was added | The prompt | Why it matters |
      |---|---|---|
      | Task only (bare minimum) | "Summarize this report." | A valid request, but which report? How long? For whom? The model has almost nothing to work with. |
      | + Role | "You are a business analyst. Summarize this report." | Better. Now the model has a perspective and an expertise level to bring. |
      | + Context | "You are a business analyst. Summarize this quarterly sales report for our department manager, who wants a quick overview before a Monday meeting." | Much stronger. Now it knows the audience and the purpose, so it knows what to emphasize and what to leave out. |
      | + Format (complete RTCF) | "You are a business analyst. Summarize this quarterly sales report for our department manager, who wants a quick overview before a Monday meeting. Provide 5 bullet points, each one sentence. Start with the most important finding." | Complete. This produces a polished, ready-to-use answer that needs very little editing. |

      Notice how each addition makes the prompt more useful without making it a chore. A complete RTCF prompt is usually 2 to 5 sentences. That is all it takes.
- title: AI is a conversation, not a search engine
  intro: 'This is one of the most important mindset shifts in the course. Most of us were trained to use technology like a search box: type, get a result, move on. AI tools work differently, and treating them like a search engine is a big reason people get frustrated.'
  blocks:
  - type: lesson
    title: Two mindsets, side by side
    body: |
      | Search-engine mindset | Conversation mindset |
      |---|---|
      | One prompt, then done | The first prompt starts the conversation |
      | If the result is wrong, try a different search | If the result is not right, follow up: "Make it shorter," "Try a different angle" |
      | Type keywords, not full sentences | Write in natural sentences and give context |
      | The result is fixed, take it or leave it | The result is a starting draft you shape with feedback |
      | Feel like you failed if you have to ask again | Iteration is the skill, not a sign of failure |
  - type: lesson
    title: Powerful follow-up moves
    body: |
      After the first response, you can refine, redirect, or expand using plain language. The most useful follow-ups:

      | Follow-up prompt | What it does |
      |---|---|
      | "Make it shorter / longer." | Adjusts length without rewriting your prompt. |
      | "Try a more formal / casual tone." | Shifts the register to match your audience. |
      | "Give me 3 alternative versions." | Generates options to compare. |
      | "Explain that last point in simpler terms." | Breaks down jargon for a broader audience. |
      | "Add a section on [topic]." | Expands the output without starting over. |
      | "Rewrite this as if the reader has never worked in healthcare." | Reframes the audience and complexity mid-conversation. |
      | "Check your previous response for any errors or assumptions." | A self-review nudge. The model often catches its own mistakes when asked. |

      In your work, this means you do not need the perfect prompt on the first try. The professionals who get the most out of AI treat it as a working session, not a one-shot vending machine. Start with a solid RTCF prompt, then refine.
- title: The chain-of-thought nudge
  intro: Here is a simple technique that sharply improves answers on complex tasks. It is called chain-of-thought, and it takes just one extra phrase at the end of your prompt.
  blocks:
  - type: lesson
    title: Ask it to show its work
    body: |
      **What it is:** add a phrase like "Think through this step by step before giving your final answer." That tells the model to reason out loud before committing.

      **Why it works:** when an LLM spells out its reasoning, it tends to catch its own errors and produce more accurate, careful output, especially on analysis, decisions, or multi-step logic.

      **When to use it:** complex analysis, comparing options, troubleshooting, building an argument, or any task where you want the model to show its work instead of jumping to a conclusion.

      **Example:**

      > "You are a logistics coordinator. Evaluate whether our current supplier arrangement is cost-effective given the following data: [your data here]. Think through each factor step by step before giving your recommendation."

      Without the nudge, the model may jump straight to a recommendation without weighing the tradeoffs, and you might miss something important.

      Other useful reasoning nudges:

      - "Before answering, list any assumptions you are making."
      - "Identify potential weaknesses in this plan before proposing improvements."
      - "What would someone who disagrees with this conclusion say?"
- title: Practice and go deeper
  blocks:
  - type: activity
    title: Prompt Makeover Lab
    body: |
      **Purpose:** to practice turning weak, vague prompts into strong RTCF prompts, and to see the difference yourself, in real time, with a live AI tool.

      **Instructions:**

      1. Open ChatGPT or Gemini in your browser.
      2. For each prompt below, first run the original vague version and note the result. Then rewrite it using RTCF and run your improved version. Record both.
      3. Notice what changed, why it mattered, and which version you would actually use at work.

      **Prompt 1, general professional.** Original: "Write a report." Ask yourself: what report? What is its purpose? Who will read it? What format? Then write your complete RTCF version.

      **Prompt 2, healthcare or office setting.** Original: "Help me with a patient email." Consider: what type of message? What information must be included? What tone fits? Then write your complete RTCF version.

      **Prompt 3, your own field.** Original: "Give me some information about my job." Make this completely specific to your real job title, a real task you do, and a realistic output you would actually use. Then write your complete RTCF version.

      **Reflection:** What was the biggest difference between the vague and RTCF versions? Which part of RTCF made the largest single impact for you: Role, Task, Context, or Format? Could you use any of these improved prompts in your job this week?
  - type: lesson
    title: What you can do now
    body: |
      After this topic and the Prompt Makeover Lab, you should be able to:

      - Explain why prompting skill matters, and why the same tool gives wildly different results in different hands.
      - Apply RTCF (Role, Task, Context, Format) to any workplace prompting task.
      - Turn a vague prompt into a complete, strategic one in under two minutes.
      - Use follow-up prompts to refine output instead of starting over.
      - Use the chain-of-thought nudge to improve reasoning on complex tasks.
  - type: lesson
    title: 'Dig deeper: recommended reading'
    body: |
      Each of these takes 5 to 15 minutes.

      - **OpenAI, "Prompt Engineering Guide."** The official guide from the makers of ChatGPT. Clear, well organized, full of tested techniques. (Advanced)
      - **Anthropic, "Prompt Library: Real Examples Across Use Cases."** A browsable library of strong prompts across dozens of workplace scenarios. Great for inspiration and pattern spotting. (Advanced)
      - **Google, "How to Write Better AI Prompts."** An accessible, beginner-friendly take with real examples.
      - **MIT Sloan Management Review, "Effective Prompts for AI."** Research-backed advice on prompt construction from an enterprise view.
      - **Ethan Mollick, One Useful Thing, "How to Use AI to Do Stuff: An Opinionated Guide."** Mollick is a Wharton professor and one of the most practical AI educators writing today.
  - type: quiz
    title: Quick check
    body: |
      When you are ready, take the short quiz. It covers why prompting matters, the four parts of RTCF, refining in conversation, and the chain-of-thought nudge.

      I'll paste the quiz link here once it is ready. It opens in a new tab.
    quiz_url: ''
    quiz_label: Open the quiz
---
