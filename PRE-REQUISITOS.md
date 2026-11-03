# Pré-requisitos

O onboarding supõe um Hermes já em operação. A skill de onboarding confere cada item abaixo na primeira etapa e relata o que encontrou. Nada aqui exige que você abra o terminal: se algo faltar, a skill diz quem resolve.

## Obrigatórios

| Item | Como a skill confere | Se faltar |
|---|---|---|
| Hermes rodando como serviço persistente | `hermes --version` e estado do serviço | instalar e configurar o serviço antes de seguir |
| Bot no Discord da empresa, responde por menção e em threads | a própria conversa onde a skill foi chamada | conectar o gateway do Discord |
| Permissão do bot para criar categorias, canais e threads, e para ler o histórico dos canais do segundo cérebro | tentativa controlada, com confirmação do operador | ajustar as permissões do bot no servidor |
| Lista de pessoas autorizadas a falar com o Hermes | arquivo de configuração do gateway | definir nominalmente quem pode usar |
| Autenticação válida no GitHub, com escrita no repositório do segundo cérebro | `gh auth status` ou equivalente, sem exibir token | autenticar a conta da empresa |
| Provedor de modelo autenticado | o Hermes responde e a configuração mostra provedor e modelo | autenticar o provedor |
| Cofre ou arquivo de segredos fora do Git | caminho informado pelo operador | criar um cofre antes de qualquer chave nova |

Regras que valem sempre:

- o repositório do segundo cérebro da sua empresa é **privado**;
- nenhuma chave, token, senha ou código de convite é colado no Discord, no repositório ou em prints;
- o Hermes pede ao operador qualquer credencial nova e a guarda só no cofre ou no `.env`.

## Recomendados

| Item | Para que serve |
|---|---|
| Rede privada e firewall no servidor | reduzir a superfície de ataque do Hermes |
| Plano de recuperação do servidor | saber voltar de um reinício ou falha |
| Um canal de testes no Discord | ensaiar rotinas antes de enviar ao time |

## Opcionais, em camadas

Cada camada soma capacidade e custo. Comece sem elas e ative quando houver uso real. Detalhes em [`ferramentas/`](./ferramentas/README.md).

| Camada | O que acrescenta | Exige |
|---|---|---|
| Documentação atualizada de bibliotecas e APIs | o Hermes consulta a documentação oficial atual ao integrar sistemas | conta e chave no [Context7](./ferramentas/context7/README.md) |
| Busca e leitura estruturada da web | pesquisas e extração de páginas | conta e chave no [Firecrawl](./ferramentas/firecrawl/README.md) (há plano gratuito) |
| Memória de fatos e entidades | o Hermes lembra de preferências, pessoas e decisões entre sessões | provedor de memória do Hermes, ver [`ferramentas/memoria/`](./ferramentas/memoria/README.md) |

## Antes de ligar as rotinas

- Avise as pessoas que usam o Hermes que as conversas alimentam o segundo cérebro (decisões, fatos, aprendizados e lições), sem cópia integral.
- Defina quem pode pedir a correção ou a exclusão de um registro.
