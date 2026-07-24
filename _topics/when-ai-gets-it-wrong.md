---
title: When AI Gets It Wrong
slug: when-ai-gets-it-wrong
category: ai
description: The warning label. How AI makes things up, and the one habit that protects you, your employer, and the people you serve.
video_url: ''
parts:
- title: The warning label, and why it comes first
  intro: 'Estimated time: 18 to 22 minutes. Format: read and fact-check. Tools: a search engine.'
  blocks:
  - type: lesson
    title: AI proposes, you verify, you decide
    body: |
      Every powerful tool comes with instructions for safe use. A scalpel, a forklift, a prescription. All genuinely useful, and all able to cause real harm when misused. AI is no different.

      This is the warning label. It is not here to scare you off, you have already seen how valuable these tools are. It is here because the most dangerous user is not the skeptic who refuses to try it. The most dangerous user is the one who trusts AI completely, skips verification, and lets a wrong answer cause a real problem.

      By the end of this topic, one habit should be locked in:

      > **AI proposes. You verify. You decide.**

      That habit protects you, your employer, and the people you serve.
- title: 'Hallucination: when AI makes things up'
  intro: The single most important limit to understand is what researchers call a hallucination, and it is nothing like what the word might suggest.
  blocks:
  - type: lesson
    title: What hallucination means
    body: |
      > **AI hallucination** is the tendency of large language models to generate text that is factually wrong, fabricated, or entirely invented, stated with complete confidence and fluency, as if it were true.

      The model does not know it is wrong. It has no internal fact-checker. It simply generates the most statistically likely next token, and sometimes that leads somewhere false. Common forms include invented statistics, fabricated citations and sources, wrong dates, misattributed quotes, fictional organizations, incorrect legal or medical information, and plausible-sounding details that simply do not exist.
  - type: lesson
    title: Why it happens
    body: |
      Remember from the first topic: an LLM does not retrieve facts from a database. It predicts the most likely next word based on patterns in its training data. When you ask for a specific fact, a date, a citation, a statistic, it generates what sounds like the right kind of answer.

      - If the true answer was common in its training data, it is often right.
      - If the true answer was obscure, recent, or poorly documented, it may produce something plausible but completely invented, written with the same smooth confidence as when it is correct.

      Here is the core danger: there is no built-in signal that tells you when the model is guessing. A hallucinated citation looks identical to a real one. A made-up statistic is formatted exactly like a real one. Without verification, you cannot tell the difference from the text alone.
  - type: lesson
    title: 'A case that made headlines: Mata v. Avianca (2023)'
    body: |
      **What happened:** In May 2023, a New York attorney named Steven Schwartz filed a legal brief in federal court that cited more than half a dozen prior cases to support his client. It was a real lawsuit. The citations looked completely legitimate: proper case names, docket numbers, jurisdictions, page references.

      **The problem:** not one of those cases existed. Every citation had been fabricated by ChatGPT. When opposing counsel could not find the cases and the judge demanded copies, the attorney admitted he had used ChatGPT to research the brief and had never checked whether the cases were real. He simply assumed the tool was reliable.

      **The consequences:** the judge imposed sanctions. The attorney and his firm were fined. It became one of the most widely cited examples of AI hallucination causing real professional harm, covered by The New York Times, The Washington Post, NPR, and nearly every major legal publication.

      **The lesson for you:** the attorney was not reckless or incompetent. He was simply overconfident in a tool he did not fully understand. That is exactly the mistake you will not make, because you are learning about this right now.
  - type: lesson
    title: Five types you may meet at work
    body: |
      The Mata case is dramatic, but hallucinations show up in much more everyday forms.

      | Type | What it looks like | The workplace risk |
      |---|---|---|
      | **Invented statistics** | A confident number with no real source: "Studies show 73% of employees report..." | You put it in a report. A supervisor asks for the source. There is none. |
      | **Fabricated citations** | A journal article, report, or book that sounds plausible but does not exist | You cite it in a proposal. Someone tries to look it up. Trust in your work takes a hit. |
      | **Wrong dates or timelines** | A law described as effective in 2019 that actually passed in 2022 | Compliance errors; incorrect guidance given to a client or patient. |
      | **Misattributed quotes** | A quote pinned to the wrong person, or never said at all | Reputational risk; spreading misinformation in professional messages. |
      | **Plausible but wrong procedures** | Step-by-step instructions that are mostly right but contain one subtly wrong step | Operational errors; safety incidents; patient harm in healthcare. |
