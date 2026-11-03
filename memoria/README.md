# Memória (`memoria/`)

## Propósito
Guarda o que a operação aprendeu ao trabalhar com o Hermes: decisões, fatos, aprendizados, erros e lições. É o pilar de **memória** do segundo cérebro e cresce todo dia pela rotina de captura.

## Conteúdo
| Pasta | O que entra | Quem escreve |
|---|---|---|
| [`decisoes/`](./decisoes) | escolhas entre alternativas, com motivo e autor | Hermes, a partir das interações |
| [`fatos/`](./fatos) | informação estável sobre empresa, clientes, processos e sistemas | Hermes, com confirmação de quem informou |
| [`aprendizados/`](./aprendizados) | o que passa a mudar o jeito de trabalhar | Hermes |
| [`erros-e-licoes/`](./erros-e-licoes) | o que deu errado, a causa e o ajuste | Hermes, sem culpado |
| [`_modelos/`](./_modelos) | modelos de cada tipo de registro | operador |

## Como ler e escrever
- Um arquivo por registro, nomeado `AAAA-MM-DD-assunto-curto.md`.
- Todo registro tem data, autor, fonte e confiança (`confirmado`, `inferido` ou `a confirmar`).
- Um registro corrigido não é apagado em silêncio: o novo aponta para o anterior e diz o que mudou.
- Pedido de correção ou exclusão feito pela pessoa citada é atendido pelo responsável definido em `context/regras-de-governanca.md`.

## O que não entra
Transcrições, conversas completas, segredos, dados pessoais sensíveis, saúde, RH e remuneração.

## Quem alimenta
A skill [`segundo-cerebro-captura`](../skills/installable/segundo-cerebro-captura/SKILL.md), na rotina diária. As revisões em [`diario/`](../diario/README.md) leem esta pasta.
