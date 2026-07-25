#!/usr/bin/env python3
"""
Local preview renderer for Tutorial Hub.

Not part of the Jekyll build. This mimics the site closely enough to eyeball
layout and content changes without installing Ruby. Jekyll remains the source
of truth. Run:  python3 _dev/preview.py
Output goes to ./preview/
"""
import yaml, glob, os, re, html as _html, markdown

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT  = os.path.join(ROOT, "preview")
for sub in ("assets/css", "assets/js", "assets/downloads"):
    os.makedirs(os.path.join(OUT, sub), exist_ok=True)

def read(p): return open(os.path.join(ROOT, p), encoding="utf-8").read()
def write(p, s): open(os.path.join(OUT, p), "w", encoding="utf-8").write(s)

write("assets/css/style.css", read("assets/css/style.css"))
write("assets/js/main.js",   read("assets/js/main.js"))
write("assets/favicon.svg",  read("assets/favicon.svg"))
try: write("assets/downloads/job-search-pipeline.md", read("assets/downloads/job-search-pipeline.md"))
except Exception: pass

icons = re.sub(r"{%-?.*?-?%}", "", read("_includes/icons.svg"), flags=re.DOTALL)
nav   = yaml.safe_load(read("_data/topics.yml"))
md    = markdown.Markdown(extensions=["tables", "sane_lists", "fenced_code"])
FM    = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.DOTALL)

def icon(n, cls="icon"): return f'<svg class="{cls}" aria-hidden="true"><use href="#icon-{n}"></use></svg>'
def turl(s): return f"topics-{s}.html"
def curl(i): return f"courses-{i}.html"
def nurl(s): return f"news-{s}.html"
def cat_of(cid): return next((c for c in nav["categories"] if c["id"] == cid), None)
def slugify(t): return re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")

def live_topics(c):
    out = []
    if c.get("sections"):
        for sec in c["sections"]:
            for t in sec["topics"]:
                if t["status"] == "live": out.append(dict(t, _section=sec["label"]))
    else:
        for t in c.get("topics", []):
            if t["status"] == "live": out.append(dict(t, _section=""))
    return out

def all_topics(c):
    out = []
    if c.get("sections"):
        for sec in c["sections"]:
            for t in sec["topics"]: out.append(dict(t, _section=sec["label"]))
    else:
        for t in c.get("topics", []): out.append(dict(t, _section=""))
    return out

def vid_id(u):
    if not u: return ""
    if "youtu.be/" in u:  return u.split("youtu.be/")[1].split("?")[0].split("/")[0]
    if "watch?v=" in u:   return u.split("watch?v=")[1].split("&")[0]
    if "/embed/" in u:    return u.split("/embed/")[1].split("?")[0]
    return u

def video_html(u, title=""):
    v = vid_id(u)
    if not v: return ""
    return (f'<div class="video-wrap"><div class="video-frame">'
            f'<iframe src="https://www.youtube-nocookie.com/embed/{v}" title="Video: {title}"></iframe>'
            f'</div></div>')

def fmtdate(d):
    import datetime
    try:
        if hasattr(d, "strftime"): return d.strftime("%B %d, %Y").replace(" 0", " ")
        return datetime.datetime.strptime(str(d)[:10], "%Y-%m-%d").strftime("%B %d, %Y").replace(" 0", " ")
    except Exception: return str(d)

NEWS = []
for f in glob.glob(os.path.join(ROOT, "_news", "*.md")):
    raw = open(f, encoding="utf-8").read(); m = FM.match(raw)
    if not m: continue
    fm = yaml.safe_load(m.group(1)); fm["_body"] = raw[m.end():]
    fm["_slug"] = os.path.basename(f)[:-3]; NEWS.append(fm)
NEWS.sort(key=lambda p: str(p.get("date", "")), reverse=True)

HEAD = ('<!doctype html><html lang="en"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width, initial-scale=1">'
        '<link rel="preconnect" href="https://fonts.googleapis.com">'
        '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
        '<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600;9..144,700'
        '&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">'
        '<link rel="stylesheet" href="assets/css/style.css">'
        '<link rel="icon" href="assets/favicon.svg" type="image/svg+xml"><title>{title}</title></head><body>')

