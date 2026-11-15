# Canonical Batch Correction Report

Date: 2026-11-15 UTC.

## Scope and immutable starting point

- Repository: `saipradikmallakuntla-tech/praia-digital-seo-audit` only.
- Branch: `seo-improvements`.
- Starting commit: `a64f3c725282a866d6652aa70c91d7a1ab7336b2`.
- Inherited `main` remains `44dac228e94d748a950acfd09937ace2100f3a07`.
- No upstream or third-party repository was read or modified during execution. No PR, merge, deployment or workflow dispatch was performed.

## Atomic repair commits

| Batch | Scope | Files | Canonical elements before / after | Commit |
| --- | --- | ---: | ---: | --- |
| B001 | `assets/ferramentas/` | 4 | 8 / 4 | [c6a2c6d9aa6768e32cfb4b55a51874e70642ba92](https://github.com/saipradikmallakuntla-tech/praia-digital-seo-audit/commit/c6a2c6d9aa6768e32cfb4b55a51874e70642ba92) |
| B002 | `assets/simples/` | 4 | 8 / 4 | [cca728971b18ca6eb0b056733be36d26a65817ca](https://github.com/saipradikmallakuntla-tech/praia-digital-seo-audit/commit/cca728971b18ca6eb0b056733be36d26a65817ca) |

B001 parent is the starting commit; B002 parent is B001. Each commit changes exactly its four approved HTML files. Eight separate blobs were uploaded and their returned Git hashes matched the prepared hashes. Leaf, assets and root trees were verified without sending the entire repository as a payload. Branch references were rechecked and updated with `force=false`.

Exactly eight canonical elements were removed: one stale/conflicting root-level URL and seven identical repeats. The retained canonical in every file is `https://praia.digital/` followed by that file's exact repository path. No body, script, style, meta tag, title or H1 bytes were changed. Source sizes were 31,287 bytes for B001 and 31,453 bytes for B002; the largest individual encoded upload was under 12 KB.

## Exact file hashes

| Batch | Repository path | Original Git blob SHA | Corrected Git blob SHA |
| --- | --- | --- | --- |
| B001 | `assets/ferramentas/captura-manual-leads-imobiliarias-2026.html` | `f669424562254eafb6ac3689db53027d67f14a34` | `84194e8d8f005e1378b141905870c01ed777aade` |
| B001 | `assets/ferramentas/checklist-automatizacao-corretores-litoral-2026.html` | `bb82f5cb5c0c0b75eb52942fb1f6bf0cc4e102e6` | `56e3db39178f91bc2e54aaeb4ca05d9c7ebf6967` |
| B001 | `assets/ferramentas/recomendacao-automatica-imoveis-litoral-2026.html` | `ef6240ddb98a7419af8215f37cd30517498a6cf1` | `8c669a5568dcd508fe5c9d13828eb17b65cb0aef` |
| B001 | `assets/ferramentas/simulador-roi-parcerias-imobiliarias-2026.html` | `8d77820b1f93d12940d44c424871d5425f8a78d9` | `140245efe837921a3b4bd072527b155eaf3135f5` |
| B002 | `assets/simples/checklist-captacao-leads-litoral-30dias.html` | `fa425d12b34eb10b049fa0624004ce1bfce4f8fb` | `8af66f656da1c5987ecdd5bbd36d72317c1386e6` |
| B002 | `assets/simples/modelo-receita-ia-imobiliaria-sem-taxa.html` | `461c4bad446b50ee25e0febbbd58ebc7f9ea73cb` | `78f8f55a992d8084a98e7e0723780ae71bc1122a` |
| B002 | `assets/simples/proposta-comercial-padrao-imobiliaria.html` | `85e7ca45ec34a860c078ab452c86fc43f8bd18db` | `554bcae0f2b0daed57f6ba0269e49af7691369ed` |
| B002 | `assets/simples/recomendacoes-ia-imobiliaria-litoral-30dias.html` | `20e82d1dbcb71bcfe5a3a57dba703a492f7c2029` | `2f846204661711b09640c5f32e5a92bd84842a96` |

Corrected UTF-8 file SHA-256 digests, in the same row order:

1. `191b7191286a6c0b8ae71b4fd6c6d372637e333ab76c2ee870ff84b3cc056887`
2. `7b4882483fef8b56d860aaeb4c3551b0a8191d5e7b4af542fd0400696361323e`
3. `add5ff9b278a5918064b46e3a75190d09a476e5784662ba5f4d10a34c0ca4d19`
4. `e4efb0bb53ec5e5573eabdf86185e148f66faeec40db1287d30147ac93dff9ff`
5. `e7b211c373e2f0012b897e53e415a9b71358c50044188b4eddee479ebeb4eae7`
6. `fd2512fcf6536e69400dea5c4c948b94d596bdbf26c143b506c9d7d855f33888`
7. `97f421d0e44901eeea7d29a65eec181d879091fa93f1e9b3edf631f488d67fe0`
8. `d589902c0a2e656b384372fcfcd93424466ffc981e1cdd34f8c5cfe7aa5d1ee0`

## Fresh canonical / meta / H1 verification

The check used eight independent GitHub blob GET responses after creation of the repair commits, not the local prepared payloads. The branch was then read back at B002.

- 8/8 returned Git blob hashes and SHA-256 digests matched the prepared manifest.
- 8/8 pages have exactly one canonical element, inside `<head>`, at the exact expected HTTPS URL.
- Remaining duplicate canonical pages across these eight files: **0**.
- Remaining stale/conflicting canonical pages across these eight files: **0**.
- 8/8 pages have exactly one nonempty `<h1>`.
- 8/8 meta sequences, titles, H1 values and all noncanonical bytes exactly match their original source.
- 8/8 canonical-only transformations are byte-idempotent.

### Preserved metadata warnings

This is not a full metadata-clean release. All eight pages already repeat social/robots/viewport metadata. Six also repeat their meta description and keywords: the B001 checklist and recommendation pages plus all four B002 pages. Those existing tags were intentionally preserved to honor canonical-only scope. The capture-manual and ROI pages each have one nonempty meta description; the other six have two. Metadata cleanup requires a separately approved batch.

## Deferred audit summary and next cursor

The preflight inspected 13,000 fork HTML files and four satellite homepages. The four satellite canonicals were correct and their repositories were not modified. No legacy GitHub-host canonical URLs remained. All 6,533 sitemap target files existed and had one self-canonical; preferred URL formatting is a separate matter. These observations are source-snapshot checks, not new HTTP or browser checks of praia.digital.

The following queues are deferred, unmodified and require a new approved plan:

1. **338 public-page URL normalizations**, offset **0**: 115 directory-index route normalizations and 223 percent-encoding normalizations. First sorted path: `academy/cursos/flipping-completo/index.html`. Queue SHA-256: `2a251e164379241e52b9eca08e1a713be8095982ee068a18158676b109e722ea`.
2. **65 missing-canonical candidates**, offset **0**, requiring indexation/redirect review before adding any tag. First sorted path: `academy/cursos/airbnb-do-zero/vendas.html`. Queue SHA-256: `1221125da7f59ebef7fed397d701a2bd392a079f501c97184a8dcbcf33eebf1e`.

Queue digests use the preflight candidate records sorted by path, encoded as UTF-8 JSON with sorted keys, no ASCII escaping and compact separators. Records contain path, reason, public_candidate, expected, before, blob_sha and bytes. The canonical policy source is `scripts/seo_audit.py` at blob `b36489b5511fe51863ec2aacc19619d87bff2f11`; the immutable preflight source is the starting commit above. Public candidates exclude internal paths, existing robots noindex pages and partial/template paths. Preserve genuine local aliases; do not run a blanket self-canonical replacement or the broad metadata generator as part of this eight-file task. Backups, operational/noindex material, templates and adversarial fixtures are not automatically repair targets.

## Non-deploying safeguards and resumable handoff

Before writing and again after both repairs, Actions returned `enabled: false`; GitHub Pages returned 404/unconfigured. The unchanged deployment workflow guard requires both the upstream repository name and `refs/heads/main`, which this audit fork cannot satisfy. No deployment settings, workflows, CNAME, DNS or main-branch references were changed.

Supermemory namespace: `praia_digital`. Checkpoint document: `praia-digital-canonical-batches-2026-11-15`. A precommit checkpoint was saved and independently read back before branch writes; the B001 continuation was also saved and read back. The final handoff records both repair SHAs, the documentation commit containing this file, old/new Git blob and SHA-256 hashes, verification results, safety checks and the deferred cursors. A report cannot embed its own containing commit SHA without changing that SHA; that value is therefore recorded in the final checkpoint and the user-facing receipt.

This report is committed separately from the two canonical-only commits. No fresh browser, live-site, ranking, complete metadata cleanup or full-repository zero-defect claim is made.
