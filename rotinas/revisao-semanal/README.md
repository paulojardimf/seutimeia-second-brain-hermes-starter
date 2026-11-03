# Rotina semanal — revisão da semana

## Status
Não configurada por padrão.

## Objetivo
Olhar os últimos 7 dias do diário e da memória: o que andou, o que travou, decisões sem dono, erros que apareceram.

## Agenda padrão
| Campo | Valor |
|---|---|
| Expressão cron | `0 17 * * 5` (sexta, fim do expediente) |
| Destino | canal `revisoes` |
| Skill | `segundo-cerebro-revisao` (modo semanal) |

## Prompt do job
```text
Carregue a skill segundo-cerebro-revisao e faça a revisão semanal da janela dos últimos 7 dias. Confira a cobertura do diário, agrupe os registros de memoria/, aponte pendências sem dono, erros e decisões sem execução, grave em diario/revisoes/ e envie o resumo ao canal revisoes com as perguntas que o time precisa responder.
```
