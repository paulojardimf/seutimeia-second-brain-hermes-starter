<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/par-horizontal-grafite.svg">
    <img src="assets/par-horizontal-papel.svg" alt="Paulo Jardim e SeuTimeIA" width="560">
  </picture>
</p>

# Segundo cérebro para Hermes

Um repositório para o seu agente Hermes montar, com você, o segundo cérebro da sua operação. Você dá o link ao Hermes. Ele instala a skill de onboarding, entrevista você e as pessoas do time pelo Discord e escreve o que aprende neste repositório. Depois disso, as rotinas de diário e de revisão mantêm a base viva sem ninguém precisar lembrar.

Este repositório é um ponto de partida. Não contém o segundo cérebro de ninguém: só estrutura, método, skills e rotinas.

## De onde você parte

O método supõe que o Hermes já existe e já trabalha para você. Os requisitos estão em [`PRE-REQUISITOS.md`](./PRE-REQUISITOS.md). Em resumo:

- o Hermes roda no seu servidor, em rede protegida, como serviço persistente;
- o bot está no Discord da empresa, com permissão para criar categorias, canais e threads;
- o Hermes tem autenticação válida no GitHub e um provedor de modelo;
- as chaves ficam em um cofre ou no `.env` do Hermes, nunca neste repositório.

Se algum ponto faltar, a skill de onboarding diagnostica e diz o que falta antes de começar.

## Os três pilares

| Pilar | Pergunta que responde | Onde vive |
|---|---|---|
| **Contexto** | Quem somos, o que fazemos e como decidimos? | [`context/`](./context/README.md), [`projects/`](./projects/README.md), [`ferramentas/`](./ferramentas/README.md) |
| **Memória** | O que aconteceu, o que decidimos e o que aprendemos? | [`diario/`](./diario/README.md), [`memoria/`](./memoria/README.md) |
| **Cadência** | O que roda sozinho e com que método? | [`rotinas/`](./rotinas/README.md), [`skills/`](./skills/README.md) |

Contexto muda devagar e é revisado por pessoas. Memória cresce todo dia e é escrita pelo Hermes a partir das conversas. Cadência é o que transforma a primeira em segunda sem esforço manual.

## Como começar

1. Abra o canal onde o Hermes responde, no Discord da empresa.
2. Mande a mensagem de [`START-HERE.md`](./START-HERE.md), com o link deste repositório (ou do seu repositório criado a partir dele).
3. O Hermes instala as skills, confere o ambiente e começa a entrevista em uma thread.
4. Responda por texto ou por áudio. Quem mais precisar contribuir é convidado na mesma thread.
5. No fim, o Hermes propõe os canais e as rotinas. Você aprova uma vez e eles são criados.

## O que a entrevista produz

- perfil e contexto do negócio, pessoas e papéis (a partir de quem está no Discord);
- inventário das ferramentas que o Hermes realmente acessa;
- decisão do que fica no segundo cérebro e do que continua nas ferramentas de execução;
- canais do Discord para o segundo cérebro, criados só se ainda não existirem;
- o pacote inicial de rotinas: diário, revisão semanal, quinzenal e mensal.

## Memória que se constrói sozinha

Todo dia o Hermes lê as interações que as pessoas autorizadas tiveram com ele e separa o que merece ficar:

- **decisões**, com quem decidiu e por quê;
- **fatos** estáveis sobre a empresa, clientes e processos;
- **aprendizados** que mudam como o trabalho é feito;
- **erros** e **lições aprendidas**, sem culpado.

Cada item recebe data, fonte e autor. Conversas inteiras não são copiadas. Detalhes em [`memoria/`](./memoria/README.md).

## Estrutura do repositório

| Pasta ou arquivo | Papel |
|---|---|
| [`PRE-REQUISITOS.md`](./PRE-REQUISITOS.md) | estado esperado do Hermes antes de começar |
| [`START-HERE.md`](./START-HERE.md) | a mensagem que inicia tudo |
| [`context/`](./context/README.md) | identidade, negócio, pessoas, canais e governança |
| [`projects/`](./projects/README.md) | contexto dos projetos ativos |
| [`ferramentas/`](./ferramentas/README.md) | o que o Hermes acessa e como |
| [`memoria/`](./memoria/README.md) | decisões, fatos, aprendizados, erros e lições |
| [`diario/`](./diario/README.md) | diário executivo por dia |
| [`rotinas/`](./rotinas/README.md) | crons, horários, destinos e prompts |
| [`skills/`](./skills/README.md) | skills instaláveis e skills-base |
| [`playbooks/`](./playbooks/README.md) | procedimentos reutilizáveis |
| [`agentes/`](./agentes/README.md) | papéis e regras do agente |
| [`historico/`](./historico/README.md) | legado e arquivados, fora do contexto padrão |

## Regra-mãe

**README ou pasta.** Toda pasta relevante tem um `README.md` que diz o propósito, o conteúdo, o que está ativo e como o agente lê e escreve ali.

Segunda regra: **estrutura se copia, conteúdo confidencial não.** Segredos, dados pessoais e credenciais não entram neste repositório. Ele deve ser privado quando contiver contexto real da sua empresa (veja [`context/regras-de-governanca.md`](./context/regras-de-governanca.md)).

---

Método de implantação de agentes por [Paulo Jardim](https://github.com/paulojardimf) e SeuTimeIA. Auditoria de sanitização em [`AUDITORIA.md`](./AUDITORIA.md).
