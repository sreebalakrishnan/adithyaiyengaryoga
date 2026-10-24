# Changelog

What changed in each version of the Adithya Institute of Iyengar Yoga website, newest first.
Each version is a Git tag on this repository; the commit hashes are the exact snapshots.

| Version | Date | Where it lives |
|---|---|---|
| 1.4.9 | 2026-10-24 | **Staging:** https://adithyaiyengaryoga.sreeb.dev, deploys itself from `main`, not indexed |
| 1.4.8 | 2026-10-24 | Tag `v1.4.8` |
| 1.4.7 | 2026-10-24 | Tag `v1.4.7` |
| 1.4.6 | 2026-10-24 | Tag `v1.4.6` |
| 1.4.5 | 2026-10-24 | Tag `v1.4.5` |
| 1.4.4 | 2026-10-24 | Tag `v1.4.4` |
| 1.4.3 | 2026-10-24 | Tag `v1.4.3` |
| 1.4.2 | 2026-10-24 | Tag `v1.4.2` |
| 1.4.1 | 2026-10-24 | Tag `v1.4.1` |
| 1.4.0 | 2026-10-24 | Tag `v1.4.0` |
| 1.3.2 | 2026-10-24 | Tag `v1.3.2` |
| 1.3.1 | 2026-10-24 | Tag `v1.3.1` |
| 1.3.0 | 2026-10-23 | Tag `v1.3.0`; **was staging:** https://adithyaiyengaryoga.sreeb.dev — deploys itself from `main`, not indexed |
| 1.2.1 | 2026-10-23 | Tag `v1.2.1` |
| 1.2.0 | 2026-10-23 | Tag `v1.2.0` |
| 1.1.0 | 2026-10-23 | Tag `v1.1.0` |
| 1.0.0 | 2026-10-23 | This repository, tag `v1.0.0` (first commit) |
| 0.1 | before 2026-10-23 | **Yogen's original:** https://adithyaiyengaryoga-website.yogs313.workers.dev — Astro on a Cloudflare Worker; its source is not in this repository |

## Planned

Taken from the UX review of 23 October 2026, in the order that matters most. Each needs Yogen and Narayan Sir, not just code.

- Yogen's own story on the home page, in his words, in place of the empty "What students find" section.
- Hero rewritten for someone starting out (back pain, stiffness, stress), with a photograph of the hall rather than Guruji's portrait.
- A "no sweating, no holding the breath, no straining the face" section built on *sthira sukham asanam*, in Sanskrit, Kannada and English.
- Visit page filled in with Narayan Sir: batches and class length, the fee policy, languages, how to reach the hall (metro, landmark, parking), what to wear and when to eat, and a WhatsApp link.
- Nav trimmed to what a beginner needs; Roots and Glossary move to the footer.

## 1.4.9 — 2026-10-24

Tag `v1.4.9`. From Yogen.

### Added
- **A third picture of Guruji in the home page banner:** the black-and-white tribute with "My Ending should be your beginning", his signature and his dates (14 December 1918 to 20 August 2014). It is from the Google Maps listing and carries the logo of BKS Iyengar Yogashala, Malaysia, who are credited in its caption. The banner's buttons now say "Picture 1 of 3" and so on.

### Fixed
- **Every banner picture was cut off at the bottom.** The pictures grew taller than their frame, so the bottom tenth of Guruji's portrait and of the pen drawing was clipped, and would have hidden the tribute's dates and logo. They now fit the frame exactly, and the caption has room for two lines.

## 1.4.8 — 2026-10-24

Tag `v1.4.8`. From Yogen, from his own observation of students.

### Added
- **One sentence on the Narayan Sir page, after who comes to him:** "Over the years, students with long-standing conditions have seen improvement with this practice, alongside their medical care." It is worded as improvement seen over the years, not as a cure, and does not compare the practice with other treatment. Students' own words, with their written consent, would say more and are still wanted.

