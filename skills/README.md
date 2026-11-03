# Mapa de Skills (`skills/`)

## Propósito
Esta pasta guarda as skills operacionais do starter kit, a skill instalável de onboarding e futuras adaptações do ambiente.

Skills aqui não são decoração. Elas existem para codificar:
- como o contexto é lido
- como o dia é priorizado
- como a sessão é salva
- como a estrutura é higienizada
- como o onboarding acontece sem improviso

## Conteúdo atual
| Skill / grupo | Caminho | Papel |
|---|---|---|
| onboarding | `installable/seutimeia-second-brain-onboard/` | conduzir a construção do segundo cérebro pelo Discord |
| captura | `installable/segundo-cerebro-captura/` | gravar decisões, fatos, aprendizados, erros e lições do dia |
| revisão | `installable/segundo-cerebro-revisao/` | revisões semanal, quinzenal e mensal |
| `cerebro` | `starter/cerebro/` | ligar contexto e produzir briefing curto |
| `rotina` | `starter/rotina/` | cockpit diário curto |
| `salve` | `starter/salve/` | gravar o que importa ao fim de uma sessão |
| `higiene-semanal` | `starter/higiene-semanal/` | revisão estrutural semanal |
| `varredura-de-sessoes` | `starter/varredura-de-sessoes/` | consolidado executivo de sessões |

## Instalação
O Hermes roda, a partir da raiz do repositório:
```bash
bash scripts/install-onboard-skill.sh
```
O script copia todas as skills de `installable/` para a pasta de skills do Hermes (`$HERMES_HOME/skills`, por padrão `~/.hermes/skills`). Depois, no Hermes: `/reload-skills` e `/skill seutimeia-second-brain-onboard`.

## Skills autorais da operação
Todas as skills que o Hermes criar nas interações com o time, e que não vêm prontas com o Hermes nem com este método, ficam em [`autorais/`](./autorais/README.md), versionadas no repositório da empresa.

## Regra de modelagem
Skill boa tem, no mínimo:
- objetivo
- trigger / quando usar
- entradas
- processo
- saída esperada
- regra crítica ou anti-padrões

Se não houver isso, provavelmente ainda é só nota ou playbook frouxo.