def header():
    cols = ""
    for c in nav["categories"]:
        items = ""
        if c.get("sections"):
            for sec in c["sections"]:
                items += (f'<li><a class="mega__link" href="{curl(c["id"])}#{sec["id"]}">'
                          f'<span class="t">{sec["label"]}</span>'
                          f'<span class="soon-tag">{len(sec["topics"])}</span></a></li>')
        else:
            for t in c.get("topics", []):
                if t["status"] == "soon":
                    items += (f'<li><span class="mega__link is-soon"><span class="t">{t["title"]}</span>'
                              f'<span class="soon-tag">Coming soon</span></span></li>')
                else:
                    items += (f'<li><a class="mega__link" href="{turl(t["slug"])}">'
                              f'<span class="t">{t["title"]}</span></a></li>')
        cols += (f'<div class="mega__col"><a class="mega__col-head" href="{curl(c["id"])}">'
                 f'{icon(c["icon"], "cat-icon")}<div><h3>{c["label"]}</h3><p>{c["blurb"]}</p></div></a>'
                 f'<ul class="mega__list">{items}</ul></div>')
    return (f'<a class="skip-link" href="#main">Skip to main content</a>{icons}'
            '<header class="site-header"><div class="container site-header__bar">'
            '<a class="brand" href="index.html"><span class="brand__mark" aria-hidden="true">TH</span>'
            '<span>Tutorial Hub</span></a>'
            '<nav class="primary-nav" aria-label="Primary"><ul>'
            f'<li><button type="button" class="nav-link" id="megaToggle" aria-expanded="false" '
            f'aria-controls="megaPanel" aria-haspopup="true">{icon("list")} Courses {icon("chevron","chev")}</button></li>'
            '<li><a class="nav-link" href="tools-job-search-pipeline.html">Job Search</a></li>'
            '<li><a class="nav-link" href="news.html">News</a></li>'
            '<li><a class="nav-link" href="about.html">About</a></li></ul></nav></div>'
            f'<div class="mega" id="megaPanel" data-open="false" role="region" aria-label="All courses" hidden>'
            f'<div class="mega__inner">{cols}</div></div></header>'
            '<div class="mega-overlay" id="megaOverlay" data-open="false" hidden></div><main id="main">')

def footer():
    cats = "".join(f'<li><a href="{curl(c["id"])}">{c["label"]}</a></li>' for c in nav["categories"])
    return ('</main><footer class="site-footer"><div class="container"><div class="footer-grid">'
            '<div><a class="brand" href="index.html"><span class="brand__mark">TH</span><span>Tutorial Hub</span></a>'
            '<p style="margin-top:16px;max-width:36ch;color:#9aa0b4;">A growing library of plain-English technology '
            'lessons, open to anyone who wants to learn. No jargon, no gatekeeping.</p></div>'
            f'<div><h4>Courses</h4><ul>{cats}</ul></div>'
            '<div><h4>Site</h4><ul><li><a href="index.html#courses">All courses</a></li>'
            '<li><a href="tools-job-search-pipeline.html">Job Search Pipeline</a></li>'
            '<li><a href="news.html">News</a></li><li><a href="about.html">About this site</a></li></ul></div>'
            '</div><div class="footer-bottom">&copy; 2026 Mr. Perez. Original lessons, written and maintained by a '
            'working technology instructor.</div></div></footer>'
            '<script src="assets/js/main.js" defer></script></body></html>')

def page(t, b): return HEAD.replace("{title}", t) + header() + b + footer()

# ---------- HOME ----------
cards = ""
for c in nav["categories"]:
    n = len(live_topics(c))
    cards += (f'<a class="course-card reveal" href="{curl(c["id"])}"><div class="course-card__icon">{icon(c["icon"])}</div>'
              f'<h3>{c["label"]}</h3><p>{c["blurb"]}</p><div class="course-card__foot">'
              f'<span class="course-card__count">{n} lesson{"s" if n != 1 else ""} ready</span>'
              f'<span class="course-card__cta">Explore course {icon("arrow")}</span></div></a>')
teaser = ""
if NEWS:
    nc = "".join(
        f'<li class="post-card reveal"><a class="post-card__link" href="{nurl(p["_slug"])}">'
        f'<p class="post-card__date">{fmtdate(p.get("date",""))}</p><h3>{p["title"]}</h3>'
        + (f'<p class="post-card__summary">{p.get("summary")}</p>' if p.get("summary") else "")
        + f'<span class="post-card__cta">Read post {icon("arrow")}</span></a></li>' for p in NEWS[:3])
    teaser = ('<section class="section band" id="latest-news"><div class="container">'
              '<div class="news-head reveal"><div><h2 class="section-title mt-0">Latest news</h2>'
              '<p class="lead">New lessons, tips, and updates.</p></div>'
              f'<a class="btn btn--ghost" href="news.html">All news {icon("arrow")}</a></div>'
              f'<ul class="post-list post-list--home">{nc}</ul></div></section>')
