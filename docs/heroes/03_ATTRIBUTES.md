# Atributos

## Objetivo

Definir atributos primários e suas responsabilidades antes da aprovação de
fórmulas numéricas.

## Status

Planned - Fase 2

## Dependências

- [Sistema de herói](01_HERO_SYSTEM.md)
- [Classes](02_CLASSES.md)
- [Combate](../core/03_COMBAT.md)
- [Fórmulas](../technical/03_BALANCE_FORMULAS.md)

## Atributos Primários

### STR - Strength

Converte-se futuramente em:

- dano físico;
- dano crítico físico.

### DEX - Dexterity

Converte-se futuramente em:

- velocidade de ataque;
- chance crítica;
- evasão.

### INT - Intellect

Converte-se futuramente em:

- dano mágico;
- redução de recarga;
- amplificação de cura.

### CON - Constitution

Converte-se futuramente em:

- vida máxima;
- regeneração de vida;
- redução de controle.

## Ordem de Composição

Direção planejada:

`base + nível + raça + classe + equipamento → valores efetivos`

As conversões exatas devem ser centralizadas no sistema de atributos e no
documento de fórmulas.

## Regras

- Atributos primários são persistidos; valores derivados são recalculáveis.
- Nenhuma conversão numérica entra sem cenários de teste.
- Um atributo pode apoiar múltiplas builds, mas deve manter identidade clara.
- Dano crítico, cura e redução de recarga só produzem efeito quando os sistemas
  correspondentes existirem.
- A UI compacta deve priorizar os quatro atributos e resumir derivados.

## Pendências

- Definir valores base e crescimento por nível.
- Definir arredondamento e limites.
- Decidir se pontos são automáticos ou distribuídos pelo jogador.
- Validar interação com raça, classe e equipamento.

## Histórico de Alterações

- 2026-06-10: STR, DEX, INT e CON definidos conforme o briefing.
- 2026-06-10: criado o template modular.
- 2026-06-11: removida estratégia manual da ordem de composição.
