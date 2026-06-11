# Sistema de Itens

## Objetivo

Definir o modelo compartilhado de itens, Poder, espaços de equipamento e
equipamento automático.

## Status

In Progress

## Dependências

- [Loot e economia](../core/04_LOOT_ECONOMY.md)
- [Atributos](../heroes/03_ATTRIBUTES.md)
- [Raridades](05_RARITIES.md)
- [Modelo de dados](../technical/02_DATA_MODEL.md)

## Estado Atual

A demo utiliza:

- `weapon`;
- `armor`;
- `accessory`;
- Poder para comparação;
- autoequipamento do item superior.

Esse modelo permanece válido até a expansão de equipamentos.

## Espaços Planejados

- Helm;
- Weapon;
- Weapon 2;
- Chest;
- Gloves;
- Belt;
- Boots;
- Ring 1;
- Ring 2;
- Amulet.

Os identificadores persistidos devem ser estáveis e diferentes dos nomes
localizados apresentados na UI.

## Poder e Atributos

Poder continua sendo o resumo principal de qualidade. Itens futuros podem
fornecer STR, DEX, INT, CON e estatísticas derivadas, sem tornar Poder a única
regra de decisão.

## Equipamento Automático

O autoequipamento deve:

- comparar itens do mesmo espaço;
- considerar Poder na primeira versão;
- respeitar configurações futuras do jogador;
- explicar quando e por que um item foi equipado;
- funcionar para herói e companheiros por meio do mesmo sistema.

## Regras

- A expansão dos dez espaços deve ocorrer em uma sprint própria.
- `Weapon 2` depende da definição de duas mãos e restrições de classe.
- Dois anéis são instâncias separadas do mesmo tipo de espaço.
- Novos espaços exigem migração dos saves e revisão da interface 5x4.
- Não adicionar afixos complexos antes da validação dos atributos primários.

## Pendências

- Definir compatibilidade de armas.
- Definir critérios de desempate do autoequipamento.
- Definir apresentação compacta dos dez espaços.
- Planejar migração de `armor` e `accessory` para espaços específicos.

## Histórico de Alterações

- 2026-06-10: espaços futuros registrados conforme o briefing.
- 2026-06-10: criado o template modular.
