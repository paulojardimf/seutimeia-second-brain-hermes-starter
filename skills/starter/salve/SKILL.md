---
name: salve
description: Fecha a sessão sem perder decisões, aprendizados e contexto durável, publicando só o que merece virar memória operacional.
---

# Salve

## Objetivo
Fechar uma sessão sem perder decisões, contexto de projeto e aprendizados duráveis.

## Trigger
- fim de sessão relevante
- conclusão de entrega com mudança estrutural
- pedido do usuário para registrar o que ficou decidido

## Entradas
- decisões tomadas
- arquivos alterados no repositório
- contexto de projeto impactado
- mudanças que afetam rotinas, ferramentas ou governança

## Processo
1. revisar o que realmente virou fato durável
2. atualizar somente os arquivos canônicos necessários
3. verificar se arquivos novos ficaram sem README correspondente
4. publicar no GitHub usando o padrão canônico
5. se o push falhar, explicitar o ponto de falha

## Saída esperada
Repositório consistente, atualizado e sem lixo transitório na área ativa.
