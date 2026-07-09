# Rotinas Map — starter kit

## Lógica do mapa
As rotinas existem para manter o second brain:
- vivo
- coerente
- limpo
- alinhado à operação real

## Rotinas-base sugeridas
| Rotina | Frequência | Objetivo | Canal sugerido | Prioridade inicial |
|---|---|---|---|---|
| diário do brain | dias úteis | consolidar decisões, sinais e foco do dia | Discord ou Telegram | alta |
| revisão semanal/mensal | semanal | atualizar leitura executiva e padrões | Discord | alta |
| higiene semanal | semanal | revisar estrutura, README, mapas e lacunas | Discord | alta |
| sync de projetos/repositórios | semanal | alinhar brain com repositórios e projetos ativos | Discord | média |
| follow-up operacional | semanal | lembrar pendências, donos e handoffs | Discord, Slack ou Telegram | opcional |
| watchdog de infra | recorrente | alertar incidente operacional real | Discord ou Slack | opcional |

## Ordem de ativação recomendada
1. começar sem cron nenhum
2. validar a estrutura manualmente
3. ativar `salve` e o diário
4. ativar higiene semanal
5. ativar sync de projetos quando já existir mais de um repositório ou mais de um projeto vivo
6. só depois adicionar rotinas mais sofisticadas

## Regra estratégica
Rotina ruim automatiza bagunça.
Primeiro vem governança. Depois automação.

## Onde documentar cada rotina
- identidade e objetivo: `rotinas/<nome>/README.md`
- estado executivo: `rotinas/STATUS.md`
- destino/canal: `context/canais-e-destinos.md`
- skill relacionada: `skills/` quando a rotina depender de um método específico
