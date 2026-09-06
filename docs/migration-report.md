# Migration report — 2026-09-07

## Result
All four pages implemented locally with the original dark red navigation, red headings, white background, portrait and academic lists. Public deployment is pending authentication as `haishi-harry-li`; the existing SSH identity belongs to another account and was not used for publishing. No repository has been created remotely and the Google Site has not been changed.

## Content verification
Compared every nonempty original heading/paragraph and every content hyperlink occurrence with the migrated pages, allowing local file URL substitutions, removal of Google Scholar tracking parameters, and the verified ETSG award URL correction:

| Page | Content blocks | Link occurrences |
|---|---:|---:|
| Home | 29 | 48 |
| Research | 18 | 38 |
| Policy Discussions | 19 | 36 |
| International Economics Joint Conference | 4 | 4 |

All comparisons passed. Research includes the published-paper list beyond its first Google `role=main` block. The current homepage has one distinct Work in Progress entry; the earlier duplicate is no longer present. Scholarly text and publication status were preserved.

## Browser verification
All four pages and the custom 404 document loaded successfully at widths of 1440, 390 and 320 pixels (15 checks). No horizontal overflow, JavaScript errors or external runtime requests were observed. Each page has exactly one h1. All 46 local page references resolved, all local font references resolved, and the eight PDF files have valid PDF signatures. Screenshots are in `docs/previews/`.

The custom 404 document was tested directly and at a simulated nested missing URL: its assets loaded correctly. Keyboard skip navigation and HTTP downloads of all eight PDFs passed. The validator also passed in a fresh copy without local migration snapshots. GitHub's production missing-route response still requires deployment verification. No mainland-China network tests have been performed.

## Local downloads and provenance
Downloaded the portrait and eight documents already publicly linked by the user's site. CV, paper and slides were checked with PDF text extraction. All four conference documents are image-only PDFs, so their first pages were rendered and visually checked against their labeled year and purpose. Files were preserved rather than OCR-modified. Fonts were fetched for local serving with SIL OFL licenses included.

