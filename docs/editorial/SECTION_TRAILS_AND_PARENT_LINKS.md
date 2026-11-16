# Section Trails & Parent-Link Conventions

Version 1.0 · 2026-11-16 UTC · **Editorial specification only; no visible trail, heading, URL or code changed.**

[IA and navigation standards](IA_AND_NAVIGATION_STANDARDS.md) · [Decision register](NAVIGATION_DECISION_REGISTER.md) · [Editorial checklist](CHECKLIST_REVISAO.md)

## 1. Separate the reader-facing roles

A global menu helps readers move across a site. A breadcrumb describes a real editorial hierarchy. A parent-return link offers a useful route back. A heading identifies the current page. Related links offer another task or topic. A decorative kicker may repeat an identity without doing any of those jobs.

Do not treat these roles as interchangeable. Repeated wording is not sufficient evidence for removal, and a link hidden in a closed mobile menu is not necessarily an equivalent parent-return route. This document specifies writing and documentation conventions, not DOM order, styling, ARIA, structured data or responsive behavior.

## 2. Four-family writing matrix

The following are proposed patterns, not claims that every existing page already has these trails. Angle-bracket labels are editorial placeholders, not URLs to create.

| Family | Section landing trail | Child-page trail | Parent-return wording and verified destination |
| --- | --- | --- | --- |
| imoveis | Início → Imóveis | Início → Imóveis → <page title> | Voltar para Imóveis → [imoveis.html](https://praia.digital/imoveis.html) |
| ferramentas | Início → Ferramentas | Início → Ferramentas → <tool title> | Voltar para Ferramentas → [ferramentas/index.html](https://praia.digital/ferramentas/index.html) |
| bairros | Início → Bairros | Início → Bairros → <city, when evidenced> → <neighbourhood> | Voltar para Bairros → [bairros/index.html](https://praia.digital/bairros/index.html); a verified city grouping may be a more precise immediate return |
| blog | Início → Blog | Início → Blog → <article title> | Voltar para o Blog → [blog/index.html](https://praia.digital/blog/index.html) |

**Início** means [the production home](https://praia.digital/) only for production-family content. On a section landing page, the section is current and the parent is Início; do not add a self-return link. The different article in “Voltar para o Blog” is natural Portuguese, not a second section identity.

An ancestor is linked only when its destination or anchor has been verified for that editorial record. The current-page label stays plain text. Existing `.html` and `index.html` spellings are retained in this specification; an alternative directory spelling requires its own evidence and decision.

## 3. Choose the primary parent deliberately

1. Record the page's primary reader task and current identity.
2. Choose one parent from the controlled taxonomy; record why it is the best reader-facing parent.
3. Preserve the exact established page identity and distinguish proposed wording from an href change.
4. Record related topics, municipalities, audiences and tools separately from the main trail.
5. If the actual parent or destination is unknown, mark NEEDS_EVIDENCE. Do not infer a new route from folder structure or a similar filename.

A Blog article comparing neighbourhoods normally has Blog as its primary parent and Bairros as a related destination. An app at the production `/apps/` hub does not automatically belong beneath the three-calculator Ferramentas landing page. Document the genuine relationship rather than manufacturing a uniform path.

For Imóveis, preserve listing/filter context and avoid promising that every named city has current stock. For Ferramentas, preserve simulation assumptions, dates and non-guarantee language. A guide and a calculator can share a topic without becoming the same page.

## 4. Preserve geographic meaning in Bairros

Keep the municipality needed to identify a neighbourhood, especially when names repeat across cities. A city can appear in the visible wording without being a link. Link a city intermediary only after the actual city page or existing directory anchor has been evidenced; otherwise use a shorter verified trail and retain the city in the heading/context.

A return such as “Bairros de <Cidade>” is a candidate only when its destination is established. Do not invent `bairros/<cidade>/`, guess fragment IDs, remove city-group anchors or convert an index into an official list of distinct neighbourhoods. Preserve alternative-name and unconfirmed-reference caveats.

The separate E01-008/E01-009 city/directory URL questions remain pending in the earlier URL-governance register. This writing specification does not settle canonicals, aliases or redirects.

## 5. Independent satellite navigation is not a fabricated breadcrumb

Use the exact owned roots:

- [Aplicativos do Litoral / Central de apps](https://saipradikmallakuntla-tech.github.io/praia-digital-satellite-hub/).
- [Maresia em Dia](https://saipradikmallakuntla-tech.github.io/maresia-em-dia/).
- [Acesso à Praia](https://saipradikmallakuntla-tech.github.io/acesso-a-praia/).
- [Costa em Contexto](https://saipradikmallakuntla-tech.github.io/costa-em-contexto/).

“Central de apps” is the proposed consistent network-return label in documentation. Links between these properties switch independent apps; do not present the production Praia Digital site as their hierarchical parent or suggest shared login, saved records, data APIs or institutional affiliation. The hub itself does not need a return link to itself.

Preserve the full app names. Functional descriptors such as “Manutenção” and “Contexto regional” may be documented as role-specific aliases, not ambiguous replacements for product identity. The broader network has six utilities/seven sites; this pass does not remove or review the three additional apps.

## 6. Keep, shorten or omit: evidence before editorial disposition

Reuse the earlier [five-part redundancy guide](https://github.com/saipradikmallakuntla-tech/praia-digital-seo-audit/blob/6cb8f058e2fd8c55a7db901ad86cacbbff5287ac/docs/ux/REDUNDANT_TRAIL_REMOVAL_GUIDELINES.md). A decorative line can be an omission candidate only when it has the same referent and purpose as retained content, contributes no unique context, leaves an understandable route/orientation, and has an actual recorded editorial review.

Use KEEP_CONTEXT, SHORTEN_CANDIDATE, REMOVE_CANDIDATE or NEEDS_EVIDENCE with a reason. These are writing dispositions, not instructions to remove a component. Missing evidence means keep the existing content pending review. No heading, accessible label, breadcrumb schema, filter state or limitation is removed by this package.

## 7. Safety, language and source dates

- Maresia remains a maintenance organizer with user-chosen intervals, browser-local records and an ICS snapshot—not inspection, professional advice or automatic synchronization.
- Acesso remains a dated documentary pilot. Unknown never means yes; source publication/reading dates do not confirm current operation, accessibility or bathing safety.
- Costa remains a regional source/scale guide. Preserve source year, scale and the distinction between susceptibility and parcel-level risk or safety certification.
- The hub is PT/EN; the three original apps remain PT. A language/filter query is not a new hierarchy or proof of a translated interface.
- Preserve source dates, geography and essential caveats near their claims. They are substantive content, not removable navigation clutter.

## 8. Manual editorial sign-off checklist

- [ ] Exact current wording, evidence date and destination recorded, or explicitly UNKNOWN.
- [ ] One primary parent and a documented reader-purpose rationale.
- [ ] Existing verified ancestors linked; current-page text unlinked; no guessed intermediate URL/anchor.
- [ ] Municipality, language, active-context and limitation information retained.
- [ ] Related links distinguished from hierarchy and from app switching.
- [ ] Any shortening/omission has specific evidence, retained wayfinding and a real reviewer/date.
- [ ] E01/E02/UXN dependencies and unresolved URL questions referenced without changing their states.
- [ ] Editorial approval separated from implementation and production authorization.

No checklist item is pre-checked. API file read-back confirms documentation publication only. No code, browser, accessibility or automated test suite is run or authorized here.
