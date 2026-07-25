---
title: Advanced Prompting Techniques
slug: advanced-prompting
category: ai
description: From framework to fluency. Four techniques that turn good prompts into professional-grade output.
lead_in: Once the basics feel natural, a few extra moves take your results from good to genuinely professional. In this lesson I will show you four techniques the best AI users lean on every day, and just as important, how to tell when to put the tool down and handle something yourself. None of it needs any technical background.
video_url: ''
parts:
- title: From RTCF to fluency
  intro: 'Estimated time: 35 minutes. Format: read, apply, and run the tournament. Tools: ChatGPT or Gemini.'
  blocks:
  - type: lesson
    title: Layering technique on top of the framework
    body: |
      In "Prompting Fundamentals" you learned RTCF. It gives you a reliable starting point, and for many everyday tasks it is all you need. But the most effective users do not stop there. They layer extra techniques on top to get output that is more accurate, more tailored, and more immediately useful.

      This topic covers four techniques that professionals use daily. None of them require technical knowledge, and all of them are learnable in a single session. By the end of the Prompt Tournament activity, you will have practiced each one on a real task and seen the difference with your own eyes.

      You can picture the four levels as a staircase: a basic prompt, then RTCF, then few-shot plus chain-of-thought, then persona plus iterative refinement. Each step up produces noticeably better work.
- title: 'Technique 1: few-shot prompting'
  intro: 'The name sounds technical, but the idea is simple: before you ask for what you want, show the AI an example of exactly what you want.'
  blocks:
  - type: lesson
    title: Show it a finished example
    body: |
      You give the model a few "shots," sample inputs and outputs, so it picks up the pattern, tone, format, and level of detail you expect.

      Think of it like training a new employee. Instead of describing the job in the abstract, you hand them a finished example and say: "Here is what a good one looks like. Now do one like this for the new situation." The AI picks up the pattern and copies it.

      There are three levels:

      - **Zero-shot:** no examples, just the request. Fine for simple tasks.
      - **One-shot:** one example. Works well for most professional formatting tasks.
      - **Few-shot:** two or more examples. Use it when the format or style is very specific and hard to describe in words.
  - type: lesson
    title: Side by side
    body: |
      | Without an example (zero-shot) | With one example (one-shot) |
      |---|---|
      | "Write a follow-up email after a job interview." | "Write a follow-up email after a job interview. Here is the tone and length I want. Example: 'Hi Ms. Chen, Thank you for taking the time to meet with me yesterday about the Medical Records Coordinator role. I enjoyed learning about your team's workflow and am excited about the opportunity. Please let me know if you need anything else. I look forward to hearing from you. Best, Maria.' Now write a similar email for someone who interviewed for a Warehouse Supervisor position at a logistics company." |
      | **Result:** generic, often too long, may miss the industry entirely. | **Result:** matches the tone, length, and warmth of your example, ready to send or lightly edit. |

      In your work, this means when you have a format that works, a successful email, a good summary, a well-written report, save it. It becomes your example the next time you need something similar. The AI learns from your best work.
- title: 'Technique 2: chain-of-thought prompting'
  intro: A standard prompt asks for an answer. A chain-of-thought prompt asks the model to think through the problem step by step first.
  blocks:
  - type: lesson
    title: Ask it to show its work
    body: |
      One instruction does it: "Think step by step before responding." This reliably improves output on tasks that involve reasoning, analysis, planning, or multi-step decisions.

      It works because of how LLMs generate text. When a model is made to spell out its reasoning instead of jumping to a conclusion, it surfaces assumptions, catches contradictions, and produces more defensible answers. It is the AI version of showing your work.

      You can trigger it with phrases like "Think step by step," "Walk me through your reasoning," or "Before you answer, explain your logic." It is best for complex decisions, multi-step procedures, analysis, troubleshooting, building checklists, and any case where the process matters as much as the final output.
  - type: lesson
    title: Two versions of the same prompt
    body: |
      | Standard prompt | Chain-of-thought prompt |
      |---|---|
      | "You are a healthcare office manager. Write a plan for reducing patient no-shows at our clinic." | "You are a healthcare office manager. Think step by step about the root causes of patient no-shows before writing a plan to reduce them. First identify the most common reasons patients miss appointments. Then propose one action for each cause. Finally, summarize the three highest-priority actions." |

      The chain-of-thought version produces a structured, reasoned plan instead of a generic list. Better still, you can read the reasoning and catch it if the AI made a wrong assumption about your clinic. The standard version gives you a finished answer you cannot question.
