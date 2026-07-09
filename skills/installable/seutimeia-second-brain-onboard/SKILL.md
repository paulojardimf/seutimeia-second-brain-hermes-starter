---
name: seutimeia-second-brain-onboard
description: Onboarding guiado para transformar esta base clonada em um segundo cérebro operacional real, seguindo a metodologia SeuTimeIA.
version: 2.0.0
author: SeuTimeIA + Hermes
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [second-brain, onboarding, hermes, github, metodologia-seutimeia]
---

# SeuTimeIA Second Brain Onboard

## Quando usar
Use esta skill imediatamente após clonar o repositório-base do segundo cérebro.

### Triggers comuns
- "instala e roda o onboard do segundo cérebro"
- "vamos iniciar meu second brain"
- "quero adaptar essa base pra minha realidade"
- "rodar onboarding do starter kit"

## Objetivo
Transformar esta base genérica em uma primeira versão útil do segundo cérebro do usuário, sem inventar dados, sem burocratizar a operação e sem deixar o repositório com cara de template morto.

## Regra-mãe
Você não está preenchendo um template por preencher.
Você está definindo uma base operacional que precisa ser útil já na primeira semana.

## Princípios
- perguntar o mínimo necessário para destravar contexto real
- escrever nos arquivos conforme as respostas aparecem
- não manter placeholder genérico depois que o usuário já respondeu
- não duplicar backlog de ferramenta de execução
- priorizar simplicidade, governança e utilidade prática
- explicitar trade-offs quando houver mais de um caminho bom
- separar claramente conteúdo durável de detalhe transitório

## Leitura obrigatória antes de começar
Ler, nesta ordem:
1. `README.md`
2. `STARTER-INTERVIEW.md`
3. `CHANNEL-DECISION.md`
4. `SKILLS-MAP.md`
5. `ROTINAS-MAP.md`
6. `context/README.md`
7. `projects/README.md`
8. `skills/README.md`
9. `rotinas/README.md`
10. `ferramentas/README.md`

## Arquivos-base que podem ser atualizados no onboarding
- `context/user-profile.md`
- `context/business-context.md`
- `context/people.md`
- `context/canais-e-destinos.md`
- `context/regras-de-governanca.md`
- `projects/project-state.md`
- `README.md` se a operação precisar de framing mais específico
- `SKILLS-MAP.md` e `ROTINAS-MAP.md` se a primeira versão já estiver clara

## Fluxo de execução

### Etapa 1 — orientar e alinhar
Explique em 3 a 6 linhas:
- o que este repositório é
- o que ele não é
- como o onboarding vai funcionar
- qual será a saída ao final

### Etapa 2 — conduzir a entrevista
Use `STARTER-INTERVIEW.md` como roteiro-base.
Conduza por blocos, sem despejar todas as perguntas de uma vez.

#### Ordem preferida
1. identidade operacional
2. mapa do negócio
3. ferramentas reais
4. cadência
5. governança
6. implantação do Hermes

### Etapa 3 — materializar enquanto avança
À medida que as respostas surgirem, atualizar os arquivos adequados.

#### Regras de materialização
- se o usuário respondeu, o placeholder deve sumir
- se a resposta for parcial, registrar o que já está claro e marcar a lacuna explicitamente
- se uma definição afetar várias áreas, atualizar os arquivos relevantes na mesma rodada
- se surgir projeto ativo claro, refletir isso em `projects/project-state.md`
- se surgir ferramenta importante, criar ou adaptar a pasta correspondente em `ferramentas/`

### Etapa 4 — decidir o canal das rotinas
Usar `CHANNEL-DECISION.md` e fechar uma recomendação prática:
- canal principal
- motivo
- o que fica para depois
- riscos da escolha

Registrar em `context/canais-e-destinos.md`.

### Etapa 5 — recomendar o pacote inicial
Ao final, entregar:
1. skills que devem ser usadas agora
2. rotinas que devem ser ativadas agora
3. rotinas que devem esperar
4. playbooks que farão sentido depois
5. principais lacunas ainda não preenchidas
6. próximos passos concretos

## Critérios de decisão que a skill deve usar

### Ferramenta de execução principal
- se o usuário já usa Linear, ClickUp, Notion ou Jira com disciplina: não duplicar backlog no repositório
- se não existe ferramenta viva: usar o repositório como mapa de contexto, não como task manager improvisado

### Canal das rotinas
- Discord: melhor para operação viva com múltiplos canais/threads
- Telegram: melhor para acompanhamento pessoal direto
- Slack: melhor quando o time/cliente já vive lá
- WhatsApp: melhor para adoção fácil, pior para governança
- Web/CLI: melhor para fase inicial sem entrega proativa ainda

### Profundidade da implantação
- operação pequena → manter estrutura curta e viva
- operação com equipe, clientes e múltiplas ferramentas → aprofundar mapas e fronteiras

## Saída final esperada
Fechar o onboarding com este formato:

### 1. Estrutura adaptada
- o que foi preenchido
- o que foi ajustado
- o que ainda falta

### 2. Decisões de operação
- canal principal
- ferramenta de execução principal
- fronteira entre contexto durável e backlog
- ferramentas que entram e ferramentas que ficam fora

### 3. Pacote inicial recomendado
- skills iniciais
- rotinas iniciais
- playbooks necessários depois

### 4. Riscos e lacunas
- o que ainda está ambíguo
- o que não deveria ser automatizado ainda

### 5. Próximos passos
- 3 a 7 passos concretos

## Anti-padrões
- responder com consultoria genérica
- criar projeto fictício
- criar rotina só porque “parece sofisticado”
- duplicar backlog da ferramenta de execução
- deixar placeholders genéricos intactos depois das respostas
- automatizar antes de definir canal, fonte canônica e governança

## Regra de ouro
Melhor um segundo cérebro simples, vivo e usado do que um sistema bonito, complexo e morto.