ncourses = len(nav["categories"]); nlessons = sum(len(live_topics(c)) for c in nav["categories"])
home = (f'<section class="hero"><div class="container">'
        f'<p class="hero__eyebrow">{icon("sparkles")} Plain English, no gatekeeping</p>'
        '<h1>Learn technology, <span class="u">without the jargon</span>.</h1>'
        '<p class="hero__lead">A growing library of clear, patient lessons on AI at work, Excel, and the devices you '
        'use every day. Written by a working instructor for anyone who wants to learn, no background required.</p>'
        f'<div class="hero__actions"><a class="btn" href="#courses">Explore the courses {icon("arrow")}</a>'
        f'<a class="btn btn--ghost" href="{curl("ai")}">Start with AI at Work</a></div>'
        f'<dl class="hero__stats">'
        f'<div class="hero__stat"><dd style="margin:0"><span class="n">{ncourses}</span><span class="l">Courses</span></dd></div>'
        f'<div class="hero__stat"><dd style="margin:0"><span class="n">{nlessons}</span><span class="l">Lessons ready</span></dd></div>'
        f'<div class="hero__stat"><dd style="margin:0"><span class="n">Self-paced</span><span class="l">Start anytime</span></dd></div>'
        f'</dl></div></section>'
        '<section class="section" id="courses"><div class="container"><div class="section-head reveal">'
        '<h2 class="section-title mt-0">Courses</h2><p class="lead">Each course is a set of short lessons you can take '
        f'in order or dip into as you need.</p></div><div class="course-grid">{cards}</div></div></section>{teaser}'
        )
write("index.html", page("Tutorial Hub", home))

# ---------- COURSES ----------
for c in nav["categories"]:
    lt, at = live_topics(c), all_topics(c)
    live, soon = len(lt), len(at) - len(lt)
    meta = f'{live} lesson{"s" if live != 1 else ""} ready' + (f" &middot; {soon} more coming soon" if soon else "")
    if c.get("sections"): meta += f' &middot; {len(c["sections"])} sections'
    about = f'<p class="lead course-hero__about">{c["about"]}</p>' if c.get("about") else ""

    def row(i, t):
        act = (f'<a class="btn" href="{turl(t["slug"])}">Start lesson {icon("arrow")}</a>'
               if t["status"] == "live" else '<span class="soon-pill">Coming soon</span>')
        cls = "" if t["status"] == "live" else " is-soon"
        num = i if t["status"] == "live" else "&middot;"
        return (f'<li class="lesson-row{cls}"><span class="lesson-row__num" aria-hidden="true">{num}</span>'
                f'<div class="lesson-row__body"><h3>{t["title"]}</h3><p>{t.get("blurb","")}</p></div>'
                f'<div class="lesson-row__action">{act}</div></li>')

    if c.get("sections"):
        jump = "".join(f'<li><a href="#{s["id"]}"><span class="n">{i}</span>{s["label"]}</a></li>'
                       for i, s in enumerate(c["sections"], 1))
        secs, n = "", 0
        for i, sec in enumerate(c["sections"], 1):
            rows = ""
            for t in sec["topics"]:
                if t["status"] == "live": n += 1
                rows += row(n, t)
            blurb = f'<p class="lead">{sec["blurb"]}</p>' if sec.get("blurb") else ""
            secs += (f'<section class="course-section reveal" id="{sec["id"]}"><div class="course-section__head">'
                     f'<p class="course-section__label">Section {i}</p><h2>{sec["label"]}</h2>{blurb}</div>'
                     f'{video_html(sec.get("video_url",""), sec["label"])}'
                     f'<ol class="lesson-list">{rows}</ol></section>')
        inner = (f'<nav class="section-jump" aria-label="Sections in this course"><h2>In this course</h2>'
                 f'<ol>{jump}</ol></nav>{secs}')
    else:
        rows = "".join(row(i, t) for i, t in enumerate(c.get("topics", []), 1))
        inner = f'<h2 class="section-title">Course lessons</h2><ol class="lesson-list">{rows}</ol>'

    b = (f'<div class="band"><div class="container course-hero">'
         f'<nav class="breadcrumb" aria-label="Breadcrumb"><ol><li><a href="index.html">Home</a></li>'
         f'<li><span aria-current="page">{c["label"]}</span></li></ol></nav>'
         f'<span class="course-hero__eyebrow">{icon(c["icon"])} Course</span><h1>{c["label"]}</h1>{about}'
         f'<p class="course-hero__meta">{meta}</p></div></div>'
         f'<div class="container section--tight">{inner}</div>')
    write(curl(c["id"]), page(c["label"] + " - Tutorial Hub", b))