- title: 'Technique 3: persona and constraint prompting'
  intro: 'RTCF''s Role sets who the AI is writing for. Persona plus constraint prompting goes further: give the AI a clear identity, then set boundaries on what it should never do, always include, or specifically avoid.'
  blocks:
  - type: lesson
    title: The structure
    body: |
      The pattern is easy to remember:

      > You are [specific persona]. Never [constraint to avoid]. Always [positive constraint]. [Then give your task.]

      The persona tells the AI the expertise level, vocabulary, and judgment to apply. The constraints shape every sentence. Without them, even a well-defined persona can drift into generic responses.
  - type: lesson
    title: The same structure across workplaces
    body: |
      | Field | Persona | Constraints added |
      |---|---|---|
      | **Healthcare** | A patient care coordinator writing discharge instructions | Never use medical jargon without defining it. Always include a phone number for questions. Never give specific medication dosages. |
      | **Logistics / warehousing** | A warehouse supervisor writing a daily safety briefing for 12 people | Always lead with the most critical hazard of the day. Never exceed 150 words. Always end with a one-sentence motivation line. |
      | **Business / administration** | An executive assistant drafting a response to a client complaint | Never admit fault on the company's behalf without approval. Always acknowledge the client's frustration in the first sentence. Never use passive voice. |
      | **Early childhood education** | A preschool teacher writing a weekly parent newsletter | Always use a warm, encouraging tone. Never use acronyms or jargon. Always include one specific classroom highlight. |
      | **Retail / customer service** | A customer service specialist replying to a negative online review | Never be defensive. Always thank the customer for their feedback. Never promise a resolution you cannot guarantee. |

      Pro tip: start with just one constraint and see what it changes. Then add a second. Adding constraints one at a time shows you which boundaries actually shape the output and which are redundant. That leads straight into the next technique.
- title: 'Technique 4: iterative refinement'
  intro: 'The biggest mistake new users make is treating every prompt as one transaction: one prompt, one output, done. Professionals use AI the way a good editor uses a draft, as the start of a conversation, not the end.'
  blocks:
  - type: lesson
    title: Cycle toward the answer
    body: |
      Iterative refinement means deliberately cycling: generate a first draft, decide what works and what does not, then send a short follow-up that targets exactly what needs to change. Each cycle gets closer. Because the AI keeps the context of your conversation, your follow-ups can be short and precise.

      Here is a real example, drafting a professional email to a difficult vendor:

      | Round | Prompt sent | What to evaluate and refine |
      |---|---|---|
      | **1, initial** | "You are a purchasing manager. Write an email to our vendor about a late delivery that is hurting our production schedule." | Is the tone right? Is the problem clear? Too aggressive or too passive? Does it say what you need from them? |
      | **2, refine tone** | "The email is too formal. Make it more direct but still professional. We need them to commit to a delivery date by end of business today." | Is there a clear deadline? Is the urgency felt without being hostile? Would you send this? |
      | **3, add specifics** | "Add that this is the third late delivery in two months, and that we will review our contract if it continues." | Does the new information shift the tone appropriately? Is the escalation clear without being a legal threat? |
      | **4, final polish** | "Tighten it to under 100 words. Cut anything that sounds like filler." | Is it concise? Is every sentence pulling weight? Read it aloud. Does it sound like you? |

      The mindset shift: AI does not have to get it right the first time, and neither do you. What matters is that each cycle is intentional. You know what you are improving and why. That deliberateness is what separates a professional user from someone who pastes in a task and hopes.
