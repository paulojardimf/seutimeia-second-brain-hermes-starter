---
name: segundo-cerebro-captura
description: Lê as interações do dia entre as pessoas autorizadas e o Hermes e grava no segundo cérebro as decisões, fatos, aprendizados, erros e lições, mais o diário do dia.
version: 1.0.0
author: Paulo Jardim e SeuTimeIA
license: MIT
platforms: [linux, macos]
metadata:
  hermes:
    tags: [second-brain, diario, memoria, rotina]
---

# Captura diária do segundo cérebro

## Quando usar
Na rotina diária do segundo cérebro, ou quando alguém pedir "fecha o dia", "registra o que aconteceu hoje" ou "captura essa sessão".

## O que lê
1. As sessões do Hermes do período (ontem 00h até agora, no fuso do `context/canais-e-destinos.md`), de todas as pessoas autorizadas, usando a busca de sessões do Hermes.
2. As mensagens dos canais e threads onde o Hermes foi chamado.
3. `memoria/` e o diário dos últimos dias, para não duplicar nem contradizer registros.

Não lê DMs, canais fora da lista autorizada nem conteúdo que a pessoa marcou como confidencial.

## O que grava
Para cada coisa durável, um registro curto no modelo de `memoria/_modelos/`:

| Tipo | Pasta | Critério |
|---|---|---|
| Decisão | `memoria/decisoes/` | alguém com autoridade escolheu entre alternativas, e há motivo |
| Fato | `memoria/fatos/` | informação estável sobre empresa, cliente, processo, sistema ou pessoa (papel) |
| Aprendizado | `memoria/aprendizados/` | algo que passa a mudar como o trabalho é feito |
| Erro e lição | `memoria/erros-e-licoes/` | algo deu errado, o que causou, o que muda a partir de agora |

Todo registro tem **data, autor, fonte (canal ou sessão e link) e confiança** (confirmado pela pessoa, inferido ou a confirmar). Inferência nunca vira fato confirmado. Se o registro contradiz outro, aponte a divergência em vez de sobrescrever.

Depois grava o diário em `diario/AAAA/MM/AAAA-MM-DD.md`, com as seções: o que foi feito, decisões (links), fatos novos (links), aprendizados e erros (links), pendências com responsável, perguntas em aberto.

## Skills criadas na operação
Se, nas interações do dia, o Hermes criou ou ajustou uma skill para o time (ou se um processo se repetiu e merece uma), confira se a cópia está em `skills/autorais/<nome>/SKILL.md`. Grave a cópia, atualize o índice em `skills/autorais/README.md` e cite a skill no diário. Skill nova só é proposta, nunca criada sem o pedido ou a aprovação de uma pessoa.

## Regras
- Síntese, não transcrição. Cite no máximo uma frase curta quando o texto exato importar.
- Atribua decisões a quem decidiu. Pergunta ou sugestão do Hermes não é decisão do cliente.
- Erros e lições descrevem causa e ajuste, nunca culpa.
- Nada de segredos, dados pessoais sensíveis, dados de saúde, assuntos de RH ou valores de remuneração. Na dúvida, não grave e liste em "a confirmar".
- Dia sem interação gera uma linha no diário, não um texto inventado.
- Releia cada arquivo depois de escrever e faça um único commit do dia.

## Entrega
Envie ao canal `diario` um resumo de até 12 linhas: contagem por tipo de registro, as 3 decisões ou lições mais relevantes com link, e pendências que vencem. Se algo precisar de confirmação humana, liste no fim com a pergunta direta e o nome de quem deve responder.

## Falhas
Se não conseguir ler as sessões, escrever no repositório ou postar no Discord, diga qual passo falhou e o que ficou gravado. Não declare o dia fechado.