# ---------- TOPICS ----------
for f in glob.glob(os.path.join(ROOT, "_topics", "*.md")):
    d = yaml.safe_load(FM.match(open(f, encoding="utf-8").read()).group(1))
    c = cat_of(d["category"]); clabel = c["label"] if c else d["category"]
    video = video_html(d.get("video_url", ""), d["title"]) or (
        f'<div class="video-wrap"><div class="video-placeholder">{icon("play")}<div>'
        '<strong>A video walkthrough is coming for this lesson.</strong>'
        '<span>Everything you need is written out below, so you can start right now.</span></div></div></div>')

    cnav = ""
    if c:
        if c.get("sections"):
            blocks, n = "", 0
            for sec in c["sections"]:
                it = ""
                for t in sec["topics"]:
                    if t["status"] != "live":
                        it += (f'<li><span class="course-nav__link is-soon"><span class="n">&middot;</span>'
                               f'{t["title"]} <span class="soon-tag">Soon</span></span></li>')
                    else:
                        n += 1
                        if t["slug"] == d["slug"]:
                            it += (f'<li><span class="course-nav__link is-current" aria-current="page">'
                                   f'<span class="n">{n}</span>{t["title"]}</span></li>')
                        else:
                            it += (f'<li><a class="course-nav__link" href="{turl(t["slug"])}">'
                                   f'<span class="n">{n}</span>{t["title"]}</a></li>')
                blocks += f'<p class="course-nav__section">{sec["label"]}</p><ol class="course-nav__list">{it}</ol>'
            cnav = (f'<nav class="course-nav" aria-label="Lessons in this course">'
                    f'<a class="course-nav__back" href="{curl(c["id"])}">{icon("arrow-left")} {c["label"]}</a>'
                    f'{blocks}</nav>')
        else:
            it = ""
            for i, t in enumerate(c.get("topics", []), 1):
                if t["status"] != "live":
                    it += (f'<li><span class="course-nav__link is-soon"><span class="n">{i}</span>{t["title"]} '
                           f'<span class="soon-tag">Soon</span></span></li>')
                elif t["slug"] == d["slug"]:
                    it += (f'<li><span class="course-nav__link is-current" aria-current="page">'
                           f'<span class="n">{i}</span>{t["title"]}</span></li>')
                else:
                    it += (f'<li><a class="course-nav__link" href="{turl(t["slug"])}">'
                           f'<span class="n">{i}</span>{t["title"]}</a></li>')
            cnav = (f'<nav class="course-nav" aria-label="Lessons in this course">'
                    f'<a class="course-nav__back" href="{curl(c["id"])}">{icon("arrow-left")} {c["label"]}</a>'
                    f'<ol class="course-nav__list">{it}</ol></nav>')

    toc = "".join(f'<li><a href="#{p.get("id") or slugify(p["title"])}">{p["title"]}</a></li>' for p in d["parts"])
    parts = ""
    for i, part in enumerate(d["parts"], 1):
        pid = part.get("id") or slugify(part["title"]); blocks = ""
        for b in part.get("blocks", []):
            bt = b.get("type", "lesson")
            tag = {"activity": f'<span class="chip">{icon("pencil")}</span> Activity &middot; try it',
                   "quiz": f'<span class="chip">{icon("badge")}</span> Check your understanding'
                   }.get(bt, f'<span class="chip">{icon("book")}</span> Lesson')
            md.reset(); body = md.convert(b.get("body", "")) if b.get("body") else ""
            title = f'<h3>{b["title"]}</h3>' if b.get("title") else ""
            qb = (f'<a class="btn btn--quiz" href="{b["quiz_url"]}" target="_blank" rel="noopener">'
                  f'{b.get("quiz_label","Open the quiz")} {icon("external")}</a>'
                  if bt == "quiz" and b.get("quiz_url") else "")
            imgs = ""
            for im in (b.get("images") or []):
                cap = f'<figcaption>{im["caption"]}</figcaption>' if im.get("caption") else ""
                imgs += f'<figure class="figure"><img src="{im["src"]}" alt="{im.get("alt","")}">{cap}</figure>'
            blocks += (f'<div class="block block--{bt}"><p class="block__tag">{tag}</p>{title}'
                       f'<div class="block__body rich">{body}{imgs}{qb}</div></div>')
        intro = f'<p class="lead">{part["intro"]}</p>' if part.get("intro") else ""
        parts += (f'<section class="part reveal" id="{pid}"><p class="part__label">Part {i}</p>'
                  f'<h2>{part["title"]}</h2>{intro}{blocks}</section>')

    livel = live_topics(c) if c else []
    idx = next((i for i, t in enumerate(livel) if t["slug"] == d["slug"]), -1); pager = ""
    if idx >= 0 and len(livel) > 1:
        pv = (f'<a class="pager__link pager__link--prev" href="{turl(livel[idx-1]["slug"])}">'
              f'<span class="pager__dir">{icon("arrow-left")} Previous</span>'
              f'<span class="pager__title">{livel[idx-1]["title"]}</span></a>') if idx > 0 else "<span></span>"
        nx = (f'<a class="pager__link pager__link--next" href="{turl(livel[idx+1]["slug"])}">'
              f'<span class="pager__dir">Next {icon("arrow")}</span>'
              f'<span class="pager__title">{livel[idx+1]["title"]}</span></a>') if idx < len(livel)-1 else "<span></span>"
        pager = f'<nav class="pager" aria-label="More lessons">{pv}{nx}</nav>'

    leadin = f'<p class="lesson-intro">{d["lead_in"]}</p>' if d.get("lead_in") else ""
    lead   = f'<p class="lead">{d["description"]}</p>' if d.get("description") else ""
    b = (f'<article class="topic"><div class="band"><div class="container topic-hero">'
         f'<nav class="breadcrumb" aria-label="Breadcrumb"><ol><li><a href="index.html">Home</a></li>'
         f'<li><a href="{curl(d["category"])}">{clabel}</a></li>'
         f'<li><span aria-current="page">{d["title"]}</span></li></ol></nav>'
         f'<h1>{d["title"]}</h1>{lead}'
         f'<div class="lesson-actions"><button type="button" class="btn btn--ghost btn--sm" id="printLesson">'
         f'{icon("print")} Print this lesson</button></div>{video}</div></div>'
         f'<div class="container section--tight"><div class="topic-body">'
         f'<aside class="lesson-sidebar">{cnav}<nav class="toc" aria-label="On this page"><h2>On this page</h2>'
         f'<ol>{toc}</ol></nav></aside>'
         f'<div class="topic-parts rich">{leadin}{parts}{pager}</div></div></div></article>')
    write(turl(d["slug"]), page(d["title"] + " - Tutorial Hub", b))

