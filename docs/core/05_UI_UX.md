# UI e UX

## Objetivo

Definir a filosofia visual, estrutura da interface, hierarquia de informações e experiência de uso do TBH2.

A interface deve permitir que o jogador acompanhe a jornada do aventureiro com atenção parcial, sem exigir interação constante.

O foco da UI não é o combate.

O foco da UI é a jornada.

---

## Status

Draft

---

## Dependências

* Gameplay Central
* Visão do Projeto
* Progressão
* Sistema de Itens
* Companion System
* Direção Artística

---

# Filosofia da Interface

A interface deve servir à jornada.

O jogador deve compreender rapidamente:

* onde está;
* o que está acontecendo;
* o que encontrou;
* o que conquistou;
* qual é seu próximo objetivo.

A interface não deve competir com o mundo.

Ela deve apoiar a exploração.

O jogador deve sentir:

> "Meu aventureiro está vivendo uma jornada contínua."

---

# Princípios de UX

## Leitura Instantânea

As informações mais importantes devem ser compreendidas em poucos segundos.

O jogador deve conseguir identificar rapidamente:

* mapa atual;
* progresso do mapa;
* nível;
* vida;
* eventos recentes.

---

## Atenção Periférica

O jogo deve continuar compreensível mesmo quando observado rapidamente durante outras atividades.

A interface deve funcionar como um Companion.

---

## Progressão Visível

O jogador deve perceber crescimento constantemente.

Exemplos:

* novos equipamentos;
* níveis;
* regiões;
* chefes derrotados;
* dificuldades desbloqueadas.

---

## Mundo Primeiro

A exploração deve ocupar o maior espaço visual possível.

Menus e painéis são ferramentas de apoio.

O mundo é o protagonista.

---

# Estrutura Geral

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
* eventos ambientais.

O herói permanece visualmente estável enquanto o mundo se move ao redor dele.

Objetivo:

Transmitir sensação de viagem contínua.

---

## 2. Painel de Informações

Exibe informações essenciais.

Exemplos:

* nível;
* ouro;
* região;
* mapa atual;
* progresso do ato;
* dificuldade.

Essas informações devem permanecer visíveis o tempo todo.

---

## 3. Feed de Eventos

Responsável por registrar acontecimentos recentes.

Exemplos:

* item encontrado;
* nível obtido;
* chefe derrotado;
* nova região desbloqueada;
* evento especial.

Objetivo:

Transformar progresso em narrativa.

---

## 4. Navegação Principal

Permite acesso aos sistemas do personagem.

Botões previstos:

* Hero
* Inventory
* Skills
* Map

A navegação deve ser simples e consistente.

---

# Tela Principal

A tela principal deve priorizar exploração.

Elementos visíveis:

* cenário;
* herói;
* inimigos;
* progresso do mapa;
* informações básicas.

O jogador deve compreender a situação atual sem abrir menus.

---

# Painel Hero

Responsável pela visualização do personagem.

Deve exibir:

* sprite ampliado;
* equipamentos;
* atributos;
* habilidades;
* Power Score;
* Build Score.

Objetivo:

Mostrar claramente a evolução do personagem.

---

# Estrutura de Equipamentos

Espaços planejados:

* Helm
* Weapon
* Weapon 2
* Chest
* Gloves
* Belt
* Boots
* Ring 1
* Ring 2
* Amulet

Os equipamentos devem ser visualmente organizados ao redor do personagem.

---

# Inventário

Responsável pelo gerenciamento de itens.

Deve permitir:

* visualização rápida;
* filtros;
* comparação;
* identificação de upgrades.

Categorias previstas:

* Armas
* Armaduras
* Acessórios
* Consumíveis
* Quest Items

---

# Feed de Loot

Todo loot importante deve possuir destaque visual.

Exemplos:

* Item Raro encontrado
* Item Lendário encontrado
* Novo conjunto encontrado

O objetivo é reforçar a sensação de recompensa.

---

# Feedback Visual

A interface deve comunicar informações sem depender de texto.

Exemplos:

* parallax comunica exploração;
* desaceleração comunica encontro;
* animações comunicam combate;
* brilho comunica raridade;
* efeitos comunicam progressão.

---

# Exploração Viva

A exploração deve parecer contínua.

Elementos planejados:

* múltiplas camadas de parallax;
* clima;
* objetos decorativos;
* ruínas;
* animais;
* eventos ambientais.

Esses elementos existem para enriquecer a jornada.

Não possuem função mecânica obrigatória.

---

# Acessibilidade

A interface deve permanecer legível em janelas pequenas.

Objetivos:

* alto contraste;
* fontes legíveis;
* ícones reconhecíveis;
* informações hierarquizadas.

A informação nunca deve depender apenas de cor.

---

# Regras

* O mundo possui prioridade sobre menus.
* A exploração ocupa a maior área da interface.
* O combate não deve monopolizar a tela.
* Todo painel deve possuir propósito claro.
* O jogador deve identificar upgrades rapidamente.
* O feed de eventos deve contar a história da jornada.
* A interface deve funcionar adequadamente em 360x600.

---

# Pendências

* Produzir wireframes.
* Definir layout definitivo da tela principal.
* Definir layout do Hero Panel.
* Definir layout do Inventário.
* Definir sistema de comparação de itens.
* Definir apresentação visual das raridades.
* Validar legibilidade em resolução reduzida.

---

# Histórico de Alterações

* 2026-06-10: filosofia de Companion incorporada.
* 2026-06-10: exploração definida como elemento principal da interface.
* 2026-06-10: introduzidos Hero Panel, Inventário e Feed de Eventos.
* 2026-06-10: reorganização completa do sistema de UI e UX.