## 1.4.7 — 2026-10-24

Tag `v1.4.7`. From Yogen.

### Removed
- **The sentence after "who comes to him" on the Narayan Sir page:** "The practice works alongside medical care and does not replace it: decisions about treatment stay between each person and their doctor." The medical-care notes on the practice page and on Ways to practise are unchanged.

## 1.4.6 — 2026-10-24

Tag `v1.4.6`. From Yogen.

### Added
- **Who comes to Narayan Sir, on his page:** some people come with serious long-standing conditions, among them arthritis and Parkinson's disease, and some when surgery has been advised, often after other approaches have not helped. It is worded as who comes, not as a promise of results, and sits next to the line that the practice works alongside medical care and does not replace it. The page makes no cure claim.

## 1.4.5 — 2026-10-24

Tag `v1.4.5`. From Yogen. Follows from the students' ages (25 to over 75).

### Changed
- **"Who can practise?" on the practice page** no longer says children can be introduced to yoga. It now says adults of any age, that Narayan Sir's students range from 25 to over 75, and that props adapt the practice to each person. This answer also feeds the page's structured data, so the search-result version changes with it.
- **Women's health** now says "through the adult years and menopause" instead of "from adolescence to menopause".

## 1.4.4 — 2026-10-24

Tag `v1.4.4`. From Yogen.

### Changed
- **The Youth entry is removed from Ways to practise**, and "youth" from that page's share text. Narayan Sir's youngest student is 25, so there is no youth class. The remaining entries are renumbered 1 to 6.
- **Students' ages are stated on the Narayan Sir page:** "His students range in age from 25 to over 75."

## 1.4.3 — 2026-10-24

Tag `v1.4.3`. From Yogen.

### Changed
- **Languages.** Narayan Sir speaks Kannada, Tamil, Telugu, English and Hindi, and his students are multilingual, so the sentence on the home and Narayan Sir pages no longer says only Kannada and Tamil. It now says language is not a barrier and that his presence teaches. The facts file (`src/site.json`), which feeds search and AI summaries, lists all five languages.

## 1.4.2 — 2026-10-24

Tag `v1.4.2`.

### Changed
- **The lineage list on the home page matches the Narayan Sir timeline:** 1987 (begins learning from Sri B. Raghavendra Shenoy), Decades (continues to study under Guruji), 1989 (begins teaching at the Rashtrothana Parishad) and 2002 (starts the Vijayanagar studio). It had a single "Since 1989" line.

## 1.4.1 — 2026-10-24

Tag `v1.4.1`. Corrects when Narayan Sir began teaching, from Yogen.

### Changed
- **"Teaching in Vijayanagar since 1988" is replaced everywhere** with the dates Yogen gave: he began learning from Sri B. Raghavendra Shenoy in 1987, began teaching in 1989 at the Rashtrothana Parishad, and started the Vijayanagar studio in 2002. The site now says "teaching since 1989, and in Vijayanagar since 2002". This covers the home page (line above the heading, share text, the lineage list and the Narayan Sir section), the Narayan Sir page (opening line, share text, "Teaching since 1989" section), the years scale on the practice page, the footer, and `src/site.json`, whose `foundingDate` is now 2002. That file feeds the structured data and `llms.txt`.
- **The Narayan Sir timeline** has three new entries (1987, 1989 and 2002), loses the 1988 entry, and the "Decades" line now reads "He continues to study under Guruji."

## 1.4.0 — 2026-10-24

Tag `v1.4.0`.

### Added
- **A version page at `/version.txt`** that shows the version, its release date and its notes from this changelog, so anyone can check what the live site contains: https://adithyaiyengaryoga.sreeb.dev/version.txt. `build.py` writes it from the newest row of the version table above. It has no timestamp, so rebuilding unchanged sources still changes nothing. `CLAUDE.md` explains how to check what is live, including the server's deploy log.

