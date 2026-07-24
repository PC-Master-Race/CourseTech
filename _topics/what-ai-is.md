---
title: What AI Actually Is
slug: what-ai-is
category: ai
description: Demystifying the technology before you touch it. By the end you'll be able to explain AI in plain English to anyone.
lead_in: Before we touch a single tool, I want you to really understand what AI is, because that is what makes everything else in this course click into place. In this lesson I will show you how to tell AI apart from ordinary software, where it came from, and what it is actually doing when it answers you. Get this straight and you will use these tools with confidence instead of guesswork.
video_url: ''
parts:
- title: Three things that are not the same
  intro: Before you can use AI well at work, you need to know what it actually is. Not what movies say, not what a coworker heard, and not what this week's headlines are shouting. Let's clear the air.
  blocks:
  - type: lesson
    title: Software, automation, and AI
    body: |
      One of the most common sources of confusion at work is blurring three different things: software, automation, and artificial intelligence. They are related, but they are not the same. Here is how to tell them apart.

      | | What it does | Who decides? | Workplace example |
      |---|---|---|---|
      | **Software** | Follows a fixed set of instructions written by a programmer | The programmer, in advance | A payroll app that calculates hours and deductions the same way every time |
      | **Automation** | Uses software to replace repetitive, rule-based tasks. Always follows the same steps | The programmer. The rules are fixed | An auto-email sent every time a patient submits an intake form |
      | **Artificial intelligence** | Learns patterns from data and makes decisions or generates outputs. Can handle new situations it was never explicitly programmed for | The AI model, based on what it learned from data | A chatbot that understands a patient's unique question and answers in natural language |

      The key difference: software and automation follow rules. AI learns from examples. A traditional spell-checker follows a fixed dictionary. An AI writing assistant learns what "sounds right" from billions of examples of human writing, and that is a fundamentally different kind of system.
- title: How we got here, a short history
  intro: You do not need the history of AI to use it. But understanding the arc, where it started and where it is now, helps you see why today's tools work the way they do and why they sometimes fail.
  blocks:
  - type: lesson
    title: 'Stage 1: Rules-based AI (1950s to 1980s)'
    body: |
      Early AI systems were elaborate "if this, then that" rule books written by human experts. Programmers coded thousands of rules by hand: "If the patient has a fever AND a sore throat, then flag for a strep test." These systems were powerful inside their narrow area, but they broke down the moment a situation came up that a programmer had not anticipated. They could not learn. They could not adapt.
  - type: lesson
    title: 'Stage 2: Machine learning (1980s to 2010s)'
    body: |
      Machine learning changed everything. **Machine learning (ML)** is a type of AI in which a system learns patterns from large amounts of data instead of following hand-coded rules. Rather than programming every rule, the system finds patterns on its own. You show it a million emails, some spam and some not, and it learns the difference. That is how your email filter works today. ML let AI take on messy, real-world problems at scale.
  - type: lesson
    title: 'Stage 3: Large language models (2017 to now)'
    body: |
      **Large language models (LLMs)** are AI systems trained on massive amounts of text that can understand and generate human language. They power tools like ChatGPT, Gemini, and Claude. They came out of a breakthrough called the "transformer," and they let AI do something that used to seem impossible: hold a natural conversation, write a memo, summarize a report, or explain a concept, all from plain-English instructions given by ordinary people.

      That last point is worth pausing on. For the first time, you do not need to be a programmer to use the power of AI. That is exactly why this course exists.
