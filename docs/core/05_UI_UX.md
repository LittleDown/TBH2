# UI e UX

## Objetivo

Definir a filosofia visual, hierarquia de informações, estrutura de interface e experiência de uso do TBH2.

A interface deve permitir que o jogador acompanhe a jornada do aventureiro com atenção parcial, sem exigir interação constante.

O foco da UI não é o combate isolado.

O foco da UI é a jornada.

A interface deve responder à pergunta:

> "O jogador consegue entender o que está acontecendo com um olhar rápido?"

---

## Status

In Progress

---

## Dependências

* [Visão do projeto](00_VISION.md)
* [Gameplay central](01_CORE_GAMEPLAY.md)
* [Progressão](02_PROGRESSION.md)
* [Combate](03_COMBAT.md)
* [Loot e economia](04_LOOT_ECONOMY.md)
* [Sistema de itens](../items/01_ITEM_SYSTEM.md)
* [Identidade de Taskbar](../taskbar/01_TASKBAR_IDENTITY.md)
* [Sistema de companion](../taskbar/04_COMPANION_SYSTEM.md)
* [Direção artística e worldbuilding](../art/01_ART_DIRECTION_WORLDBUILDING.md)

---

# Escopo deste Documento

Este documento define:

* filosofia de UI;
* princípios de UX;
* hierarquia de informação;
* áreas principais da interface;
* comportamento visual dos estados do jogo;
* papel do feed de eventos;
* regras de legibilidade;
* regras para janela compacta;
* critérios de sucesso da experiência visual.

---

# Fora do Escopo

Este documento não deve definir:

* arte final;
* sprites finais;
* paleta definitiva;
* fórmulas de raridade;
* regras de loot;
* fórmulas de Power;
* fórmulas de Build Score;
* comportamento interno do Companion;
* implementação técnica dos widgets;
* arquitetura de código da interface.

Esses assuntos pertencem aos documentos proprietários de cada domínio.

---

# Visão Geral

A interface do TBH2 deve servir à jornada.

O jogador deve compreender rapidamente:

* onde está;
* o que está acontecendo;
* o estado do herói;
* o estado do inimigo;
* o que encontrou;
* o que conquistou;
* qual é o próximo objetivo.

A interface não deve competir com o mundo.

Ela deve apoiar a exploração.

O jogador deve sentir:

> "Meu aventureiro está vivendo uma jornada contínua."

---

# Filosofia da Interface

TBH2 é um Idle RPG Companion.

A interface deve funcionar com baixa frequência de interação.

O jogador não deve precisar observar cada segundo da tela para entender o progresso.

A interface deve permitir três formas de uso:

## 1. Observação Rápida

O jogador olha por poucos segundos e entende:

* mapa atual;
* estado atual;
* vida;
* progresso;
* evento recente.

---

## 2. Acompanhamento Passivo

O jogador deixa o jogo aberto enquanto trabalha, estuda ou usa o computador.

A UI deve transmitir movimento e progresso sem exigir resposta constante.

---

## 3. Interação Pontual

O jogador retorna para tomar decisões relevantes.

Exemplos:

* trocar equipamento;
* comparar item;
* revisar build;
* distribuir atributos;
* abrir inventário;
* verificar mapa;
* preparar chefe.

---

# Princípios de UX

## 1. Leitura Instantânea

As informações mais importantes devem ser compreendidas em poucos segundos.

Prioridade:

* estado atual da jornada;
* vida do herói;
* vida do inimigo, quando houver combate;
* mapa atual;
* progresso do mapa;
* recompensa recente.

---

## 2. Atenção Periférica

A interface deve funcionar mesmo quando o jogador observa rapidamente durante outras atividades.

O TBH2 não deve depender de leitura constante.

A UI deve comunicar por:

* movimento;
* ritmo;
* animação;
* contraste;
* ícones;
* feedback visual curto;
* mensagens breves.

---

## 3. Mundo Primeiro

A exploração deve ocupar o maior espaço visual possível.

Menus e painéis são ferramentas de apoio.

O mundo é o protagonista.

A tela não deve parecer uma planilha de números com uma animação decorativa.

A animação da jornada é parte central da experiência.

---

## 4. Progressão Visível

O jogador deve perceber crescimento constantemente.

Exemplos:

