# Mapa de Ferramentas (`ferramentas/`)

## Propósito
Documentar a superfície operacional de ferramentas, integrações e CLIs que sustentam a execução do Hermes e do segundo cérebro.

A regra é simples: **cada ferramenta relevante vive na própria pasta**. Isso evita playbook solto, dá espaço para materiais auxiliares e melhora a navegação quando a base crescer.

## Índice por ferramenta
| Ferramenta | Pasta | Papel | Status esperado |
|---|---|---|---|
| Hermes | `hermes/` | agente principal, skills, crons, gateway e memória | ativo |
| GitHub | `github/` | repositório canônico e publicação | ativo |
| Linear | `linear/` | backlog, projetos, issues e follow-up | opcional |
| Discord | `discord/` | cockpit operacional com threads/canais | opcional |
| Telegram | `telegram/` | acompanhamento pessoal e rotinas diretas | opcional |
| Slack | `slack/` | operação em times que já vivem no Slack | opcional |
| Notion | `notion/` | documentação, proposta, bases de dados | opcional |
| Google Workspace | `google-workspace/` | Gmail, Calendar, Drive, Docs, Sheets | opcional |
| N8N | `n8n/` | webhooks, transporte e integrações | opcional |
| Sentry | `sentry/` | observabilidade de erros | opcional |
| Langfuse | `langfuse/` | tracing e monitoramento de agentes/LLMs | opcional |
| MCP | `mcp/` | camada de tools padronizadas | opcional |
| Workers de código e leitura | `workers-de-codigo-e-leitura/` | leitura pesada e execução delegada | opcional |

## Regra operacional
Ferramenta entra aqui só quando houver:
- acesso real verificado
- função operacional clara
- risco explícito
- identidade (usuário x agente x time) definida

## Regra de modelagem
1. arquivo principal de cada ferramenta fica no padrão `README.md` dentro da pasta da ferramenta
2. documentos auxiliares ficam na mesma pasta da ferramenta
3. se uma ferramenta ganhar material novo, ele deve nascer já vinculado ao README local
4. nada de espalhar playbook solto na raiz de `ferramentas/`
