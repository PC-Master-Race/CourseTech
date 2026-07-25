---
title: Local AI vs. Hosted AI
slug: local-vs-hosted-ai
category: ai
lead_in: 'Every AI tool you use runs in one of two places: on someone else''s computer, or on your own. Most people use the first kind every day without realizing it. The second kind is newer and comes with very different rules about privacy, cost, and what your computer needs to handle. This lesson breaks down the difference, especially the privacy side, which matters a lot if you work with sensitive information. It''s also the final lesson, so I''ll close with where to go from here.'
description: Runs on their computer or yours? The difference in privacy, cost, and what your machine needs.
video_url: ''
parts:
- title: The two kinds of AI
  blocks:
  - type: lesson
    title: Hosted and local, defined
    body: |
      > **Hosted AI** runs on a company's servers and you reach it through a website or app. ChatGPT, Gemini, Claude, and Microsoft Copilot are all hosted. Your prompt travels over the internet to their computers, gets processed there, and the response comes back. You do not need a powerful computer, because the heavy work happens on their end.

      > **Local AI** runs entirely on your own computer, with no internet needed. The model is downloaded and stored on your hard drive. When you send a prompt, it is processed right on your machine and the response comes back without any data leaving your device. This needs a computer with enough power to run the model, which we will get to.
- title: 'Privacy: the biggest practical difference'
  intro: The most important difference, especially for your job, is what happens to the information you type in.
  blocks:
  - type: lesson
    title: Where your data goes
    body: |
      | Question | Hosted AI | Local AI |
      |---|---|---|
      | Where does my data go? | Your prompt goes to the company's servers. Logs are often saved even if you would rather they were not, partly for legal reasons, and your chats may be used to improve their model unless you opt out. | Nowhere. Your data never leaves your computer. It is processed locally and stays on your device. |
      | Can my employer or a client see what I type? | Possibly. With an enterprise version like Copilot, admins usually have access to logs. Free consumer versions vary by provider. | No. Nothing is transmitted. Only someone with physical access to your computer could see it. |
      | Is it safe for sensitive data (patient or financial records)? | Generally not recommended without an enterprise contract and a data agreement. Consumer versions should never receive confidential client data. | Yes. This is one of the main reasons people run local AI. Sensitive data stays on your machine. |

      > **Free vs. enterprise accounts.** Free accounts on ChatGPT, Gemini, and Claude are consumer products, and the companies may use your conversations to improve their models. Never type patient names, Social Security numbers, client financial details, student records, or any confidential information into a free consumer AI account. Enterprise accounts have different terms that usually prohibit training on your data, but always read the policy before you type anything sensitive.
