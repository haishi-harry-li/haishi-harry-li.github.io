# Website migration implementation plan

**Goal:** Publish all four pages of the existing academic website with similar styling and locally hosted essential assets.

**Architecture:** Plain HTML pages and shared CSS deployed with GitHub Pages. A one-time importer preserves source text, links, and emphasis; future edits are direct HTML edits.

**Tech stack:** HTML, CSS, Python for migration and verification, Chrome for browser checks.

## Global constraints
Preserve the dark red navigation, red headings, white background, portrait/biography layout, section order, and scholarly content. No runtime Google dependencies. Never claim mainland reachability without mainland tests. User approved the design on 2026-09-07. Work proceeds inline; no delegated agents.

## Tasks
- [x] Inventory all original sections and outgoing links, including content outside the first Google role=main container.
- [x] Retrieve portrait, CV, author working paper, policy slides, conference calls and programs; validate file signatures and PDF text. Record any failures.
- [x] Create index.html, research.html, policy-discussions.html and international-economics-joint-conference.html from the original sections. Preserve inline bold/italic/link semantics while removing Google markup.
- [x] Create assets/styles.css with responsive desktop/mobile layouts and locally hosted font files with licenses. Create an accessible skip link and navigation, metadata, sitemap.xml, robots.txt and 404.html.
- [x] Add README.md with editing and publishing steps, .nojekyll, .gitignore and GitHub Pages deployment configuration restricted to website files.
- [x] Compare normalized source text and outgoing links against generated pages. Check internal links, downloads, headings and canonical URLs.
- [x] Serve locally and inspect desktop and mobile pages using Chrome; verify no overflow, missing assets, runtime errors or third-party network dependencies. Save preview screenshots outside deployment output.
- [x] Audit external links, distinguishing HTTP errors and access restrictions. Record evidence in docs/migration-report.md.
- [x] Commit reviewed website and deliver a complete preview with the precise account connection step.
- [x] Publish and verify public pages after authentication as haishi-harry-li.
- [ ] Obtain mainland-China access results without a VPN; requires an external network test.

## Files
- Four root HTML pages: readable, directly editable migrated content.
- assets/styles.css, assets/fonts/, assets/images/, assets/papers/, assets/cv/, assets/conferences/, assets/slides/: shared styling and local downloads.
- scripts/import_site.py: repeatable one-time migration from captured originals and asset map.
- scripts/check_site.py: content parity and local link validation.
- .github/workflows/pages.yml: Pages artifact contains only public site files.
- docs/migration-report.md: original sources, download provenance and verification outcomes.
- README.md: local preview, editing, deployment and transition instructions.

## Validation commands
```bash
python scripts/check_site.py
python -m http.server 8000 --bind 127.0.0.1
```
Browser checks visit every page at desktop and mobile sizes, compare document width to viewport width, inspect heading hierarchy and record network requests. PDF checks use pdftotext to confirm each download is the intended document. External audit results do not automatically modify source links.
