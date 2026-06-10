# Documentação do TBH2

## Objetivo

Servir como ponto central da documentação modular de game design, conteúdo,
balanceamento e implementação do TBH2.

## Status

In Progress

## Dependências

- [Visão do projeto](core/00_VISION.md)
- [Roadmap](technical/04_ROADMAP.md)

## Visão Geral

Cada documento possui responsabilidade única. Decisões compartilhadas devem ser
definidas no domínio proprietário e referenciadas por links relativos.

Os GDDs anteriores são material histórico e não constituem a fonte principal de
verdade após esta migração.

## Estrutura

### Core

- [Visão](core/00_VISION.md)
- [Gameplay central](core/01_CORE_GAMEPLAY.md)
- [Progressão](core/02_PROGRESSION.md)
- [Combate](core/03_COMBAT.md)
- [Loot e economia](core/04_LOOT_ECONOMY.md)
- [UI e UX](core/05_UI_UX.md)

### Heróis

- [Sistema de herói](heroes/01_HERO_SYSTEM.md)
- [Classes](heroes/02_CLASSES.md)
- [Atributos](heroes/03_ATTRIBUTES.md)
- [Habilidades](heroes/04_SKILLS.md)

### Monstros

- [Sistema de monstros](monsters/01_MONSTER_SYSTEM.md)
- [Monstros comuns](monsters/02_COMMON_MONSTERS.md)
- [Monstros elite](monsters/03_ELITE_MONSTERS.md)
- [Chefes](monsters/04_BOSSES.md)

### Mapas

- [Estrutura do mundo](maps/01_WORLD_STRUCTURE.md)
- [Ato I](maps/02_ACT_I.md)
- [Ato II](maps/03_ACT_II.md)
- [Ato III](maps/04_ACT_III.md)
- [Dificuldades](maps/05_DIFFICULTIES.md)

### Itens

- [Sistema de itens](items/01_ITEM_SYSTEM.md)
- [Armas](items/02_WEAPONS.md)
- [Armaduras](items/03_ARMORS.md)
- [Acessórios](items/04_ACCESSORIES.md)
- [Raridades](items/05_RARITIES.md)

### Taskbar

- [Identidade de Taskbar](taskbar/01_TASKBAR_IDENTITY.md)
- [Sistema de sessão](taskbar/02_SESSION_SYSTEM.md)
- [Sistema diário](taskbar/03_DAILY_SYSTEM.md)
- [Sistema de companion](taskbar/04_COMPANION_SYSTEM.md)

### Técnico

- [Sistema de save](technical/01_SAVE_SYSTEM.md)
- [Modelo de dados](technical/02_DATA_MODEL.md)
- [Fórmulas de balanceamento](technical/03_BALANCE_FORMULAS.md)
- [Roadmap](technical/04_ROADMAP.md)
- [Arquitetura técnica](technical/05_ARCHITECTURE.md)

### Histórico

- [Documentos anteriores](archive/README.md)

## Regras

- Alterar primeiro o documento proprietário de cada decisão.
- Usar links relativos para dependências.
- Não copiar regras completas entre arquivos.
- Registrar decisões relevantes no histórico do documento.
- Tratar `Draft` como proposta, `In Progress` como definição ativa e `Approved`
  como decisão validada.

## Dados

- Versão atual da arquitetura documental: 1.0.
- Idioma principal: português.
- Formato: Markdown compatível com GitHub.

## Pendências

- Definir responsáveis por domínio.
- Aprovar documentos Core.
- Migrar decisões válidas dos GDDs históricos.

## Histórico de Alterações

- 2026-06-10: criada a arquitetura modular inicial.
