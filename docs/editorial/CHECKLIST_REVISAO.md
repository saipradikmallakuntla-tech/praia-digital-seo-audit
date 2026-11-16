# Checklist de Revisão — Artigos do Blog

## Obrigatório antes de publicar

### SEO
- [ ] Título SEO com palavra-chave principal e diferenciação
- [ ] Meta description ≤ 160 caracteres, com palavra-chave e CTA
- [ ] H1 único, contendo a palavra-chave principal
- [ ] H2/H3 hierárquicos, sem saltos
- [ ] URL canônica apontando para si mesma
- [ ] Slug limpo, sem acentos excessivos, hífens no lugar de espaços

### Conteúdo
- [ ] Introdução ≤ 3 parágrafos, com promessa clara
- [ ] Pelo menos 3 H2s com conteúdo original
- [ ] Conteúdo exclusivo (não duplicado internamente)
- [ ] FAQ com 2-4 perguntas relevantes
- [ ] CTA contextual para curso relacionado
- [ ] 3-5 links internos para artigos relacionados
- [ ] 1 link externo de autoridade (quando aplicável)

### Técnico
- [ ] Schema BlogPosting presente
- [ ] Schema FAQPage presente (se houver FAQ)
- [ ] BreadcrumbList presente
- [ ] Meta robots: index, follow
- [ ] Open Graph completo
- [ ] Twitter Card completa
- [ ] Imagem OG definida (1200x630px)
- [ ] Sem links quebrados
- [ ] Sem referências a variantes/URLs antigas

### Aprovação
- [ ] Revisão ortográfica e gramatical
- [ ] Validação de dados/fatos
- [ ] Aprovação do responsável editorial
- [ ] Registro no REGISTRO_EDITORIAL.json

## Complemento de arquitetura e navegação editorial

Referências: [IA & Navigation Standards](IA_AND_NAVIGATION_STANDARDS.md), [Section Trails & Parent Links](SECTION_TRAILS_AND_PARENT_LINKS.md) e [Navigation Decision Register](NAVIGATION_DECISION_REGISTER.md).

- [ ] Seção e pai editorial definidos pela finalidade do leitor, sem confundir tema, município e hierarquia.
- [ ] Rótulo, destino e evidência atual registrados; ausência de evidência marcada explicitamente.
- [ ] Ancestrais apontam para página/âncora verificada; página atual sem auto-link e nenhum intermediário inventado.
- [ ] Contexto municipal, idioma, datas e limites substantivos preservados.
- [ ] Links relacionados e troca de aplicativos independentes separados da trilha principal.
- [ ] Revisor, data, justificativa, dependências e próxima ação registrados no documento Markdown.
- [ ] Aprovação editorial distinguida de publicação documental e de autorização técnica.

Este complemento é documental. Os itens técnicos/JSON herdados acima não autorizam sua implementação ou alteração nesta passagem. Nenhum código, schema, canonical, redirect, sitemap, `sw.js`, registro JSON, suíte de testes, workflow ou deploy é alterado; nenhum item foi marcado como concluído por publicar o pacote.
