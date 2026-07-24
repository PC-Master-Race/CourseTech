---
title: Image AI, A Practical Intro
slug: image-ai
category: ai
description: Expanding beyond text. What image AI can do at work, where it falls short, and how to prompt it well.
lead_in: So far everything has been about words, but AI can make pictures too, and it is already showing up in workplaces like yours. In this lesson you will learn what image AI can do, where it falls short, and how to write a prompt that gives you something you can actually use. I will be honest with you about the limits so you do not get burned.
video_url: ''
parts:
- title: 'Beyond text: a new tool in your kit'
  intro: 'Estimated time: 25 minutes. Format: read and generate one image. Tools: Gemini or Canva AI.'
  blocks:
  - type: lesson
    title: What image AI is for
    body: |
      Everything so far, RTCF, chain-of-thought, persona and constraint, iterative refinement, has been about text. Text is where most workplace value lives right now. But there is a second kind of tool worth understanding, because it is already showing up in your field: image generation.

      **Image AI** tools create original visuals from a written description. Marketing teams mock up campaigns in minutes. Healthcare educators make training diagrams without a graphic designer. Logistics companies make safety signage. Construction firms make site-layout visuals. The technology is not perfect, and this topic will be honest about what it cannot do, but it is real, it is accessible, and it is already part of professional workflows in every industry in this room.

      This is a short introduction. You will learn how these tools work, where they fit, which ones to use, their limits, and how to write an image prompt that gives you something usable. Then you will generate one.
- title: How image generation actually works
  intro: You do not need the math. But knowing the basic mechanism explains why these tools behave the way they do, why they sometimes produce brilliant results and sometimes a person with six fingers.
  blocks:
  - type: lesson
    title: Diffusion models, in plain English
    body: |
      Tools like Gemini, Adobe Firefly, and DALL-E are built on something called a **diffusion model**. During training, the model was shown millions of images, photographs, illustrations, diagrams, paintings, each paired with a text description. It learned the statistical relationships between words and visual patterns.

      When you type a prompt, the model does not search a database or paste images together. It starts with random visual noise, imagine static on a television, and gradually refines that noise, guided by your text, until a coherent image emerges. Each step moves the image closer to your description.

      Why this matters: the model is generating something statistically plausible, not looking up the correct answer. That is why it can produce a stunning, photorealistic hospital room but put the outlets in the wrong place, or write text on a sign that looks like letters but spells nothing. It learned what images look like, not what the world is actually like.

      The takeaway for work: image AI is a powerful drafting tool, not a production tool. It gets you to a starting point fast. A professional designer, educator, or subject-matter expert still needs to check the output for accuracy and quality before it goes anywhere important.
- title: What image AI can do at work, by industry
  intro: This is not a future prediction. These are current uses that workers in these fields are already trying.
  blocks:
  - type: lesson
    title: Use cases and realistic time savings
    body: |
      | Field | Use cases | Realistic time savings |
      |---|---|---|
      | **Healthcare & patient services** | Patient education diagrams, anatomy illustrations, multilingual signage, staff training visuals | Cuts out hours of stock-photo searching or waiting on a designer. A training flyer that took 2 days now takes 20 minutes. |
      | **Logistics, warehousing & manufacturing** | Safety posters, equipment layout diagrams, hazard-zone visuals, onboarding guides | Safety signage that needed a vendor can be mocked up in-house in under an hour, then refined with a designer. |
      | **Business administration & office** | Presentation visuals, report infographics, headshots (with caveats), social media graphics | A slide visual that would have needed a stock site or a designer can be made and customized in minutes. |
      | **Early childhood & education** | Classroom illustrations, story visuals, newsletter headers, culturally inclusive imagery | Teachers can create visuals that reflect their specific student community instead of generic stock. |
      | **Retail, marketing & customer service** | Product mockups, promotional flyers, campaign images, seasonal graphics | Small businesses without a design budget can make professional-looking materials for pennies per image. |
      | **Construction, trade & technical** | Site layout visuals, compliance posters, procedure diagrams, equipment ID guides | Job aids that once needed professional illustration can be drafted quickly, then polished by a designer. |
