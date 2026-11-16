# Redundant Trail Removal Guidelines

Version 1.0 · 2026-11-16 UTC · **Editorial decision guide only; no visible trail, page, schema or navigation code has been changed.**

[Header copy standards](MOBILE_HEADER_COPY_STANDARDS.md) · [Decision register](MOBILE_NAV_AND_TRAIL_COPY_REGISTER.md) · [Existing navigation contract](../navigation-standard.md)

## Purpose and limits

Reduce stacked labels that repeat an already clear destination or current-page title, while preserving the information a reader needs to know where they are and how to go back. A repeated word is not, by itself, evidence of redundant navigation.

This document governs proposed visible wording and content-priority decisions in the five named owned repositories only. It is not an instruction to delete a breadcrumb component, hide a block with CSS, change JavaScript, remove a heading, rewrite a URL, modify `BreadcrumbList`/JSON-LD, change ARIA, or alter a service worker. No code, suite, crawl, PR, merge or deployment is authorised by it.

The issue is reader-reported. Current page bodies, screenshots and rendered labels were not inspected in this exercise. The register therefore uses UNKNOWN for current visible copy unless the specific observation has been recorded. Examples below are hypothetical proposals, not measured before/after findings.

## 1. Distinguish the content roles

| Content role | Reader purpose | Default editorial treatment |
| --- | --- | --- |
| Global menu | Reach principal destinations across the site | Preserve its role and established taxonomy. A collapsed mobile menu may not provide the same immediate orientation as a visible parent link. |
| Property identity | Identify the site/app the reader is using | Keep one clear identity. Do not stack decorative repeats of the brand and region. |
| Page heading | Identify the current page/topic | Preserve a meaningful primary heading. Do not delete it because a trail also names the page. |
| Visible breadcrumb / parent-return link | Explain actual hierarchy or return to a useful parent | Keep meaningful hierarchy, geography and return paths. Consider shorter wording only with evidence. |
| Decorative kicker / repeated current-page label | Repeat an identity/category without adding context or a destination | Candidate for omission in a future authorised implementation, after the decision below. |
| Structured data / accessible labels / skip links | Serve machine interpretation or accessible operation | Outside this removal exercise. Visual repetition is not permission to remove or alter these. |
| Active filters, dates, limitations or source notes | Explain the current state and the limits of a claim | Preserve near the relevant content; not disposable trail decoration. |

## 2. Five-part redundancy decision

Record the answers and evidence under a stable UXN ID. Mark a visible line REMOVE_CANDIDATE only when all five answers are yes:

1. **Same referent:** does it repeat the same page/destination, not merely use a similar word?
2. **Same purpose:** does it repeat an existing identity or heading rather than express hierarchy, return navigation, geography or state?
3. **No unique context:** would omitting it lose no city/region, parent-child relationship, source limitation, language cue or disambiguation?
4. **Usable alternative:** does the remaining experience retain an appropriate, understandable route and orientation, including when the mobile menu is closed and without assuming JavaScript or an undocumented link exists?
5. **Recorded review:** is there specific current evidence and an actual editorial reviewer/date accepting the retained content and proposed omission?

If any answer is no, KEEP_CONTEXT or propose a narrower wording change. If evidence is missing, use NEEDS_EVIDENCE and keep the existing content pending review. The fact that a destination appears somewhere in the top menu is not sufficient to pass this decision.

These are editorial dispositions, not implementation statuses. REMOVE_CANDIDATE never means removed, approved for code changes, or safe for production.

## 3. Dispositions and required rationale

| Disposition | When to use | What the record must say |
| --- | --- | --- |
| KEEP_CONTEXT | The line adds hierarchy, geography, a unique return path or necessary explanation | Identify the exact information and destination being retained. |
| SHORTEN_CANDIDATE | The role is useful but its phrasing is unnecessarily long | Give proposed wording, unchanged intended destination, preserved meaning and unresolved evidence. |
| REMOVE_CANDIDATE | All five redundancy conditions are evidenced and reviewed | Identify the repeated role/referent and demonstrate the retained wayfinding; code implementation remains unauthorised. |
| NEEDS_EVIDENCE | Current wording, purpose, destination or alternative is not established | State the missing evidence and exact next review action. Do not infer removal. |
| OUT_OF_SCOPE | Internal/operational material, an unowned property or an unapproved extra app | Record the boundary without opening or changing the excluded material. |

## 4. Page-family guidance

### Property catalogue — `imoveis.html`

A hypothetical “Início > Imóveis” line and a heading “Imóveis” may repeat the current-page name. That does not prove the real page has this text or that its home link is unnecessary. Assess each role and the remaining route. Do not remove catalogue controls, active-filter context, listing counts or the page heading to reduce top-of-screen density. Do not claim current inventory from older Markdown.

