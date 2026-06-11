# Documentação do TBH2

## Objetivo

Servir como ponto central da documentação modular do TBH2, reunindo decisões de game design, conteúdo, balanceamento, arquitetura, implementação e histórico do projeto.

Este documento funciona como índice principal da documentação.

Ele não substitui os documentos específicos de cada domínio.

---

## Status

In Progress

---

## Dependências

* [Visão do projeto](core/00_VISION.md)
* [Gameplay central](core/01_CORE_GAMEPLAY.md)
* [Roadmap](technical/04_ROADMAP.md)
* [Arquitetura técnica](technical/05_ARCHITECTURE.md)

---

# Visão Geral

A documentação do TBH2 é organizada de forma modular.

Cada documento possui responsabilidade única.

Decisões compartilhadas devem ser definidas no documento proprietário do domínio e referenciadas por links relativos.

Os GDDs anteriores, briefings e relatórios de sprint são materiais históricos.

Eles podem ser consultados, mas não constituem a fonte principal de verdade após esta migração.

---

# Fonte de Verdade

A fonte de verdade do projeto é composta pelos documentos modulares listados neste índice.

Regra geral:

```text
Decisão de produto → documento de domínio
Fórmula numérica → Fórmulas de Balanceamento
Estrutura de dados → Modelo de Dados
Persistência → Sistema de Save
Arquitetura → Arquitetura Técnica
Planejamento → Roadmap
```

Evitar duplicar regras completas entre documentos.

Quando uma decisão afetar múltiplos domínios, o documento proprietário deve conter a regra principal e os demais devem apenas referenciar.

---

# Status dos Documentos

## Draft

Documento em proposta.

Pode conter ideias ainda não validadas.

---

## In Progress

Documento ativo.

Representa a direção atual do projeto, mas ainda pode sofrer ajustes.

---

## Approved

Documento validado.

Representa decisão aprovada e estável até nova revisão formal.

---

## Deprecated

Documento ou decisão substituída.

Permanece apenas para histórico.

---

# Estrutura da Documentação

## Core

Documentos centrais do jogo.

* [Visão](core/00_VISION.md)
* [Gameplay central](core/01_CORE_GAMEPLAY.md)
* [Progressão](core/02_PROGRESSION.md)
* [Combate](core/03_COMBAT.md)
* [Loot e economia](core/04_LOOT_ECONOMY.md)
* [UI e UX](core/05_UI_UX.md)

---

## Heróis

Documentos relacionados ao personagem principal, identidade de build e evolução do herói.

* [Sistema de herói](heroes/01_HERO_SYSTEM.md)
* [Classes](heroes/02_CLASSES.md)
* [Atributos](heroes/03_ATTRIBUTES.md)
* [Habilidades](heroes/04_SKILLS.md)
* [Raças](heroes/05_RACES.md)
* [Companheiros de grupo](heroes/06_PARTY_COMPANIONS.md)

---

## Monstros

Documentos relacionados aos inimigos, elites e chefes.

* [Sistema de monstros](monsters/01_MONSTER_SYSTEM.md)
* [Monstros comuns](monsters/02_COMMON_MONSTERS.md)
* [Monstros elite](monsters/03_ELITE_MONSTERS.md)
* [Chefes](monsters/04_BOSSES.md)

---

## Mapas

Documentos relacionados à campanha, mundo, atos, dificuldades e dungeons.

* [Estrutura do mundo](maps/01_WORLD_STRUCTURE.md)
* [Ato I](maps/02_ACT_I.md)
* [Ato II](maps/03_ACT_II.md)
* [Ato III](maps/04_ACT_III.md)
* [Dificuldades](maps/05_DIFFICULTIES.md)
* [Dungeons](maps/06_DUNGEONS.md)

---

## Itens

Documentos relacionados a equipamentos, raridades e itemização.

* [Sistema de itens](items/01_ITEM_SYSTEM.md)
* [Armas](items/02_WEAPONS.md)
* [Armaduras](items/03_ARMORS.md)
* [Acessórios](items/04_ACCESSORIES.md)
* [Raridades](items/05_RARITIES.md)

---

## Arte

Documentos relacionados à direção visual, worldbuilding e identidade estética.

* [Direção artística e worldbuilding](art/01_ART_DIRECTION_WORLDBUILDING.md)

---

## Taskbar

Documentos relacionados à identidade do TBH2 como companion de área de trabalho.

* [Identidade de Taskbar](taskbar/01_TASKBAR_IDENTITY.md)
* [Sistema de sessão](taskbar/02_SESSION_SYSTEM.md)
* [Sistema diário](taskbar/03_DAILY_SYSTEM.md)
* [Sistema de companion](taskbar/04_COMPANION_SYSTEM.md)

---

## Técnico

