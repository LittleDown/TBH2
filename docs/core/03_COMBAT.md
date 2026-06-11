# Combate

## Objetivo

Definir o combate automático, estratégias e evolução futura das categorias de
dano e defesa.

## Status

In Progress

## Dependências

- [Gameplay central](01_CORE_GAMEPLAY.md)
- [Atributos](../heroes/03_ATTRIBUTES.md)
- [Habilidades](../heroes/04_SKILLS.md)
- [Sistema de monstros](../monsters/01_MONSTER_SYSTEM.md)
- [Fórmulas](../technical/03_BALANCE_FORMULAS.md)

## Combate Atual

A demo alterna ataques automáticos entre herói e inimigo. Ataque, defesa,
estratégias, vitória, derrota e recompensa formam o núcleo já jogável.

As estratégias Agressivo, Balanceado e Defensivo modificam atributos efetivos sem
interromper o encontro.

## Combate Futuro

O combate continuará automático. A expansão planejada adiciona:

- habilidades em autocast;
- ativação e desativação individual;
- prioridade configurável;
- cast manual opcional somente após validação do autocast.

## Categorias de Dano

- físico: mitigado principalmente por armor;
- mágico: mitigado principalmente por spell armor;
- puro: ignora mitigações comuns, sujeito a regras específicas.

## Categorias Defensivas

- armor;
- spell armor;
- evasion;
- parry;
- redução de controle.

A ordem de resolução ainda não está aprovada. Ela deve definir acerto, evasão,
parry, crítico, categoria de dano, mitigação e aplicação final.

## Regras

- A Fase 1 continua usando o cálculo atual de ataque menos defesa.
- Categorias avançadas entram somente na Fase 4.
- Dano puro deve ser raro e claramente comunicado.
- Evasion e parry precisam de limites para evitar longas sequências sem dano.
- Eventos devem informar categoria e resultado sem acoplar regras à UI.
- Toda nova defesa precisa de fonte, contrajogo e feedback visual.

## Pendências

- Definir ordem completa de resolução.
- Definir fórmulas de armor e spell armor.
- Definir limites de evasão, parry e crítico.
- Definir representação compacta de cura e controle.

## Histórico de Alterações

- 2026-06-10: categorias futuras de dano e defesa registradas.
- 2026-06-10: criado o template modular.
