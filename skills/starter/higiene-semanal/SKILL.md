---
name: higiene-semanal
description: Revisão semanal da estrutura do second brain para manter legibilidade, governança e aderência à realidade.
---

# Higiene semanal

## Objetivo
Garantir que o second brain não degenere em pasta de arquivos soltos, backlog duplicado e contexto velho.

## Trigger
- cron semanal
- antes de compartilhar o repositório com alguém
- antes de ligar automações novas

## Processo
1. detectar arquivos sem pasta adequada
2. detectar pastas sem `README.md`
3. detectar documento ativo citado no mapa mas inexistente
4. detectar material de legado misturado na área ativa
5. detectar placeholders antigos demais
6. corrigir ou registrar ação externa necessária

## Saída esperada
Árvore limpa, legível e coerente.