* novo nível;
* item encontrado;
* mapa avançado;
* chefe derrotado;
* nova região desbloqueada;
* dificuldade desbloqueada;
* melhoria de Power;
* melhoria de Build Score.

---

## 5. Baixo Ruído Visual

A interface deve evitar poluição.

A janela é compacta.

Efeitos visuais devem ser curtos, legíveis e úteis.

O excesso de partículas, brilho, textos ou ícones pode prejudicar a leitura.

---

# Formato da Janela

A interface deve funcionar adequadamente em:

```text
360x600
```

Essa dimensão deve ser tratada como referência principal.

A UI pode ser adaptável no futuro, mas a experiência base precisa funcionar nesse formato.

---

# Hierarquia de Informação

A ordem de leitura recomendada é:

1. mundo e estado da jornada;
2. herói;
3. inimigo ou ameaça atual;
4. vida;
5. mapa e progresso;
6. evento recente;
7. loot ou recompensa;
8. navegação;
9. detalhes secundários.

A tela principal não deve tentar exibir todos os detalhes do personagem ao mesmo tempo.

Detalhes devem ficar em painéis específicos.

---

# Estrutura Geral da Interface

A interface é dividida em quatro áreas principais.

---

## 1. Área de Exploração

Elemento principal da tela.

Responsável por exibir:

* cenário;
* herói;
* inimigos;
* chefes;
* animações;
* eventos ambientais;
* movimento do mundo;
* transição para combate.

O herói permanece em posição visual relativamente estável.

O mundo se move ao redor dele.

Objetivo:

Transmitir sensação de viagem contínua.

---

## 2. Painel de Informações

Exibe informações essenciais.

Exemplos:

* nível;
* vida;
* ouro;
* região;
* ato;
* mapa atual;
* progresso do mapa;
* dificuldade.

Essas informações devem ser compactas e legíveis.

Nem todas precisam ter o mesmo destaque.

---

## 3. Feed de Eventos

Responsável por registrar acontecimentos recentes.

Exemplos:

* item encontrado;
* nível obtido;
* chefe derrotado;
* nova região desbloqueada;
* dificuldade desbloqueada;
* evento especial;
* derrota do herói.

Objetivo:

Transformar progresso em narrativa curta.

O feed não deve virar log técnico.

---

## 4. Navegação Principal

Permite acesso aos sistemas do personagem.

Botões previstos:

* Hero;
* Inventory;
* Skills;
* Map.

A navegação deve ser simples, previsível e consistente.

---

# Tela Principal

A tela principal deve priorizar exploração.

Elementos visíveis:

* cenário;
* herói;
* inimigo, quando houver;
* progresso do mapa;
* vida do herói;
* vida do inimigo, quando houver;
* informações básicas;
* evento recente.

O jogador deve compreender a situação atual sem abrir menus.

---

# Estados Visuais da Jornada

A interface deve comunicar claramente o estado atual do loop.

---

## Exploração

O mundo está em movimento.

Sinais visuais:

* herói caminhando;
* parallax ativo;
* cenário fluindo;
* eventos ambientais sutis;
* ausência de ameaça imediata.

Sensação desejada:

> "A jornada continua."

---

## Encontro

Um inimigo aparece.

Sinais visuais:

* cenário desacelera;
* inimigo entra em cena;
* herói muda postura;
* atenção se desloca para o centro da ação.

Sensação desejada:

> "Algo interrompeu a viagem."

---

## Combate

Herói e inimigo lutam automaticamente.

Sinais visuais:

* cenário parado ou quase parado;
* animações de ataque;
* dano visível;
* barras de vida relevantes;
* efeitos curtos.

Sensação desejada:

> "Meu herói está enfrentando um desafio."

---

## Vitória

O inimigo é derrotado.

Sinais visuais:

* animação de vitória;
* queda ou desaparecimento do inimigo;
* recompensa exibida;
* feed atualizado;
* retorno gradual à exploração.

Sensação desejada:

> "Avancei."

---

## Derrota

O herói é derrotado.

Sinais visuais:

* feedback claro de falha;
* mensagem curta;
* retorno a estado seguro;
* indicação de que a build precisa melhorar.

Sensação desejada:

> "Ainda não estou pronto."

---

# Painel Hero

Responsável pela visualização do personagem.

Deve exibir:

* sprite ampliado;
* nível;
* vida;
* atributos principais;
* equipamentos;
* Power;
* Build Score;
* classe futura;
* habilidades futuras.

