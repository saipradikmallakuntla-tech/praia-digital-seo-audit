# Information Architecture & Editorial Navigation Standards

Version 1.0 · 2026-11-16 UTC · **Documentation publication authorized; public-copy decisions remain PROPOSED. No technical rollout.**

[Section trails and parent links](SECTION_TRAILS_AND_PARENT_LINKS.md) · [Decision register](NAVIGATION_DECISION_REGISTER.md) · [Existing navigation guidance](../navigation-standard.md) · [Editorial checklist](CHECKLIST_REVISAO.md)

## 1. Purpose and publication boundary

Give editors and regional coordinators one documented vocabulary, section map, parent-link convention and review process. This is a non-coding content-architecture pass, not a menu redesign or a claim that live navigation has been fixed.

The authorized branch is `docs/editorial-navigation-and-ia-standards` in exactly five repositories owned by `saipradikmallakuntla-tech`. Each branch starts at its own reviewed `main` commit:

| Repository | Main baseline |
| --- | --- |
| praia-digital-seo-audit | `44dac228e94d748a950acfd09937ace2100f3a07` |
| praia-digital-satellite-hub | `0cd9842627f0de5328af2dd82a4d02a227b3f5b2` |
| maresia-em-dia | `ad87fb55fc7f2b820e2e18fef4756a53b5daba84` |
| acesso-a-praia | `2e9785a3e9c4e6244268f2fa40ca49f91fa99434` |
| costa-em-contexto | `78d9a6da054bae133a1078a6b643697a8316be45` |

Only the three new editorial Markdown documents, Markdown cross-references in existing guidance/checklist, and the four scoped README.md files are publication targets. The Google Drive brief is a linked summary, not a second rulebook. Keep `main`, `seo-improvements`, all other pre-existing branches, and all upstream/third-party repositories unchanged. Do not merge or cherry-pick technical work.

No HTML, CSS, JavaScript, `sw.js`, other code, workflow, configuration, schema, dataset, canonical, redirect, sitemap or URL is changed. No test suite, repository program, generator, browser automation, PR, merge, deployment or settings change is authorized. Historical commands in existing documents are evidence only. No further Firecrawl call belongs to this publication.

## 2. Evidence and limits

The preceding read-only review on 2026-11-16 used Exa search/live content retrieval and static public-page inspection. It observed the main site, four scoped satellite roots and the four section landing pages below. This is not a rendered-browser assessment, exhaustive guide-trail audit, indexation assessment or functional verification.

