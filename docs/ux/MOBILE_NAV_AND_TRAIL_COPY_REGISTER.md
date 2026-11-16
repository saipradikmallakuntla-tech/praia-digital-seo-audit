# Mobile Navigation and Trail Copy Register

Version 1.0 · 2026-11-16 UTC · **11 seed records; 11 UNREVIEWED; 0 substantive editorial approvals; technical rollout NOT_AUTHORISED.**

[Header copy standards](MOBILE_HEADER_COPY_STANDARDS.md) · [Trail decision guide](REDUNDANT_TRAIL_REMOVAL_GUIDELINES.md) · [Existing navigation contract](../navigation-standard.md)

## Scope, evidence and publication contract

This is the Markdown decision registry for the reader-reported mobile header/trail clutter issue. Only five repositories under `saipradikmallakuntla-tech` are in scope: the audit fork, satellite hub, Maresia em Dia, Acesso à Praia, and Costa em Contexto. The user explicitly confirmed the documentation branches from each `main`, these three new documents, a link addition in `docs/navigation-standard.md`, four satellite README updates, API read-back and a new linked Supermemory checkpoint. That confirmation does not approve proposed public wording or any implementation.

The review read 36 selected Markdown sources across the five repositories, including all six satellite Markdown files. It inventoried 782 audit `docs/` Markdown paths, not all of which were read. File-tree metadata confirmed the named catalogue/ROI paths and the city/neighbourhood families. Page bodies, live sites, actual header wording and viewport behaviour were not fetched or tested. Path existence is not proof of publication, availability, copy parity or a defect.

All current rendered labels, trails, H1s and exact live destinations are UNKNOWN unless a future dated observation establishes them. Where this document cites the existing Markdown menu contract or README, it identifies a documented baseline, not an observed rendered value. All examples and alternatives below are proposals.

### Immutable branch bases

| Owned repository | Source branch | Verified base commit |
| --- | --- | --- |
| praia-digital-seo-audit | main | `44dac228e94d748a950acfd09937ace2100f3a07` |
| praia-digital-satellite-hub | main | `0cd9842627f0de5328af2dd82a4d02a227b3f5b2` |
| maresia-em-dia | main | `ad87fb55fc7f2b820e2e18fef4756a53b5daba84` |
| acesso-a-praia | main | `2e9785a3e9c4e6244268f2fa40ca49f91fa99434` |
| costa-em-contexto | main | `78d9a6da054bae133a1078a6b643697a8316be45` |

The documentation branch is `docs/mobile-nav-and-trail-copy-spec` in each repository. It starts from that repository's own main, not a technical or other editorial branch. References to the earlier governance package use immutable links; no merge or cherry-pick is requested. Only eight Markdown paths across the five repositories may differ from these bases: this register, its two companion documents, the navigation-standard link addition, and the four satellite READMEs. No code, `sw.js`, workflow, configuration, dataset, PR, merge, automated suite, generator, crawl, deployment or settings change is included.

## Shared record defaults and state model

These defaults apply to every seed record: current rendered copy UNKNOWN; evidence of current viewport fit NOT_COLLECTED; named owner/reviewer UNASSIGNED; actual review date UNSET; human approval NOT_PERFORMED; status UNREVIEWED; implementation NOT_AUTHORISED. Suggested roles below are assignments to make, not claims that people have reviewed anything.

State progression: UNREVIEWED → IN_REVIEW → NEEDS_EVIDENCE or READY_FOR_EDITORIAL_APPROVAL → EDITORIALLY_APPROVED, DEFERRED or OUT_OF_SCOPE. A hold is not approval. Append decisions; never silently replace evidence, renumber records or count registration as completion. Editorial approval never automatically authorises code, accessibility verification, tests or production publication.

Each decision entry must contain: stable ID; repository and exact source ref/path; evidence type and date; current wording/destination or UNKNOWN; proposed wording; page/brand/navigation/trail role; retained geography/parent route/limitation; rationale; source-publication and source-reading dates where applicable; actual reviewer and review date; disposition; dependencies/blockers; last action; next action. Record disagreements rather than inventing consensus.

