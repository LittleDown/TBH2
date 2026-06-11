# Companheiros de Grupo

## Objetivo

Definir NPCs de apoio que complementam a composição de combate.

## Status

Planned - Fase 5

## Dependências

- [Classes](02_CLASSES.md)
- [Atributos](03_ATTRIBUTES.md)
- [Habilidades](04_SKILLS.md)
- [Dungeons](../maps/06_DUNGEONS.md)

## Visão Geral

O jogador poderá utilizar até três NPCs companheiros. Com o herói principal, o
grupo poderá alcançar quatro participantes.

Cada companheiro:

- acompanha o nível do jogador;
- possui identidade de classe ou função;
- utiliza equipamentos;
- complementa Tank, Healer ou DPS no grupo;
- atua automaticamente.

## Regras

- Companheiros não substituem o herói principal.
- Sincronizar nível não significa copiar todos os atributos.
- Equipamentos de companheiros devem reutilizar o sistema de itens.
- O jogador configura composição, não comandos por turno.
- A primeira versão deve funcionar localmente e sem requisitos online.

## Dados Planejados

- `companion_id`;
- nível sincronizado;
- classe ou função;
- equipamentos;
- estado de desbloqueio;
- prioridade de habilidades futura.

## Pendências

- Definir como companheiros são desbloqueados.
- Definir distribuição de loot entre herói e grupo.
- Definir apresentação compacta de quatro participantes.

## Histórico de Alterações

- 2026-06-10: criado a partir do briefing de expansão de sistemas.
