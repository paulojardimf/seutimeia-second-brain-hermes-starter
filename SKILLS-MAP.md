# Skills Map — starter kit

## Skills-base do kit

| Skill | Papel | Quando usar | Status inicial |
|---|---|---|---|
| `seutimeia-second-brain-onboard` | onboarding guiado da base clonada | primeiro passo depois do clone | prioritária |
| `cerebro` | onboarding + boot de contexto | início de sessão e implantação inicial | recomendada |
| `rotina` | cockpit diário | rotina operacional pessoal/equipe | opcional |
| `salve` | flush de fim de sessão | quando o brain precisa registrar decisões e aprendizados | recomendada |
| `higiene-semanal` | revisão estrutural do repositório | manutenção semanal | recomendada |
| `varredura-de-sessoes` | consolidado executivo das sessões | diário ou semanal | opcional |

## Ordem recomendada
1. instalar `seutimeia-second-brain-onboard`
2. rodar o onboarding inicial
3. depois decidir se `cerebro`, `rotina` e `salve` entram no fluxo vivo

## Como instalar a skill principal
```bash
bash scripts/install-onboard-skill.sh
```

Depois, na nova sessão do Hermes:
- `/reload-skills`
- `/skill seutimeia-second-brain-onboard`
- `vamos iniciar meu second brain`

## Skills que normalmente serão adaptadas depois
- skill de proposta comercial
- skill jurídica/documental
- skill de operação em ferramenta específica (Linear, Notion, Gmail, etc.)
- skill de cliente/projeto específico

## O que veio da referência do brain do Paulo, mas foi generalizado
- separação entre contexto durável e backlog operacional
- uso de GitHub como memória versionada
- uso de README por pasta
- distinção entre skills, rotinas, playbooks e projetos
- flush de sessão e higiene recorrente

## O que deliberadamente NÃO foi copiado
- dados pessoais
- projetos confidenciais
- clientes reais
- canais reais
- automações privadas
- rotinas sensíveis
