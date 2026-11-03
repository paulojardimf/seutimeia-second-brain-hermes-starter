# Memória do Hermes

## Papel
Camada de memória que complementa este repositório. O segundo cérebro guarda o que a empresa decidiu e aprendeu, em arquivos revisáveis. A memória do Hermes guarda fatos e entidades de forma pesquisável entre sessões (preferências, pessoas, clientes, termos).

## Camadas, da mais simples à mais completa
| Camada | O que é | Quando ativar | Custo de operação |
|---|---|---|---|
| 1. Fatos locais (Holographic / `fact_store`) | provedor de memória do Hermes que guarda fatos curtos e permite corrigi-los | desde o início | baixo |
| 2. GBrain | busca por significado sobre fontes explícitas (documentos do segundo cérebro, por exemplo), com correção e retirada | quando o repositório tiver volume e a busca por texto não bastar | médio |
| 3. Honcho | memória por pessoa e sessão, com representações derivadas por modelo | quando houver várias pessoas usando o Hermes e valor em perfis individuais | alto |

GBrain é de [Garry Tan](https://github.com/garrytan/gbrain) e Honcho é da [Plastic Labs](https://github.com/plastic-labs/honcho) (licença AGPL-3.0; leia as obrigações antes de empacotar). Instale pelas fontes oficiais, em versão fixada.

## Como as camadas se encaixam no Hermes
O Hermes aceita **um** provedor de memória externo por vez. A camada 1 (Holographic) é esse provedor: instale com `hermes plugins install holographic` e ative com `memory.provider: holographic`. GBrain e Honcho não competem com ele: entram por uma ponte MCP local (um servidor `shared-memory` registrado com `hermes mcp add`), que grava e busca nos dois e permite corrigir e retirar registros. Cada camada acima da 1 é um serviço a mais para manter, com banco, credenciais e backup próprios.

Antes de propor qualquer camada, o Hermes confere o que já existe no servidor (PostgreSQL com pgvector, serviços e plugins), como pede a etapa 0 da skill de onboarding.

## Princípios
- comece pela camada 1 e só suba de camada com uso real que justifique;
- cada instalação do cliente é isolada: usuário, banco, credenciais e processo próprios;
- memória não concede permissão e não altera skills sozinha;
- o que o assistente disse não vira fato confirmado pelo cliente;
- precisa existir caminho de correção e exclusão, com responsável definido;
- teste de gravar, buscar, corrigir e retirar um registro de teste antes de usar com dados reais.

## Modelos
GBrain e Honcho precisam de um modelo de geração e de embeddings. As opções são rodar modelos locais (sem cobrança por chamada, mas com consumo de CPU, memória e disco do servidor) ou usar um provedor da própria empresa (sem carga local, mas com custo por uso e dados saindo do servidor). Decida por escrito antes de instalar.

## O que documentar aqui
- camada ativa e data;
- versão e origem de cada componente;
- onde estão os dados e o backup;
- responsável por correção e exclusão;
- resultado dos testes.