### Seasonal ROI — `ferramentas/calculadora-roi-temporada.html`

A compact label such as “ROI de temporada” is a wording candidate. A meaningful parent label such as “Ferramentas” may still be useful even if a menu contains other investment destinations. Establish its actual destination; do not invent a `/ferramentas/` URL. Keep the explanation that results depend on assumptions and are not guaranteed returns. Do not conflate this route with the distinct app URL mentioned in the inherited README.

### City directory and city detail

“Cidades” can be a compact directory label, but a detail page may need a visible way back to the city directory. The city's own name belongs in its identity/heading, not in several decorative lines. Preserve geographic qualifiers needed for disambiguation. Preferred spelling of `cidades/index.html` versus a directory URL remains the separate E01-008 decision; do not normalise links here.

### Neighbourhood directory and detail

Retain the city that identifies a neighbourhood and any useful parent/return link. A global menu does not necessarily tell a reader which municipality contains a similarly named neighbourhood. A hypothetical parent phrase “Bairros de <Cidade>” may be more useful than stacked generic labels, but the placeholder must be replaced only after source review and the destination is established. Do not remove city-group anchors, article-return context or change their targets. The separate E01-009 URL decision remains pending.

### Independent hub and the three scoped apps

Do not make repeated site names into a new breadcrumb hierarchy between independent apps. A link that switches to another app has a different purpose from a current-page label. Keep an understandable network-switching route and each site's identity; only redundant decorative repeats are candidates for omission. Do not imply shared records, authentication, live data, ownership authority over `praia.digital`, or institutional affiliation.

Preserve dated documentary limitations and unknowns in Acesso, regional scale/non-certification language in Costa, and maintenance/ICS/local-record limitations in Maresia. They are substantive content, not optional clutter. Only the hub is documented as bilingual among these four properties.

## 5. Editorial wireframe, not an implementation

A useful writing brief describes this reading order in prose:

1. One recognisable property identity and a clearly named menu/action.
2. A parent/context line only when it provides meaningful information or navigation.
3. One clear page/topic heading.
4. A short useful introduction or essential limitation, then the page's primary task/content.

This is not a layout prescription. It does not set breakpoints, visibility, dimensions, DOM order, focus behaviour or heading markup. If a writing decision depends on those behaviours, record the dependency and hold it for a separately authorised design/engineering review.

## 6. Safeguards and review checklist

- Distinguish global navigation, a visible trail, the H1/topic and structured data in the record. Do not bundle their removal.
- Record exact current wording and destinations from actual evidence; otherwise write UNKNOWN.
- Compare the proposed omission/shortening with the closed-menu experience, long place names and the reader's return journey. No such browser or assistive-technology review was run here.
- Preserve source dates, disclaimers, language limits and independent-app boundaries.
- Confirm that a proposed wording change does not change the reader promise, remove necessary context or invent a route.
- Require an actual editorial reviewer/date before a disposition is signed off. Documentation publication is not substantive copy approval.
- Leave canonicals, redirects, indexing, sitemaps, URLs, breadcrumb schema, headings, accessible names, runtime files and `sw.js` unchanged.
- Do not reuse old test counts or unavailable release evidence as validation of this package.

## Source anchors and dependencies

- [Navigation roles and established groups](https://github.com/saipradikmallakuntla-tech/praia-digital-seo-audit/blob/44dac228e94d748a950acfd09937ace2100f3a07/docs/navigation-standard.md).
- [Neighbourhood review: preserved guide URLs, city/return context and scope limits](https://github.com/saipradikmallakuntla-tech/praia-digital-seo-audit/blob/44dac228e94d748a950acfd09937ace2100f3a07/docs/neighborhood-guide-review.md). Its historical test results are not fresh results for this specification.
- [Existing E01 register: city/neighbourhood URL decisions remain separate](https://github.com/saipradikmallakuntla-tech/praia-digital-seo-audit/blob/3dfa148cbcb862a70fbae1fba252e87e73b32a65/docs/editorial/E01_PUBLIC_GUIDES_AND_URLS_REGISTER.md).
- [Satellite network boundaries](https://github.com/saipradikmallakuntla-tech/praia-digital-satellite-hub/blob/0cd9842627f0de5328af2dd82a4d02a227b3f5b2/SATELLITE_NETWORK_ARCHITECTURE.md).

## Decision log

- 2026-11-16: AI-assisted editorial guidance published with the user's documentation-only confirmation. No visible trail has been removed, and no substantive human approval or technical rollout is recorded.
