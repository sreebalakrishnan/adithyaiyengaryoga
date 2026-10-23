# Changelog

What changed in each version of the Adithya Institute of Iyengar Yoga website, newest first.
Each version is a Git tag on this repository; the commit hashes are the exact snapshots.

| Version | Date | Where it lives |
|---|---|---|
| 1.1.0 | 2026-10-23 | **Staging:** https://adithyaiyengaryoga.sreeb.dev — deploys itself from `main` |
| 1.0.0 | 2026-10-23 | This repository, tag `v1.0.0` (first commit) |
| 0.1 | before 2026-10-23 | **Yogen's original:** https://adithyaiyengaryoga-website.yogs313.workers.dev — Astro on a Cloudflare Worker; its source is not in this repository |

## Planned

Taken from the UX review of 23 October 2026, in the order that matters most. Each needs Yogen and Narayan Sir, not just code.

- Yogen's own story on the home page, in his words, in place of the empty "What students find" section.
- Hero rewritten for someone starting out (back pain, stiffness, stress), with a photograph of the hall rather than Guruji's portrait.
- A "no sweating, no holding the breath, no straining the face" section built on *sthira sukham asanam*, in Sanskrit, Kannada and English.
- Visit page filled in with Narayan Sir: batches and class length, the fee policy, languages, how to reach the hall (metro, landmark, parking), what to wear and when to eat, and a WhatsApp link.
- Nav trimmed to what a beginner needs; Roots and Glossary move to the footer.

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
- Canonical and sitemap URLs still point at the workers.dev original (`SITE_URL` in `build.py`), so search engines do not treat the staging copy as a duplicate. Change `SITE_URL` when this becomes the real address.

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
