# Rotina diária — captura e diário

## Status
Não configurada por padrão. A skill de onboarding cria depois da aprovação do operador.

## Objetivo
Fechar o dia lendo as interações de todas as pessoas autorizadas com o Hermes e gravando decisões, fatos, aprendizados, erros e lições em [`memoria/`](../../memoria/README.md), mais o diário do dia em [`diario/`](../../diario/README.md).

## Agenda padrão
| Campo | Valor |
|---|---|
| Expressão cron | `0 18 * * 1-5` (ajuste horário e fuso ao expediente da empresa) |
| Destino | canal `diario` |
| Skill | `segundo-cerebro-captura` |
| Saída no Discord | resumo de até 12 linhas com link |

## Prompt do job
```text
Carregue a skill segundo-cerebro-captura e rode a captura do dia no repositório do segundo cérebro desta empresa. Leia as sessões e os canais autorizados desde a última captura, grave os registros em memoria/ e o diário do dia, faça um commit e envie o resumo ao canal diario. Não invente dados e não copie conversas. Se algum passo falhar, diga qual e o que ficou gravado.
```

## Regras
- sem interação no dia, uma linha no diário dizendo isso;
- sem dump bruto de conversa;
- nada de segredos ou assuntos sensíveis;
- cada registro tem autor, data, fonte e confiança.
