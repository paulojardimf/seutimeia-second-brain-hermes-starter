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
| onboarding instalável | `installable/seutimeia-second-brain-onboard/` | conduzir a implantação inicial do repo clonado |
| `cerebro` | `starter/cerebro/` | ligar contexto e produzir briefing curto |
| `rotina` | `starter/rotina/` | cockpit diário curto |
| `salve` | `starter/salve/` | flush de fim de sessão |
| `higiene-semanal` | `starter/higiene-semanal/` | revisão estrutural semanal |
| `varredura-de-sessoes` | `starter/varredura-de-sessoes/` | consolidado executivo de sessões |

## Skill instalável principal
A primeira skill que deve ser instalada é:
- `seutimeia-second-brain-onboard`

Origem no repositório:
- `skills/installable/seutimeia-second-brain-onboard/SKILL.md`

Instalação local:
```bash
bash scripts/install-onboard-skill.sh
```

Depois:
1. abra uma nova sessão no Hermes neste diretório
2. rode `/reload-skills` se necessário
3. carregue `/skill seutimeia-second-brain-onboard`
4. diga: `vamos iniciar meu second brain`

## Regra de modelagem
Skill boa tem, no mínimo:
- objetivo
- trigger / quando usar
- entradas
- processo
- saída esperada
- regra crítica ou anti-padrões

Se não houver isso, provavelmente ainda é só nota ou playbook frouxo.
