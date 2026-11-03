# Context7

## Papel
Entrega ao Hermes a documentação atual de bibliotecas, frameworks e APIs. Útil quando o Hermes for integrar um sistema (por exemplo ERP, CRM ou API de marketing) e precisar da sintaxe correta da versão atual, em vez de lembrar de memória.

## Quando faz sentido
- o Hermes vai escrever ou revisar integrações com APIs de terceiros;
- a equipe quer respostas que citem a documentação oficial.

## O que o operador faz
1. Cria a conta da empresa no Context7 e gera a chave de API.
2. Guarda a chave no cofre da empresa (nunca no Git ou no chat).
3. Pede ao Hermes que registre o Context7 como servidor MCP, lendo a chave do cofre, e teste com uma consulta simples.

## O que documentar aqui
- quem é o titular da conta;
- onde a chave está guardada (nome no cofre, nunca o valor);
- data do teste e resultado;
- limites do plano.

## Riscos
- a chave em arquivo de texto ou no Discord;
- consulta com dados do cliente da empresa dentro do texto buscado: a busca deve citar só nomes de bibliotecas e APIs.
