# Auditoria de sanitização

## Objetivo
Registrar o que foi usado como **estrutura** e o que foi mantido fora por ser conteúdo privado ou específico.

## O que serve de referência
- separação entre contexto, projetos, memória, skills, rotinas, ferramentas, playbooks e histórico;
- regra de README por pasta;
- distinção entre contexto durável e backlog operacional;
- skills de onboarding, captura e revisão;
- cadência de diário e revisões.

## O que não está neste repositório
- dados pessoais ou de negócio de qualquer pessoa ou empresa;
- clientes, projetos e repositórios privados;
- canais, ids de Discord, Telegram ou WhatsApp reais;
- cron jobs reais e arquivos de diário;
- memória privada, credenciais e chaves.

## Revisão de 03/11/2026
Varredura do conteúdo atual (arquivos e nomes) por: nomes de pessoas e empresas, ids numéricos longos, URLs de convite, tokens, chaves, e-mails e caminhos locais de servidor. A mensagem de convite que citava o nome de um mentorado foi removida; o nome continua no histórico do Git. Fora a menção às pastas padrão do Hermes (`~/.hermes`) nos scripts, nada de ambiente privado foi encontrado.

## Regra antes de publicar derivações
1. procurar nomes próprios, clientes, projetos e canais reais;
2. remover ids, URLs privadas e referências operacionais sensíveis;
3. conferir se o arquivo ensina a estrutura sem expor conteúdo;
4. repetir a varredura depois de cada mudança relevante.
