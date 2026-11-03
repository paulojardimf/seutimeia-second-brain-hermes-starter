# Status executivo das rotinas

Atualize este arquivo quando uma rotina for criada, alterada ou testada. Estado inicial: nenhuma rotina criada.

| Rotina | Estado | Cron padrão | Destino | Skill | Último teste |
|---|---|---|---|---|---|
| [`diario-do-brain`](./diario-do-brain/README.md) | não criada | `0 18 * * 1-5` | `diario` | `segundo-cerebro-captura` | — |
| [`revisao-semanal`](./revisao-semanal/README.md) | não criada | `0 17 * * 5` | `revisoes` | `segundo-cerebro-revisao` | — |
| [`revisao-quinzenal`](./revisao-quinzenal/README.md) | não criada | `0 9 1,15 * *` | `revisoes` | `segundo-cerebro-revisao` | — |
| [`revisao-mensal`](./revisao-mensal/README.md) | não criada | `0 9 1 * *` | `revisoes` | `segundo-cerebro-revisao` | — |
| [`higiene-semanal`](./higiene-semanal/README.md) | não criada | `0 9 * * 1` | `revisoes` | `higiene-semanal` | — |
| [`sync-projetos-repos`](./sync-projetos-repos/README.md) | opcional | semanal | `revisoes` | — | — |

Estados: `não criada`, `criada, sem teste`, `testada`, `pausada`. Só registre `testada` com a data e o resultado da execução real.