- title: The four cognitive technologies in your workplace
  intro: AI is not one single thing. Researchers and business analysts sort it into four broad categories of what they call cognitive technologies, AI systems that do tasks that used to need human thinking. You almost certainly meet all four on the job already, even if you did not know what to call them.
  blocks:
  - type: lesson
    title: The four types, and where you have seen them
    body: |
      | Technology | What it does | How it works | You have seen it in... |
      |---|---|---|---|
      | **Language** | Reads, writes, translates, summarizes, and holds conversations in human language | Trained on vast amounts of text: books, websites, documents | ChatGPT, autocorrect, Grammarly, email auto-reply suggestions |
      | **Vision** | Identifies objects, people, text, and patterns in images and video | Trained on millions of labeled images | Face ID on your phone, security cameras, barcode readers, medical imaging |
      | **Prediction** | Forecasts outcomes or flags anomalies by finding patterns in past data | Trained on past records: transactions, behaviors, outcomes | Credit card fraud detection, scheduling software, inventory forecasting |
      | **Recommendation** | Suggests what you might want next, based on your behavior and similar users | Trained on user behavior across millions of people | Netflix suggestions, Amazon "you might also like," job matches, Spotify playlists |

      In your role, this means you are not starting from zero. You have been navigating AI systems for years. This course is about learning to use them on purpose and with skill, especially the language tools that are reshaping how professionals write, research, analyze, and communicate.
  - type: activity
    title: AI already in your work life
    body: |
      Estimated time: 10 to 12 minutes. Best done on your own first, then shared with the class.

      **Purpose:** to ground the ideas you just read in your own experience, and to notice how much AI you already navigate every day.

      **Instructions:**

      1. List at least **3 examples** of AI, or what might be AI, that you run into in your trade, your daily tasks, or your personal life. Think about apps, software, devices, or services you use often.
      2. Next to each one, take your best guess at which of the four categories it fits: Language, Vision, Prediction, or Recommendation.
      3. Be ready to share at least one example with the class.

      Examples to get you thinking:

      - Does your GPS app reroute you in real time? (Prediction)
      - Does your email filter flag spam before you see it? (Language / Prediction)
      - Does your workplace use badge scanning or facial recognition? (Vision)
      - Does your scheduling software suggest good appointment times? (Prediction)
      - Does a platform recommend products, content, or connections from your history? (Recommendation)
      - Does autocorrect or autocomplete help you write faster? (Language)

      **Reflection:** looking at your list, which of these tools do you actively control, and which ones work on you in the background, often without your awareness? What does that difference make you think about?
- title: What large language models actually do
  intro: This part surprises most people, and understanding it will make you a much sharper, more careful user of these tools.
  blocks:
  - type: lesson
    title: 'The honest answer: they predict the next word'
    body: |
      When you type a message into ChatGPT or Gemini and press send, here is what is really happening. The model reads your input and predicts, word by word, what text is most likely to come next. (Technically it works in tokens, where a token is roughly a word or part of a word.) It does this by drawing on statistical patterns it learned from an enormous amount of text during training.

      It does not search the internet, unless a specific web-search feature is turned on. It does not "know" facts the way you look something up in a textbook. It generates text that is statistically likely to be correct and coherent, based on patterns in its training data. Most of the time that output is genuinely useful. Sometimes it is confidently wrong. You will learn much more about that in "When AI Gets It Wrong."
  - type: lesson
    title: A helpful way to picture it
    body: |
      Imagine a colleague who has read every book, article, email, manual, and website ever published, in dozens of languages, and who is remarkably good at putting together a helpful answer to almost any question. They are incredibly well-read.

      But they were not in the room when your company made its last policy change, and they cannot see your patient files or your internal data. That colleague is a useful collaborator, not an oracle. That is the mindset to bring to every chat with an LLM.
