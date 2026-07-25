# Curriculum review (planned)

A note to myself and to any future session. **Once all ~17 subjects are loaded in,
do a full structural review of the library** rather than adding each new subject to
whatever category looks closest. Ruben asked for this explicitly.

## Why wait until the end

Reorganizing is cheap in this setup, so there is no reason to guess early:

- A lesson's course is one field, `category:`, in its own file.
- The menu and every course page read from `_data/topics.yml`. Move an entry, and
  the nav, course landing page, sidebar, and prev/next all follow automatically.
- The URL is the `slug`, which does not have to change when a lesson moves
  categories. So reorganizing does not break existing links.

## Problems already visible (as of the first three courses)

**1. "Devices & Digital Life" is three different subjects in one bucket.**
It currently mixes phones (iPhone, Android), a desktop operating system
(Windows 11), and digital literacy (Staying Safe Online). Ruben flagged this
himself. Likely fix: split into something like

- **Mobile Devices** (iPhone, Android, and phone-specific topics)
- **Basic Computing** (Windows, files and folders, mouse and keyboard, printing)
- **Digital Life & Safety** (online safety, scams, passwords, email, social media)

**2. "AI at Work" is 21 lessons in one flat list.**
That is a full course with clear internal arcs, but every lesson currently looks
equally weighted in the sidebar. Options to consider:

- Split into two courses (foundations, then applied and ethics), or
- Add a grouping level inside a course, so the sidebar can show sections like
  "Foundations," "Prompting," "Judgment and ethics," "Where it is going."

The second option is a template change, not just a data change, so decide the
structure before building it.

**3. Course order on the home page.**
Right now the order is AI, Office, Devices. Once Basic Computing exists, the more
logical progression for a beginner is probably computing basics first, then office
software, then AI. Worth revisiting once the catalog is full.

## What the review should cover

- Whether each course's lessons actually belong together.
- Whether the order inside each course builds properly (nothing depends on a
  concept introduced later).
- Whether any lesson is doing two jobs and should be split, or two lessons overlap
  enough to merge.
- Whether cross-references between lessons still point at the right places after
  any moves.
- Whether the number of courses on the home page is still scannable, or needs a
  grouping level of its own.