- [Praia Digital](https://praia.digital/) uses the journey groups **Comprar, Investir, Meu Imóvel, Profissionais, Inteligência**. Retain these as the global-menu baseline; the section taxonomy below is not a replacement menu.
- The [independent hub](https://saipradikmallakuntla-tech.github.io/praia-digital-satellite-hub/) lists six utilities. Only that hub and three original apps are in this task. Preserve the documented seven-site/six-utility topology; three additional repositories remain outside the review/write boundary.
- Satellite navigation mixes product names, functional descriptors and hub-return aliases such as “Central de apps” and “Central da rede”. Different roles can legitimately have different wording; record the role before calling a difference a defect.
- “Blog & Estudos” is a page heading, while “Blog” is a navigation label. They need not be identical. Likewise, a promotional heading is not a new taxonomy category.
- Drive searches in English and Portuguese returned no matching coastal navigation/style documentation. This is a search result, not proof that no such document exists anywhere. Firecrawl had zero credits during that review and was not used to scrape.
- All six Markdown files in the four scoped satellite main trees and selected audit guidance were reviewed. The large audit repository was not read exhaustively. Reading a source does not renew its underlying facts.

## 3. Controlled section taxonomy

| Stable editorial key | Navigation label | Observed parent destination | Reader purpose and limits |
| --- | --- | --- | --- |
| imoveis | Imóveis | [Property catalogue](https://praia.digital/imoveis.html) | Find and understand property listings. Do not infer current stock from geography or older documentation. |
| ferramentas | Ferramentas | [Tools landing page](https://praia.digital/ferramentas/index.html) | Reach tools and their explanatory context. The current landing page presents three seasonal-rental calculators; do not describe it as a complete directory of every app. |
| bairros | Bairros | [Neighbourhood directory](https://praia.digital/bairros/index.html) | Reach local guides by city, preserving geography, alternative-name and evidence distinctions. An index is not an official register of distinct neighbourhoods. |
| blog | Blog | [Blog index](https://praia.digital/blog/index.html) | Reach editorial articles and studies. Article type and evidence must support any “study” claim. |

Use Portuguese accents and natural capitalization in display names; stable keys are documentation identifiers, not instructions to rename paths. Preserve the exact observed `.html`/`index.html` destinations above. No automatic trailing-slash normalization, canonical selection, migration or redirect is implied.

Each page gets one primary editorial parent by reader purpose. A blog article about a neighbourhood remains under Blog unless a documented identity decision says otherwise; Bairros is then a contextual related destination. Topic, municipality, audience and content type are separate descriptive facets, not competing parent sections. Do not add empty intermediate categories or undocumented city URLs.

Keep three distinct concepts: **Ferramentas** (the documented section), **Apps gratuitos** (the production-family [apps hub](https://praia.digital/apps/)), and **Aplicativos do Litoral** (the independent owned satellite directory). A contextual link between them does not establish shared accounts, records, deployment authority, institutional affiliation or reciprocal integration.

## 4. Satellite identity and navigation vocabulary

| Role | Proposed documentation convention | Preserved meaning |
| --- | --- | --- |
| Independent directory identity | Aplicativos do Litoral | Full directory identity; existing English name may be explained in hub documentation. |
| Return/switch link to that directory | Central de apps | One consistent label for the same network destination. It is not a breadcrumb asserting that independent apps are production-site children. |
| Maintenance product | Maresia em Dia | “Manutenção” is a functional descriptor, not a replacement brand or an inspection promise. |
| Documentary access product | Acesso à Praia | Preserve accents and full name; documentary references are not verified current operation or accessibility. |
| Regional-source product | Costa em Contexto | “Contexto regional” is a descriptor; no parcel-level safety decision or live alert. |

README summaries use the same order: **Finalidade → Destinos de navegação → Retorno e relação com a rede → Idioma e cobertura → Limites editoriais → Padrões, evidências e revisão**. Include the exact app/hub roots, product names and immutable links to all three audit standards. Keep descriptions concise; do not invent destinations or operational facts to fill the template.

The hub is PT/EN; the three original apps retain Portuguese interfaces. Proper names remain intact in English explanatory prose. Do not imply an English interface for the original apps. Hub filters describe documentary coverage or examples, not current service availability.

## 5. Reconcile existing work without duplicating approvals

These existing packages remain separate, immutable evidence:

- [URL/content reconciliation charter](https://github.com/saipradikmallakuntla-tech/praia-digital-seo-audit/blob/3dfa148cbcb862a70fbae1fba252e87e73b32a65/docs/editorial/EDITORIAL_URL_CONTENT_RECONCILIATION_PLAN.md), including E01/E02 identities and URL questions.
- [Mobile header copy standards](https://github.com/saipradikmallakuntla-tech/praia-digital-seo-audit/blob/6cb8f058e2fd8c55a7db901ad86cacbbff5287ac/docs/ux/MOBILE_HEADER_COPY_STANDARDS.md).
- [Redundant trail decision guide](https://github.com/saipradikmallakuntla-tech/praia-digital-seo-audit/blob/6cb8f058e2fd8c55a7db901ad86cacbbff5287ac/docs/ux/REDUNDANT_TRAIL_REMOVAL_GUIDELINES.md).
- [Mobile/trail proposal register](https://github.com/saipradikmallakuntla-tech/praia-digital-seo-audit/blob/6cb8f058e2fd8c55a7db901ad86cacbbff5287ac/docs/ux/MOBILE_NAV_AND_TRAIL_COPY_REGISTER.md).

This package adds the four-section architecture and common README conventions. Reference related E01/E02/UXN IDs; do not renumber them, mark their reviews complete, silently supersede their unresolved decisions or merge their branches. An unresolved conflict goes into the new decision register with a named decision owner still to be assigned.

The hub's `DIRECT_PAGES_NETWORK_RELEASE.md` is referenced but absent from the inspected main tree. Mark release evidence unavailable and request its approved location. Do not create a substitute receipt, repeat historical test counts as fresh evidence, or claim all 42 network links were verified in this pass.

## 6. Editorial governance

Assignments below are roles, not invented people or completed reviews:

- Content editor: proposes labels, primary parent, description and related destinations.
- Regional coordinator: checks municipality/place identity, source dates, geographic scope and unknowns.
- Qualified subject reviewer: reviews finance, maintenance, accessibility or regional-source claims within actual competence.
- Content-governance owner: resolves cross-property vocabulary, records evidence and approves editorial decisions.

All named-person assignments and substantive approvals start **UNASSIGNED / NOT_PERFORMED**. Documentation publication was confirmed by the repository owner; that does not approve public wording, certify facts or authorize implementation. Use the workflow and records in the [decision register](NAVIGATION_DECISION_REGISTER.md).

Review quarterly and whenever a label, parent, destination, coverage statement or source changes. Distinguish source publication date, source-reading date, actual human-review date and API verification date. A reading date never updates an old operational fact. Preserve history and explain exceptions rather than overwriting a decision silently.

## 7. Acceptance and publication receipt

Acceptance of this package means read-only API verification of commit parentage, exact changed Markdown paths, every committed file's bytes/blob identity, immutable cross-references and unchanged pre-existing branch heads. Repository automation/Pages settings are read only, not changed. No code/browser suite or live link crawl is part of acceptance.

The Drive brief and completion message carry the resulting immutable commit/file links. This document uses relative package links because embedding its own containing commit would change that commit. Documentation verification is not proof of improved usability, accessibility, rankings or live-site behavior.

### Decision history

- 2026-11-16: User confirmed publication of this Markdown-only package, four README updates on the named documentation branches, API read-back and a Google Drive briefing. Public-copy proposals remain unreviewed; technical rollout remains unauthorized.
