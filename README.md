# Tutorial Hub

A standalone website for my vocational course content (AI at work, Excel, mobile
tech, and basic computing), separate from Canvas. Built with Jekyll and hosted on
GitHub Pages. Canvas can link to or embed these pages, but the content stays mine.

- **Live URL (project pages):** https://pc-master-race.github.io/CourseTech/
- **Editor (admin):** https://pc-master-race.github.io/CourseTech/admin/
- **Design system / tokens:** [`DESIGN.md`](DESIGN.md)

---

## How the site is put together

| Piece | Where | What it does |
|---|---|---|
| Navigation catalog | `_data/topics.yml` | One data file drives the mega menu and the home page |
| Topic pages | `_topics/*.md` | One Markdown file per topic. Front matter holds the parts and blocks |
| Page template | `_layouts/topic.html` | Renders header, video, on-page table of contents, and the lesson / activity / quiz blocks |
| Look and feel | `assets/css/style.css` + `DESIGN.md` | All colors, type, spacing, motion. Tokens live in both |
| Menu behavior | `assets/js/main.js` | Accessible mega menu, scroll reveal, active table-of-contents |
| Editor | `admin/` | Decap CMS form-based editing |

**Adding a topic is a content change, not a code change.** Add a file under
`_topics/` (or create it from `/admin`) and add one entry to `_data/topics.yml`
under the right category, using the same `slug`.

---

## Run it locally

You need Ruby (3.x) and Bundler.

```bash
gem install bundler
bundle install
bundle exec jekyll serve
```

Then open `http://localhost:4000/CourseTech/`.

> No Ruby handy? There is a plain-HTML preview of the built site in
> `preview/` (generated for a design check). It is not the real build, just a
> quick visual. The real site is what Jekyll produces from the files above.

---

## Deploy on GitHub Pages

1. Push this repo to `PC-Master-Race/CourseTech` on the `main` branch.
2. In the repo: **Settings > Pages**.
3. Under **Build and deployment**, set **Source = Deploy from a branch**,
   **Branch = `main`**, **Folder = `/ (root)`**. Save.
4. Wait a minute, then visit `https://pc-master-race.github.io/CourseTech/`.

### Moving to a custom domain later
Set `url` to your domain and blank out `baseurl` in `_config.yml`, add a file
named `CNAME` at the repo root containing your domain, and update `public_folder`
in `admin/config.yml` to `/assets/uploads`.

---

## Turning on the `/admin` editor

The admin panel (Decap CMS) lets you edit pages through a form and commits changes
straight back to this repo. It signs in with your GitHub account. GitHub Pages
cannot run the sign-in handshake by itself, so you need one small, free helper
service (an "OAuth relay"). You set this up once.

1. **Register a GitHub OAuth app.** GitHub > Settings > Developer settings >
   OAuth Apps > New OAuth App.
   - Homepage URL: `https://pc-master-race.github.io/CourseTech/`
   - Authorization callback URL: the URL of your relay (from step 2).
   - Save the **Client ID** and **Client Secret**.
2. **Deploy a tiny OAuth relay.** Any of these free options work; each has a
   one-click template in its docs:
   - Cloudflare Workers (search "decap cms cloudflare oauth")
   - Vercel or Netlify (search "decap cms oauth provider")
   Give it the Client ID and Secret from step 1.
3. **Point the CMS at your relay.** In `admin/config.yml`, uncomment `base_url`
   under `backend:` and set it to your relay's URL.
4. Visit `/admin/`, click **Login with GitHub**, and you are in.

Until this is set up, the site itself works fully. Only the editor needs it.

### What you can do in the editor
- Edit any page's text, headings, and the order of parts and blocks.
- Add or remove Lesson, Activity, and Quiz blocks.
- Upload images. **Alt text is required**, so an image cannot be saved without a
  description (this keeps the site accessible).
- Set or change a page's YouTube video link, or leave it blank.
- Add new topics, and add them to the menu under "Site navigation."

---

## Writing new content (voice rules)

So every page sounds like the same instructor:

- First person, talking straight to the student. "Let's open Excel together,"
  not "Users should open Excel."
- 8th to 9th grade reading level. Define any technical word the first time.
- Prefer bullets, numbered steps, and tables over long paragraphs.
- No em dashes anywhere.
- Skip AI-writing tells (no "delve," "leverage," "unlock," forced groups of three,
  or paragraphs that all feel the same length). Vary the rhythm.
- Warm and direct, like someone who wants the student to succeed.

---

## Accessibility notes

This site targets WCAG 2.1 AA. Key choices are in `DESIGN.md`. Highlights:
semantic landmarks, a skip link, a keyboard-operable mega menu (Escape closes it),
visible focus rings, an 18px base font for older adults, and lesson / activity /
quiz blocks marked by color **plus** an icon and a text label so meaning never
depends on color alone. All color pairs meet AA contrast.
