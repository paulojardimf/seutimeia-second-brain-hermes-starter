# Escolha do canal das rotinas

Use esta tabela para decidir onde o Hermes deve entregar as rotinas.

| Cenário | Melhor canal | Quando usar | Risco principal |
|---|---|---|---|
| operação interna com threads, histórico e múltiplos agentes | Discord | time técnico/operacional | excesso de canais mal governados |
| acompanhamento pessoal e direto | Telegram | rotina individual e leitura rápida | dispersão se misturar com conversas pessoais |
| time comercial/cliente que vive no WhatsApp | WhatsApp | adoção mais fácil pelo cliente | pior governança e menor estrutura |
| apenas setup/manual inicial | Web/CLI | fase de implantação e ajuste | zero entrega proativa |

## Regra prática
- **Discord**: melhor para operação viva com canais específicos.
- **Telegram**: melhor para acompanhamento pessoal.
- **WhatsApp**: melhor quando adoção importa mais que sofisticação.
- **Web/CLI**: melhor para construir a base antes de automatizar.

## Recomendação de implantação
1. escolher **um** canal principal
2. criar um canal/grupo dedicado
3. documentar isso em `context/canais-e-destinos.md`
4. só então configurar crons