## Review queue

| ID | Family / property | Proposed writing focus | Initial state |
| --- | --- | --- | --- |
| UXN-001 | Shared Praia Digital header | Preserve taxonomy; review long CTA and repeated brand/region copy | UNREVIEWED |
| UXN-002 | `imoveis.html` | Compact catalogue label; evaluate repeated current-page trail | UNREVIEWED |
| UXN-003 | `ferramentas/calculadora-roi-temporada.html` | Compact ROI label with honest simulation context | UNREVIEWED |
| UXN-004 | City directory | Clear directory wording; preserve unresolved URL identity | UNREVIEWED |
| UXN-005 | City detail family | One city identity and a meaningful directory return | UNREVIEWED |
| UXN-006 | Neighbourhood directory | Clear city/bairro choice without duplicated kickers | UNREVIEWED |
| UXN-007 | Neighbourhood detail family | Preserve municipality and useful parent/return context | UNREVIEWED |
| UXN-008 | Satellite hub | Short PT/EN identity with independent-app and evidence limits | UNREVIEWED |
| UXN-009 | Maresia em Dia | Retain full name and maintenance/ICS limits | UNREVIEWED |
| UXN-010 | Acesso à Praia | Retain full name, dates and explicit operational unknowns | UNREVIEWED |
| UXN-011 | Costa em Contexto | Retain full name and regional-scale/non-certification context | UNREVIEWED |

## UXN-001 — Shared Praia Digital header

- Documented baseline: the existing navigation standard lists Comprar, Investir, Meu Imóvel, Profissionais and Inteligência, 25 submenu links, logo `/`, and “Falar com especialista” at `/interesse.html`. Current rendered copy remains UNKNOWN.
- Proposal: retain the documented taxonomy; use one concise identity instead of repeated brand/region lines. Consider “Fale com a equipe” only if the contact owner confirms that promise and the loss of the specialist wording is acceptable. This alternative is not approved and does not change the destination.
- Trail disposition: NEEDS_EVIDENCE; do not assume the global menu replaces unique visible parent context.
- Roles/dependencies: editorial lead + UX writer + contact/offer owner. No named reviewer assigned. This review must not redefine the separate E01/E02 batches.
- Next action: assign the actual reviewers and obtain a dated representative header observation or user-provided screenshot; record closed/open-menu wording, destination and which lines truly repeat a role before selecting any alternative.

## UXN-002 — Property catalogue

- Source family: `praia-digital-seo-audit` / `imoveis.html`; source path confirmed by metadata, body not read.
- Proposal: “Imóveis” as a compact destination label. Treat a repeated current-page kicker/trail as a removal candidate only after the five-part decision passes. Preserve the meaningful page heading, filters, active-state context and appropriate return route.
- Trail disposition: NEEDS_EVIDENCE, not removed. No current listing count or inventory claim is taken from older documents.
- Roles/dependencies: catalogue editor + UX writer; UXN-001. Named assignees pending.
- Next action: record the actual current labels and destinations, separate filter/status text from decorative trail copy, and document exactly what context would remain after any proposed omission.

## UXN-003 — Seasonal ROI calculator

- Source family: `praia-digital-seo-audit` / `ferramentas/calculadora-roi-temporada.html`; metadata confirmed, body not read.
- Proposal: “ROI de temporada” for compact navigation; explain “retorno sobre o investimento” in suitable explanatory copy and retain an assumptions/not-guaranteed-return caveat. This does not assert which inputs or results the calculator actually implements.
- Trail disposition: NEEDS_EVIDENCE. Keep a meaningful tools parent if it adds orientation; its exact destination is UNKNOWN. Do not invent a tools-directory href.
- Roles/dependencies: tool-content editor + UX writer + qualified finance reviewer for substantive financial claims; UXN-001. The README's `/apps/simulador-roi-temporada/` is not automatically the same editorial identity as this file.
- Next action: establish the exact tool identity, current label and real parent destination; then review the short label and retained simulation limitation without changing calculations or runtime copy.