- title: The tools, a brief comparison
  intro: You do not need to master every tool. You need to know which one fits your situation. Here are the three you are most likely to meet.
  blocks:
  - type: lesson
    title: Gemini, Canva AI, and Adobe Firefly
    body: |
      | Comparison point | Gemini (Google) | Canva AI (Magic Studio) | Adobe Firefly |
      |---|---|---|---|
      | **Best for** | General workplace use, built into Google Docs, Gmail, and Slides. A great starting point, and good at text in images. | Non-technical users who want drag-and-drop design alongside AI. Great for flyers and presentations. | High visual quality, best for marketing and professional materials, built into Adobe Creative Cloud. |
      | **Ease of use** | Easy. In the Gemini app and Google Workspace. No design experience needed. | Very easy. The most beginner-friendly. Templates take you from prompt to finished design fast. | Moderate. More powerful, but works best if you know some Adobe tools. |
      | **Legal / copyright** | Available for personal and commercial use per Google's terms. Always check current policy. | Licensed for commercial use within Canva's terms. Note the free vs. Pro differences. | Trained only on Adobe Stock and openly licensed content. Currently the safest for professional commercial use. |
      | **Free access?** | Yes, with a free Google account. Some features need Gemini Advanced. | Yes, free tier. Some AI features need Canva Pro (about $15/month). | Limited free tier. Full access needs a Creative Cloud subscription. |

      For a first activity, Gemini (free, no download, works on phones) or Canva AI (free tier, most beginner-friendly) are easiest. If you have an Adobe account, Firefly is excellent. Avoid tools that require an email sign-up on the spot.
- title: 'Key limitations: use image AI carefully'
  intro: These are not small bugs waiting for a patch. They come from how the models work. Understanding them is part of being a responsible user.
  blocks:
  - type: lesson
    title: 'Accuracy errors: the six-fingers problem'
    body: |
      Image models are trained on patterns, not on how the world actually works. So they can produce anatomically wrong hands, sign text that looks real but says nothing, architecture that breaks physics, and equipment with the wrong number of parts or buttons.

      **Professional guidance:** always have a subject-matter expert review any generated image that shows a procedure, a piece of equipment, or a physical space, especially in training materials, safety documentation, or patient communications, where accuracy affects people.
  - type: lesson
    title: Bias in visual representation
    body: |
      Models trained on internet data inherit the biases in that data. A prompt for "a doctor" may default to one demographic. A prompt for "a worker" may not reflect your actual workforce. A prompt for "a family" may reflect cultural defaults that do not match your community. These defaults are not always obvious until you look critically.

      **Professional guidance:** be specific in your prompts about representation. If your workplace or community is diverse, describe that explicitly. Review generated images for stereotyping before using them.
  - type: lesson
    title: Legal and copyright uncertainty
    body: |
      The legal picture around AI images is still evolving. Questions about copyright, ownership, and commercial licensing are being decided in courts right now. Adobe Firefly was trained on licensed content specifically to lower legal risk. Other tools have less clear provenance. Using AI images in published marketing, commercial products, or official documents carries some legal uncertainty.

      **Professional guidance:** for commercial or high-stakes use, Firefly is the lowest-risk option. For internal drafts and mockups, most tools are fine. When in doubt, check your organization's policy, and for important materials, ask your legal or compliance team.
  - type: lesson
    title: AI images cannot show your real situation
    body: |
      A generated image is always generic in some way. It shows a plausible version of something, not your specific workplace, your team, your product, or your patient. For materials that must be specific, a safety poster for your actual facility, training with your actual equipment, an AI image is a starting point, not a finish line.

      **Professional guidance:** use AI images for drafting and mockups. For final materials that need to reflect a real-world context, work with a photographer or designer to capture or customize the real thing.