- title: 'When not to use AI: the professional judgment line'
  intro: These four techniques make AI more powerful, which makes it even more important to know where AI should not be your tool. Knowing this line is professional competence, not skepticism.
  blocks:
  - type: lesson
    title: Five situations to step in yourself
    body: |
      | Poor fit for AI | Why it falls short | What to use instead |
      |---|---|---|
      | Real-time or live data | LLMs have a training cutoff. They cannot give today's price, current inventory, live patient status, or breaking regulatory updates. | Your organization's live systems, verified government sites, or real-time dashboards. Use AI to interpret data once you have it. |
      | Physical judgment or hands-on assessment | AI cannot observe, touch, or experience the physical world. It cannot judge a patient's skin color, a machine's vibration, or whether a joint looks right. | Your own trained senses. AI can help document or research after the assessment, not replace it. |
      | Legal accountability and binding decisions | AI is not a licensed attorney or certified professional. Its output is not legally defensible. | A qualified professional for any decision with legal or contractual weight. Use AI to draft or research, then have it reviewed. |
      | Highly confidential or personal information | Entering protected health info, Social Security numbers, or trade secrets into a public tool creates real privacy and compliance risk. | Your organization's approved internal tools, or handle it manually. Know your AI usage policy. |
      | Situations needing genuine human empathy or authority | A termination, delivering bad news, addressing a crisis. These need a human presence and accountability AI cannot replicate. | Your own judgment and interpersonal skill. AI can help you prepare talking points, but the conversation is yours. |

      The goal is not to avoid AI. It is to use it where it genuinely helps and step in where it genuinely does not. That judgment is what employers are starting to look for: not just "can this person use AI," but "does this person know when not to."
- title: Practice and wrap up
  blocks:
  - type: activity
    title: The Prompt Tournament
    body: |
      **Purpose:** to see, side by side, how each layer of technique changes the quality and usability of AI output. By the end you will have a concrete answer to: "Which version would I actually use at work?"

      **The task:** draft a professional response to an upset customer or client. Pick the scenario that fits your field:

      - **Healthcare / social services:** a patient is upset about an unexpected bill and left an angry voicemail. Draft a written response.
      - **Business / logistics / retail:** a customer is angry about a delayed order and posted a negative review. Draft a professional response.
      - **Education / community services:** a parent is upset about a decision or miscommunication and sent an angry email. Draft a response that de-escalates and invites dialogue.

      **Run all three rounds in the same chat** so the AI builds on the context.

      1. **Round 1, basic prompt.** Type a simple, natural request. No RTCF, no structure. The kind of prompt you would have written before this course.
      2. **Round 2, add RTCF.** Rewrite the same task with a specific Role, a precise Task, real Context about the situation and audience, and your preferred Format.
      3. **Round 3, add few-shot and chain-of-thought.** Build on your RTCF prompt. Add one example of the tone and length you want (quote a sentence or two you consider professional), then add: "Before writing, think step by step about what this customer needs to hear and why. Then write the response."

      **Evaluate all three.** For each question, which round wins: Which is closest to something you would actually send? Which best matches your field's tone? Which needs the least editing? Which shows the most professional judgment?

      **Reflect:** Which round produced something usable without major editing, and what made it better? How much longer did the Round 3 prompt take, and was it worth it? Where in your job would a Round 1 prompt be enough, and where is Round 3 worth the effort?
  - type: lesson
    title: What you can do now
    body: |
      After this topic and the Prompt Tournament, you should be able to:

      - Use few-shot prompting by giving the AI one or more examples of the format, tone, or structure you want before you make your request.
      - Apply chain-of-thought instruction to get the AI to reason through complex problems step by step, producing more defensible, checkable output.
      - Build persona and constraint prompts that define who the AI is writing as and set clear boundaries on what it should always and never do.
      - Practice iterative refinement, treating the conversation as a draft cycle rather than a single transaction.
      - Identify where AI is the wrong tool: real-time data, physical judgment, legal accountability, confidential information, and high-stakes human conversations.
  - type: quiz
    title: Quick check
    body: |
      When you are ready, take the short quiz on the four techniques and the judgment line.

      I'll add the quiz link here soon. It opens in a new tab.
    quiz_url: ''
    quiz_label: Open the quiz
---
