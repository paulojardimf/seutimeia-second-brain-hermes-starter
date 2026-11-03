---
name: seutimeia-second-brain-onboard
description: Conduz pelo Discord a construção do segundo cérebro da operação, a partir de um Hermes já instalado. Confere o ambiente, entrevista as pessoas, preenche o repositório, cria canais e agenda as rotinas de diário e revisões.
version: 3.0.0
author: Paulo Jardim e SeuTimeIA
license: MIT
platforms: [linux, macos]
metadata:
  hermes:
    tags: [second-brain, onboarding, hermes, discord, github, rotinas]
---

# Onboarding do segundo cérebro

## Quando usar
Quando alguém pedir para montar, iniciar ou retomar o segundo cérebro, ou mandar o link do repositório do método. Frases típicas: "vamos montar o segundo cérebro", "roda o onboarding", "continua de onde paramos".

## Premissa
O Hermes já está instalado, autenticado e no Discord da empresa. Você trabalha em dois repositórios: o **método** (público, somente leitura) e o **segundo cérebro da empresa** (privado, onde você escreve). Se só existir o método, peça o link do repositório privado e confirme com quem pediu antes de escrever.

## Regras que valem em todas as etapas
1. Não invente dados. O que não foi dito fica marcado como lacuna.
2. Nunca peça, repita ou grave chaves, senhas, tokens ou códigos de convite no chat ou no repositório. Credencial nova vai para o cofre ou `.env` pelo operador.
3. Conversas não são copiadas. Registre sínteses com autor, data e fonte.
4. Criar canais, categorias e rotinas exige uma aprovação explícita do operador, uma vez, sobre a lista completa.
5. Quem fala com você é identificado pelo nome no Discord. Só registre uma pessoa em `context/people.md` com o papel que ela mesma disse ou que o operador confirmou.
6. Antes de escrever, leia o arquivo atual. Depois de escrever, leia de volta.
7. Não duplique backlog de ferramentas de execução (Linear, Notion, ClickUp, Jira, planilhas).
8. Mensagens longas viram thread. Mensagens ao canal principal ficam curtas.

## Etapa 0 — Diagnóstico do ambiente
Confira e relate em uma tabela curta o resultado de cada item de `PRE-REQUISITOS.md`: versão do Hermes e serviço persistente, Discord (servidor, canal e quem está autorizado), GitHub (identidade, privacidade do repositório, escrita), modelo e provedor, cofre, e as ferramentas opcionais já ativas (Context7, Firecrawl, provedor de memória). Faça também o inventário do que já existe no servidor: bancos de dados (por exemplo PostgreSQL e extensões como pgvector), serviços em execução, provedor de memória do Hermes, ferramentas MCP, versões e espaço em disco. Registre em `ferramentas/` e use na Etapa 5 em vez de propor o que já está instalado. Mostre só o necessário; nunca imprima valores de segredos. Se faltar um item obrigatório, pare e diga exatamente o que falta e quem resolve.

## Etapa 1 — Alinhamento
Em até seis linhas: o que é este repositório, o que será feito, quanto tempo leva, e que o resultado são contexto, memória e rotinas. Pergunte se a entrevista começa agora.

## Etapa 2 — Entrevista
Use `STARTER-INTERVIEW.md`. Um bloco por vez, em thread. Aceite áudio. Ao fim de cada bloco, escreva nos arquivos e confirme em duas linhas o que gravou.

Ordem: identidade operacional, mapa do negócio, pessoas, ferramentas reais, cadência, governança, implantação do Hermes. Para pessoas, liste quem está no servidor Discord e pergunte o papel de cada um em vez de supor.

Skills que o time pedir ao longo do processo, ou que o Hermes criar, são gravadas em `skills/autorais/`, conforme o README da pasta.

Arquivos que você preenche: `context/user-profile.md`, `context/business-context.md`, `context/people.md`, `context/canais-e-destinos.md`, `context/regras-de-governanca.md`, `projects/project-state.md` e, em `ferramentas/`, uma pasta por ferramenta que o Hermes realmente acessa.

## Etapa 3 — Canais do Discord
Liste as categorias e canais existentes e procure algo equivalente ao segundo cérebro. Proponha, sem criar, a estrutura mínima:

- categoria **Segundo Cérebro**;
- `diario` — resumo diário das interações;
- `revisoes` — revisões semanais, quinzenais e mensais;
- `decisoes-e-licoes` — decisões, aprendizados, erros e lições, para consulta rápida;
- `cerebro-testes` — ensaio das rotinas (opcional).

Se já houver canal equivalente, use-o e registre o id em `context/canais-e-destinos.md`. Definir as permissões: leitura para o time autorizado, escrita só do Hermes, exceto `cerebro-testes`. Depois da aprovação, crie e releia a lista de canais.

## Etapa 4 — Rotinas
Proponha o pacote inicial de `rotinas/` com horário, destino e responsável:

| Rotina | Padrão | Destino |
|---|---|---|
| diário | dias úteis, fim do expediente | `diario` |
| revisão semanal | sexta, fim do expediente | `revisoes` |
| revisão quinzenal | dias 1 e 15, manhã | `revisoes` |
| revisão mensal | dia 1, manhã, sobre o mês anterior | `revisoes` |
| higiene semanal | segunda, manhã | `revisoes` |

Ajuste ao fuso e aos horários da empresa. Crie cada job pelo mecanismo de cron do Hermes (confira a sintaxe da versão instalada com `hermes cron --help`), usando o prompt de `rotinas/<nome>/README.md` e as skills `segundo-cerebro-captura` e `segundo-cerebro-revisao`. Rode cada uma uma vez em `cerebro-testes` ou manualmente e confirme que a mensagem chegou no destino e que o repositório foi atualizado. Registre estado real em `rotinas/STATUS.md`: o que foi criado, o que foi testado e o que ficou pendente.

## Etapa 5 — Ferramentas e memória
Para cada camada (Context7, Firecrawl, memória), diga o que já está instalado e testado, o que falta, o custo e o que o operador precisa fazer. Não ative nada sem a chave estar no cofre. Registre em `ferramentas/<nome>/README.md` o estado real.

## Etapa 6 — Entrega
Feche com:

1. **Estrutura adaptada**: o que foi preenchido, ajustado e o que falta.
2. **Decisões de operação**: canal principal, ferramenta de execução, fronteira entre contexto durável e backlog, quem pode corrigir ou excluir registros.
3. **Rotinas ativas** e as que esperam.
4. **Riscos e lacunas**.
5. **Próximos 3 a 7 passos**, com responsável.

Faça um commit com mensagem clara e envie a síntese ao canal principal com o link do commit.

## Retomada
Se a entrevista parar, grave o ponto em `projects/project-state.md` (seção "Onboarding") com o bloco atual e as lacunas. Ao ser chamado de novo, leia essa seção e continue dali, sem repetir perguntas já respondidas.

## Anti-padrões
- consultoria genérica no lugar de perguntas específicas;
- criar canal ou rotina sem aprovação;
- registrar algo que ninguém disse;
- automatizar antes de definir canal, fonte canônica e governança;
- deixar placeholders depois de a pessoa ter respondido.

## Regra de ouro
Melhor um segundo cérebro simples e usado do que um sistema bonito e abandonado.
