# Comece aqui

Para quem vai pedir ao Hermes que monte o segundo cérebro. Leva uns dez minutos para dar a partida; a entrevista acontece depois, no ritmo do time.

## 1. Tenha o seu repositório

Crie um repositório **privado** a partir deste (botão *Use this template* ou *Fork*, ou uma cópia do conteúdo). É nele que o Hermes vai escrever. Este repositório público fica só como referência do método.

Dê ao Hermes permissão de escrita nesse repositório, pela autenticação GitHub que ele já usa.

## 2. Confira os pré-requisitos

Leia [`PRE-REQUISITOS.md`](./PRE-REQUISITOS.md). Se o Hermes já está no Discord, autenticado no GitHub e com modelo configurado, você já está pronto.

## 3. Mande esta mensagem ao Hermes no Discord

Mencione o bot no canal principal e cole, trocando o link:

```text
Vamos montar o segundo cérebro da nossa operação.

O repositório do método está em https://github.com/paulojardimf/seutimeia-second-brain-hermes-starter e o nosso repositório privado é <LINK DO SEU REPOSITÓRIO>.

1. Clone os dois, leia o README e o PRE-REQUISITOS do método e instale as skills em skills/installable com scripts/install-onboard-skill.sh.
2. Recarregue as skills e carregue a seutimeia-second-brain-onboard.
3. Confira o ambiente (Hermes, Discord, GitHub, modelo, cofre) e me diga o que encontrou antes de começar.
4. Abra uma thread e conduza a entrevista por blocos. Escreva as respostas no nosso repositório conforme eu for respondendo.
5. No fim, proponha os canais do Discord e as rotinas (diário, revisão semanal, quinzenal e mensal) e espere a minha aprovação antes de criar.

Não invente dados, não peça nem repita chaves ou senhas no chat e não copie conversas inteiras para o repositório.
```

## 4. Responda a entrevista

O Hermes usa o roteiro de [`STARTER-INTERVIEW.md`](./STARTER-INTERVIEW.md). Pode responder por texto ou áudio, em partes, e chamar colegas para a mesma thread: quem fala com o Hermes é identificado pelo nome no Discord e entra na lista de pessoas do contexto.

## 5. Aprove o pacote inicial

Ao fim, o Hermes mostra os canais e rotinas que pretende criar, com horários e destinos. Você aprova, ajusta ou corta. Só depois ele cria e confere que cada rotina rodou ao menos uma vez em teste.

## 6. Acompanhe

Nos primeiros dias olhe o diário e as revisões no Discord e corrija o que estiver errado direto na conversa. O Hermes atualiza o repositório. Quando os registros começarem a se acumular em [`memoria/`](./memoria/README.md), o segundo cérebro está funcionando.

## Quando algo travar

- O Hermes não instala a skill: peça que mostre o erro e o caminho de skills que ele usa (`HERMES_HOME`).
- O bot não cria canais: falta permissão no servidor. Peça ao administrador do Discord.
- Faltam chaves de integração: veja [`ferramentas/`](./ferramentas/README.md); o operador cria a chave e coloca no cofre.
