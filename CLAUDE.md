# adithyaiyengaryoga.com

Website of **Narayan Sir**, a direct student of B.K.S. Iyengar ("Guruji"). He has taught Iyengar yoga since 1989, and in Vijayanagar, Bengaluru since 2002, at the **Adithya Institute of Iyengar Yoga**.

People: **Yogen** (Yogendra) is Narayan Sir's student and owns this project; the site is made for his teacher. **Sree** (GitHub `sreebalakrishnan`) hosts the repo and the staging site. Claude sessions here normally run as the GitHub login `yogs313`.

## Purpose

Not sales. The site shares the fundamental principles of Narayan Sir's practice, why and how it works, and the wisdom passed down from his guru, so visitors become curious and come to learn in person. He speaks Kannada, Tamil, Telugu, English and Hindi, and his students are multilingual, so language is not a barrier: his presence teaches, and students grasp the essence by practising with him over months. The site should give a taste of that. (Do not say he is uncomfortable in English; interviews are still best recorded in Kannada or Tamil, where he speaks most freely.)

The practice as he teaches it: works from the inside out, on the internal organs more than outer appearance; brings breath and mind together with intensity but without strain; works below conscious effort; lets energy reach every part of the body; over the long term guides the body back to its natural, healthy state. Respectful of other approaches (gyms, other yoga), which have their own value.

## Confirmed facts (all confirmed by Yogen)

- Timeline, as Yogen gave it: began learning from Sri B. Raghavendra Shenoy in **1987**; began teaching in **1989** at the Rashtrothana Parishad; started the Vijayanagar studio in **2002**. **Not 1988**: an earlier brief said "taught in Vijayanagar since 1988" and that was wrong. Say "teaching since 1989, and in Vijayanagar since 2002". Address: #37/4/24, Prashanth Nagar, I Main Road (Thimmenahalli), Vijayanagar, Bengaluru 560040. Map: https://maps.app.goo.gl/G2W5rmQw3kvCNjBH7
- Classes: Monday to Friday, mornings 6–10 am, evenings 4–8 pm.
- Languages (Yogen): he speaks Kannada, Tamil, Telugu, English and Hindi; students are multilingual and language is not a barrier.
- Email adityaiyoga@gmail.com (the real address; never "correct" its spelling). Phone +91 98456 15277, which matches his entry in the Pune institute's teacher directory.
- Spelling is **Adithya**. "Aditya" appears only in the email address and as a recorded alternate name for search.
- He learnt directly from Guruji for **decades** (no specific years known). Do not invent years.
- He is a listed teacher in the Pune institute's directory (Karnataka list, "Narayan V"), which gives no certificate level. **Do not write "certified" or a level** unless Yogen confirms one.
- Approved quote, Yogen's confirmation that it is Narayan Sir's: "As a direct student of B.K.S. Iyengar Guruji, I carry the responsibility of preserving the authenticity of his teachings while making them accessible to modern practitioners. The precision, alignment, and therapeutic focus that define Iyengar Yoga are not merely techniques—they are a way of life to which I have dedicated myself." It comes from the old site, not a recording, so never label it a translation.
- The eight limbs are grouped as Iyengar teaches: outer quest (*bahiranga*) = yama, niyama, asana; inner quest (*antaranga*) = pranayama, pratyahara; innermost quest (*antaratma*) = dharana, dhyana, samadhi. Do not use the classical five-and-three split.
- Narayan Sir is a **direct student of Guruji and a teacher**. Do not call him a founder of "one of the best centres" or add marketing superlatives.

## Rules

