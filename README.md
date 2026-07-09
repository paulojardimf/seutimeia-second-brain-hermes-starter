# SeuTimeIA Second Brain — Hermes Starter

Starter kit público para criar um **segundo cérebro operacional guiado pelo Hermes**.

Este repositório **não é** o segundo cérebro do Paulo Jardim.
Ele é uma **base sanitizada e replicável**, inspirada na lógica operacional usada pela SeuTimeIA para implantar um segundo cérebro em mentorias, workshops e clientes.

## Para quem serve
- mentorados que querem estruturar um segundo cérebro em GitHub
- clientes de operação de agentes
- workshops da SeuTimeIA
- uso interno do time para onboarding e implantação

## O que este kit entrega
- estrutura inicial do repositório
- READMEs por pasta
- templates para contexto, projetos, ferramentas e rotinas
- skills-base para onboarding, rotina, salvamento e higiene
- prompt pronto para iniciar uma nova conversa no Hermes
- orientação para escolher o canal de entrega das rotinas (Discord, Telegram ou WhatsApp)

## O que este kit não entrega
- dados privados de Paulo Jardim
- conteúdo de clientes reais
- backlog interno
- credenciais, canais ou automações já configuradas

## Fluxo recomendado
1. Clone este repositório.
2. Crie um repositório seu a partir desta base.
3. Abra uma nova conversa no Hermes.
4. Cole o prompt de kickoff em [`START-HERE.md`](./START-HERE.md).
5. Deixe o Hermes conduzir a entrevista e preencher a base com o seu contexto.
6. Depois instale/adapte as skills e crons conforme a sua operação.

## Estrutura
- [`context/`](./context/README.md) — identidade, negócio, equipe, canais e regras duráveis
- [`projects/`](./projects/README.md) — inteligência dos projetos e mapa executivo
- [`skills/`](./skills/README.md) — skills-base do starter kit
- [`rotinas/`](./rotinas/README.md) — cadência recorrente, entregas e canais
- [`ferramentas/`](./ferramentas/README.md) — inventário real de ferramentas e integrações
- [`playbooks/`](./playbooks/README.md) — procedimentos reutilizáveis
- [`agentes/`](./agentes/README.md) — papéis dos agentes
- [`diario/`](./diario/README.md) — diário executivo
- [`historico/`](./historico/README.md) — legado, arquivados e snapshots

## Skills-base incluídas
- `cerebro` — onboarding e boot de contexto
- `rotina` — cockpit diário
- `salve` — flush de fim de sessão
- `higiene-semanal` — revisão estrutural do brain
- `varredura-de-sessoes` — consolidado executivo por sessões

Detalhamento em [`SKILLS-MAP.md`](./SKILLS-MAP.md).

## Rotinas-base incluídas
- rotina diária do brain
- revisão semanal/mensal
- higiene semanal
- sincronização de projetos/repositórios
- exemplos de decisão de canal de entrega

Detalhamento em [`ROTINAS-MAP.md`](./ROTINAS-MAP.md).

## Regra-mãe
**Estrutura se copia. Conteúdo não.**

Se algo for específico de uma pessoa, empresa, cliente, projeto confidencial, credencial ou canal privado, isso deve ser reconstruído no onboarding — nunca herdado deste repo.
