# Rotina mensal — revisão do mês

## Status
Não configurada por padrão.

## Objetivo
Dar uma leitura executiva do mês civil anterior: direção, resultados, riscos, o que mudar no contexto, nas rotinas e nas skills.

## Agenda padrão
| Campo | Valor |
|---|---|
| Expressão cron | `0 9 1 * *` (dia 1, manhã) |
| Destino | canal `revisoes` |
| Skill | `segundo-cerebro-revisao` (modo mensal) |

## Prompt do job
```text
Carregue a skill segundo-cerebro-revisao e faça a revisão mensal do mês civil anterior. Cruze diario/, memoria/ e projects/project-state.md, descreva o que melhorou e o que piorou, liste riscos e propostas de mudança com decisor indicado, grave em diario/revisoes/ e envie o resumo ao canal revisoes.
```

## Observação
Quando o dia 1 e o dia 15 coincidirem com a revisão quinzenal, as duas rodam em sequência. É esperado: a mensal olha o mês, a quinzenal olha os padrões.
