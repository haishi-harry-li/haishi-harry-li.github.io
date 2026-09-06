# Personal website migration design

## Agreed direction
Migrate Haishi "Harry" Li’s public Google Site to GitHub Pages under account `haishi-harry-li`, preserving a similar visual style. Planned address: https://haishi-harry-li.github.io/. A custom domain is optional and is not required for this first migration.

## Visual design
Preserve the dark red top navigation bar, white background, dark body text, red section headings, underlined text links, generous spacing, and simple academic publication lists. Keep the existing portrait on the left and biography on the right on desktop; stack them on narrow screens. Use locally served fonts or system fallbacks. Make navigation wrap or collapse accessibly on mobile. Preserve publication emphasis and the original section order.

## Pages and content
Migrate all four existing navigation destinations: Home (`index.html`), Research (`research.html`), Policy Discussions (`policy-discussions.html`), and International Economics Joint Conference (`international-economics-joint-conference.html`). Home contains the profile, five working papers, one work in progress, six accepted/published papers, teaching and advising. Research includes the five working-paper abstracts. Preserve policy discussion links and both conference years’ calls and programs.

Use the live source captured on 2026-09-07. The Work in Progress entry is now “Public Knowledge or Proprietary Innovation? Unintended Consequences of R&D Subsidies on Knowledge Spillovers”; the previously observed duplicate is absent. Do not silently alter scholarly claims, paper status, dates, or authorship.

## Architecture and assets
Use static HTML and shared CSS, with minimal JavaScript only if needed for accessible mobile navigation. No backend, Google embeds, remotely loaded Google fonts, or analytics are required. Serve the existing portrait and publicly downloadable author-provided CV and working paper from local asset paths after checking actual file types and contents. Inventory conference and policy attachment links, including any Google redirects, and migrate accessible author-provided files. Preserve external publisher, coauthor, Scholar, and video links as optional outbound links. Do not guess replacement URLs or publish publisher PDFs without an appropriate shareable version. Missing downloads must be reported explicitly.

## Discoverability and accessibility
Use semantic headings, descriptive page titles, portrait alt text, keyboard-visible focus, language metadata, canonical URLs, a sitemap, and robots.txt allowing indexing. Preserve research abstracts as crawlable HTML. Do not promise indexing or citation increases.

## Verification and deployment
Compare desktop screenshots with the original, check mobile layout for overflow and usable navigation, verify all internal links and local downloads, and audit external links with distinctions between broken URLs and automated-access restrictions. Verify that essential rendering and downloads do not request Google services.

Publish from the public repository `haishi-harry-li/haishi-harry-li.github.io` after account authentication is available. Never request passwords or tokens in chat. Check HTTPS and each deployed page. Mainland access requires tests of the actual deployed domain and PDFs without a VPN, ideally across university and mobile networks; tests from this workspace alone cannot establish that. Retain the original Google Site during transition and provide a migration notice for its owner to add. No existing Google content will be removed as part of this migration.

## Review
This document records the proposed implementation of the user's accepted migration direction and similar-style constraint. It does not claim deployment or mainland verification has happened.
