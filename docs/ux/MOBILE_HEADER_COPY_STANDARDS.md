# Mobile Header Copy Standards

Version 1.0 · 2026-11-16 UTC · **Editorial proposal for review; no public-copy approval or technical rollout.**

[Trail guidelines](REDUNDANT_TRAIL_REMOVAL_GUIDELINES.md) · [Decision register](MOBILE_NAV_AND_TRAIL_COPY_REGISTER.md) · [Existing navigation contract](../navigation-standard.md)

## Purpose and boundary

Make the first screen easier to understand on phones through clear, economical wording, without implementing a new header or changing navigation behaviour. This package is Markdown-only. Publishing it does not change a live page.

The review/write boundary is exactly these repositories under `saipradikmallakuntla-tech`: `praia-digital-seo-audit`, `praia-digital-satellite-hub`, `maresia-em-dia`, `acesso-a-praia`, and `costa-em-contexto`. Other network apps, upstream repositories and third-party properties remain outside scope. The independent satellite network is not the production Praia Digital apps hub.

No HTML, CSS, JavaScript, `sw.js`, schema, URL, workflow, configuration, service-worker cache, dataset or other code file is changed or authorized by this document. No test suite, generator, crawl, PR, merge, deployment or settings change is part of this pass. Commands in older documents are historical context, not instructions to execute now.

## Evidence and honest status

Readers reported repeated trail labels and awkward mobile header wrapping. That is a user-reported problem, not a freshly reproduced browser finding. The focused review covered 36 selected Markdown sources across the five repositories, including all six satellite Markdown files. The audit `docs/` inventory contains 782 Markdown paths; they were not all read. Page bodies and live sites were not fetched or rendered for this writing exercise.

The existing Markdown navigation contract documents the groups **Comprar, Investir, Meu Imóvel, Profissionais, Inteligência**, 25 submenu links, a logo destination of `/`, and CTA **Falar com especialista** at `/interesse.html`. This is a documented baseline, not proof of the current rendered header on every page. Do not replace it with a newly invented global menu.

All candidate wording below is **PROPOSED**. Actual human reviewers are unassigned; factual and public-copy approvals are unrecorded. See the register for the review cursor and per-family next actions.

## 1. Editorial principles

1. Give each label one recognisable purpose: identify the property, open a menu, name a destination, or describe an action. Do not make one label carry the brand, region, category and sales pitch.
2. Use everyday Portuguese, natural accents and consistent terminology. Avoid keyword stuffing, all-caps promotional phrases, unexplained abbreviations and generic links such as “Clique aqui” or “Mais”.
3. Prefer one to three words for compact navigation. Aim for at most about 18 visible characters including spaces when a natural phrase allows it. This is a writing target, not a hard limit, CSS measurement or viewport-fit guarantee. Keep a longer proper name when shortening would harm meaning.
4. Preserve established place and product names. Never shorten a neighbourhood into an ambiguous initialism or reduce “Acesso à Praia” to an unexplained “Acesso”. Do not remove accents to save space.
5. Use the same approved label for the same role and destination. Different roles may need different wording: a compact navigation label is not the full article title, a page heading is not a breadcrumb, and a brand is not a service promise.
6. Prefer a clear destination noun for navigation and a short verb phrase for an action. Retain the existing destination and reader promise unless a separate editorial decision explicitly establishes otherwise. Wording does not authorize an href change.
7. Do not add a second brand/region/category line merely to repeat the menu or page heading. Keep useful context, limitations and unique parent navigation; apply the trail decision guide rather than deleting by appearance alone.
8. Never claim a guaranteed return, current service availability, accessibility clearance, professional inspection, automatic synchronisation or live hazard information to make a label more persuasive.

## 2. Candidate label matrix

These are writing options, not observed before/after changes or instructions to replace live text.