## UXN-004 — City directory

- Source family: `praia-digital-seo-audit` / `cidades/index.html`; directory-family metadata reviewed, body not read.
- Proposal: “Cidades” as a compact destination label; remove no unique orientation on the assumption that a category is present in the menu.
- Trail disposition: NEEDS_EVIDENCE. Keep existing destinations and aliases pending the separate E01-008 identity/spelling decision.
- Roles/dependencies: city-directory editor + content-governance owner + UX writer; E01-008 and UXN-001. No substantive E01 approval is recorded.
- Next action: record the actual directory heading/trail and destination evidence; draft an explicit keep/shorten/omit rationale without rewriting `index.html` or URL spelling.

## UXN-005 — City detail pages

- Source family: `praia-digital-seo-audit` / `cidades/` detail pages; family inventory is not a claim that every page was read.
- Proposal: one complete city name as the topic identity, with a concise, useful directory return where required. “Cidades” is a parent-label candidate, not proof of its current wording or href.
- Trail disposition: KEEP_CONTEXT provisionally for useful hierarchy/geography; current rendered evidence still needed. Do not reduce long place names to unexplained initials.
- Roles/dependencies: city editor + local-context reviewer + UX writer; UXN-004 / E01-008.
- Next action: choose and record representative city examples and their exact source refs; identify unique parent and geographic information before proposing a repeated-label omission.

## UXN-006 — Neighbourhood directory

- Source family: `praia-digital-seo-audit` / `bairros/index.html`; family metadata and the existing neighbourhood Markdown review were read, not the page body.
- Proposal: “Bairros” as the destination label and a clear city/bairro selection prompt where the existing task supports it. Do not invent controls or a new catalogue.
- Trail disposition: NEEDS_EVIDENCE. Preserve city grouping, anchors and return context; do not reuse historical guide counts as fresh facts.
- Roles/dependencies: neighbourhood editor + content-governance owner + UX writer; E01-009 and UXN-001.
- Next action: document the current heading, city-group context and return labels; keep the pending preferred-URL decision separate from copy simplification.

## UXN-007 — Neighbourhood detail pages

- Source family: `praia-digital-seo-audit` / `bairros/` detail pages; full family text was not reviewed.
- Proposal: retain the full neighbourhood name plus the municipality needed to identify it. “Bairros de <Cidade>” is a parent-phrase pattern only; the placeholder is not publishable copy and no destination is inferred.
- Trail disposition: KEEP_CONTEXT provisionally for the municipality and a useful return path. Similar words in a global menu do not prove redundancy.
- Roles/dependencies: neighbourhood editor + local-context reviewer + UX writer; UXN-006 / E01-009. Any safety or market claim needs its own qualified evidence.
- Next action: select dated examples, including a long or potentially ambiguous place name, and record retained city/parent/article-return context before proposing an omission.

## UXN-008 — Independent coastal satellite hub

- Source: `praia-digital-satellite-hub` / `README.md`, `NETWORK.md`, `SATELLITE_NETWORK_ARCHITECTURE.md` at the immutable base listed above.
- Proposal: “Apps do litoral” / “Coastal apps” as short PT/EN hub labels, subject to review. Preserve the distinction between documentary/example coverage and current availability; network links do not imply shared records or institutional integration.
- Trail disposition: NEEDS_EVIDENCE. App switching is not a breadcrumb hierarchy and must not be lost as decorative repetition.
- Roles/dependencies: hub content owner + PT/EN reviewer + UX writer; existing E02-012. Documentation describes seven sites/six apps; three other app repositories remain outside this task.
- Next action: review the short labels and their destinations, and request the approved release-report location. `DIRECT_PAGES_NETWORK_RELEASE.md` is absent from the inspected hub tree; the README annotation records unavailable evidence, not a newly verified release.

## UXN-009 — Maresia em Dia

