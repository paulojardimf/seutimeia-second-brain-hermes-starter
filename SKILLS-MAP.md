# Skills Map — starter kit

## Lógica do mapa
As skills aqui não existem para enfeitar o repositório. Elas existem para orientar:
- como ligar contexto
- como rodar o dia
- como salvar contexto durável
- como revisar estrutura
- como transformar conversa em memória útil

## Skills-base do kit
| Skill | Papel | Quando usar | Status inicial |
|---|---|---|---|
| `seutimeia-second-brain-onboard` | onboarding guiado da base clonada | primeiro passo depois do clone | prioritária |
| `cerebro` | boot de contexto com leitura do repositório + fontes canônicas | início de sessão | recomendada |
| `rotina` | cockpit diário curto | começo do dia / priorização | opcional |
| `salve` | flush de fim de sessão | fechamento de trabalho relevante | recomendada |
| `higiene-semanal` | revisão estrutural | manutenção semanal | recomendada |
| `varredura-de-sessoes` | consolidado executivo das sessões | diário ou semanal | opcional |

## Ordem recomendada
1. instalar `seutimeia-second-brain-onboard`
2. rodar o onboarding inicial
3. decidir se `cerebro`, `rotina` e `salve` entram no fluxo vivo
4. ativar `higiene-semanal` quando a base já tiver corpo suficiente
5. ativar `varredura-de-sessoes` quando houver volume real de uso

## Como instalar a skill principal
```bash
bash scripts/install-onboard-skill.sh
```

Depois, na nova sessão do Hermes:
- `/reload-skills`
- `/skill seutimeia-second-brain-onboard`
- `vamos iniciar meu second brain`

## Skills que normalmente serão adaptadas depois
- proposta comercial
- contratos / jurídico documental
- operação por ferramenta específica (Linear, Notion, Gmail, Sentry, Langfuse, N8N)
- skill de cliente ou projeto específico
- consolidado de operação ou gestão

## O que veio da referência operacional e foi generalizado
- separação entre contexto durável e backlog operacional
- uso de GitHub como memória versionada
- uso de README por pasta relevante
- distinção entre skills, rotinas, playbooks, ferramentas e projetos
- flush de sessão e higiene recorrente
- consolidado por sessões em vez de dump bruto de conversa

## O que deliberadamente NÃO foi copiado
- dados pessoais privados
- projetos confidenciais
- clientes reais
- canais reais
- automações privadas
- rotinas sensíveis
- segredos e credenciais
