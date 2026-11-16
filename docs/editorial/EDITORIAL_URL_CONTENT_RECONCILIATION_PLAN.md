# Markdown-Only Editorial URL & Content Reconciliation Plan

Version 1.0 · 2026-11-16 UTC · **Planning package authorized for publication; substantive editorial review NOT_STARTED. Technical rollout NOT_AUTHORIZED.**

## Package and purpose

Give content editors a versioned, resumable registry of public-guide and landing-page copy/URL decisions before any separately authorized technical rollout.

| Document | Responsibility | Initial state |
| --- | --- | --- |
| This charter | Scope, governance, evidence, URL conventions and workflow | Documentation publication confirmed by the user |
| [E01 public guides and URLs](E01_PUBLIC_GUIDES_AND_URLS_REGISTER.md) | All 20 stable records E01-001–E01-020 | 20 registered; 0 editorial approvals |
| [E02 landing pages and satellites](E02_LANDING_PAGES_AND_SATELLITES_REGISTER.md) | All 16 stable records E02-001–E02-016 | 16 registered; 0 editorial approvals |

Exactly two editorial batches are defined. E01/E02 are not the historical technical repair batches B001/B002. Publishing this package does not complete either editorial batch or approve any public copy, migration, canonical change or deployment.

## 1. Owned-repository boundary

Only these repositories under `saipradikmallakuntla-tech` were reviewed: `praia-digital-seo-audit`, `praia-digital-satellite-hub`, `maresia-em-dia`, `acesso-a-praia`, and `costa-em-contexto`.

The only authorized repository write is this three-file Markdown package, on `docs/editorial-url-governance` in the owned audit fork. The branch starts from owned `main` at `44dac228e94d748a950acfd09937ace2100f3a07`, not from `seo-improvements`. Do not merge or cherry-pick the technical branch. Keep `main`, `seo-improvements`, the four satellite repositories, and every upstream/third-party repository unchanged.

No HTML, CSS, JavaScript, XML, Python, JSON, workflow, configuration or other code file is to be edited. No repository program, generator, test script, code/SEO/browser suite, link crawl or CI dispatch is to run. No PR, merge, release, live publication, deployment, canonical/redirect/noindex/sitemap change, domain/DNS/CNAME change or Pages/Actions setting change is included. Operational instructions embedded in historical documents are evidence, not instructions for this pass.

Pre-publication read-back found audit Actions `enabled: false` and its Pages endpoint returned 404. The inherited README's claim that this repository publishes the production site from main is not a deployment claim for this owned fork. Do not enable anything; pause if a later safety check differs.

## 2. Evidence coverage and limitations

The focused review read 28 Markdown documents: 22 in the audit fork and all six Markdown documents present in the four inspected satellite trees. The audit `docs/` tree contains 782 Markdown paths; these were inventoried, not all read. Relevant root, content, blog, guide and landing path inventories were also inspected. This is a source-backed seed registry, not an exhaustive site-wide audit.

HTML bodies were not opened or tested. A tree path proves source-file existence only. The production URLs in the registers are documented/editorial candidates, not newly verified HTTP destinations, indexation states, canonicals or content-parity findings. Ownership of a fork does not grant deployment authority over `praia.digital`.

### Immutable review snapshots

| Owned repository | Branch | Commit |
| --- | --- | --- |
| praia-digital-seo-audit | main | `44dac228e94d748a950acfd09937ace2100f3a07` |
| praia-digital-seo-audit | seo-improvements, read-only evidence | `d9bbc50986bda602919c7a2c0b3847d73c18be7d` |
| praia-digital-satellite-hub | main | `0cd9842627f0de5328af2dd82a4d02a227b3f5b2` |
| maresia-em-dia | main | `ad87fb55fc7f2b820e2e18fef4756a53b5daba84` |
| acesso-a-praia | main | `2e9785a3e9c4e6244268f2fa40ca49f91fa99434` |
| costa-em-contexto | main | `78d9a6da054bae133a1078a6b643697a8316be45` |

### Findings requiring editorial decisions