# ---------- NEWS ----------
if NEWS:
    items = "".join(
        f'<li class="post-card reveal"><a class="post-card__link" href="{nurl(p["_slug"])}">'
        f'<p class="post-card__date">{fmtdate(p.get("date",""))}'
        + (f' &middot; {p.get("author")}' if p.get("author") else "") + "</p>"
        f'<h2>{p["title"]}</h2>'
        + (f'<p class="post-card__summary">{p.get("summary")}</p>' if p.get("summary") else "")
        + f'<span class="post-card__cta">Read post {icon("arrow")}</span></a></li>' for p in NEWS)
    listing = f'<ul class="post-list">{items}</ul>'
else:
    listing = '<p class="lead">No posts yet.</p>'
write("news.html", page("News",
    f'<div class="band"><div class="container course-hero"><nav class="breadcrumb" aria-label="Breadcrumb"><ol>'
    f'<li><a href="index.html">Home</a></li><li><span aria-current="page">News</span></li></ol></nav>'
    f'<span class="course-hero__eyebrow">{icon("list")} News &amp; updates</span><h1>News</h1>'
    f'<p class="lead course-hero__about">Short posts on new lessons, tips, and updates.</p></div></div>'
    f'<div class="container section--tight">{listing}</div>'))
for p in NEWS:
    md.reset(); h = md.convert(p["_body"])
    a = f' &middot; {p.get("author")}' if p.get("author") else ""
    s = f'<p class="lead">{p.get("summary")}</p>' if p.get("summary") else ""
    write(nurl(p["_slug"]), page(p["title"] + " - Tutorial Hub",
        f'<article class="post"><div class="band"><div class="container topic-hero">'
        f'<nav class="breadcrumb" aria-label="Breadcrumb"><ol><li><a href="index.html">Home</a></li>'
        f'<li><a href="news.html">News</a></li><li><span aria-current="page">{p["title"]}</span></li></ol></nav>'
        f'<h1>{p["title"]}</h1><p class="post-meta">{fmtdate(p.get("date",""))}{a}</p>{s}</div></div>'
        f'<div class="container section--tight"><div class="post-layout"><div class="post-body rich">{h}</div></div>'
        f'<p class="post-back"><a href="news.html">{icon("arrow-left")} Back to all news</a></p></div></article>'))

