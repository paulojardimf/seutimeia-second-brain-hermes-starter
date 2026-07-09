---
name: cerebro
description: Liga o contexto operacional do second brain, combinando leitura mínima do repositório com o estado atual dos projetos e das fontes canônicas.
---

# Cérebro

## Objetivo
Ligar o contexto operacional antes de qualquer trabalho que afete projeto, processo, rotina ou decisão relevante.

## Trigger
- início de sessão
- pedido explícito de "ligar o cérebro"
- começo de trabalho em projeto sem contexto recente

## Entradas
- `README.md`
- `context/user-profile.md`
- `context/business-context.md`
- `projects/README.md`
- `projects/project-state.md`
- `README.md` da pasta relevante
- fontes de execução citadas pelo usuário (Linear, Notion, Discord etc.) quando forem necessárias para reduzir drift

## Processo
1. Ler o contexto mínimo obrigatório.
2. Identificar em qual frente/projeto a demanda cai.
3. Conferir se há drift entre o second brain e a ferramenta de execução.
4. Responder com briefing curto: foco, risco, próximos passos e fontes.

## Saída esperada
- briefing compacto, acionável e com referência às fontes
- nada de despejo de markdown

## Regra crítica
Se o contexto do repositório contradisser a realidade atual de execução, apontar a divergência explicitamente.