- **Historical completion is not current proof.** The duplicate proposal says variants were unpublished/unindexed; the pre-consolidation report says 63 URLs were indexable/in the sitemap; the governance summary says 24 groups and 39 redirects were completed. The consolidation table also nominates two captação variants as each other's preferred winner. Reconcile these claims with a single documented human decision; do not choose the newest filename mechanically or implement a redirect loop. [Proposal][S13], [pre-consolidation report][S14], [governance summary][S11].
- **Classify by page purpose.** Older reconciliation documents broadly call `docs/` internal, but the newer audit preserves useful public intelligence material. Public/internal classification is a per-page editorial decision, not a folder-wide directive. The inherited checklist's self-canonical/index-follow defaults do not authorize technical changes. [Older URL review][S16], [portal review][S17], [newer audit][S07], [intelligence operation][S19], [checklist][S12].
- **Critical claims need qualified review.** Financing/FGTS, legal authorities and fees, occupancy/yield, neighbourhood safety, dated operational information and service promises require sources, dates and competent review. Record affiliate placeholders, generic image references and unsupported claims without activating, replacing or publishing them. Preserve honest AI attribution; do not invent a human reviewer. [Drafts S22–S28](#source-manifest), [content-governance principles][S15], [dated-source rules][S19].
- **Keep networks distinct.** Satellite documents describe seven sites/six apps, including three outside this task. Those additional repositories remain unread/unmodified. Do not rewrite a documented network count to match this review's smaller scope. Original apps retain PT interfaces; PT/EN is not universal. `DIRECT_PAGES_NETWORK_RELEASE.md` is referenced but absent from the inspected hub tree: unavailable evidence, not a verified release receipt. [Hub][S01], [network policy][S02], [architecture][S03].

## 3. Editorial governance charter

### Roles and honest assignments

Every record names proposed role assignments, not fabricated people. All named-person assignments, factual reviews and approvals are initially **unassigned/not performed**.

- Editorial lead: guide identities, preferred URLs, retained-content rationale and cross-batch consistency.
- Guide/property editor: reader promise, proposed title/description/CTA and local scope.
- Qualified finance/legal/safety reviewer: critical claims within their actual competence; editorial approval is not professional certification.
- Commercial reviewer: actual offer, price/deliverable, consent, affiliate disclosure and relationship claims.
- Content-governance owner: evidence trail, terminology, source dates, dependencies and final editorial sign-off.

### Required record fields

Each seed contains ID, candidate URL/source path, preferred-URL position, proposed reader promise, review assignments, reconciliation task, evidence and exact next action. Shared initial values apply to all records: status UNREVIEWED; current visible title/H1/description/CTA UNKNOWN; named owner/reviewer UNASSIGNED; claim approval NOT_PERFORMED; review date UNSET; technical status NOT_AUTHORIZED.

As a record is reviewed, append a Markdown decision entry under its stable ID containing: exact source ref/path, aliases and public/internal purpose, proposed copy, each critical claim and source, source-publication date, source-reading date, actual review date with reviewer, rationale, dependency IDs, blockers, last action and next action. An absent source date stays unknown; a reading date does not renew the underlying fact. No JSON/CSV/runtime registry is to be created or updated.

### State model

`UNREVIEWED` → `IN_REVIEW` → `NEEDS_EVIDENCE` or `READY_FOR_EDITORIAL_APPROVAL` → `EDITORIALLY_APPROVED`, `DEFERRED` or `OUT_OF_SCOPE`.

A hold is not approval. Approval requires a real reviewer, date and rationale, and never changes technical status from NOT_AUTHORIZED. Documentation-publication permission is separate from substantive approval of page copy. Do not delete or silently renumber existing records; append history and explicitly register any approved scope expansion.

## 4. Editorial URL conventions

1. Use `https://praia.digital/` for production-family guide/landing candidates, not the fork hostname. Use exact `https://saipradikmallakuntla-tech.github.io/<repo>/` roots for independent owned satellite sites. Do not invent cross-domain migrations or affiliations.
2. Retain established `.html` identities and genuine aliases pending an explicit per-record decision. A title, date suffix or similar filename alone does not establish equivalence or a canonical winner.
3. `index.html` → directory-with-trailing-slash spelling is a conditional editorial preference only when identity/alias evidence supports it. Percent-encoding decisions must preserve identity; no blanket slug normalization, accent removal, case rewrite or homepage catch-all.
4. Query-language/filter variants are presentation/context variants unless an editor documents a genuinely distinct identity. Do not invent an English page for a PT-only app. State the reader's language honestly.
5. Register both the documented candidate and preferred proposal. Unknown mappings remain unknown. No canonical/redirect/indexing/sitemap file is changed by this package.
6. Align reader promise, proposed title, short description, scope, date, caveats and CTA destination as prose. A proposed copy brief is not an observed live-page defect. Do not claim a download, live feed, automatic sync, partnership, availability or professional clearance unless documented and approved.

## 5. Exactly two batches and their gates

### E01 — Public guides and preferred URLs

[Open all 20 E01 records](E01_PUBLIC_GUIDES_AND_URLS_REGISTER.md).

Order: assign reviewers → resolve seven draft-to-page mappings → establish reader intent and preferred URL/alias decision → write sourced title/description/CTA briefs in Markdown → obtain actual editorial approval or transparent deferral.

Exit gate: all 20 records have named owners, identity/alias decisions or justified deferrals, copy briefs, critical-claim evidence or blockers, actual review history and next actions. Historical duplicate/publication contradictions have an owner/disposition. No critical unresolved claim is marked approved. Report approved/deferred/unreviewed counts separately; do not equate registration with completion.

### E02 — Landing pages and scoped satellite alignment

[Open all 16 E02 records](E02_LANDING_PAGES_AND_SATELLITES_REGISTER.md).

The seed is 11 landing candidates, four scoped satellite roots (hub plus Maresia/Acesso/Costa), and the production apps hub. Classify landing purpose before proposing public copy. Establish E01 dependencies, align promise/CTA/eligibility, preserve geographic/language/data boundaries, and obtain actual property/commercial approval or record a hold.

Independent E02 evidence gathering may proceed, but a landing dependent on unresolved E01 copy/identity cannot be signed off. Exit gate: every record has public/internal disposition, named owner/reviewer, dependency approval or documented exception, sourced promise/CTA contract, evidence dates, limitation language and next action. Missing release evidence stays missing; out-of-scope network apps remain untouched. No satellite repository write is included.

## 6. Cross-batch knowledge-management blockers

| ID | Blocker | Required editorial disposition |
| --- | --- | --- |
| KM-01 | Older canonical checkpoint still says report pending, although the correction report exists on the inspected owned branch. | Preserve the old document; reference this discrepancy in the new checkpoint. Do not resume repairs or claim the old final handoff is freshly verified. |
| KM-02 | Conflicting consolidation/publication histories and reciprocal captação winner proposals. | Establish one human-owned source of truth and content-retention rationale before any future technical proposal. |
| KM-03 | Hub release report is referenced but absent from the inspected tree. | Request an approved document/location; record unavailable evidence without inventing a release receipt. |
| KM-04 | Blanket internal/index-follow conventions conflict with page-level public-intelligence boundaries. | Classify actual audience/purpose; preserve existing technical directives. |
| KM-05 | Fork-publication and network-specific scope statements are inherited contexts. | Record this task's actual five-owned-repository/non-deploying boundary; do not follow upstream links or expand scope. |

### Parked technical history — not E01/E02 work

Supermemory already contains `praia-digital-canonical-batches-2026-11-15` under `praia_digital`, with 19 extracted memories at the initial review. It records canonical repairs at `cca728971b18ca6eb0b056733be36d26a65817ca` and report pending. The [correction report][S08] now exists at inspected reporting head `d9bbc50986bda602919c7a2c0b3847d73c18be7d`, blob `f2a92c35d2c25ddaf978d49865372192157d5cf3`. Do not repeat either repair or overwrite that checkpoint.

The historical report parks 338 URL-normalization candidates (115 directory-index, 223 encoding), offset 0, first `academy/cursos/flipping-completo/index.html`, digest `2a251e164379241e52b9eca08e1a713be8095982ee068a18158676b109e722ea`; and 65 missing-canonical review candidates, offset 0, first `academy/cursos/airbnb-do-zero/vendas.html`, digest `1221125da7f59ebef7fed397d701a2bd392a079f501c97184a8dcbcf33eebf1e`. Source preflight: `a64f3c725282a866d6652aa70c91d7a1ab7336b2`.

These counts/digests are historical, not regenerated or freshly validated. They authorize no new target, repair, crawl or script execution. Preserve operational/noindex material, backups, templates, fixtures and genuine aliases. No automatic queue reconstruction or promotion into the editorial registers.

## 7. Checkpoint and resumption contract

New Supermemory namespace/document: `praia_digital` / `praia-digital-editorial-url-governance-2026-11-16`. This is separate from the older technical checkpoint. The versioned Markdown package is the decision registry; Supermemory is its compact resume index.

After the confirmed three-file commit, independently read the commit, diff and all three files via API. Confirm exactly these Markdown additions, parentage from main, unchanged protected branch heads and non-deploying settings. Save the new checkpoint only after that verification, including immutable file links, commit and blob hashes, source snapshots, batch counts/states, blockers, parked offsets, last action and resume cursor. Retrieve the new document; distinguish successful document ingestion from completed learned-memory extraction. Preserve and read back the older checkpoint without writing to it.

Initial substantive cursor: **E01-001**. Next action: assign the editorial lead and qualified finance reviewer, then resolve financing guide/variant identity and the evidence/copy brief in Markdown. Both batches remain NOT_STARTED with zero editorial approvals. No further public copy or technical action is implied.

At a later pause or batch boundary, record completed record IDs, actual reviewer/date/decision, remaining blockers and first unreviewed ID. Re-read branch/commit on resume, reconcile concurrent changes, and never repeat commits or overwrite other work blindly. A document cannot embed its own containing commit SHA without changing it; the verified immutable receipt belongs in Supermemory and the user-facing completion message.

## Source manifest

All links below point to reviewed Markdown in the five owned repositories, never upstream.

| ID | Reviewed source |
| --- | --- |
| S01 | [Hub README][S01] |
| S02 | [Direct Pages network policy][S02] |
| S03 | [Satellite architecture][S03] |
| S04 | [Maresia README][S04] |
| S05 | [Acesso README][S05] |
| S06 | [Costa README][S06] |
| S07 | [SEO audit/fix report, historical evidence only][S07] |
| S08 | [Canonical correction report, historical evidence only][S08] |
| S09 | [Inherited Praia Digital README][S09] |
| S10 | [Coastal topic opportunities report][S10] |
| S11 | [Editorial governance summary][S11] |
| S12 | [Inherited review checklist][S12] |
| S13 | [Duplicate consolidation proposal][S13] |
| S14 | [Pre-consolidation audit][S14] |
| S15 | [Content-governance principles][S15] |
| S16 | [Historical URL reconciliation][S16] |
| S17 | [Historical portal reconciliation][S17] |
| S18 | [Withdrawn-content audit][S18] |
| S19 | [Public intelligence editorial operation][S19] |
| S20 | [Content-gap and audience map][S20] |
| S21 | [Historical publication-gate report][S21] |
| S22 | [Riviera seasonal-rental Markdown draft][S22] |
| S23 | [Seasonal-yield Markdown draft][S23] |
| S24 | [Capitania Markdown draft][S24] |
| S25 | [Buying-safely Markdown draft][S25] |
| S26 | [Foreign-buyer documentation Markdown draft][S26] |
| S27 | [Financing Markdown draft][S27] |
| S28 | [First-home Markdown draft][S28] |

## Decision log

- 2026-11-16: AI-assisted focused review and two-batch seed package prepared. User explicitly confirmed this three-file documentation publication and the new checkpoint. Human substantive page-copy/factual approvals remain unrecorded; all named reviewers unassigned. No technical rollout is authorized.

[S01]: https://github.com/saipradikmallakuntla-tech/praia-digital-satellite-hub/blob/0cd9842627f0de5328af2dd82a4d02a227b3f5b2/README.md
[S02]: https://github.com/saipradikmallakuntla-tech/praia-digital-satellite-hub/blob/0cd9842627f0de5328af2dd82a4d02a227b3f5b2/NETWORK.md
[S03]: https://github.com/saipradikmallakuntla-tech/praia-digital-satellite-hub/blob/0cd9842627f0de5328af2dd82a4d02a227b3f5b2/SATELLITE_NETWORK_ARCHITECTURE.md
[S04]: https://github.com/saipradikmallakuntla-tech/maresia-em-dia/blob/ad87fb55fc7f2b820e2e18fef4756a53b5daba84/README.md
[S05]: https://github.com/saipradikmallakuntla-tech/acesso-a-praia/blob/2e9785a3e9c4e6244268f2fa40ca49f91fa99434/README.md
[S06]: https://github.com/saipradikmallakuntla-tech/costa-em-contexto/blob/78d9a6da054bae133a1078a6b643697a8316be45/README.md
[S07]: https://github.com/saipradikmallakuntla-tech/praia-digital-seo-audit/blob/d9bbc50986bda602919c7a2c0b3847d73c18be7d/SEO_AUDIT_AND_FIX_REPORT.md
[S08]: https://github.com/saipradikmallakuntla-tech/praia-digital-seo-audit/blob/d9bbc50986bda602919c7a2c0b3847d73c18be7d/CANONICAL_BATCH_CORRECTION_REPORT.md
[S09]: https://github.com/saipradikmallakuntla-tech/praia-digital-seo-audit/blob/44dac228e94d748a950acfd09937ace2100f3a07/README.md
[S10]: https://github.com/saipradikmallakuntla-tech/praia-digital-seo-audit/blob/44dac228e94d748a950acfd09937ace2100f3a07/relatorio-pautas-litoral-2026.md
[S11]: https://github.com/saipradikmallakuntla-tech/praia-digital-seo-audit/blob/44dac228e94d748a950acfd09937ace2100f3a07/docs/editorial/GOVERNANCA_EDITORIAL.md
[S12]: https://github.com/saipradikmallakuntla-tech/praia-digital-seo-audit/blob/44dac228e94d748a950acfd09937ace2100f3a07/docs/editorial/CHECKLIST_REVISAO.md
[S13]: https://github.com/saipradikmallakuntla-tech/praia-digital-seo-audit/blob/44dac228e94d748a950acfd09937ace2100f3a07/docs/editorial/CONSOLIDACAO_DUPLICATAS.md
[S14]: https://github.com/saipradikmallakuntla-tech/praia-digital-seo-audit/blob/44dac228e94d748a950acfd09937ace2100f3a07/docs/editorial/AUDITORIA_PRE_CONSOLIDACAO.md
[S15]: https://github.com/saipradikmallakuntla-tech/praia-digital-seo-audit/blob/44dac228e94d748a950acfd09937ace2100f3a07/docs/ai/hermes-agents-content-governance.md
[S16]: https://github.com/saipradikmallakuntla-tech/praia-digital-seo-audit/blob/44dac228e94d748a950acfd09937ace2100f3a07/docs/seo/url_reconciliation_final_2026-08-16.md
[S17]: https://github.com/saipradikmallakuntla-tech/praia-digital-seo-audit/blob/44dac228e94d748a950acfd09937ace2100f3a07/docs/seo/final_portal_reconciliation_2026-08-16.md
[S18]: https://github.com/saipradikmallakuntla-tech/praia-digital-seo-audit/blob/44dac228e94d748a950acfd09937ace2100f3a07/docs/editorial/auditoria-conteudos-retirados-2026-08-20.md
[S19]: https://github.com/saipradikmallakuntla-tech/praia-digital-seo-audit/blob/44dac228e94d748a950acfd09937ace2100f3a07/docs/inteligencia/OPERACAO-EDITORIAL.md
[S20]: https://github.com/saipradikmallakuntla-tech/praia-digital-seo-audit/blob/44dac228e94d748a950acfd09937ace2100f3a07/docs/content/lacunas-conteudo-pautas-leads-2026.md
[S21]: https://github.com/saipradikmallakuntla-tech/praia-digital-seo-audit/blob/44dac228e94d748a950acfd09937ace2100f3a07/docs/seo/relatorio-publication-gate-E.1.8-2026-08-18.md
[S22]: https://github.com/saipradikmallakuntla-tech/praia-digital-seo-audit/blob/44dac228e94d748a950acfd09937ace2100f3a07/content/posts/airbnb-riviera-sao-lourenco-2026.md
[S23]: https://github.com/saipradikmallakuntla-tech/praia-digital-seo-audit/blob/44dac228e94d748a950acfd09937ace2100f3a07/content/posts/alta-temporada-2026-2027-yield-aluguel-litoral.md
[S24]: https://github.com/saipradikmallakuntla-tech/praia-digital-seo-audit/blob/44dac228e94d748a950acfd09937ace2100f3a07/content/posts/capitania-portos-sp-guia-pratico-2026.md
[S25]: https://github.com/saipradikmallakuntla-tech/praia-digital-seo-audit/blob/44dac228e94d748a950acfd09937ace2100f3a07/content/posts/comprar-imovel-com-seguranca-litoral-2026.md
[S26]: https://github.com/saipradikmallakuntla-tech/praia-digital-seo-audit/blob/44dac228e94d748a950acfd09937ace2100f3a07/content/posts/documentacao-marinha-estrangeiros-italianos-argentinos-2026.md
[S27]: https://github.com/saipradikmallakuntla-tech/praia-digital-seo-audit/blob/44dac228e94d748a950acfd09937ace2100f3a07/content/posts/financiamento-imobiliario-litoral-2026.md
[S28]: https://github.com/saipradikmallakuntla-tech/praia-digital-seo-audit/blob/44dac228e94d748a950acfd09937ace2100f3a07/content/posts/primeiro-imovel-litoral-sp-2026.md