Documentos relacionados à implementação, persistência, arquitetura e balanceamento.

* [Sistema de save](technical/01_SAVE_SYSTEM.md)
* [Modelo de dados](technical/02_DATA_MODEL.md)
* [Fórmulas de balanceamento](technical/03_BALANCE_FORMULAS.md)
* [Roadmap](technical/04_ROADMAP.md)
* [Arquitetura técnica](technical/05_ARCHITECTURE.md)

---

## Histórico

Documentos históricos, GDDs antigos, briefings, relatórios de sprint e registros de execução.

* [Documentos anteriores](archive/README.md)

Materiais históricos não devem ser usados como fonte principal de implementação quando houver documento modular equivalente.

---

# Documentos Históricos Recomendados

Os seguintes documentos podem ser mantidos no histórico do projeto:

* Relatório da demo técnica jogável
* Sprint UX/Visual 01 — Exploração Viva
* Briefings enviados ao Codex
* GDDs anteriores
* Auditorias de versões antigas
* Relatórios de migração

Esses arquivos ajudam a entender a evolução do projeto, mas não substituem os documentos ativos.

---

# Regras de Manutenção

* Alterar primeiro o documento proprietário de cada decisão.
* Usar links relativos para dependências.
* Não copiar regras completas entre arquivos.
* Registrar decisões relevantes no histórico do documento.
* Não promover documento para `Approved` sem validação prática.
* Não iniciar implementação baseada em documento `Draft` sem confirmação.
* Não usar GDD antigo como fonte principal quando houver documento modular atualizado.
* Toda mudança persistente deve considerar save, migração e compatibilidade.
* Toda fórmula deve ser centralizada em `technical/03_BALANCE_FORMULAS.md`.
* Toda mudança estrutural deve respeitar `technical/05_ARCHITECTURE.md`.

---

# Convenções

## Idioma

Português.

---

## Formato

Markdown compatível com GitHub.

---

## Links

Usar links relativos.

Exemplo:

```md
[Progressão](core/02_PROGRESSION.md)
```

---

## Histórico de Alterações

Cada documento deve manter uma seção própria de histórico.

Formato recomendado:

```md
## Histórico de Alterações

- 2026-06-10: descrição objetiva da alteração.
```

---

## Títulos

Usar títulos claros e previsíveis.

Evitar nomes ambíguos.

---

# Fluxo de Atualização

## 1. Identificar o Domínio

Antes de alterar uma regra, identificar onde ela pertence.

Exemplos:

* dano físico pertence a Combate e Fórmulas;
* slots de equipamento pertencem a Sistema de Itens;
* campos persistidos pertencem ao Modelo de Dados;
* save e migração pertencem ao Sistema de Save;
* organização de fases pertence ao Roadmap.

---

## 2. Atualizar Documento Proprietário

A regra principal deve ser alterada no documento responsável.

---

## 3. Atualizar Referências

Documentos dependentes devem receber apenas referência ou resumo mínimo.

---

## 4. Registrar Histórico

Toda decisão relevante deve ser registrada no histórico do documento alterado.

---

## 5. Validar Impacto Técnico

Antes de implementar, verificar impacto em:

* save;
* modelo de dados;
* arquitetura;
* UI;
* balanceamento;
* testes.

---

# Prioridade Atual da Documentação

A prioridade atual é consolidar:

1. Core
2. Sistema de Save
3. Modelo de Dados
4. Fórmulas de Balanceamento
5. Arquitetura Técnica
6. Roadmap
7. Sistema de Itens
8. Sistema de Monstros
9. Estrutura do Mundo

Somente depois disso a documentação futura deve avançar para sistemas mais complexos como:

* dungeons;
* party companions;
* raças completas;
* habilidades avançadas;
* endgame;
* multiplayer.

---

# Dados

* Versão atual da arquitetura documental: 1.0
* Idioma principal: português
* Formato: Markdown compatível com GitHub
* Organização: modular por domínio
* Fonte principal: documentos ativos listados neste índice

---

# Pendências

* Definir responsáveis por domínio.
* Aprovar documentos Core.
* Aprovar Modelo de Dados.
* Aprovar Arquitetura Técnica.
* Aprovar Roadmap.
* Migrar decisões válidas dos GDDs históricos.
* Separar documentos históricos de documentos ativos.
* Criar índice do diretório `archive`.
* Validar links relativos no GitHub.
* Definir padrão de nomes para relatórios de sprint.

---

# Histórico de Alterações

* 2026-06-10: criada arquitetura modular inicial.
* 2026-06-10: adicionados raças, companheiros de grupo e dungeons ao índice.
* 2026-06-10: adicionada direção artística e worldbuilding.
* 2026-06-10: definidos status documentais.
* 2026-06-10: reforçada distinção entre documentação ativa e histórico.
