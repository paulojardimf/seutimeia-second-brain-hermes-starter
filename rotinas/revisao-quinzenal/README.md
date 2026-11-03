# Rotina quinzenal — revisão de padrões

## Status
Não configurada por padrão.

## Objetivo
Procurar o que se repete em 15 dias: erros com a mesma causa, lições registradas e ainda não aplicadas, fatos contraditórios, rotinas que não geram valor.

## Agenda padrão
| Campo | Valor |
|---|---|
| Expressão cron | `0 9 1,15 * *` (dias 1 e 15, manhã) |
| Destino | canal `revisoes` |
| Skill | `segundo-cerebro-revisao` (modo quinzenal) |

## Prompt do job
```text
Carregue a skill segundo-cerebro-revisao e faça a revisão quinzenal dos últimos 15 dias. Procure padrões recorrentes, erros com a mesma causa e lições ainda não incorporadas ao contexto, às skills ou às rotinas. Proponha mudanças concretas com decisor indicado, grave em diario/revisoes/ e envie o resumo ao canal revisoes. Não altere nada sem aprovação.
```
