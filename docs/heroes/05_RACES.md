# Raças

## Objetivo

Definir as opções de raça da criação de personagem e seus limites de integração
com atributos, classes e progressão.

## Status

Planned - Fase 2

## Dependências

- [Sistema de herói](01_HERO_SYSTEM.md)
- [Classes](02_CLASSES.md)
- [Atributos](03_ATTRIBUTES.md)
- [Roadmap](../technical/04_ROADMAP.md)

## Opções Planejadas

- Humano;
- Elfo;
- Anão;
- Meio-Orc.

Cada raça deve fornecer:

- um conjunto pequeno de bônus de atributos;
- uma passiva racial única;
- identidade visual reconhecível na janela compacta.

## Regras

- Raça e classe são escolhas independentes.
- Nenhuma raça pode impedir o uso de um arquétipo.
- Bônus raciais não devem substituir equipamentos ou progressão.
- Passivas entram apenas na Fase 3.
- A Fase 2 pode persistir a raça e aplicar bônus básicos antes das passivas.
- Saves anteriores recebem uma raça neutra ou escolha pendente sem perder dados.

## Dados Planejados

| Campo | Responsabilidade |
|---|---|
| `race_id` | Identificador estável para save e conteúdo |
| `name` | Nome apresentado |
| `attribute_modifiers` | Bônus pequenos de STR, DEX, INT e CON |
| `passive_id` | Referência futura à passiva racial |
| `visual_id` | Referência visual |

Valores numéricos ainda não estão aprovados.

## Pendências

- Definir a fantasia mecânica de cada raça.
- Decidir como saves existentes escolhem ou recebem uma raça.
- Validar bônus com todas as classes.

## Histórico de Alterações

- 2026-06-10: criado a partir do briefing de expansão de sistemas.