Objetivo:

Mostrar claramente a evolução do personagem.

O painel Hero não deve competir com a tela principal.

Ele é uma tela de consulta e decisão.

---

# Equipamentos na Interface

Os equipamentos devem ser visualmente organizados ao redor ou próximos ao personagem.

Slots planejados:

```text
helmet
weapon
offhand
chest
gloves
belt
boots
ring_1
ring_2
amulet
```

A UI deve permitir leitura rápida de:

* slot ocupado;
* raridade;
* item equipado;
* possível upgrade;
* item favorito ou bloqueado.

Detalhes completos pertencem ao Sistema de Itens.

---

# Inventário

Responsável pelo gerenciamento de itens.

Deve permitir:

* visualização rápida;
* comparação;
* identificação de upgrades;
* filtro por tipo;
* filtro por raridade;
* proteção de itens favoritos;
* venda ou descarte futuro.

Categorias previstas:

* Armas;
* Armaduras;
* Acessórios;
* Consumíveis futuros;
* Itens especiais futuros.

O inventário deve evitar microgerenciamento excessivo.

---

# Comparação de Itens

A comparação deve ajudar o jogador a decidir rapidamente.

Informações importantes:

* item atual;
* novo item;
* diferença de Power;
* diferença de Build Score;
* raridade;
* atributos principais;
* tags relevantes;
* alerta se quebrar sinergia;
* alerta se substituir item favorito.

A comparação não deve depender apenas de números brutos.

Build Score deve ajudar a indicar valor real para a build atual.

---

# Feed de Loot

Todo loot importante deve possuir destaque visual.

Exemplos:

* item raro encontrado;
* item épico encontrado;
* item lendário encontrado;
* novo item com Build Score superior;
* item de conjunto futuro;
* item mítico futuro.

O objetivo é reforçar a sensação de recompensa.

Loot comum pode aparecer de forma discreta.

Loot raro deve gerar momento perceptível.

---

# Feedback Visual

A interface deve comunicar informações sem depender apenas de texto.

Exemplos:

* parallax comunica exploração;
* desaceleração comunica encontro;
* animações comunicam combate;
* brilho comunica raridade;
* impacto comunica dano;
* queda do inimigo comunica vitória;
* mudança de ritmo comunica transição;
* destaque comunica recompensa.

Texto deve complementar o feedback visual, não substituir tudo.

---

# Exploração Viva

A exploração deve parecer contínua.

Elementos planejados:

* múltiplas camadas de parallax;
* clima;
* objetos decorativos;
* ruínas;
* animais;
* vegetação;
* vestígios narrativos;
* eventos ambientais.

Esses elementos existem para enriquecer a jornada.

Eles não possuem função mecânica obrigatória.

Eventos ambientais devem ser silenciosos e não exigir ação.

---

# Feed de Eventos

O feed de eventos deve contar a história curta da jornada.

Bons exemplos:

* `Lobo Cinzento derrotado.`
* `Você encontrou Espada Rara.`
* `Nível 12 alcançado.`
* `Mapa concluído: Bosque dos Sussurros.`
* `Chefe derrotado: Senhor dos Ossos.`

Evitar excesso de mensagens técnicas.

Evitar spam de cada cálculo interno.

O feed deve registrar eventos relevantes, não todos os detalhes do sistema.

---

# Companion na Interface

O Companion pode aparecer como presença narrativa curta.

Função:

* comentar eventos importantes;
* reforçar sensação de companhia;
* reagir a marcos;
* trazer personalidade ao herói.

Limites:

* não virar chatbot;
* não ocupar espaço principal;
* não interromper o fluxo;
* não substituir o feed de eventos;
* não comentar eventos irrelevantes em excesso.

Detalhes pertencem ao Sistema de Companion.

---

# Acessibilidade

A interface deve permanecer legível em janelas pequenas.

Objetivos:

* alto contraste;
* fontes legíveis;
* ícones reconhecíveis;
* informações hierarquizadas;
* feedback visual curto;
* estados distinguíveis sem depender apenas de cor.

A informação nunca deve depender apenas de cor.

Exemplos:

* raridade deve usar cor e ícone ou moldura;
* dano crítico deve usar cor e texto curto;
* derrota deve usar animação e mensagem;
* bloqueio deve usar ícone e texto.