| Role / property | Documented basis or proposed compact wording | Editorial disposition |
| --- | --- | --- |
| Main Praia Digital groups | Comprar · Investir · Meu Imóvel · Profissionais · Inteligência | Retain the documented taxonomy while checking actual examples. Do not rename groups just to satisfy a character target. |
| Menu control | Menu | Documented in the existing contract; review the actual accessible name and closed/open context later. |
| Close-menu action | Fechar menu | Candidate wording only; no new control or accessibility attribute is implemented. |
| Main contact CTA | Existing contract: Falar com especialista. Possible alternative: Fale com a equipe. | Keep the baseline pending owner review. The alternative requires confirmation of who answers and whether the revised promise is accurate; it is not approved. Destination remains the documented `/interesse.html` for this proposal. |
| Property catalogue navigation | Imóveis | Candidate destination label, not a claim about the current H1 or inventory. |
| Seasonal ROI calculator navigation | ROI de temporada | Candidate compact label. Explain ROI as “retorno sobre o investimento” in nearby explanatory copy when needed, not by overcrowding the header. Keep simulation caveats. |
| Local directory navigation | Cidades · Bairros | Candidate labels for these destinations, not replacements for the five global groups. |
| Independent hub | Apps do litoral / Coastal apps | PT/EN hub-only candidates; retain its full identity in explanatory documentation. Do not imply a production-family integration. |
| Maresia | Maresia em Dia | Retain the full product name; not “Laudo” or a prescribed maintenance service. |
| Access pilot | Acesso à Praia | Retain the full name; documentary coverage is not current operational confirmation. |
| Regional source guide | Costa em Contexto | Retain the full name; not a property-risk map or current alert service. |

A short label that still fits badly remains a review item. Do not declare it fixed, hide necessary words, invent a new abbreviation, reduce legibility, or prescribe CSS/JavaScript changes in this package.

## 3. First-screen content hierarchy

The writing brief should distinguish: property identity; the menu/action needed to navigate; one meaningful page heading; an optional parent/context line that adds information; and any essential limitation close to the relevant claim. Avoid repeating the same brand, category and current-page title in stacked lines without a separate reader purpose.

Do not remove the page heading, skip-link wording, accessible control names, active filters, empty-state explanations or safety/source caveats as “clutter”. The goal is less redundant prose, not fewer ways to navigate or understand a result.

For cities and neighbourhoods, keep the city/region needed to disambiguate a place. For the ROI calculator, keep the distinction between an input-based scenario and a guaranteed investment result. A short header must not turn a nuanced page into a misleading promise.

## 4. Language and property limits

The hub supports PT/EN according to its Markdown architecture. The three original apps in this task retain Portuguese interfaces. Do not promise an English interface or add translated runtime labels for them. Proper names may remain unchanged in English explanatory material. The English hub candidate “Coastal apps” is not a request to translate the apps.

Preserve each app's limits: Maresia organises local records and a bounded ICS snapshot, not automatic sync or professional advice; Acesso presents dated documentary references and unknowns, not verified current accessibility or operation; Costa explains regional sources/scales, not parcel-level safety or real-time hazards. Keep source-publication, source-reading and actual review dates distinct.

Satellite documentation describes seven sites / six utilities, including three repositories outside this assignment. Do not rewrite those topology counts to match this five-repository review.

## 5. Editorial review and acceptance

Use the stable register IDs. For each decision, record the exact evidence/ref, current visible wording or UNKNOWN, proposed wording, destination, language, reason, retained context, actual reviewer/date, blockers and next action. Assign people honestly; role suggestions are not completed human review.

A later, separately authorised manual review should consider representative 320, 360 and 390 px phone views, a wider view, enlarged text, closed/open-menu context, keyboard/screen-reader wording, and long place names. No such checks were performed here. These examples are review considerations, not an automated test plan or permission to run a suite.

Acceptance of this documentation package means the files, links and scope can be read back through the API. Acceptance of particular public wording requires actual editorial review. Implementation, accessibility verification and production publication each remain separate, unauthorised steps. Do not claim improved fit, conversion, accessibility, SEO or rankings from publishing Markdown.

## Source anchors

- [Immutable existing navigation contract](https://github.com/saipradikmallakuntla-tech/praia-digital-seo-audit/blob/44dac228e94d748a950acfd09937ace2100f3a07/docs/navigation-standard.md).
- [Immutable accessibility review boundaries](https://github.com/saipradikmallakuntla-tech/praia-digital-seo-audit/blob/44dac228e94d748a950acfd09937ace2100f3a07/docs/plano-acessibilidade-2026-08-18.md).
- [Immutable satellite architecture and language/data limits](https://github.com/saipradikmallakuntla-tech/praia-digital-satellite-hub/blob/0cd9842627f0de5328af2dd82a4d02a227b3f5b2/SATELLITE_NETWORK_ARCHITECTURE.md).
- [Existing editorial charter, separate workstream](https://github.com/saipradikmallakuntla-tech/praia-digital-seo-audit/blob/3dfa148cbcb862a70fbae1fba252e87e73b32a65/docs/editorial/EDITORIAL_URL_CONTENT_RECONCILIATION_PLAN.md).

## Decision log

- 2026-11-16: AI-assisted writing specification published with the user's explicit documentation-only confirmation. Proposed labels remain unreviewed. No human substantive approval, implementation, browser verification or production change is asserted.