- title: What it takes to run local AI
  intro: Running AI locally means your computer does all the work. Think of the difference between streaming a movie (hosted) and playing a video game stored on your computer (local). The game needs a machine powerful enough to run it. Local AI is the same. Here is what the key terms mean.
  blocks:
  - type: lesson
    title: Memory, GPU, storage, and processor
    body: |
      - **Memory (RAM):** your computer's short-term memory, the space it uses for what it is actively working on. Running a local model needs a lot of it. A small model might run comfortably in 8 GB, while a larger one might need 32 GB or more. Most everyday laptops have 8 to 16 GB, enough for smaller local models.
      - **GPU (graphics processing unit):** a chip originally built for video games. The same math it is good at is exactly what AI models need, so a dedicated GPU (like NVIDIA's) is much faster than the main processor alone. It can be the difference between a 30-second response and a 2-second one. The GPU's own memory is called **VRAM**, and bigger models need more of it.
      - **Storage (hard drive or SSD):** model files are large, from 4 to 8 GB for a small model up to 20 to 70 GB or more for a big one. You need free space to store them, and a faster SSD or NVMe drive loads them more quickly.
      - **CPU (central processing unit):** your main processor. Without a dedicated GPU, the CPU does all the AI work. That still works, just slower, unless your computer has newer "unified memory," which many Macs and some newer PCs have. On a budget, a modern CPU can get smaller models done. It just takes more patience.
  - type: lesson
    title: 'Model size: what 3B vs 30B means'
    body: |
      You will often see numbers like 3B, 7B, 13B, or 30B. The B stands for billion, meaning the number of **parameters**, the internal settings adjusted during training. More parameters generally means the model handles more complex questions and gives more nuanced answers, but it is also bigger, slower, and needs more powerful hardware.

      | Model size | Good at | Limits | Hardware needed |
      |---|---|---|---|
      | **3B** | Simple tasks: basic questions, short summaries, casual conversation, light writing help. | Struggles with complex reasoning or multi-step tasks. More factual errors. | Most modern laptops with 8 GB RAM. No GPU required. |
      | **7B** | A solid everyday model: drafting emails, summarizing documents, basic coding help. | Limited on highly technical topics. Slower without a GPU. | 8 to 16 GB RAM. Better with a GPU, but works on CPU. |
      | **13B to 30B** | Noticeably smarter: complex instructions, longer accurate content, reasoning through problems. | Needs more powerful hardware. Slow without a dedicated GPU or unified memory. | 16 to 32 GB RAM. A dedicated GPU (8 GB+ VRAM) strongly recommended. |
      | **70B and above** | Approaches the quality of top hosted models. Excellent reasoning and analysis. | Needs very powerful, expensive hardware most people do not have at home. | 64 GB+ RAM. A high-end GPU (24 GB+ VRAM). |
- title: Local vs. hosted at a glance
  blocks:
  - type: lesson
    title: Side by side
    body: |
      | | Local AI | Hosted AI |
      |---|---|---|
      | **Privacy** | Strong. Data never leaves your device. Ideal for confidential work. | Free accounts may use your data for training. Enterprise offers more protection, but your data still sits with a third party and can be subject to legal discovery. |
      | **Cost** | Free after setup. No subscription. You pay for hardware once. | Free tiers exist but are limited. Stronger features usually need a subscription ($20 to $200+ a month). |
      | **Internet** | Not required. Works fully offline once downloaded (you can enable web search if you want). | Required. No internet, no access. |
      | **Ease of setup** | More technical. You download software and model files. Not plug-and-play, and it can be finicky to fix. | Very easy. Visit a website, make an account, start typing. |
      | **Capability** | Depends on model size and your hardware. Smaller models are less capable, but quality is consistent and fully under your control. | Access to the most capable models available, though quality can vary with the provider's infrastructure and settings you do not control. |
      | **Updates** | Manual. You choose when to download a new version. | Automatic. You always get the latest version your plan allows. |
      | **Best for** | Privacy-sensitive work and people who want full control. | Beginners and most everyday workplace tasks, and teams that want high-quality output with no setup. |
- title: Where you go from here
  blocks:
  - type: lesson
    title: You came in curious, you are leaving capable
    body: |
      That is the whole course. You now know what AI actually is, how to use it, where it falls short, when to be careful, and how it fits your specific field. Most people have not done that work. Five things to carry forward:

      - **Keep using the tools.** The only way to get better is to keep going. Pick one task from your plan and try it with AI this week. If it works, great. If not, adjust and try again.
      - **Stay current.** AI moves fast. Following one or two people who cover AI in your industry keeps you informed without being overwhelmed.
      - **Know your workplace's policy.** Before using AI at work with real client or patient data, find out if your employer has an AI use policy. If they do not, that is an opportunity: you now know enough to help write one.
      - **Teach someone else.** The best way to lock in what you learned is to explain it to someone who does not know it yet.
      - **Come back to your commitment.** If you wrote down how you intend to use AI, keep it somewhere visible. In a few months, look again and ask: am I actually doing this?

      The workers who shape how AI is used in their workplaces will be the ones who understood it early, asked the hard questions, and kept the human at the center. That is exactly what you did here. Go do something great with it.
  - type: activity
    title: Make your plan real
    body: |
      One last step to turn everything into action.

      1. Pick the single AI task from your field you are most ready to try.
      2. Write the tool you will use, and the first prompt you will type.
      3. Name the one check you will always do before the output is used, your human-in-the-loop step.
      4. Do it once this week. Then note what worked and what you would change.

      **Go further.** Decide whether your task belongs on hosted or local AI, and defend it using the privacy question specifically: what exactly are you typing in, and who could see it? If the honest answer makes you uneasy, that is your signal to change either the tool or the information you feed it.
  - type: quiz
    title: Quick check
    body: |
      When you are ready, take the short quiz on hosted vs. local AI, privacy, and what it takes to run a model on your own computer.

      I'll add the quiz link here once it is built. It opens in a new tab.
    quiz_url: ''
    quiz_label: Open the quiz
---
