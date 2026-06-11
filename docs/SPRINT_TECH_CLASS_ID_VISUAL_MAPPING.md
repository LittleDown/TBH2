# Sprint Tecnica - Class ID e Visual Mapping

## Objetivo

Introduzir identidade persistente de classe e desacoplar a interface dos
assets exclusivos do Guerreiro, preparando o Arqueiro sem implementar seu
gameplay completo.

## Status

Implemented

## Dependencias

* [Modelo de Dados](technical/02_DATA_MODEL.md)
* [Sistema de Save](technical/01_SAVE_SYSTEM.md)
* [Arquitetura Tecnica](technical/05_ARCHITECTURE.md)
* [Sistema de Heroi](heroes/01_HERO_SYSTEM.md)
* [Classes](heroes/02_CLASSES.md)

## Visao Geral

A sprint adiciona `class_id` ao agregado `Hero`, define `warrior` como valor
padrao e aceita `archer` como identidade tecnica suportada.

O combate continua automatico. Nao existe selecao de classe, balanceamento
por classe, habilidade, projetil ou estrategia manual.

## Estrutura

### Dominio

`hero/classes.py` concentra:

* identificadores suportados;
* classe padrao;
* normalizacao de valores;
* nomes de exibicao.

`Hero` persiste somente `class_id`. Definicoes futuras de classe nao devem ser
duplicadas no save.

### Persistencia

O schema atual usa `save_version = 4`.

Saves sem `class_id` recebem:

```text
class_id = "warrior"
```

A migracao preserva nivel, XP, ouro, inventario, equipamentos, estatisticas e
progresso de campanha. Classes desconhecidas tambem usam o Guerreiro como
fallback seguro.

### Visual Mapping

`ui/class_visuals.py` resolve o perfil visual:

| class_id | Diretorio | Ataque visual |
| --- | --- | --- |
| `warrior` | `assets/warrior` | `attack_melee` |
| `archer` | `assets/archer` | `attack_ranged` |

Ordem de resolucao:

1. frame da classe solicitada;
2. frame equivalente do Guerreiro;
3. `idle.png` seguro;
4. ausencia controlada quando nenhum asset existe.

### Estados Visuais

O controlador trabalha com acoes genericas:

* `idle`;
* `walk`;
* `combat_idle`;
* `attack_melee`;
* `attack_ranged`;
* `hit`;
* `victory`;
* `defeat`.

Cada acao e convertida em um ou mais frames de renderizacao.

### Assets do Arqueiro

`assets/archer` possui o contrato completo de nomes. Nesta sprint, os PNGs sao
placeholders copiados dos equivalentes do Guerreiro e identificados no README
da pasta.

## Regras

* Novo heroi sempre inicia como `warrior`.
* `archer` pode ser construido e salvo, mas ainda nao possui gameplay proprio.
* A UI compacta e a expandida usam o mesmo resolvedor visual.
* Ausencia de asset nunca deve impedir o carregamento do jogo.
* Combate permanece automatico.
* `StrategySystem`, `CombatStrategy` e `ChangeCombatStrategy` permanecem
  proibidos.
* `race_id` continua pendente para uma sprint propria.

## Dados

Teste controlado do Guerreiro:

```python
Hero()
```

Teste controlado do Arqueiro:

```python
Hero(class_id="archer")
```

Nao ha tela de troca de classe na interface atual.

## Validacao

Cobertura automatizada:

* novo heroi com Guerreiro padrao;
* construcao e serializacao do Arqueiro;
* migracao de save sem `class_id`;
* preservacao de progresso na migracao;
* fallback para classe desconhecida;
* fallback para animacao ausente;
* contrato de assets das duas classes;
* ataque visual ranged preparado;
* ausencia de dependencias de estrategia manual;
* regressao do combate automatico.

## Pendencias

Proxima sprint Arqueiro MVP:

* produzir sprites definitivos;
* definir atributos e crescimento;
* implementar ataque a distancia sem interacao manual;
* adicionar projetil somente se necessario para leitura visual;
* definir armas permitidas;
* validar loot e Build Score por classe;
* decidir quando a escolha de classe entra no fluxo do jogador.

Permanecem fora de escopo:

* habilidades completas;
* arvore de talentos;
* passivas;
* DEX funcional;
* tela de selecao;
* party;
* multiplayer.

## Historico de Alteracoes

* 2026-06-11: sprint implementada com `class_id`, save v4, visual mapping,
  fallback seguro e placeholders do Arqueiro.
