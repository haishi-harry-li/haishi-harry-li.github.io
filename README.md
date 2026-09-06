# Haishi “Harry” Li — personal website

A static academic website for **https://haishi-harry-li.github.io/**, migrated from the four pages of the Google Site. The original red-and-white style is preserved; fonts, portrait, CV, one working paper, policy slides and conference documents are served locally.

## Preview

Open `index.html` in a browser, or run:

```bash
python -m http.server 8000 --bind 127.0.0.1
```

Then visit http://127.0.0.1:8000/. No Node.js, build step or backend is needed.

## Edit

- `index.html`: biography, research summary, teaching and advising.
- `research.html`: working-paper abstracts and published papers. Update this and the homepage together when a paper changes.
- `policy-discussions.html`: policy writing and talks.
- `international-economics-joint-conference.html`: conference descriptions and downloads.
- `assets/styles.css`: shared colors, spacing and mobile layout.
- `assets/cv/haishi-harry-li-cv.pdf`: replace with a new PDF to update the CV without changing its URL.
- `assets/papers/`, `assets/slides/`, `assets/conferences/`: public documents.

Keep paper titles, author names, dates and status accurate. HTML special characters in new text should be escaped (`&amp;`, `&lt;`, `&gt;`). The importer in `scripts/` was used only for the initial migration; rerunning it would overwrite manual page edits. Its original source snapshots are local and excluded from Git.

## Publish to GitHub Pages

1. Authenticate to GitHub as **haishi-harry-li**. With GitHub CLI installed, run `gh auth login --hostname github.com --git-protocol https --web`. Never paste credentials into chat or website files.
2. Create a public repository named **haishi-harry-li.github.io** in that account, without an initial README. Push this repository's `main` branch.
3. In the repository, open **Settings → Pages → Build and deployment → Source**, and select **GitHub Actions**.
4. Under **Actions → Publish academic website**, run the workflow (or push another change).
5. Check https://haishi-harry-li.github.io/ and each navigation page and PDF. The website is not live merely because the files are present locally.

The workflow publishes only the root HTML pages, assets, sitemap, robots.txt and .nojekyll. Documentation, migration tools and preview screenshots are excluded from the website artifact, though committed files are visible in the public source repository.

## Check changes

```bash
python -m pip install beautifulsoup4
python scripts/check_site.py
```

The check verifies local links, PDF signatures, local font references and page metadata. On the original migration workspace it additionally compares all content blocks and link occurrences to the captured Google Site. It does not test mainland connectivity. See `docs/migration-report.md` for the initial validation record.

## Transition

Keep the original site available and add this notice once the new site is verified:

> My website has moved to https://haishi-harry-li.github.io/. Please update your bookmarks.

Update the homepage URL in your university profile, Google Scholar profile, CV source, and other academic profiles you control. The currently migrated CV still prints the Google Site address; replace it with an updated PDF when available.

Test the homepage and PDF downloads from mainland China without a VPN, ideally on both a university network and a mobile connection. A successful test elsewhere does not demonstrate mainland access. If access is unreliable, the static site can be deployed to another host, with an optional custom domain providing a stable address.

## Fonts and content

Lato, Bitter and Arvo are served locally under the SIL Open Font License. Their license files are in `assets/fonts/`. Scholarly text, photographs and documents retain their respective owners' rights; no blanket open-source license is applied to those materials.