- title: The human-in-the-loop principle
  intro: 'Understanding hallucination leads straight to one of the most important principles in professional AI use. It fits in three lines: AI proposes. Human verifies. Human decides.'
  blocks:
  - type: lesson
    title: You keep the judgment
    body: |
      This does not mean you distrust every word the AI produces. It means you keep the professional judgment that is yours to keep. AI is a remarkably fast and capable drafting tool. The quality control, the verification, and the final decision belong to you.

      Think of it like this. If you hired a very fast, very articulate research assistant who sometimes confidently said wrong things without realizing it, you would not fire them. You would check their work before it went to anyone important. That is exactly the relationship to build with AI.
  - type: lesson
    title: A verification checklist
    body: |
      Not every output needs the same scrutiny. Match your effort to the stakes.

      | Ask about the output | Stakes | What to do |
      |---|---|---|
      | Does it contain specific facts, dates, statistics, or cited sources? | Always check | Search each fact independently. Do not use the AI to check its own output, use a separate source. |
      | Will it go to a patient, client, supervisor, or outside party? | High | Read for plausibility. Verify any claim you did not already know. If in doubt, remove it or find a real source. |
      | Does it involve legal, medical, financial, or safety information? | Critical | Treat the whole thing as a draft. Have a qualified professional review anything that will influence a real decision. |
      | Does it give step-by-step instructions? | High | Walk through each step yourself. Test on a low-stakes example before you rely on it. |
      | Is it a creative draft you will review and edit anyway? | Lower | Read for tone, accuracy, and completeness. Light verification is usually enough, but still check any specific claims. |

      In your work, this means every time AI produces something that will leave your hands, an email, a report, a patient message, take 60 seconds to ask: are there any specific claims here that I have not verified? That minute is your professional protection.
- title: A first look at what else can go wrong
  intro: Hallucination is the most immediate risk, but not the only one. Here is a short preview of three more limits. You will go much deeper on all of these in Week 3.
  blocks:
  - type: lesson
    title: Bias, privacy, and outdated information
    body: |
      **Bias in AI output.** AI models learn from human-generated text, so they can reflect and amplify the biases in that data. Hiring tools have been shown to favor certain groups. Writing tools can default to cultural assumptions that do not fit your audience. AI is not neutral. Always read its output with a critical eye, especially when it describes people, recommends individuals, or targets specific communities.

      **Privacy risks.** When you type information into a public AI tool, that input may be stored, used to train future models, or seen by the company running the tool. So do not enter patient names, employee records, financial account details, proprietary business data, or any confidential information into ChatGPT, Gemini, or similar public tools. If your organization has an AI usage policy, follow it. If you are unsure, ask your supervisor first.

      **Outdated information.** LLMs have a training cutoff, a point after which they know nothing. They cannot tell you about a law passed last month, a current drug interaction update, or today's prices. This matters most in fast-changing fields like healthcare regulation and compliance. Always confirm time-sensitive information against a current, primary source.

      > **Coming in Week 3.** An entire week on responsible use: real case studies of AI bias causing harm, your organization's privacy obligations, the ethical frameworks used to govern AI, and a personal checklist for responsible use on the job. Today's preview is just the first label.
