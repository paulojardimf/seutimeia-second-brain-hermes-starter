# Projetos (`projects/`)

## Propósito
Esta pasta concentra a **inteligência dos projetos**: contexto, direção, dependências, riscos, repositórios, documentos e decisões relevantes.

A regra continua a mesma:
- **GitHub / second brain** guarda contexto durável e mapa executivo.
- **Linear / ClickUp / Notion / Jira** guardam execução, prazo, owner e checklist operacional.

## Como ler
1. Abra este `README.md` para ver a estrutura do portfólio.
2. Entre em `active/`, `backlog/` ou `roadmaps/`.
3. Dentro de cada projeto ativo, use o `README.md` da pasta como mapa do projeto.
4. Quando existir subpasta `repositorios/`, ela serve para espelhos de contexto técnico (`AGENTS.md`, `CLAUDE.md`, `CHANGELOG.md`, arquitetura, integrações, decisões de stack).

## Estrutura recomendada
| Caminho | Papel | Status esperado |
|---|---|---|
| `project-state.md` | visão macro do portfólio, stack e governança | obrigatório |
| `active/` | projetos e frentes já em execução ou prioritários | recomendado |
| `backlog/` | projetos mapeados, mas ainda sem tração suficiente | opcional |
| `roadmaps/` | iniciativas estruturantes de médio/longo prazo | opcional |

## Exemplos de projetos que costumam existir
| Tipo | Exemplo | O que documentar aqui |
|---|---|---|
| implantação em cliente | operação de agentes para escritório/empresa | contexto, stack, integrações, riscos, fontes canônicas |
| operação interna | segundo cérebro da operação | estrutura, governança, automações, limites |
| frente comercial | nova oferta, workshop, mentoria, onboarding | tese, materiais, ativo canônico, handoff |
| produto interno | CRM, copiloto, RAG, monitoramento | decisões técnicas, escopo, dependências |

## Regras
- não criar checklist operacional aqui se isso já está na ferramenta de execução
- cada projeto documentado precisa dizer: **o que é, por que importa, estado, riscos e links canônicos**
- projeto ativo deve privilegiar pasta própria com `README.md`
- se um projeto perder prioridade real, mover para `backlog/` ou `historico/`
- se houver mais de um repositório, documentar a fronteira entre eles
