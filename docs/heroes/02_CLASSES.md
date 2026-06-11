# Classes

## Objetivo

Definir os arquétipos iniciais e seus pontos de integração com atributos,
habilidades e combate.

## Status

Planned - Fase 2

## Dependências

- [Sistema de herói](01_HERO_SYSTEM.md)
- [Atributos](03_ATTRIBUTES.md)
- [Habilidades](04_SKILLS.md)
- [Combate](../core/03_COMBAT.md)

## Arquétipos Iniciais

### Tank

Fantasia: resistência, proteção e estabilidade.

- atributos prioritários esperados: CON e STR;
- maior capacidade de sobreviver;
- habilidades futuras de mitigação e controle.

### Healer

Fantasia: sustentação e recuperação.

- atributo prioritário esperado: INT;
- cura e suporte automáticos;
- valor ampliado quando companheiros forem introduzidos.

### DPS

Fantasia: eliminar ameaças com rapidez.

- atributos prioritários esperados: STR, DEX ou INT conforme a build;
- maior pressão ofensiva;
- menor margem defensiva.

Tank, Healer e DPS são papéis mecânicos iniciais. Nomes de fantasia como
Guerreiro, Sacerdote ou Arqueiro são conteúdo posterior e não estão aprovados.

## Estrutura de Classe

Cada classe deve possuir:

- identificador estável;
- atributo primário;
- identidade visual;
- modificadores de crescimento;
- árvore de habilidades futura;
- progressão própria.

## Regras

- Classes são definições de conteúdo, não subclasses completas de `Hero`.
- Estratégias Agressivo, Balanceado e Defensivo continuam independentes.
- Toda classe deve completar o conteúdo solo.
- O Healer precisa ser funcional antes da introdução de companheiros.
- Árvores e habilidades pertencem à Fase 3.

## Pendências

- Definir nomes finais e identidade visual.
- Escolher atributos primários exatos.
- Prototipar uma diferença passiva simples por arquétipo.
- Validar os três arquétipos no modo solo.

## Histórico de Alterações

- 2026-06-10: arquétipos alinhados ao briefing de expansão.
- 2026-06-10: criado o template modular.