# ---------- TOOLS ----------
try:
    raw = read("_includes/job-search-pipeline.md"); md.reset(); doc = md.convert(raw)
    intro = ('<div class="tool-intro rich"><h2 class="section-title">What this is, in plain terms</h2>'
             '<p>Think of this as a set of instructions you hand to an AI assistant. You fill in a few blanks about '
             'yourself, paste it in, and the AI searches the job sites you pick, scores each opening against your '
             'background, and writes you a resume and cover letter for the best matches. It never applies for you.</p>'
             '<h2 class="section-title">How to use it</h2><ol class="tool-steps">'
             '<li><strong>Get an AI helper</strong> that can read your files and go online.</li>'
             '<li><strong>Gather your stuff</strong> into one folder: resumes and work history.</li>'
             '<li><strong>Fill in the blanks</strong> marked with [square brackets].</li>'
             '<li><strong>Paste it in and let it run.</strong> You review everything and apply yourself.</li>'
             '</ol></div>')
    access = (f'<section class="pipeline-access" id="pipelineAccess" data-gate="off">'
              f'<div class="pipeline-access__bar"><div><h2 class="section-title mt-0">The instructions for your AI</h2>'
              f'<p class="lead">This part is written for the AI, so some of it looks technical. You do not need to '
              f'read it.</p></div><div class="pipeline-access__actions">'
              f'<button type="button" class="btn" id="copyPipeline">{icon("copy")} Copy all</button>'
              f'<a class="btn btn--ghost" href="assets/downloads/job-search-pipeline.md" download>'
              f'{icon("download")} Download (.md)</a></div></div>'
              f'<div class="pipeline-doc rich">{doc}</div></section>')
    rs = '<script type="text/plain" id="pipelineRaw">' + _html.escape(raw) + "</script>"
    write("tools-job-search-pipeline.html", page("Job Search Pipeline",
        f'<div class="band"><div class="container course-hero"><nav class="breadcrumb" aria-label="Breadcrumb"><ol>'
        f'<li><a href="index.html">Home</a></li><li><span aria-current="page">Job Search Pipeline</span></li></ol></nav>'
        f'<span class="course-hero__eyebrow">{icon("sparkles")} Free tool</span>'
        f'<h1>The Automated Job Search Pipeline</h1>'
        f'<p class="lead course-hero__about">Let an AI do the heavy lifting of your job search.</p></div></div>'
        f'<div class="container section--tight">{intro}{access}{rs}</div>'))
except Exception as e:
    print("tools page skipped:", e)

# ---------- ABOUT ----------
raw_about = read("about.md"); body_src = FM.sub("", raw_about)
m = re.search(r'<div class="prose[^"]*"[^>]*>(.*?)</div>', body_src, re.DOTALL)
prose_md = re.sub(r"{{.*?}}", "#", (m.group(1) if m else body_src))
md.reset(); prose = md.convert(prose_md.strip())
write("about.html", page("About",
    f'<div class="band"><div class="container topic-hero"><nav class="breadcrumb" aria-label="Breadcrumb"><ol>'
    f'<li><a href="index.html">Home</a></li><li><span aria-current="page">About</span></li></ol></nav>'
    f'<h1>About this site</h1><p class="lead">Why it exists, who it is for, and how to get the most out of it.</p>'
    f'</div></div><div class="container section--tight"><div class="prose rich">{prose}</div></div>'))

print("rendered", len(glob.glob(os.path.join(OUT, "*.html"))), "pages ->", OUT)
