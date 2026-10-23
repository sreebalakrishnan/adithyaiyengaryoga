# Adithya Institute — recovered and refactored website

Recovered from https://adithyaiyengaryoga-website.yogs313.workers.dev on 23 October 2026.
This is an editable static reconstruction of the browser-delivered website, not the original Astro source or Cloudflare Worker server code. All eight public pages, responsive images and invocation audio are included. Google Fonts remains an external dependency with local system-font fallbacks.

## Run locally

Requires Python 3, no packages required:

```sh
python3 build.py
python3 -m http.server 8765 --bind 127.0.0.1 --directory dist
```

Open http://127.0.0.1:8765. Serve the directory rather than double-clicking HTML files, because links and assets use root-relative paths.

## Edit

- `src/pages/*.html`: readable page content. A page whose name starts with `_` (currently `_teachings.html`) is a draft: kept in source, left out of the build and sitemap.
- `src/partials/header.html` and `footer.html`: shared navigation and contact details.
- `public/assets/js/site.js`: named, readable enhancement logic for navigation, galleries, glossary and diagrams.
- `public/assets/css/refinements.css`: shared visual changes and mobile layout.
- `public/assets/css/page-*.css`: recovered page-specific styles.
- `public/_astro/`: original optimized images and component styles. Scoped attributes are intentionally preserved so those styles remain functional.
- `editorial-backlog.json`: unfinished content removed from public pages. Keep this outside the deployed directory.
- `dist/`: deployable output, regenerated with `python3 build.py`.

The original site's claims and contact information are retained, not independently fact-checked. Class offerings were marked unconfirmed in the source, so the refactor includes an explicit instruction to confirm current availability with the institute.

## Changes

- Replaced the negative teaching-years counter with the stable founding year, 1988, and corrected negative years on the teacher page.
- Added prominent first-visit, call and directions actions, and moved class information near the top of the homepage.
- Preserved branding and photographs; introduced a restrained cream and green palette.
- Removed visible interview notes and testimonial placeholders without inventing stories or quotes.
- Replaced automatic slideshow motion with manual picture controls.
- Kept all text visible without JavaScript. Added focus styles, Escape-to-close navigation, active page indication, and glossary live result counts.
- Centralized the header, footer and behavior; extracted inline page styles.
- Added a sitemap and configurable canonical/social URLs using an included image.

## Deploy to your existing host

Only upload the contents of `dist/`. The live Worker has not been modified.
For a different production domain, set it at build time:

```sh
SITE_URL=https://your-domain.example python3 build.py
```

Use your existing Cloudflare deployment workflow to serve `dist/` as static assets. If the Worker has private routes or server features, merge these assets into the original project rather than replacing that server blindly. The original Astro component source cannot be reconstructed exactly from the served HTML.

## Next useful improvements

1. Confirm fees, batch start times, beginner requirements and currently available class types; add a concise first-visit FAQ.
2. Replace the unfinished story material with interviews approved by Narayan Sir, and genuine student testimonials with permission.
3. Publish short, reviewed teaching excerpts in Kannada/Tamil with English translations and captions.
4. Add an enquiry or booking form once the recipient and handling process are chosen. Current call/email links already work without a backend.
5. Connect the intended custom domain and update SITE_URL when ready.

## Verification

Build succeeded; JavaScript syntax passed. All eight pages' local links, anchors and asset references were checked. Browser checks covered desktop and 390px mobile layouts, image switching, glossary matches and empty results, body-map selection and mobile menu/Escape behavior. External contact links were inspected, not used to place calls or send messages. No live deployment was performed.