- title: Prompting for images
  intro: 'The same ideas that make text prompts better, specificity and context, apply to images. The difference is that "format" now includes visual elements: style, composition, lighting, color, and medium.'
  blocks:
  - type: lesson
    title: The five-part formula
    body: |
      Use this structure: **Subject + Setting + Style + Mood + Format.**

      - **Subject:** who or what is in the image. Not "a worker" but "a female warehouse supervisor in her 40s wearing a hard hat and safety vest, reviewing a clipboard."
      - **Setting:** where the scene is and what surrounds the subject. Not "a workplace" but "a busy warehouse with shelving and boxes in the background, natural daylight from overhead windows."
      - **Style:** photorealistic, flat illustration, watercolor, infographic, technical diagram, professional photography, hand-drawn sketch, minimalist icon.
      - **Mood:** professional and calm, energetic and bright, warm and welcoming, clinical and clean, serious and authoritative.
      - **Format:** aspect ratio, orientation, or use. Landscape 16:9 for a slide, square for social media, portrait for a flyer, white or transparent background for a logo.
  - type: lesson
    title: Vague versus specific
    body: |
      | Vague prompt (weak) | Specific prompt (usable) |
      |---|---|
      | A nurse | A female nurse in her 30s with natural hair, wearing teal scrubs and a stethoscope, standing in a bright modern clinic hallway, smiling warmly at the camera, photorealistic professional photography, natural lighting, 16:9 landscape |
      | Safety poster | A workplace safety poster showing a warehouse worker in full PPE (hard hat, safety vest, steel-toe boots, gloves) next to clearly labeled safety equipment, with a bold header area at the top for text, flat illustration style, high-contrast colors, portrait orientation for printing |
      | Training diagram | A clean step-by-step training diagram showing 4 numbered steps for hand-washing, each with a simple clear icon, minimalist infographic style, blue and white color scheme, horizontal layout for a printed handout |

      Quick tip: start with your subject and style. If the result is not right, refine just like you would with text. Most image tools accept follow-ups in the same session: "Make the background white." "Change her uniform to navy blue." "Remove the text from the sign."
- title: Practice and go deeper
  blocks:
  - type: activity
    title: Generate for your field
    body: |
      **Purpose:** to move from understanding image AI to using it, generating one work-relevant image, evaluating it honestly, and building the habit of checking before any AI visual is used professionally.

      **Your task:** generate one image relevant to your trade, program, or job. Pick the format that would save you the most time:

      - A **training diagram**: a step-by-step visual, safety procedure, or labeled diagram for your field.
      - A **workplace flyer or poster**: an announcement, safety notice, or promotional flyer.
      - A **product or service mockup**: a visual of a product, service, or space in your industry.
      - A **presentation visual**: an image for a slide deck or report you might actually give.

      **Beginner path, fill-in template.** Paste this into Gemini or Canva AI, filling the brackets: "A [photorealistic / flat illustration / professional diagram] showing [what you want to show] in a [setting]. The image should feel [professional / warm / clinical / energetic]. [Portrait / landscape / square] orientation, suitable for [a training handout / a poster / a slide]." Example: "A flat illustration showing a warehouse worker in full PPE checking items against a clipboard, with shelving in the background. Professional and clear. Landscape orientation, suitable for a training handout."

      **Advanced path.** Write your own prompt with the five-part formula, then generate it twice with different styles: Version A "photorealistic professional photography," Version B "clean flat illustration, minimal color palette." Which would you actually use, and why?

      **Critique your output honestly:**

      - Is it accurate? Does anything look physically wrong or technically off for your field?
      - Is it usable as-is, or does it need editing? What specifically?
      - Would you actually use it at work, as a draft, a mockup, or a final?
      - How long did it take versus creating it from scratch or finding a stock image?
      - Any bias, representation, or appropriateness concerns for your audience?
  - type: lesson
    title: What you can do now
    body: |
      After this topic and the Generate for Your Field activity, you should be able to:

      - Explain in plain terms how diffusion-based image models work, and why they produce confident-but-sometimes-wrong results.
      - Name at least three workplace use cases for image AI in your field.
      - Compare Gemini, Canva AI, and Adobe Firefly, and pick the right one for a situation.
      - Recognize the four key limitations: accuracy errors, bias, legal uncertainty, and lack of real-world specificity.
      - Write a specific image prompt with the five-part formula and refine it.
      - Evaluate an AI image critically before using it: accuracy, representation, usability, and legal appropriateness.
  - type: lesson
    title: 'Dig deeper: recommended reading'
    body: |
      - **Canva, "Canva AI Features and Magic Studio Overview."** A plain-English explanation of Canva's AI image tools. A great, accessible starting point.
      - **"Getting Started with AI Image Generators."** An overview of the ethical and legal side of AI images: copyright, artist rights, and what "training data" really means for creators.
      - **Harvard Business Review, "Generative AI Has an Intellectual Property Problem."** A clear look at the legal risks of using AI images commercially. Important context before you use them at work.
  - type: quiz
    title: Quick check
    body: |
      When you are ready, take the short quiz on how image AI works, the four limitations, and the five-part prompt formula.

      I'll add the quiz link here soon. It opens in a new tab.
    quiz_url: ''
    quiz_label: Open the quiz
---