## 1.3.2 — 2026-10-24

Tag `v1.3.2`.

### Changed
- **The three principles on the home page now say what they belong to.** "Breath and mind together", "The inner body first" and "Measured in years" sat below both diagrams and read as if they described both. They now sit under the heading "What the inside-out practice rests on".

### Fixed
- **A grey tooltip appeared over the diagrams** ("Layers of the body, from the surface to the centre"). It came from a `<title>` element inside each diagram. The five diagrams (home, practice, Roots) now carry the same text as an `aria-label`, so screen readers still announce them, and the two diagrams on each page are labelled "Outside in" and "Inside out".

## 1.3.1 — 2026-10-24

Tag `v1.3.1`.

### Fixed
- **Two lines under the current page in the navigation.** The original stylesheet drew a rope-coloured border under the active link and `refinements.css` added an underline as well. The border is removed; the underline stays.

## 1.3.0 — 2026-10-23

Less "AI-designed". Tag `v1.3.0`. Prompted by a design review of AI-built sites: the look and behaviour fixes are done here; the copy has to come from Narayan Sir and Yogen.

### Changed
- **Hero stat row replaced with one plain line:** "Classes Monday to Friday · 6–10 am and 4–8 pm". The row of big numbers ("1988 / 6–10 / 4–8" with small captions) was hard to read and is a common AI landing-page pattern; the founding year is already in the line above the heading.
- **The outside-in / inside-out diagram shows both directions side by side** (stacked on phones) instead of hiding one behind a toggle. People rarely click the second button, so half the point was going unseen. On the home page the diagram now has two-thirds of the row, with the breathing ring beside it on wide screens and below it otherwise.
- **Small spaced capitals are kept only for the line above the home heading.** The class-time labels ("Morning practice", "Evening practice", "Class days") are now in ordinary sentence case.
- The toggle's script is removed from `site.js`.

### Added
- **Eleven lines to rewrite** in `editorial-backlog.json` (entries with a `rewrite` field), each with its page and a note. They follow the "not X, but Y" and three-fragment patterns that read as AI-written. First among them: the "In his words" quote on the home page, which needs Narayan Sir to confirm he said it.

## 1.2.1 — 2026-10-23

The permanent address is not chosen yet, so the site is now built for staging. Tag `v1.2.1`.

### Fixed
- **Share previews were blank.** Share images and other absolute links pointed at the workers.dev site, where `/og/hall.jpg` and `/og/lineage.jpg` do not exist. They now point at the staging address.

### Changed
- **Staging is not indexed.** Every page carries `noindex`, `robots.txt` no longer lists the sitemap, and nothing points search engines at workers.dev any more. Crawlers can still reach the pages, which is how they see the `noindex`.
- `build.py` has a `FINAL_URL` setting, empty for now. Setting it makes the site indexable at that address; see "Deploy" in the README.

## 1.2.0 — 2026-10-23

Search and answer-engine readiness. Tag `v1.2.0`. No visible content changed except the browser-tab titles and the new 404 page.

### Added
- **Structured data (JSON-LD) on every page**, generated by `build.py` from one file of facts, `src/site.json`: the institute as a local business (address, map coordinates, phone, email, class hours Monday to Friday, founded 1988), Narayan Sir as its teacher (languages, a direct student of B.K.S. Iyengar), the website, and the page itself with breadcrumbs. The practice page is marked up as an FAQ (its eight questions), the glossary as a set of 58 defined terms, the Narayan Sir page as a profile and the Visit page as a contact page.
- **`llms.txt`**, a plain-text summary of the institute and its pages for AI assistants and answer engines.
- **Share previews:** 1200×630 JPEG images in `public/og/` (WhatsApp and LinkedIn do not reliably show WebP), plus site name, locale and a large-image Twitter/X card.
- **A 404 page** with the site's header and a way to the Visit page, instead of the host's default.

