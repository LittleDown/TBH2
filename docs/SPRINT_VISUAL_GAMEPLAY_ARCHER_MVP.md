# Sprint Visual-Gameplay - Arqueiro MVP

## Objetivo

Implementar o Arqueiro como variacao visual e funcional minima do heroi,
validando caminhada, postura de combate e ataque automatico a distancia sem
criar o sistema completo de classes.

## Status

Implemented

## Dependencias

* [Visao](core/00_VISION.md)
* [Gameplay Central](core/01_CORE_GAMEPLAY.md)
* [Combate](core/03_COMBAT.md)
* [UI e UX](core/05_UI_UX.md)
* [Classes](heroes/02_CLASSES.md)
* [Atributos](heroes/03_ATTRIBUTES.md)
* [Habilidades](heroes/04_SKILLS.md)
* [Modelo de Dados](technical/02_DATA_MODEL.md)
* [Arquitetura Tecnica](technical/05_ARCHITECTURE.md)
* [Sprint Class ID e Visual Mapping](SPRINT_TECH_CLASS_ID_VISUAL_MAPPING.md)

## Visao Geral

O Arqueiro usa o mesmo combate numerico do Guerreiro nesta sprint. A diferenca
esta na apresentacao:

* sprites proprios;
* postura leve durante exploracao;
* preparacao com arco ao entrar em combate;
* ausencia de avancada corpo a corpo;
* disparo automatico;
* flecha visual entre heroi e inimigo;
* impacto antes do dano flutuante.

## Estrutura

### Configuracao de Classe

O `class_id` continua persistido no save. Enquanto a selecao em UI nao existe,
a classe pode ser configurada tecnicamente:

```powershell
python src/main.py --class-id archer
python src/main.py --class-id warrior
```

A opcao atualiza somente `class_id` e preserva o restante do progresso.

### Estados Visuais

O Arqueiro utiliza:

```text
idle
walk
combat_idle
attack_ranged
hit
victory
defeat
```

Os frames vivem em `src/assets/archer`.

### Projétil

`ArrowProjectile` e um componente exclusivamente visual.

Responsabilidades:

* armazenar origem e destino;
* interpolar posicao;
* controlar velocidade visual;
* informar o momento do impacto;
* ser removido ao concluir o trajeto.

Nao possui formula de dano, acesso ao inimigo ou alteracao de HP.

### Fluxo do Ataque

```text
CombatSystem calcula e aplica o dano
↓
UI recebe hero_attack
↓
Arqueiro prepara e solta o arco
↓
ArrowProjectile percorre a cena
↓
Impacto visual
↓
Flash e dano flutuante
```

Em golpes letais, a pose de vitoria aguarda o impacto da flecha.

### Distancia

O Guerreiro mantem a avancada curta durante o golpe.

O Arqueiro permanece em `hero_home_x`. A flecha percorre o espaco ate
`enemy_x`, preservando a leitura de combate a distancia.

## Regras

* O combate permanece automatico.
* O dano continua pertencendo ao `CombatSystem`.
* A flecha nao altera HP.
* O Arqueiro nao recebe formula propria nesta sprint.
* DEX permanece apenas como direcao conceitual.
* Nao existe habilidade manual.
* Nao existe estrategia ranged selecionavel.
* O comportamento vem de `class_id`.
* O fallback visual para Guerreiro permanece ativo.

## Dados

Classe:

```text
class_id = "archer"
```

Ataque basico conceitual:

```text
basic_arrow_shot
```

Nome exibido futuro:

```text
Disparo
```

Nao foi adicionado ao modelo de habilidades nesta sprint.

## Validacao

Foram cobertos:

* inicializacao de Guerreiro e Arqueiro;
* persistencia de `class_id`;
* sprites transparentes e distintos;
* caminhada e preparacao de combate;
* ausencia de dash no ataque ranged;
* criacao, movimento e impacto da flecha;
* dano visual somente apos impacto;
* vitoria aguardando impacto;
* derrota e retorno ao loop;
* combate automatico sem alteracao de formula;
* ausencia de estrategia manual;
* carregamento da UI compacta e expandida.

## Fora do Escopo

* DEX funcional;
* critico e evasao;
* habilidades;
* talentos;
* passivas;
* arco como item completo;
* multiplos projeteis;
* fisica de projeteis;
* selecao de classe na UI;
* balanceamento final.

## Pendencias

* Avaliar som curto de disparo e impacto.
* Criar tipo de arma `bow` quando o modelo de itens for expandido.
* Definir crescimento do Arqueiro junto ao sistema de atributos.
* Integrar selecao de classe ao fluxo inicial em sprint futura.
* Revisar os sprites com direcao de arte final.

## Historico de Alteracoes

* 2026-06-11: Arqueiro MVP implementado com sprites proprios, ataque ranged,
  projétil visual e impacto desacoplado do dano.