| Local asset | Bytes | Original public source |
|---|---:|---|
| `assets/cv/haishi-harry-li-cv.pdf` | 91380 | [source](https://drive.google.com/file/d/1-DfYqKR25Qzw3TOM8JVU1cx05V-JYdkf/view?usp=sharing) |
| `assets/papers/trade-war-and-peace.pdf` | 9204584 | [source](https://drive.google.com/file/d/1Vnh-RODB7FW4atCbOd9gHMuxqcZA2HWa/view?usp=drive_link) |
| `assets/images/haishi-harry-li.jpg` | 82780 | [source](https://lh3.googleusercontent.com/sitesv/AG8ngQXKUzx0Tho22VzBA6G38zfpdl4JAjiN7uHkqhsqXpt_ZZCrLAVUXCH3th1xUuiwiKTb0x85PzB1x0KHgIXnopBxIHCed4pRp5Y0yzDJih726jRbVhth8fRLIbd3JV5suITHHbMjALwu19KmxEC4feYEfuAZXSgYU2tKFFe2wDsj1T9snUn6Ce9HjdjEFspkR31CkZUUBNnkj027Xz2zuSI_aVdeTM2RmAVAJdmE=w1280) |
| `assets/conferences/iejc-2024-call-for-papers.pdf` | 549950 | [source](https://www.dropbox.com/scl/fi/i52opfe9tkzrk5rekw0pq/call-for-papers-v6.pdf?rlkey=o45b8mferyyaspmpechq1z1ar&st=3450xf39&dl=0) |
| `assets/conferences/iejc-2024-program.pdf` | 933841 | [source](https://www.dropbox.com/scl/fi/mowh35afavv82ndiiwfdj/conference_program.pdf?rlkey=oovknxtck87x33pzcak4q76ms&st=dk1iub4m&dl=0) |
| `assets/conferences/iejc-2025-call-for-papers.pdf` | 3602272 | [source](https://www.dropbox.com/scl/fi/nytkisiiimn701jik02wa/Call-for-Papers-The-2nd-International-Economics-Joint-Conference.pdf?rlkey=t731hzl91t53lgabfjpty5jty&st=0zcyj401&dl=0) |
| `assets/conferences/iejc-2025-program.pdf` | 5067588 | [source](https://www.dropbox.com/scl/fi/jjts840ijrmcb9w1waeky/conference_program.pdf?rlkey=y39sla7o4p1pi1fcuh0j37lsa&dl=0) |
| `assets/slides/trade-war-and-its-influences-zh.pdf` | 2707066 | [source](https://www.dropbox.com/scl/fi/3cm2kcqrr8qveroelcd2s/.pdf?rlkey=ueckfjkenepcdt7r4201r4z6a&dl=0) |
| `assets/slides/us-china-strategic-capital-integration.pdf` | 266326 | [source](https://www.dropbox.com/scl/fi/93roq0mlr3cwtogcah4rc/beamer_slides_for_policy_discussion_US_China_relations-1.pdf?rlkey=c86p63uv6qn35gugi11uhe1bf&dl=0) |

The CV still prints the old Google Site address. The owner can supply a newly generated CV PDF when ready; the PDF content has not been edited.

## External links
58 unique external destinations were checked using HTTP GET from this workspace: 32 returned HTTP 200. HTTP 200 is reachability evidence, not a guarantee of correct content or mainland access. Other responses are listed below. Access denials (403/999) and rate limits (429) were not treated as broken URLs. Original destinations were preserved except the ETSG award link: the old URL returned 404, and the verified replacement is https://etsg.org/award-winners/review-of-world-economics-rowe-prize/, which explicitly lists Haishi Li and the paper as the 2021 winner. Both occurrences were corrected.

| HTTP status | Link |
|---|---|
| 403 | https://academic.oup.com/ej/advance-article-abstract/doi/10.1093/ej/ueae119/7931814?redirectedFrom=fulltext |
| 403 | https://academic.oup.com/ej/pages/editors-choice |
| 403 | https://cepr.org/voxeu/columns/comply-or-not-comply-understanding-neutral-country-supply-chain-responses-russian |
| 403 | https://cepr.org/voxeu/columns/industrial-policy-and-retaliatory-protection-under-wto-lessons-china |
| 403 | https://cepr.org/voxeu/columns/trade-policy-uncertainty-and-supply-chain-disruptions-firm-level-evidence-liberation |
| 403 | https://cepr.org/voxeu/columns/trade-war-and-peace-how-impose-international-trade-sanctions |
| 403 | https://direct.mit.edu/rest/article-abstract/doi/10.1162/REST.a.1773/136656/The-Employment-Consequences-of-Anti-Dumping?redirectedFrom=fulltext |
| 403 | https://iiep.gwu.edu/17th-gw-china-conf |
| 403 | https://onlinelibrary.wiley.com/doi/abs/10.1111/1540-6229.12147 |
| 403 | https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4153921 |
| 403 | https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4246013 |
| 403 | https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4400379 |
| 403 | https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4817589 |
| 403 | https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5343932 |
| 403 | https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5795404 |
| 403 | https://vox.lacea.org/?q=blog/employment_consequences_antidumping |
| 403 | https://www.cato.org/research-briefs-economic-policy/neutral-countries-supply-chain-responses-russian-sanctions |
| 403 | https://www.cato.org/research-briefs-economic-policy/robots-tools-jobs-evidence-brazilian-labor-markets |
| 403 | https://www.cato.org/research-briefs-economic-policy/trade-policy-uncertainty-supply-chain-disruptions-evidence |
| 404 | https://www.etsg.org/award-winners.html |
| 429 | https://www.ftchinese.com/story/001109665 |
| 403 | https://www.imf.org/en/Publications/WP/Issues/2021/01/22/We-Are-All-in-the-Same-Boat-Cross-Border-Spillovers-of-Climate-Risk-through-International-49947 |
| 403 | https://www.imf.org/external/Pubs/FT/irb/2021/FallWinter/index.pdf |
| 999 | https://www.linkedin.com/in/alanfeng |
| 403 | https://www.sciencedirect.com/science/article/abs/pii/S0022199620300593 |
| 403 | https://www.sciencedirect.com/science/article/abs/pii/S0304393224000254 |

## Deployment and transition remaining
- Authenticate GitHub CLI as `haishi-harry-li` and verify the API identity before creating the public website repository.
- Push the prepared main branch, enable GitHub Actions as the Pages source, and verify the deployed HTTPS pages and PDFs.
- Test actual mainland access without a VPN. A custom domain or alternate host may be considered if tests show unreliable access.
- After successful deployment, update the old Google Site with a move notice and update academic profile links. The old site has not been deleted or redirected.