### Changed
- **Page titles and descriptions** written for how people search: "Iyengar Yoga in Vijayanagar, Bengaluru", "What is Iyengar yoga?", "Class times and address", "Yoga glossary: Sanskrit terms explained". The Visit description now carries the days, times, area and phone number. Share titles match the page titles.
- The sitemap and `llms.txt` list the home page first.
- "Aditya Institute of Iyengar Yoga", the spelling on the Google Maps listing, is recorded as an alternate name so both spellings point to the same place.

### To change facts
Edit `src/site.json` (address, phone, hours, teacher), then run `build.py`. Page text is still edited in `src/pages/`.

## 1.1.0 — 2026-10-23

Fixes and hosting. Tag `v1.1.0`.

### Fixed
- "Teaching in Vijayanagar since 1988: **-18 years**" on the practice page — the last leftover of the negative year counter. The sentence now ends at 1988.
- On the Visit page, "Classes run Monday to Friday" was drawn on top of the 6am–8pm axis labels, on desktop and on phones. The timeline now has room beneath it.

### Changed
- The **Teachings** page is hidden until it has content: gone from the navigation, from the links on the home and Narayan Sir pages, from the build and from the sitemap. The page is kept as `src/pages/_teachings.html`; `build.py` skips any page whose name starts with `_`. Rename it back and re-add the nav item when the first teaching is ready.

### Added
- Hosting on Hostinger at adithyaiyengaryoga.sreeb.dev, deploying automatically from `main` through the GitHub app. A root `.htaccess` serves the built `dist/` folder and keeps `src/`, `build.py` and the editorial backlog off the web.
- This changelog.

### Not changed
- Canonical and sitemap URLs still pointed at the workers.dev original. Replaced in 1.2.1 by staging mode.

## 1.0.0 — 2026-10-23

Recovery and refactor of Yogen's site into an editable, dependency-free static site. Tag `v1.0.0`, commit `5f3a265`.

The Astro source and Worker code were not available, so the site was rebuilt from what the browser received: all eight pages, the responsive images and the Patanjali invocation audio. The original's claims and contact details were kept as they were, not fact-checked.

### Changed from the original
- **Home page title:** "Narayan Sir · Adithya Institute of Iyengar Yoga" → "Iyengar Yoga in Vijayanagar · Adithya Institute", so search results say where and what.
- **"Begin with a visit" section** added near the top of the home page: class times, days, the phone number and directions. First-visit, call and directions buttons made prominent.
- **Negative teaching-years counter** replaced with the founding year, 1988; the negative years on the teacher page corrected.
- **Interview notes and testimonial placeholders removed** from the public pages (the original showed bracketed editorial notes to visitors; the home page's "Learning with him" section was a placeholder). Each removed item is recorded in `editorial-backlog.json` with the page it belongs to and the interview session it should come from. No stories or quotes were invented.
- **Automatic slideshow** replaced with manual picture controls.
- **Palette:** a restrained cream and green; branding and photographs kept.
- All text readable without JavaScript. Focus styles, Escape to close the menu, the current page marked in the nav, and live result counts in the glossary added.
- Header, footer and behaviour centralised (`src/partials/`, `public/assets/js/site.js`); inline page styles moved to `public/assets/css/page-*.css`.
- Sitemap and configurable canonical and social URLs added; the "Ways to practise" page says the class list is unconfirmed and asks visitors to check with the institute.

### How it is built
`python3 build.py` stitches `src/pages/*.html` with the shared header and footer into `dist/`, which is committed. Python standard library only; Google Fonts is the one external dependency, with system fallbacks.

## 0.1 — Yogen's original

Built by Yogen with Astro and served from a Cloudflare Worker at https://adithyaiyengaryoga-website.yogs313.workers.dev. Eight pages: home, Narayan Sir, the practice, roots, ways to practise, teachings, glossary and visit. Still live and unchanged; version 1.0.0 was recovered from it on 23 October 2026.