- **Never invent quotes, stories, teachings or facts in Narayan Sir's name.** Anything unconfirmed goes in `editorial-backlog.json` (`missing`), not on the page, and is asked about.
- **No claims that the practice cures specific diseases** (India's Drugs and Magic Remedies Act, and credibility). Use "therapeutic" and "supports", students' own words, and say it works alongside medical care. Never list diseases it treats.
- No SEO keyword stuffing; write for people. Plain, specific language; avoid "not X, but Y" and three-fragment slogans (the backlog logs lines that still read that way).
- Only our own photos, optimised under about 300 KB.
- Respect the source of borrowed material: text about Guruji, Patanjali, the institute and the glossary is drawn from the Ramamani Iyengar Memorial Yoga Institute's site (bksiyengar.com, which holds its copyright), reworded and credited on Roots and Glossary. The chant recording is theirs; a permission email to info@bksiyengar.com is still advisable.
- Therapeutic or health content, and the pregnancy and women's practice, must keep the "alongside medical care" note.

## How the repo works

Static site built with the Python standard library only, no packages:

```sh
python3 build.py                                         # regenerates dist/
python3 -m http.server 8765 --bind 127.0.0.1 --directory dist   # preview at http://127.0.0.1:8765
```

- Edit `src/pages/*.html` (page content), `src/partials/` (shared header, footer, head), `src/site.json` (address, phone, hours, teacher: feeds structured data and `llms.txt`), `public/assets/js/site.js` and `public/assets/css/*.css`. Pages whose names start with `_` are drafts (currently `_teachings.html`): kept, not built.
- `dist/` is the output and **is committed**. After editing `src/` or `public/`, run `python3 build.py` and commit `dist/` with the source.
- Hostinger serves the repo root; `.htaccess` rewrites everything to `dist/` and keeps `src/`, `build.py`, `editorial-backlog.json` and root files like this one off the web (they return 404).
- **Pushing to `main` deploys to staging, https://adithyaiyengaryoga.sreeb.dev, automatically.** The owner and Sree have agreed to work directly on `main` so changes can be seen live. Still: build and look at the result first, one clear commit per change, and don't push half-done work.
- Until `FINAL_URL` in `build.py` is set, every page is built for staging with `noindex`, the sitemap is left out of `robots.txt`, and canonicals point at the staging address. Setting `FINAL_URL` is the go-live step; do it only when Yogen says the real domain is ready. The real domain (adithyaiyengaryoga.com) still serves the **old** site and must not be touched until then.
- Record each version in `CHANGELOG.md` (tags `v1.x.x`) and keep its "Planned" list honest.
- **What's live:** https://adithyaiyengaryoga.sreeb.dev/version.txt shows the version, its release date and its changelog notes. `build.py` makes it from the newest row of the version table in `CHANGELOG.md`, so add the changelog entry *before* running the build, or the page shows the previous version. It carries no commit hash or timestamp (the build runs before the commit, and builds stay reproducible), so a push that skips the changelog looks unchanged there. The certain check is the server's deploy log: a session with the Hostinger connector (Sree's) reads `.git/logs/HEAD` for `adithyaiyengaryoga.sreeb.dev`; its last line is the deployed commit and the time, to match against `git log`. A push normally shows up there within a minute.
- Commit identity: this clone uses GitHub's noreply address for `yogs313` (set locally). Push as `yogs313` (`gh auth switch --user yogs313`); the Mac's other login is `yogendraet`, which has no write access here. End commit messages with the Claude co-author line.

## Content and design notes

- Pages: Home, Narayan Sir, The practice, Ways to practise (programmes drawn from the old site, **not yet confirmed with Narayan Sir**), Roots (Patanjali, Yoga Sutras, Guruji, the institute, books), Glossary, Visit. Teachings is hidden until the first real teaching exists.
- The look was first limewash, indigo ink and hemp-rope lines (Spectral serif, Hanken Grotesk for labels, one rope line down the home page). Sree's refactor moved to a restrained cream and green palette (`public/assets/css/refinements.css`). Don't change the look back or again without Yogen's say-so.
- Keep: calm, editorial feel; responsive; accessible (visible focus, alt text, 44 px tap targets); reduced motion respected; all text visible without JavaScript.
- Noto Serif Kannada (and Noto Sans Kannada) are in the font stacks for future Kannada text but not yet loaded; add them when Kannada content arrives.
- The home hero is Guruji (portrait and a pen drawing); Narayan Sir's straight-on headshot sits in his own section. Yogen approved those choices, so don't swap pictures unasked.

## Still to come from Yogen and Narayan Sir (see `editorial-backlog.json`)

Recorded conversations in Kannada or Tamil, translated for meaning and shaped into teachings; student stories (Yogen's own first); which ways to practise he teaches and in which batches; what to wear and eat before a first class; fees and batch details. Missing content stays out of public pages until it is real.

## Working with Yogen

Make only the change asked for. When a request can be read two ways, ask one short question first. Say plainly what was not checked.

## References outside the repo (on Yogen's Mac)

- `/Users/Yogendra/work/websites/adithyaiyengaryoga` is the earlier Astro version (components, Markdown teachings collection, richer CLAUDE.md history), pushed to `yogs313/adithyaiyengaryoga-website`. It is a reference, not the base.
- `/Users/Yogendra/work/websites/adithyaiyengaryogaold` is a mirror of the old site; `/Users/Yogendra/work/websites/Main Website` is a mirror of bksiyengar.com. Both are source material only; treat their claims as unverified.