- title: Practice and go deeper
  blocks:
  - type: activity
    title: Catch the hallucination
    body: |
      **Purpose:** to experience how convincing an AI hallucination can look, and to practice verifying before anything important leaves your hands.

      **Instructions:**

      1. Read the AI-generated passage below carefully. It looks professional and authoritative.
      2. Using a search engine, spend 10 to 15 minutes fact-checking the specific claims. Look for anything that seems off, invented, or impossible to verify.
      3. Mark any claims you could not confirm or found to be wrong.
      4. Note what you found for each claim: real, wrong, or can't verify.
      5. Be ready to share: how easy was it to spot the errors, and what would have happened if this had gone to a supervisor unverified?

      **The passage to fact-check:**

      > AI in the American Workplace: Key Facts and Figures
      >
      > Artificial intelligence has been reshaping the American workforce at a remarkable pace. According to a 2022 report published by the Society for Human Resource Management (SHRM), approximately 68% of U.S. employers reported using some form of AI in their hiring processes by the end of 2021, a figure that represented a 300% increase from 2018.
      >
      > The concept of machine learning was first formally defined by computer scientist Alan Turing in his landmark 1952 paper "Computing Intelligence and the Nature of Mind," published in the journal Nature. Turing's framework established the baseline criteria that researchers still use today.
      >
      > In healthcare, a widely cited 2023 study from Johns Hopkins University School of Medicine found that AI diagnostic systems correctly identified early-stage pancreatic cancer in 94% of cases, outperforming the average specialist accuracy rate of 71%. The study spanned 14 hospital systems in eight states and over 22,000 patient records.
      >
      > In logistics, companies like Amazon and FedEx have reported productivity gains of up to 40% in warehouse operations since adopting AI-powered routing and inventory systems, according to a 2023 analysis by the National Logistics Council, a Washington D.C. trade association founded in 1987.
      >
      > The legal profession has also seen adoption. The American Bar Association's 2023 Legal Technology Survey found that 51% of solo practitioners now use AI tools regularly for research and drafting, up from just 14% in 2020.

      **Reflection:** How many errors or unverifiable claims did you find? Were you surprised? How easy was it to spot them just by reading, without searching? Based on this, how will you verify AI content in your actual job?
  - type: lesson
    title: What you can do now
    body: |
      After this topic and the Catch the Hallucination activity, you should be able to:

      - Define AI hallucination and explain, in plain terms, why it happens.
      - Recognize the types of hallucination most likely to show up in real workplace output.
      - Apply the human-in-the-loop principle: AI proposes, human verifies, human decides, every time.
      - Match your verification effort to the stakes: light review for low-risk drafts, rigorous checking for anything patient-facing, legally relevant, or going to leadership.
      - Name three other limits, bias, privacy risks, and outdated information, and know that Week 3 goes deeper on all of them.

      You made it through the Day 1 foundations. Between now and next time, try one AI tool for a real task and save the result. You will bring it back.
  - type: lesson
    title: 'Dig deeper: recommended reading'
    body: |
      Each of these takes 5 to 15 minutes.

      - **The New York Times, "California issues historic fine over lawyer's ChatGPT fabrications."** The original reporting on the Mata v. Avianca case. A concrete look at what happens when AI output goes unverified.
      - **IBM, "What Is AI Hallucination?"** A clear, accessible explanation of why hallucinations happen and how organizations are working to address them.
      - **MIT Technology Review, "In AI We Trust, Too Much?"** Ongoing coverage of AI reliability and the challenge of knowing when to trust model outputs.
      - **Stanford HAI, "How Harmful Are AI's Biases on Diverse Student Populations?"** An accessible overview of how bias enters AI systems and why it is not a simple problem to solve.
      - **Anthropic, "Core Views on AI Safety."** A transparent look at how a leading AI lab thinks about the risks of its own models and what it is doing about them.
  - type: quiz
    title: Quick check
    body: |
      When you are ready, take the short quiz. It covers hallucinations, the verify-and-decide habit, matching effort to stakes, and the three other limits.

      I'll add the quiz link here once it is built. It opens in a new tab.
    quiz_url: ''
    quiz_label: Open the quiz
---