- title: What generative AI is
  intro: You have probably heard the phrase everywhere lately. It is worth two minutes, because it is the family that today's most talked-about tools belong to.
  blocks:
  - type: lesson
    title: The kind of AI that makes new things
    body: |
      Here is the plain version. For a long time, most AI did one job: it sorted or scored things that already existed. Is this email spam, yes or no? Which of these photos has a cat in it? Useful work, but the AI was picking from options, not making anything new.

      Generative AI flipped that. It creates brand-new content that did not exist a moment ago, based on a request you type in. Ask for a thank-you note and it writes one. Ask for a picture of a calm waiting room and it paints one. The word "generative" just means it *generates*, it produces.

      > A quick note on terms. **Generative AI** is AI that creates new content, like text, images, or audio, from a plain-language request you give it.
  - type: lesson
    title: It shows up in more than text
    body: |
      Text is where most workplace value lives right now, and it is where this course spends most of its time. But generative AI is not only about writing. The same basic idea powers a few different kinds of tools.

      | You ask for... | The tool makes... | Examples you may have heard of |
      |---|---|---|
      | Writing or answers | Text | ChatGPT, Gemini, Claude |
      | A picture from a description | An image | Gemini, Canva, Adobe Firefly |
      | A voice or a bit of music | Audio | Various voice and music tools |

      One thing to hold onto: because these tools *make* something new every time, you can ask the same thing twice and get two different results. That is normal. It is also why the quality of your request matters so much, which is the whole point of the next topic on prompting.
  - type: activity
    title: Spot the generative tool
    body: |
      Think back over the last week or two. See if you can name one time you used, or watched someone use, a tool that *made* something new for them.

      1. What did it create? Text, a picture, audio, or something else?
      2. What did the person ask for to get it?

      If nothing comes to mind yet, that is fine. You will be using one before this course is over.
- title: Busting the big myths
  intro: Let's take the common misconceptions head on. You may have heard some of these. You may have believed some. Here is the reality.
  blocks:
  - type: lesson
    title: Five myths, and the truth
    body: |
      | The myth | The reality |
      |---|---|
      | "AI is going to think for itself and take over." | Today's AI tools, even the most powerful, have no goals, desires, or self-awareness. They are sophisticated pattern matchers. The takeover scenario is science fiction, not a current technical reality. These tools do exactly what they are designed to do: generate useful outputs in response to human inputs. |
      | "AI is always right." | AI language models can be confidently, fluently wrong. They can invent statistics, misattribute quotes, and make up citations that sound completely real. Verification is not optional. It is part of the skill of using AI responsibly. |
      | "AI is always wrong and can't be trusted." | This overcorrection is just as risky. Used with good judgment and verification, these tools produce genuinely useful, high-quality work. People who dismiss AI entirely will be outpaced by people who learn to use it well. |
      | "AI is going to take all the jobs." | The research is more nuanced. AI will automate certain tasks, not whole jobs. Most roles will shift: AI handles some tasks, freeing people for work that needs judgment, relationships, creativity, and ethics. The workers most at risk are the ones who refuse to adapt. You are here because you are adapting. |
      | "You have to be technical to use AI." | The whole point of modern AI tools is that you talk to them in plain language, the way you talk to a person. No coding, no technical background. What matters is communicating clearly and thinking critically about the output, which is exactly what this course teaches. |
- title: Wrap up and go deeper
  blocks:
  - type: lesson
    title: What you can do now
    body: |
      After this topic, you should be able to:

      - Explain the difference between software, automation, and AI in plain English.
      - Describe the three stages of AI development, and why LLMs are a big shift for non-technical workers.
      - Name the four cognitive technologies and give a workplace example of each.
      - Say what an LLM actually does (predicts statistically likely text from patterns) and why that matters for how you use and check it.
      - Push back on common AI myths with facts and confidence.
  - type: lesson
    title: 'Dig deeper: recommended reading'
    body: |
      These are trustworthy sources to expand your understanding. Each takes 5 to 15 minutes.

      - **McKinsey & Company, "What Is AI? A Plain-English Explainer."** A clear, jargon-free overview of AI fundamentals with real business examples across industries.
      - **Pew Research Center, "How Americans View AI and Its Impact on People and Society."** Survey data on public attitudes toward AI. Useful for understanding the range of reactions you will meet on the job.
      - **Anthropic, "What Is Claude?"** A plain-language overview of what the Claude AI assistant is and how it works.
  - type: quiz
    title: Quick check
    body: |
      When you are ready, take the short quiz to lock in the big ideas: the three-way difference, the three stages, the four cognitive technologies, what an LLM really does, and the myths.

      I'll add the quiz link right here once it is built. It opens in a new tab so you keep your place.
    quiz_url: ''
    quiz_label: Open the quiz
---
