---
name: segundo-cerebro-revisao
description: Faz as revisões semanal, quinzenal e mensal do segundo cérebro a partir do diário e dos registros de memória, e entrega padrões, riscos e próximos passos.
version: 1.0.0
author: Paulo Jardim e SeuTimeIA
license: MIT
platforms: [linux, macos]
metadata:
  hermes:
    tags: [second-brain, revisao, memoria, rotina]
---

# Revisões do segundo cérebro

## Quando usar
Nas rotinas semanal, quinzenal e mensal, ou quando alguém pedir "revisão da semana", "revisão do mês", "o que aprendemos".

## Janelas
| Revisão | Janela | Profundidade |
|---|---|---|
| Semanal | últimos 7 dias | o que andou, o que travou, decisões e pendências |
| Quinzenal | últimos 15 dias | padrões que se repetem, erros recorrentes, lições ainda não aplicadas |
| Mensal | mês civil anterior | direção, resultados, riscos, o que mudar nas rotinas e no contexto |

## Entradas
`diario/` e `memoria/` da janela, `projects/project-state.md`, `context/` e a revisão anterior do mesmo tipo (para medir o que mudou).

## Passos
1. Confira a cobertura: há diário para os dias úteis da janela? Liste os dias sem registro como lacuna, sem preencher.
2. Agrupe os registros por tema, projeto e pessoa. Conte decisões, fatos, aprendizados e erros.
3. Procure:
   - decisões sem execução ou sem responsável;
   - erros que se repetem (mesma causa em dias diferentes);
   - lições registradas e ainda não incorporadas ao contexto, às skills ou aos processos;
   - fatos desatualizados ou contraditórios.
4. Proponha mudanças concretas, cada uma com origem nos registros: atualizar `context/`, ajustar uma rotina, criar ou corrigir uma skill, tratar um risco. Uma proposta por item, com quem decide.
5. Na revisão mensal, inclua uma leitura executiva: o que melhorou, o que piorou, o que o time deveria discutir.
6. Grave a revisão em `diario/revisoes/AAAA/` (`semanal-AAAA-Sww.md`, `quinzenal-AAAA-MM-qq.md`, `mensal-AAAA-MM.md`), releia e faça commit.

## Regras
- Só afirme o que os registros sustentam; cite o arquivo.
- Não altere `context/`, skills ou rotinas por conta própria: proponha e espere aprovação.
- Sem culpados. Erros se descrevem por causa e ajuste.
- Se a janela tiver pouco material, diga isso e não infle a revisão.

## Entrega
Envie ao canal `revisoes` um resumo de até 15 linhas com os pontos principais, as propostas que dependem de decisão (com nome do decisor) e o link do arquivo da revisão. Termine com as perguntas que o time precisa responder.
