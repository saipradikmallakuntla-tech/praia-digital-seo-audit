# Editorial Navigation Decision Register

Version 1.0 · 2026-11-16 UTC · **14 seed records; 14 UNREVIEWED; 0 substantive editorial approvals. Documentation publication is authorized separately.**

[IA and navigation standards](IA_AND_NAVIGATION_STANDARDS.md) · [Section trails and parent links](SECTION_TRAILS_AND_PARENT_LINKS.md)

## 1. Authority, evidence and status

This register tracks decisions for the five named owned repositories only, on `docs/editorial-navigation-and-ia-standards`. The owner confirmed publication of Markdown and a Drive briefing, not approval of every proposed public label, factual claim or technical rollout. Named editors, coordinators, reviewers and governance owners remain UNASSIGNED; substantive reviews are NOT_PERFORMED.

Live structure observations below come from the preceding read-only public review on 2026-11-16. The Markdown sources are pinned below. They do not prove every guide has a trail defect, that an interactive menu was tested, or that a missing document exists elsewhere. No new Firecrawl call, browser/code suite or repository program is part of publication.

## 2. State and required decision record

Workflow: UNREVIEWED → IN_REVIEW → NEEDS_EVIDENCE or READY_FOR_EDITORIAL_APPROVAL → EDITORIALLY_APPROVED, DEFERRED or OUT_OF_SCOPE. A hold is not approval. Technical status remains NOT_AUTHORIZED regardless of editorial status.

For each reviewed ID append, rather than silently overwrite:

- Repository, exact page/document path and immutable source ref.
- Observed label and role, intended destination/anchor, language and geographic scope; use UNKNOWN when not evidenced.
- Proposed wording, primary parent, related destinations and reader-purpose rationale.
- Source publication date, source-reading date, actual review date and named reviewer.
- Retained context/caveats; related E01/E02/UXN IDs; blockers and disposition.
- Actual decision, approver/date, last action and exact next action.

Suggested roles are assignments to make, not invented people. Preserve previous record IDs and history. Review quarterly and whenever wording, source, parent or coverage changes.

## 3. Seed queue

All rows start UNREVIEWED, with named owner/reviewer UNASSIGNED, approval NOT_PERFORMED and technical status NOT_AUTHORIZED.

| ID | Evidence / current position | Proposed editorial decision | Proposed reviewing roles | Dependency / exact next action |
| --- | --- | --- | --- | --- |
| IAN-001 | Main public menu and existing guidance use Comprar, Investir, Meu Imóvel, Profissionais, Inteligência. | Retain these five journey groups; do not replace them with the four content-section labels. | Editorial lead + governance owner | Related UXN-001. Assign actual reviewers and confirm role distinctions before reviewing variants. |
| IAN-002 | Main navigation links Imóveis to `/imoveis.html`; individual child-guide trails were not exhaustively inspected. | Use Imóveis as the section label and documented parent; preserve inventory/filter context. | Property editor + regional coordinator | Related UXN-002. Select one real child-guide example and record its current trail/return destination. |
| IAN-003 | Ferramentas points to `/ferramentas/index.html`, currently presenting three seasonal-rental calculators. | Keep Ferramentas distinct from production Apps gratuitos and the independent directory; document real parent relationships. | Tools editor + subject reviewer | Related UXN-003/E02-016. Confirm scope and one representative tool-to-parent relationship without normalizing URLs. |
| IAN-004 | Bairros points to `/bairros/index.html`; the index includes local guides, themes, aliases and unconfirmed references. | Retain municipality context and verified city grouping; do not invent intermediary paths or an official-neighbourhood count. | Neighbourhood editor + regional coordinator | Related E01-009/UXN-006/UXN-007. Record an actual city anchor/page and handle a same-name neighbourhood case. |
| IAN-005 | Main navigation says Blog; landing heading says Blog & Estudos. | Use Blog for navigation, retain meaningful article/page titles, and parent editorial articles by purpose. | Blog editor + governance owner | Add explicit Blog-family examples; distinguish a heading difference from a taxonomy defect. |
| IAN-006 | Hub identity is Aplicativos do Litoral; public directory lists six utilities. | Preserve full network size while limiting this review to the hub plus three original apps; use the common README summary. | Hub editor + governance owner | Related E02-012/UXN-008. Confirm coverage wording; leave the other three repositories outside scope. |
| IAN-007 | Maresia uses its product name; network links also use Manutenção. | Keep Maresia em Dia as product identity and Manutenção as a role-specific descriptor; preserve maintenance/ICS limits. | Maresia editor + qualified maintenance reviewer | Related E02-013/UXN-009. Assign reviewers and approve the reader promise without implying inspection or automatic sync. |
| IAN-008 | Acesso public identity uses Acesso à Praia; main README heading omits the accent. | Use the proper name in documentation, dated evidence and explicit unknowns; never equate coverage with current service. | Acesso editor + service/accessibility evidence reviewer | Related E02-014/UXN-010. Separate original source dates, reading date and actual operational evidence. |
| IAN-009 | Costa product identity and Contexto regional descriptor coexist. | Keep Costa em Contexto as identity; explain regional source/scale limits without parcel-level safety claims. | Costa editor + qualified regional-source reviewer | Related E02-015/UXN-011. Confirm scope and source/scale wording; no new risk verification is asserted. |
| IAN-010 | Satellite returns vary between Central de apps and Central da rede. | Standardize documentation on Central de apps for the exact hub root; treat it as network switching, not fabricated parentage. | Hub/app editors + governance owner | Related UXN-008–UXN-011. Review label by role and preserve each independent app identity. |
| IAN-011 | The hub's README/architecture reference `DIRECT_PAGES_NETWORK_RELEASE.md`, absent from the inspected main tree. | Mark release evidence unavailable; do not publish a fabricated release receipt or reuse old test counts as current proof. | Documentation owner | Related KM-03/E02-012. Request the approved report/location; keep the blocker open. |
| IAN-012 | Hub supports PT/EN; the three original apps are documented as PT. | Preserve honest language labels and geographic/date limits across every README. | Editors + regional coordinators | Related E02-012–E02-015. Verify the wording of each summary, not runtime translations. |
| IAN-013 | Prior URL and mobile/trail packages exist on separate documentation branches with unresolved substantive reviews. | Cross-reference their immutable records and this package; do not merge branches, reset cursors or inherit unearned approval. | Governance owner | Preserve E01/E02/UXN IDs and URL questions; record any actual conflict before sign-off. |
| IAN-014 | No matching coastal navigation/style notes were found in the prior Drive searches. | Create the confirmed Drive brief as a linked index to the nine committed Markdown documents, not a competing source of rules. | Documentation owner + governance owner | After API read-back, record the actual commit/file links and briefing URL in the publication receipt. |