- Source: `maresia-em-dia` / `README.md` at its immutable base.
- Proposal: retain “Maresia em Dia” as the compact product identity. Keep maintenance advice boundaries, browser-local record limitations and the bounded ICS snapshot explanation; do not imply automatic synchronisation or engineering inspection.
- Trail disposition: NEEDS_EVIDENCE. Preserve useful network switching; do not add an English-interface promise to this PT app.
- Roles/dependencies: app content owner + maintenance-domain reviewer for substantive advice + UX writer; existing E02-013.
- Next action: document actual header/network wording and any redundant identity line, then propose a bounded wording decision with the existing limits intact. No record, calendar or storage logic change.

## UXN-010 — Acesso à Praia

- Source: `acesso-a-praia` / `README.md` at its immutable base.
- Proposal: retain “Acesso à Praia”. Keep documentary source dates, conflicting/stale information and explicit unknowns visible near the relevant content. Documentary coverage must never become a claim of current accessibility, operation or bathing safety.
- Trail disposition: NEEDS_EVIDENCE. A short header is not grounds to delete dates or limitations. This original app remains PT-only according to the reviewed docs.
- Roles/dependencies: app content owner + documentary-source reviewer + UX writer; existing E02-014.
- Next action: record the real identity/trail/network labels and decide which repeats lack a role; preserve the distinction between source-publication, reading and actual review dates. No new field or operational check is claimed.

## UXN-011 — Costa em Contexto

- Source: `costa-em-contexto` / `README.md` at its immutable base.
- Proposal: retain “Costa em Contexto”. Preserve regional scale, source age, reviewed-geography limits and non-certification language. Do not label it as a parcel-risk map, safety clearance or current hazard alert.
- Trail disposition: NEEDS_EVIDENCE. Keep useful app switching and geographic/source context. No English runtime interface is inferred.
- Roles/dependencies: app content owner + source/scale reviewer + UX writer; existing E02-015.
- Next action: record actual header and contextual lines, then review any omission against the source-scale and geographic limits. No map, data, note/export or app-code change.

## Editorial gates and next cursor

Review order: UXN-001, then catalogue/ROI, city/neighbourhood families, and the four scoped satellite properties. Independent evidence gathering can proceed, but dependent copy cannot be signed off on an unresolved taxonomy, identity or safety promise.

Before editorial approval, each record needs actual evidence, a named reviewer/date, an explicit retained-context/destination rationale, and a resolved blocker or honest deferral. No current-page text or fit may be invented. No test results may be inferred from historical reports or documentation-only publication.

Initial substantive cursor: **UXN-001**. Last action: AI-assisted proposed writing standards and 11 seed records prepared for the user-confirmed Markdown publication. Next action: assign the editorial lead/UX writer/contact owner and obtain the representative header evidence described in UXN-001. No substantive review has begun.

## Linked workstreams, blockers and preservation

- E01-008/E01-009 and E02-012–E02-015 remain in the separate existing editorial package; their records and approval counts are unchanged. This UXN register does not renumber, supersede or complete them.
- Previous Supermemory documents in `praia_digital`: `praia-digital-editorial-url-governance-2026-11-16` and `praia-digital-canonical-batches-2026-11-15`. Preserve both. The latter still says its report is pending although the report exists on the owned technical branch; do not resume repairs or overwrite history in this writing pass.
- Parked canonical/URL queues, scripts, operational/noindex material, templates, fixtures and backups are not UXN targets. No blanket URL, indexing or breadcrumb-schema changes.
- The inherited audit README's production-publication claim is historical fork context, not permission to deploy the fork or modify upstream. Satellite topology documentation's older scope statements do not override this task's explicit five-owned-repository writing boundary.
- Hub release evidence remains unavailable. No 42-link, HTTP, browser, accessibility, real-device or production verification is claimed.

## Publication verification and checkpoint contract

