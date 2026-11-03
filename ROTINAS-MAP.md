# Mapa de rotinas

As rotinas mantêm o segundo cérebro vivo, coerente e limpo. Cada uma tem seu `README.md` com cron padrão, destino, skill e o prompt do job. O estado real fica em [`rotinas/STATUS.md`](./rotinas/STATUS.md).

| Rotina | Frequência padrão | Destino | Skill | Prioridade |
|---|---|---|---|---|
| diário (captura) | dias úteis, fim do expediente | `diario` | `segundo-cerebro-captura` | alta |
| revisão semanal | sexta, fim do expediente | `revisoes` | `segundo-cerebro-revisao` | alta |
| revisão quinzenal | dias 1 e 15, manhã | `revisoes` | `segundo-cerebro-revisao` | média |
| revisão mensal | dia 1, manhã | `revisoes` | `segundo-cerebro-revisao` | alta |
| higiene semanal | segunda, manhã | `revisoes` | `higiene-semanal` | média |
| sync de projetos e repositórios | semanal | `revisoes` | — | opcional |

## Ordem de ativação
1. diário, observado por uma semana;
2. revisão semanal;
3. higiene semanal;
4. quinzenal e mensal;
5. rotinas específicas da empresa.

## Regras
- crie o job pelo mecanismo de cron do Hermes, na sintaxe da versão instalada;
- teste cada rotina uma vez antes de deixá-la agendada;
- só marque `testada` em `rotinas/STATUS.md` com data e resultado da execução real;
- rotina ruim automatiza bagunça: governança primeiro, automação depois.
