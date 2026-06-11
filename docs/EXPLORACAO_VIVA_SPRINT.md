# Sprint UX/Visual 01 - Exploração Viva

## Objetivo

Fazer a Estrada Abandonada transmitir uma jornada contínua sem alterar combate,
XP, ouro, loot, equipamentos, mapas ou save.

## Implementação

- herói fixo próximo a 30% da largura da cena;
- caminhada contínua durante exploração;
- pose idle assim que o encontro começa;
- entrada do inimigo pela direita;
- desaceleração do mundo de 100% a 0% em 0,75 segundo;
- cenário parado durante combate e recompensa;
- aceleração de 0% a 100% ao retornar à exploração;
- parallax em três camadas:
  - fundo a 20%;
  - ambiente a 50%;
  - primeiro plano a 100%;
- elementos decorativos determinísticos e reutilizados por wrapping;
- montanhas e castelo distante;
- árvores e cercas;
- pedras, vegetação e placas.

## Escopo

A composição completa de três camadas foi aplicada inicialmente à Estrada
Abandonada. Os demais mapas preservam seus ambientes anteriores e a camada móvel
simples até receberem sprints visuais próprias.

## Validação

- testes unitários para desaceleração, parada e retomada;
- ciclo completo validado pelo `after()` do Tkinter;
- inspeção visual em exploração, encontro, combate e retorno;
- nenhuma alteração em fórmulas ou sistemas de RPG.

## Limitações

- decoração desenhada com placeholders do Canvas;
- ausência de sprites próprios para árvores, pedras e placas;
- demais mapas ainda não usam o parallax de três camadas;
- não há transição climática, iluminação dinâmica ou áudio ambiente.

## Próxima Sprint Visual

Criar um kit de elementos por bioma e aplicar o mesmo contrato de camadas aos
mapas seguintes, sem duplicar regras no controlador da jornada.