After committing, independently retrieve all eight changed Markdown files at their immutable commits, read the five base-to-docs comparisons and commit parents, and confirm that the main/technical/other editorial heads and non-deploying settings remain unchanged. No repository program or suite is to run. Satellite README pointers must use the new audit commit SHA, never a guessed `main` location. The navigation-standard change is an append-only link section, not a rewrite of its implementation text.

Create and retrieve one NEW Supermemory document: namespace `praia_digital`, ID `praia-digital-mobile-nav-and-trail-copy-spec-2026-11-16`. It must contain immutable file/commit links, branch bases, the exact eight-file receipt, verification scope, earlier checkpoint IDs, 11 UNREVIEWED / 0 approved records, blockers, last action and cursor UXN-001. Preserve earlier checkpoint content/metadata/timestamps. Distinguish saved document content from asynchronous learned-memory extraction. A containing commit SHA cannot be embedded in this file without changing that SHA; the immutable receipt belongs in the checkpoint and user handoff.

## Immutable key sources

- [Original navigation standard](https://github.com/saipradikmallakuntla-tech/praia-digital-seo-audit/blob/44dac228e94d748a950acfd09937ace2100f3a07/docs/navigation-standard.md).
- [Neighbourhood content/return-context review](https://github.com/saipradikmallakuntla-tech/praia-digital-seo-audit/blob/44dac228e94d748a950acfd09937ace2100f3a07/docs/neighborhood-guide-review.md).
- [Inherited README: journey and distinct production tool URLs](https://github.com/saipradikmallakuntla-tech/praia-digital-seo-audit/blob/44dac228e94d748a950acfd09937ace2100f3a07/README.md).
- [Existing editorial charter and reviewed-source manifest](https://github.com/saipradikmallakuntla-tech/praia-digital-seo-audit/blob/3dfa148cbcb862a70fbae1fba252e87e73b32a65/docs/editorial/EDITORIAL_URL_CONTENT_RECONCILIATION_PLAN.md).
- [E01 directory/guide dependencies](https://github.com/saipradikmallakuntla-tech/praia-digital-seo-audit/blob/3dfa148cbcb862a70fbae1fba252e87e73b32a65/docs/editorial/E01_PUBLIC_GUIDES_AND_URLS_REGISTER.md).
- [E02 satellite dependencies](https://github.com/saipradikmallakuntla-tech/praia-digital-seo-audit/blob/3dfa148cbcb862a70fbae1fba252e87e73b32a65/docs/editorial/E02_LANDING_PAGES_AND_SATELLITES_REGISTER.md).
- [Hub README](https://github.com/saipradikmallakuntla-tech/praia-digital-satellite-hub/blob/0cd9842627f0de5328af2dd82a4d02a227b3f5b2/README.md) · [Architecture](https://github.com/saipradikmallakuntla-tech/praia-digital-satellite-hub/blob/0cd9842627f0de5328af2dd82a4d02a227b3f5b2/SATELLITE_NETWORK_ARCHITECTURE.md) · [Network policy](https://github.com/saipradikmallakuntla-tech/praia-digital-satellite-hub/blob/0cd9842627f0de5328af2dd82a4d02a227b3f5b2/NETWORK.md).
- [Maresia README](https://github.com/saipradikmallakuntla-tech/maresia-em-dia/blob/ad87fb55fc7f2b820e2e18fef4756a53b5daba84/README.md) · [Acesso README](https://github.com/saipradikmallakuntla-tech/acesso-a-praia/blob/2e9785a3e9c4e6244268f2fa40ca49f91fa99434/README.md) · [Costa README](https://github.com/saipradikmallakuntla-tech/costa-em-contexto/blob/78d9a6da054bae133a1078a6b643697a8316be45/README.md).

## Decision log

- 2026-11-16: User confirmed the five main-based documentation branches, eight Markdown-only changes, independent API read-back and a new linked checkpoint. AI-assisted standards/register prepared; 11 records remain UNREVIEWED with no actual human approvals. No further Mem0 or Firecrawl calls, code changes, suite execution, PR, merge or deployment is included.
