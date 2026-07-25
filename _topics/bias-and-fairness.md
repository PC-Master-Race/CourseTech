---
title: Bias and Fairness in AI
slug: bias-and-fairness
category: ai
lead_in: 'Here is something that surprises a lot of people: AI tools are not fair just because they are automated. In fact, some of the most harmful AI outcomes look completely fair on the surface, precisely because they come from a machine and not a person. This lesson explains where unfairness in AI comes from, what it looks like in the real world, and why it matters for the work you do every day. Understanding it makes you a more careful, more valuable user of these tools.'
description: AI isn't neutral just because it's automated. Where bias comes from, and what it looks like.
video_url: ''
parts:
- title: Where bias in AI comes from
  blocks:
  - type: lesson
    title: It learns our patterns, including the unfair ones
    body: |
      Start with the most important idea in this lesson. AI learns from data, enormous amounts of it. That data was created by human beings, in human societies, over many years.

      Here is the problem: human societies have not always been fair. Hiring practices, lending decisions, housing policies, and healthcare access have all been shaped by discrimination, sometimes obvious, sometimes invisible, but real and documented. When AI trains on that historical data, it learns those patterns, including the unfair ones. Then it repeats them. Faster, and at a much larger scale.

      > **AI bias** happens when an AI system produces unfair outcomes for certain groups of people because the data it was trained on reflected past discrimination or imbalance. The AI is not "trying" to be unfair. It is simply repeating the patterns it found. But the harm to real people is just as real, regardless of intent.
- title: Bias you cannot see
  blocks:
  - type: lesson
    title: It is rarely obvious
    body: |
      Here is what makes AI bias especially hard to catch. It is rarely obvious. An AI hiring tool will not say "do not hire women" or "avoid this neighborhood." It is much more subtle.

      Instead, it might learn that resumes with certain first names have historically gotten lower ratings. Or that applicants from certain ZIP codes had higher turnover. Or that graduates of certain schools were less likely to be promoted. None of those patterns mean those people are less capable. They reflect historical inequalities in how opportunities were handed out. But the AI does not know that. It just sees the pattern and repeats it, quietly filtering people out before a human ever sees their application.
  - type: lesson
    title: 'A real example: Amazon''s hiring tool'
    body: |
      - Amazon built an AI tool to screen job applicants and rank them automatically.
      - It learned from historical hiring data, the resumes of people hired at Amazon over the previous decade.
      - Most of those hires were men, so the AI learned that male-pattern resumes were "better."
      - It began downgrading resumes that included the word "women's" (as in "women's chess club") and penalized graduates of all-women's colleges.
      - Amazon found the problem and shut the tool down. But it operated for years before anyone noticed.
- title: Predictive redlining
  blocks:
  - type: lesson
    title: An old injustice in a new form
    body: |
      You may have heard of **redlining**, the historical practice of denying loans, insurance, and services to people in certain neighborhoods, often based on race. It was declared illegal in the United States in 1968. But a new version is emerging with AI.

      > **Predictive redlining** happens when an AI system uses historical data to predict who will succeed in school or pay rent on time, and those predictions rest on data that reflects past inequality. The AI does not look at race directly. But it looks at ZIP codes, school names, and other factors closely linked to race because of historical discrimination. The result is that the same people who were excluded before get excluded again, this time by an algorithm.
- title: The deskilling risk
  blocks:
  - type: lesson
    title: Losing the skill to catch the mistakes
    body: |
      Here is one more concern, less dramatic but very real for your career.

      > **Deskilling** happens when workers rely on AI to make decisions they used to make themselves, and gradually lose the ability to make those decisions without it. Over time, they also lose the ability to catch the AI's mistakes, because they are no longer practicing the underlying skill.

      Think of a quality inspector at a factory. Every day, a computer vision system checks products. The inspector trusts it completely and stops looking carefully. Five years later, the system misses a serious defect, and the inspector cannot catch it either, because the skill has faded. What this means for you:

      - Use AI as a tool that supports your judgment, not a replacement for it.
      - Keep practicing the core skills of your field, even when AI can do them for you.
      - When AI gives you an output, review it with the knowledge of your field, not just common sense.
      - The ability to catch AI's mistakes is a professional skill. It takes staying sharp.

      *Magnifica Humanitas* speaks to this in its second chapter, tying it to the equal dignity of all human beings: any system, including AI, that treats people as less worthy based on where they were born, what language they speak, or what they look like violates a principle it calls non-negotiable, that every person has equal worth. (Source: Pope Leo XIV, *Magnifica Humanitas*, Ch. 2, vatican.va, May 15, 2026.)
- title: See it for yourself
  blocks:
  - type: activity
    title: Spot the bias live
    body: |
      Reading about bias is one thing. Seeing it in a tool you actually use is different. This uses ChatGPT so you can watch bias appear in real time, then try to correct it.

      1. Prompt ChatGPT with these three requests, one at a time: "Describe a successful accountant." "Describe a reliable contractor." "Describe a good teacher." Notice the language, the names, and the images implied.
      2. Ask yourself: what does the "default" person in each role look like? What assumptions are baked into the language?
      3. Now rewrite one of the three prompts to produce a more balanced, inclusive description. Run your new version and compare.
      4. Final question to sit with: does a better prompt fully remove the bias, or does it just make the bias less visible? What does that mean for using AI in hiring, evaluation, or recommendations at work?

      **Go further.** Write one review rule for your own field, a specific thing you will always check before using AI output that describes, evaluates, or recommends a person. Make it concrete enough that a coworker could follow it without you explaining. Then consider what your rule still would not catch, because every rule has a blind spot.
  - type: quiz
    title: Quick check
    body: |
      When you are ready, take the short quiz on where bias comes from, predictive redlining, and deskilling.

      I'll add the quiz link here once it is built. It opens in a new tab.
    quiz_url: ''
    quiz_label: Open the quiz
---
