# Modelo de Dados

## Objetivo

Definir entidades, relações e contratos de dados do projeto.

## Status

Draft

## Dependências

- [Sistema de save](01_SAVE_SYSTEM.md)
- [Sistema de herói](../heroes/01_HERO_SYSTEM.md)
- [Sistema de monstros](../monsters/01_MONSTER_SYSTEM.md)
- [Sistema de itens](../items/01_ITEM_SYSTEM.md)
- [Estrutura do mundo](../maps/01_WORLD_STRUCTURE.md)
- [Arquitetura técnica](05_ARCHITECTURE.md)

## Visão Geral

<!-- Definir convenções de identidade, versão e referências. -->

## Estrutura

### Hero

Campos atuais incluem identidade, progressão, vida, combate, estratégia,
equipamentos e estatísticas. Na Fase 2 serão adicionados:

- `race_id`;
- `class_id`;
- atributos primários STR, DEX, INT e CON.

Os identificadores devem possuir defaults ou migração para saves existentes.

### RaceDefinition

Conteúdo não persistente com identificador, bônus de atributos, passiva futura e
referência visual. O save armazena apenas `race_id`.

### ClassDefinition

Conteúdo não persistente com identificador, função, atributo primário,
crescimento e referências futuras de habilidades. O save armazena `class_id`.

### CompanionState

Estado persistente futuro para NPCs desbloqueados, nível sincronizado,
equipamentos e configuração de grupo.

### Monster

<!-- Campos, tipos, invariantes e relações. -->

### Item

<!-- Campos, tipos, invariantes e relações. -->

### Map

<!-- Campos, tipos, invariantes e relações. -->

### DungeonRun

Estado futuro e opcional de uma execução: dungeon, andar atual, chefes concluídos,
participantes e recompensas pendentes. Sua persistência ainda depende da decisão
sobre retomada de runs.

### SaveData

<!-- Campos, versão e agregados persistidos. -->

## Regras

<!-- Definir compatibilidade e propriedade dos dados. -->

## Dados

<!-- Reservado para tabelas ou diagramas futuros. -->

## Pendências

- Definir defaults de raça, classe e atributos para migração.
- Decidir se `DungeonRun` faz parte do save.
- Definir propriedade dos equipamentos de companheiros.

## Histórico de Alterações

- 2026-06-10: entidades futuras da expansão registradas.
- 2026-06-10: criado o template modular.
