# TBH2 - ROADMAP OFICIAL

## Status

In Progress

---

# Visão do Projeto

TBH2 (TaskBar Hero 2) é um Idle RPG Companion executado na lateral da área de trabalho.

O objetivo não é competir com RPGs tradicionais.

O objetivo é criar a sensação de acompanhar um aventureiro em uma jornada contínua enquanto o usuário utiliza o computador.

A fantasia principal do jogo é:

Explorar → Encontrar Inimigos → Evoluir → Encontrar Itens → Avançar Regiões → Repetir

---

# Pilar 01 - Exploração

O mundo deve parecer vivo.

O jogador deve sentir que o herói está viajando.

## Estado Atual

* Exploração implementada
* Parallax implementado
* Encontros implementados
* Combate implementado

## Próximas Melhorias

* Mais elementos ambientais
* Eventos visuais
* Melhorias de animação
* Variação de cenários
* Boss introductions

Status: Parcialmente Concluído

---

# Pilar 02 - Progressão

Este é atualmente o sistema mais importante do projeto.

O ritmo de progressão define toda a experiência do TBH2.

## Problema Atual

O jogador sobe de nível rápido demais.

Exemplo:

* Level 1 → 29 em poucos minutos

Isso não é compatível com a proposta de Idle RPG.

## Objetivo

Criar uma progressão que funcione por:

* horas
* dias
* semanas
* meses

---

# Estrutura de Progressão

## Tutorial

Level 1 - 10

Objetivo:

* apresentar sistemas
* ensinar o jogo
* gerar recompensas frequentes

Progressão rápida.

---

## Early Game

Level 11 - 20

Objetivo:

* consolidar mecânicas
* introduzir equipamentos

Progressão moderada.

---

## Mid Game

Level 21 - 50

Objetivo:

* criar decisões de build
* incentivar upgrades

Progressão lenta.

---

## Late Game

Level 51 - 100

Objetivo:

* longo prazo

Progressão lenta e consistente.

---

## Endgame

Level 100+

Objetivo:

* progressão infinita
* farm de equipamentos
* otimização de build

---

# Pilar 03 - Mapas

Os mapas não devem ser apenas números.

Cada mapa deve possuir identidade própria.

---

## Estrada Abandonada

Inimigos:

* Goblin
* Lobo

Tema:

* início da jornada

---

## Bosque dos Sussurros

Inimigos:

* Aranha
* Lobo Sombrio

Tema:

* floresta misteriosa

---

## Acampamento Saqueado

Inimigos:

* Bandido
* Mercenário

Tema:

* território hostil

---

## Cemitério da Vigília

Inimigos:

* Esqueleto
* Zumbi

Tema:

* mortos-vivos

---

## Fortaleza Esquecida

Boss:

* Capitão Ossonegro

Tema:

* encerramento do Ato I

---

# Estrutura dos Mapas

Mapas:

1 a 9

Função:

* Farm
* Progressão
* Equipamentos

Mapa 10

Função:

* Boss
* Fechamento do capítulo

---

# Sistema de Dificuldade

Cada ato deve possuir múltiplas dificuldades.

## Normal

* XP base
* Gold base
* Loot base

---

## Veterano

* XP aumentado
* Gold aumentado
* Loot aumentado

---

## Pesadelo

* Inimigos mais fortes
* Melhor loot

---

## Infernal

* Endgame

---

# Pilar 04 - Equipamentos

Próxima grande implementação.

Inspirado em:

* Diablo
* Path of Exile

## Slots

* Capacete

* Peitoral

* Luvas

* Cinto

* Botas

* Arma Principal

* Arma Secundária

* Anel

* Anel

* Amuleto

---

# Pilar 05 - Atributos

Todos os personagens possuem:

* STR
* DEX
* INT
* CON

Sem exceções.

---

## STR

* Dano físico
* Dano crítico

---

## DEX

* Velocidade de ataque
* Chance crítica
* Evasão

---

## INT

* Poder mágico
* Cura
* Redução de recarga

---

## CON

* Vida máxima
* Regeneração
* Resistência

---

# Pilar 06 - Classes

Implementar apenas após atributos.

## Guerreiro

Prioridade:

STR + CON

---

## Arqueiro

Prioridade:

DEX

---

## Mago

Prioridade:

INT

---

## Curandeiro

Prioridade:

INT + CON

---

# Pilar 07 - Habilidades

Implementar apenas após:

* Progressão
* Equipamentos
* Atributos
* Classes

Objetivo:

Criar escolhas reais.

---

# Ordem de Desenvolvimento

## Sprint Atual

Balanceamento

Objetivo:

* XP
* Níveis
* Progressão
* Dificuldades
* Bosses

---

## Sprint Seguinte

Equipamentos

Objetivo:

* slots completos
* raridades
* escalabilidade

---

## Próxima

Atributos

Objetivo:

* STR
* DEX
* INT
* CON

---

## Próxima

Classes

---

## Próxima

Habilidades

---

# Fora do Escopo Atual

Não implementar agora:

* Talentos
* Crafting
* Party System
* Multiplayer
* Pets
* Guildas
* PvP

Esses sistemas somente após a fundação principal estar validada.

---

# Meta da Versão 1.0

Ao deixar o TBH2 aberto durante um dia inteiro, o jogador deve sentir:

* progresso constante;
* descoberta de equipamentos;
* evolução do personagem;
* avanço de mapas;
* sensação de jornada contínua.

A experiência principal deve funcionar antes da expansão do conteúdo.
