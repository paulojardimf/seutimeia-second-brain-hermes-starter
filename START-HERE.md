# Start Here — instrução para o mentorado / cliente

## Passo 1 — clone esta base
```bash
git clone https://github.com/paulojardimf/seutimeia-second-brain-hermes-starter.git meu-second-brain
cd meu-second-brain
```

Se você ainda não criou seu próprio repositório, faça isso primeiro a partir desta base.

## Passo 2 — instale a skill de onboarding que já veio no repositório
```bash
bash scripts/install-onboard-skill.sh
```

Isso copia a skill `seutimeia-second-brain-onboard` para o seu Hermes local.

## Passo 3 — abra uma nova conversa no Hermes
Abra uma sessão nova no Hermes Web/CLI com acesso a este diretório local.

## Passo 4 — carregue a skill
Na nova sessão:
1. rode `/reload-skills` se necessário
2. carregue `/skill seutimeia-second-brain-onboard`

## Passo 5 — cole este prompt inicial

```text
Quero que você use a skill `seutimeia-second-brain-onboard` que já foi instalada a partir deste repositório clonado.

Atue como arquiteto do meu segundo cérebro operacional seguindo a metodologia da SeuTimeIA e usando esta base como ponto de partida.

Objetivo:
- adaptar esta estrutura para a minha realidade
- entrevistar-me passo a passo
- preencher os arquivos essenciais sem inventar dados
- organizar contexto, projetos, ferramentas, rotinas e canais de entrega
- definir quais skills e crons fazem sentido agora

Restrições:
- não manter placeholders genéricos quando eu já tiver respondido
- não criar automação desnecessária
- não duplicar backlog de ferramenta de gestão
- sempre explicitar trade-offs
- priorizar simplicidade, governança e utilidade real

Primeiro passo:
1. confirme que a skill `seutimeia-second-brain-onboard` está carregada
2. leia os arquivos obrigatórios do repositório
3. me conduza pela entrevista inicial em blocos
4. vá materializando as respostas nos arquivos corretos
5. ao final, proponha a primeira versão operacional do meu second brain
```

## Passo 6 — siga a entrevista
O Hermes deve usar [`STARTER-INTERVIEW.md`](./STARTER-INTERVIEW.md) como roteiro-base, com a skill fazendo a orquestração do processo.

## Passo 7 — escolha o canal das rotinas
Use [`CHANNEL-DECISION.md`](./CHANNEL-DECISION.md) para definir para onde os resultados das rotinas vão ser enviados.

## Passo 8 — adapte o restante das skills
Veja [`SKILLS-MAP.md`](./SKILLS-MAP.md).

## Passo 9 — configure as primeiras rotinas
Veja [`ROTINAS-MAP.md`](./ROTINAS-MAP.md).