---

# Regras de Legibilidade

* Evitar partículas sobre textos.
* Evitar efeitos sobre barras de vida.
* Evitar excesso de números simultâneos.
* Priorizar uma mensagem importante por vez.
* Manter contraste entre ator, inimigo e cenário.
* Usar animações curtas.
* Não ocultar o herói com efeitos.
* Não ocultar loot importante no feed.

---

# Relação com Taskbar

A interface deve funcionar como companion lateral.

Ela deve ser:

* compacta;
* discreta;
* persistente;
* legível;
* não invasiva;
* compreensível com olhares rápidos.

Não deve usar notificações agressivas.

Não deve capturar atenção constantemente.

Não deve atrapalhar o uso normal do computador.

---

# Relação com Arte

A direção artística define a identidade visual.

A UI deve respeitar:

* tom visual do mundo;
* legibilidade dos sprites;
* contraste entre planos;
* diferenciação entre regiões;
* leitura clara em escala pequena.

A UI não deve exigir arte excessivamente detalhada que fique ilegível em 360x600.

---

# Relação com Combate

O combate deve ser compreensível visualmente.

A UI deve mostrar:

* quem está atacando;
* quem recebeu dano;
* vida restante;
* vitória;
* derrota;
* habilidade futura usada;
* evento crítico relevante.

O combate não deve monopolizar toda a tela.

Ele é um evento dentro da jornada.

---

# Relação com Progressão

A UI deve tornar a progressão visível.

Deve comunicar:

* nível;
* XP;
* progresso de mapa;
* avanço de ato;
* desbloqueios;
* novos itens;
* melhorias de build;
* chefes derrotados.

A progressão deve ser percebida sem exigir navegação profunda.

---

# Relação com Itens

A UI deve permitir que o jogador identifique upgrades rapidamente.

Deve comunicar:

* raridade;
* slot;
* Power;
* Build Score;
* diferença em relação ao item equipado;
* sinergias relevantes;
* item favorito ou bloqueado.

Detalhes de itemização pertencem ao Sistema de Itens.

---

# Critérios de Sucesso

A UI/UX será considerada saudável quando:

* o jogador entende o estado atual com um olhar rápido;
* o mundo continua sendo o foco visual;
* a exploração parece contínua;
* o combate é claro sem exigir atenção total;
* loot importante é percebido;
* upgrades são fáceis de identificar;
* o feed conta a jornada sem virar poluição;
* menus não sufocam a tela principal;
* a interface funciona em 360x600;
* a experiência permanece discreta ao lado de outras aplicações.

---

# Regras

* O mundo possui prioridade sobre menus.
* A exploração ocupa a maior área da interface.
* O combate não deve monopolizar a tela.
* Todo painel deve possuir propósito claro.
* O jogador deve identificar upgrades rapidamente.
* O feed de eventos deve contar a história da jornada.
* A interface deve funcionar adequadamente em 360x600.
* Informações não devem depender apenas de cor.
* Eventos ambientais não devem exigir ação.
* O Companion não deve virar chatbot.
* A UI deve reforçar a fantasia de jornada contínua.
* Menos informação clara é melhor que muita informação ilegível.

---

# Dados

Reservado para dimensões, estados e componentes.

Dados técnicos, widgets finais e implementação pertencem à arquitetura e ao código.

---

# Pendências

* Produzir wireframes.
* Definir layout definitivo da tela principal.
* Definir layout do Hero Panel.
* Definir layout do Inventário.
* Definir layout do Map Panel.
* Definir sistema de comparação de itens.
* Definir apresentação visual das raridades.
* Definir comportamento do feed de eventos.
* Definir estados visuais mínimos.
* Validar legibilidade em 360x600.
* Validar contraste entre cenário, herói, inimigo e HUD.
* Validar densidade visual durante combate.
* Validar destaque de loot raro.
* Validar navegação entre Hero, Inventory, Skills e Map.

---

# Histórico de Alterações

* 2026-06-10: filosofia de Companion incorporada.
* 2026-06-10: exploração definida como elemento principal da interface.
* 2026-06-10: introduzidos Hero Panel, Inventário e Feed de Eventos.
* 2026-06-10: reorganização completa do sistema de UI e UX.
* 2026-06-10: documento reestruturado para separar UI, arte, itens, companion e implementação.