## 4. Evidence anchors

### Observed public structure

- [Production home](https://praia.digital/), [Imóveis](https://praia.digital/imoveis.html), [Ferramentas](https://praia.digital/ferramentas/index.html), [Bairros](https://praia.digital/bairros/index.html), [Blog](https://praia.digital/blog/index.html).
- [Independent hub](https://saipradikmallakuntla-tech.github.io/praia-digital-satellite-hub/), [Maresia](https://saipradikmallakuntla-tech.github.io/maresia-em-dia/), [Acesso](https://saipradikmallakuntla-tech.github.io/acesso-a-praia/), [Costa](https://saipradikmallakuntla-tech.github.io/costa-em-contexto/).

These URLs identify observed sources, not a permanent availability guarantee or a freshly repeated crawl.

### Immutable owned Markdown sources and prior records

- [Navigation guidance at reviewed main](https://github.com/saipradikmallakuntla-tech/praia-digital-seo-audit/blob/44dac228e94d748a950acfd09937ace2100f3a07/docs/navigation-standard.md).
- [Editorial checklist at reviewed main](https://github.com/saipradikmallakuntla-tech/praia-digital-seo-audit/blob/44dac228e94d748a950acfd09937ace2100f3a07/docs/editorial/CHECKLIST_REVISAO.md).
- [Neighbourhood review and its historical verification limits](https://github.com/saipradikmallakuntla-tech/praia-digital-seo-audit/blob/44dac228e94d748a950acfd09937ace2100f3a07/docs/neighborhood-guide-review.md).
- [Hub README](https://github.com/saipradikmallakuntla-tech/praia-digital-satellite-hub/blob/0cd9842627f0de5328af2dd82a4d02a227b3f5b2/README.md), [network policy](https://github.com/saipradikmallakuntla-tech/praia-digital-satellite-hub/blob/0cd9842627f0de5328af2dd82a4d02a227b3f5b2/NETWORK.md), [architecture](https://github.com/saipradikmallakuntla-tech/praia-digital-satellite-hub/blob/0cd9842627f0de5328af2dd82a4d02a227b3f5b2/SATELLITE_NETWORK_ARCHITECTURE.md).
- [Maresia README](https://github.com/saipradikmallakuntla-tech/maresia-em-dia/blob/ad87fb55fc7f2b820e2e18fef4756a53b5daba84/README.md), [Acesso README](https://github.com/saipradikmallakuntla-tech/acesso-a-praia/blob/2e9785a3e9c4e6244268f2fa40ca49f91fa99434/README.md), [Costa README](https://github.com/saipradikmallakuntla-tech/costa-em-contexto/blob/78d9a6da054bae133a1078a6b643697a8316be45/README.md).
- [E01 URL questions](https://github.com/saipradikmallakuntla-tech/praia-digital-seo-audit/blob/3dfa148cbcb862a70fbae1fba252e87e73b32a65/docs/editorial/E01_PUBLIC_GUIDES_AND_URLS_REGISTER.md), [E02 satellite/landing records](https://github.com/saipradikmallakuntla-tech/praia-digital-seo-audit/blob/3dfa148cbcb862a70fbae1fba252e87e73b32a65/docs/editorial/E02_LANDING_PAGES_AND_SATELLITES_REGISTER.md), [UXN mobile/trail records](https://github.com/saipradikmallakuntla-tech/praia-digital-seo-audit/blob/6cb8f058e2fd8c55a7db901ad86cacbbff5287ac/docs/ux/MOBILE_NAV_AND_TRAIL_COPY_REGISTER.md).

## 5. Publication, checkpoints and next action

Documentation publication and substantive editorial approval are separate. The publication receipt is created after read-only API checks: five new branches from their own main baselines; Markdown-only audit history and one README-only commit per satellite; all nine committed files read back; immutable audit links in every README; unchanged pre-existing heads and publication settings. The Drive brief carries all nine resulting GitHub file links.

No record is marked substantively approved merely because its README or standard is committed. Do not add the containing commit SHA to this file in a self-referential amendment; keep immutable receipts in the Drive brief and completion response.

Current substantive cursor: **IAN-001**. Next action: assign the actual editorial lead and governance owner, confirm the global-menu-versus-section distinction, and then review IAN-002–IAN-005 with real page-family examples. Record evidence gaps and justified deferrals; no implementation follows automatically.

### Decision history

- 2026-11-16: Owner explicitly confirmed this documentation package, README branches, API read-back and Drive briefing. Fourteen editorial seed records registered; zero human substantive reviews or approvals recorded. All technical execution remains outside scope.
