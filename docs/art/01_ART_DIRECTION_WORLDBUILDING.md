# Direção Artística e Worldbuilding

## Objetivo

Transformar a exploração em protagonista visual. O cenário deve comunicar que
existe um mundo além do combate e contar pequenas histórias mesmo sem diálogo.

## Status

In Progress

## Dependências

- [UI e UX](../core/05_UI_UX.md)
- [Estrutura do mundo](../maps/01_WORLD_STRUCTURE.md)
- [Ato I](../maps/02_ACT_I.md)
- [Sprint Exploração Viva](../EXPLORACAO_VIVA_SPRINT.md)

## Pilares Visuais

- dark fantasy medieval;
- atmosfera de aventura e descoberta;
- cores naturais e pouco saturadas;
- silhuetas legíveis na janela compacta;
- riqueza de detalhes sem competir com herói, inimigo ou HUD;
- profundidade construída por camadas e movimento.

As referências de atmosfera incluem RPGs de fantasia sombria e pixel art
clássicos. Nenhum asset deve copiar diretamente conteúdo de outra obra.

## Estrutura Modular

Cada cenário é composto por módulos independentes:

1. fundo: céu, montanhas, estruturas distantes;
2. ambiente: árvores, ruínas, cercas e arquitetura;
3. primeiro plano: pedras, vegetação, placas e vestígios;
4. eventos ambientais: partículas ou criaturas sem efeito de gameplay.

Os módulos devem ser reutilizados com espaçamento, variação e wrapping. Não gerar
mapas completos quando um conjunto de peças resolve o mesmo problema.

## Estrada Abandonada

Sensação:

- início da jornada;
- região relativamente segura;
- ruínas de uma rota antiga;
- vegetação retomando o espaço;
- sinais discretos de conflitos passados.

Paleta:

- céu cinza azulado;
- vegetação verde-musgo;
- terra ocre;
- madeira envelhecida;
- pedra fria;
- vermelho escuro reservado para vestígios e bandeiras.

Módulos oficiais iniciais:

- três árvores de estrada;
- duas formações de pedra;
- placa quebrada;
- vegetação;
- fogueira abandonada;
- espada fincada;
- carroça destruída;
- bandeira rasgada;
- rastros de carroça e pegadas.

## Suspense Ambiental

Vestígios aparecem espaçados e não acionam gameplay:

- rastros atravessando a estrada;
- fogueira fria;
- arma abandonada;
- carroça destruída;
- bandeira rasgada.

O objetivo é sugerir acontecimentos fora da tela sem explicar tudo ao jogador.
Esses elementos não são marcadores de missão e não devem se repetir com
frequência suficiente para parecer decoração comum.

## Eventos Ambientais

Eventos leves durante exploração:

- pequenos grupos de corvos;
- folhas carregadas pelo vento;
- poeira rasteira.

Eles não concedem recompensas, não interrompem a jornada e não aparecem como
eventos de combate. Futuras regiões podem usar névoa, insetos luminosos ou cinzas
com o mesmo contrato visual.

## Briefs dos Próximos Mapas

### Bosque dos Sussurros

Sensação: algo observa o aventureiro.

- árvores antigas;
- raízes expostas;
- névoa;
- ruínas parcialmente ocultas;
- luz mais escura e recortada.

### Acampamento Saqueado

Sensação: uma tragédia aconteceu recentemente.

- tendas destruídas;
- fogueiras apagadas;
- carroças quebradas;
- armas abandonadas;
- sinais de retirada apressada.

### Cemitério da Vigília

Sensação: perigo crescente.

- lápides e cruzes antigas;
- árvores secas;
- névoa constante;
- muros e capelas em ruínas;
- vegetação pálida.

## Geração Assistida de Assets

- gerar peças isoladas, não mapas completos;
- usar fundo uniforme removível ou transparência validada;
- manter perspectiva lateral consistente;
- evitar texto, personagens, monstros e UI;
- recortar cada peça e validar bordas, alpha e legibilidade;
- salvar somente assets finais usados pelo projeto;
- registrar prompt, ferramenta e limitações junto ao pacote.

## Roadmap Visual

1. Estrada Abandonada completa.
2. Bosque dos Sussurros.
3. Acampamento Saqueado.
4. Cemitério da Vigília.
5. Biblioteca compartilhada de eventos ambientais.

## Critério de Sucesso

Ao observar a exploração sem combate, o jogador deve reconhecer o mapa, perceber
profundidade e imaginar acontecimentos fora da tela.

## Histórico de Alterações

- 2026-06-10: direção consolidada e primeiro kit modular integrado.
