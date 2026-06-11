# Arquitetura Técnica

## Objetivo

Definir a arquitetura técnica futura do TBH2 e alinhar a implementação atual aos domínios necessários para evolução do projeto.

Este documento descreve responsabilidades, limites, fluxo de dados e direção de migração.

Ele não define fórmulas de balanceamento, conteúdo de campanha ou implementação imediata.

---

## Status

Draft

---

## Dependências

* Gameplay Central
* Progressão
* Combate
* Loot e Economia
* Sistema de Herói
* Sistema de Itens
* Sistema de Monstros
* Estrutura do Mundo
* Sistema de Save
* Modelo de Dados
* Fórmulas de Balanceamento

---

# Visão Geral

O TBH2 deve evoluir para uma arquitetura simples, modular e testável.

A arquitetura deve preservar três objetivos:

1. Manter o jogo executável a cada fase.
2. Separar regras de jogo da interface.
3. Evitar que sistemas futuros quebrem save, progressão ou combate.

A estrutura técnica deve servir ao jogo.

Não deve virar complexidade por si mesma.

---

# Estado Atual

O protótipo atual possui uma separação inicial por pastas:

* `hero`: estado e progressão do herói;
* `enemies`: definição e geração de inimigos;
* `items`: catálogo e sorteio de loot;
* `combat`: loop de combate, vitória, derrota, experiência e loot;
* `save`: leitura e escrita do save;
* `ui`: janela, loop visual, eventos e autosave.

Essa estrutura foi suficiente para validar a demo técnica.

Porém apresenta limitações para expansão:

* `CombatEngine` concentra responsabilidades demais;
* a UI participa de decisões de loop e persistência;
* inimigos ainda não dependem claramente de mapa, ato e dificuldade;
* itens precisam separar definição base de instância gerada;
* save precisa persistir `GameState`, não apenas partes isoladas;
* regras de recompensa, loot e progressão precisam sair do combate;
* conteúdo e regra ainda estão muito próximos;
* estratégia de combate deve ser removida como sistema ativo.

---

# Direção Arquitetural

A arquitetura futura deve usar quatro camadas leves:

1. Domínio
2. Aplicação
3. Infraestrutura
4. Apresentação

Não é necessário adotar framework pesado.

A separação existe para deixar claro quem decide o quê.

---

# Princípio Central

O estado persistente da partida deve ser representado por um agregado principal:

```text
GameState
```

A interface não deve decidir regras de jogo.

A interface envia comandos.

A aplicação processa comandos.

O domínio aplica regras.

A infraestrutura salva, carrega, fornece tempo, aleatoriedade e conteúdo.

A interface recebe eventos e estado de leitura.

---

# Camadas

## 1. Domínio

Contém entidades, objetos de valor e regras puras.

Pode conter:

* Hero;
* ItemInstance;
* MonsterInstance;
* CampaignProgress;
* Wallet;
* GameState;
* regras de dano;
* regras de equipamento;
* eventos de domínio.

Não pode conter:

* CustomTkinter;
* leitura de arquivos;
* escrita de JSON;
* timers de interface;
* texto formatado para UI;
* caminhos locais;
* lógica visual.

---

## 2. Aplicação

Coordena casos de uso.

Pode conter:

* GameSession;
* CombatSystem;
* EncounterSystem;
* RewardSystem;
* LootSystem;
* EquipmentSystem;
* ProgressionSystem;
* EconomySystem;
* SaveCoordinator;
* comandos;
* eventos;
* view models.

Não pode conter:

* widgets;
* detalhes de arquivo;
* catálogo hardcoded sem repositório;
* regra visual da interface.

---

## 3. Infraestrutura

Implementa portas técnicas.

Pode conter:

* repositório JSON;
* migrações de save;
* carregamento de conteúdo;
* fonte de aleatoriedade;
* relógio;
* logging técnico.

Não pode conter:

* regra de combate;
* decisão de loot;
* progressão de mapa;
* regra visual.

---

## 4. Apresentação

Representa a interface de Taskbar.

Pode conter:

* janela principal;
* componentes visuais;
* presenter;
* formatação de eventos;
* animações;
* agendamento visual com `after`;
* botões e painéis.

Não pode conter:

* regra de recompensa;
* regra de combate;
* cálculo de XP;
* geração de loot;
* decisão de save;
* avanço de mapa por conta própria.

A UI pode iniciar ticks.

Mas quem processa o tick é a aplicação.

---

# GameState

## Objetivo

Representar o estado completo persistente da partida.

`GameState` é o agregado raiz do save.

---

## Responsabilidades

* reunir herói, mundo, economia, inventário e estatísticas;
* representar uma fotografia consistente do progresso;
* possuir versão de schema;
* permitir save, load e migração;
* servir como entrada principal dos sistemas de aplicação.

---

## Composição Planejada

```text
GameState
├── save_version
├── created_at
├── updated_at
├── hero
├── inventory
├── equipment
├── world_progress
├── wallet
├── statistics
├── session_state
├── daily_state
└── companion_state
```

---

## Não Deve

* acessar arquivos;
* criar inimigos sozinho;
* sortear loot;
* controlar interface;
* conter catálogos completos de conteúdo.

---

# Entidades Principais do Domínio

## Hero

Representa o aventureiro do jogador.

Responsabilidades:

* identidade;
* nível;
* XP;
* vida;
* atributos;
* classe;
* raça;
* equipamentos;
* estatísticas próprias.

Campos futuros:

```text
hero_id
name
level
xp
current_hp
max_hp
strength
dexterity
intelligence
constitution
class_id
race_id
```

---

## Observação sobre Estratégia

Campos antigos relacionados a estratégia devem ser tratados como legado.

O projeto não deve manter:

* StrategySystem;
* CombatStrategy ativo;
* ChangeCombatStrategy;
* modos agressivo, balanceado ou defensivo.

A identidade de combate deve surgir de:

* equipamentos;
* atributos;
* classe;
* habilidades futuras;
* efeitos especiais;
* Build Score.

---

## Loadout

Representa a configuração equipada do herói.

Responsabilidades:

* armazenar itens equipados;
* validar slots;
* permitir comparação;
* apoiar cálculo de Power e Build Score.

Slots planejados:

```text
weapon
offhand
helmet
chest
gloves
belt
boots
ring_1
ring_2
amulet
```

---

## ItemInstance

Representa um item gerado e persistente.

Responsabilidades:

* manter atributos gerados;
* manter raridade;
* manter afixos;
* manter origem;
* manter tags;
* permitir comparação.

Não deve conter regra de geração.

A geração pertence ao `LootSystem`.

---

## MonsterInstance

Representa um inimigo em combate.

Responsabilidades:

* vida atual;
* atributos efetivos;
* categoria;
* modificadores;
* referência à definição base.

Monstros comuns são temporários.

Chefes derrotados devem ser registrados no progresso do mundo.

---

## CampaignProgress

Representa o avanço do jogador na campanha.

Responsabilidades:

* ato atual;
* mapa atual;
* dificuldade atual;
* mapas desbloqueados;
* atos desbloqueados;
* chefes derrotados;
* dificuldades desbloqueadas.

---

## Wallet

Representa a economia do jogador.

Responsabilidades:

* armazenar ouro;
* receber créditos;
* validar gastos futuros;
* impedir saldo negativo.

---

# Definições de Conteúdo

Definições são dados imutáveis do jogo.

Não devem ser salvas integralmente no save.

O save armazena apenas identificadores.

---

## WorldDefinition

Agrupa atos, mapas e dificuldades disponíveis.

---

## ActDefinition

Define um ato:

```text
act_id
name
theme
map_ids
final_boss_id
next_act_id
```

---

## MapDefinition

Define um mapa:

```text
map_id
act_id
name
order
recommended_level
monster_pool
boss_id
loot_context_id
visual_kit_id
```

---

## DifficultyDefinition

Define uma dificuldade:

```text
difficulty_id
name
unlock_requirement
monster_hp_multiplier
monster_damage_multiplier
xp_multiplier
gold_multiplier
loot_quality_multiplier
```

---

## MonsterDefinition

Define o modelo base de um monstro:

```text
monster_definition_id
name
category
archetype
base_stats
skills
loot_table_id
visual_reference
```

---

## ItemBaseDefinition

Define o tipo base de item:

```text
base_item_id
name
slot
weapon_type
armor_type
base_tags
allowed_classes
visual_reference
```

---

# Sistemas de Aplicação

## GameSession

Orquestrador principal.

Responsabilidades:

* manter o `GameState` carregado;
* receber comandos;
* executar ticks;
* chamar sistemas na ordem correta;
* publicar eventos;
* expor view state;
* sinalizar necessidade de save.

Substitui o papel central hoje dividido entre UI e CombatEngine.

---

## EncounterSystem

Responsabilidades:

* selecionar encontro adequado ao mapa;
* criar `MonsterInstance`;
* iniciar chefe quando necessário;
* encerrar encontro atual;
* preparar próximo encontro.

Usa:

* WorldDefinition;
* MapDefinition;
* MonsterDefinition;
* RandomSource.

---

## CombatSystem

Responsabilidades:

* avançar combate;
* calcular ataques;
* aplicar dano;
* detectar vitória;
* detectar derrota;
* emitir eventos de combate.

Não deve:

* sortear loot;
* conceder ouro;
* avançar mapa;
* salvar jogo;
* criar o próximo inimigo sozinho.

---

## RewardSystem

Responsabilidades:

* converter vitória em recompensa;
* conceder XP;
* conceder ouro;
* solicitar drop ao LootSystem;
* emitir eventos de recompensa.

---

## LootSystem

Responsabilidades:

* decidir se existe drop;
* selecionar raridade;
* selecionar item base;
* calcular item level;
* gerar `ItemInstance`;
* aplicar contexto de mapa, dificuldade e monstro.

---

## EquipmentSystem

Responsabilidades:

* validar equipamento;
* comparar item atual e novo item;
* calcular Power e Build Score;
* aplicar auto-equip quando permitido;
* respeitar item favorito ou bloqueado.

---

## ProgressionSystem

Responsabilidades:

* aplicar XP;
* processar level up;
* avançar progresso de mapa;
* concluir mapas;
* concluir atos;
* desbloquear dificuldades.

---

## EconomySystem

Responsabilidades:

* creditar ouro;
* validar gastos futuros;
* registrar transações;
* impedir saldo negativo.

---

## AttributeSystem

Responsabilidades:

* calcular atributos totais do herói;
* aplicar classe;
* aplicar equipamentos;
* aplicar bônus futuros;
* gerar atributos derivados.

Não deve aplicar estratégia de combate.

---

## ClassSystem

Sistema futuro.

Responsabilidades:

* resolver `class_id`;
* aplicar crescimento;
* fornecer habilidades automáticas;
* validar restrições futuras de equipamento.

---

## SaveCoordinator

Responsabilidades:

* observar eventos importantes;
* decidir quando salvar;
* solicitar save ao repositório;
* executar autosave periódico;
* impedir que a UI conheça detalhes de persistência.

---

# Portas Técnicas

## GameStateRepository

Contrato de persistência.

Operações:

```text
load() -> GameState
save(GameState)
```

Implementação inicial:

```text
JsonGameStateRepository
```

---

## ContentRepository

Contrato de conteúdo.

Responsável por carregar:

* mundo;
* atos;
* mapas;
* monstros;
* chefes;
* itens;
* classes;
* dificuldades.

No início, o conteúdo pode continuar em módulos Python.

A arquitetura deve permitir migração futura para JSON.

---

## RandomSource

Porta de aleatoriedade.

Usada por:

* seleção de monstro;
* drop;
* raridade;
* item base;
* variação de atributos.

Deve permitir seed controlada em testes.

---

## Clock

Porta de tempo.

Usada por:

* ticks;
* autosave;
* cooldowns futuros;
* sistema de sessão;
* sistema diário.

O domínio não deve chamar APIs de tempo diretamente.

---

## BalanceService

Interface para cálculos centralizados.

Responsável por:

* HP;
* Attack;
* Defense;
* XP;
* Gold;
* Power;
* Build Score;
* scaling por mapa;
* scaling por ato;
* scaling por dificuldade.

As fórmulas pertencem ao documento de Balanceamento.

---

# Comandos

Comandos representam intenção externa.

Comandos iniciais:

```text
StartSession
AdvanceTick
CloseSession
EquipItem
SellItem
```

Comandos futuros:

```text
SelectClass
SelectRace
ToggleSkillAutocast
EnterDungeon
ExitDungeon
ClaimDailyReward
```

Comandos removidos:

```text
ChangeCombatStrategy
```

Motivo:

O projeto não utiliza mais modos de combate selecionáveis.

---

# Eventos

Eventos representam fatos ocorridos.

Categorias:

## Combate

```text
EncounterStarted
HeroAttacked
MonsterAttacked
DamageApplied
MonsterDefeated
HeroDefeated
```

## Recompensa

```text
GoldGranted
XpGranted
ItemDropped
ItemEquipped
ItemDiscarded
```

## Progressão

```text
HeroLeveledUp
MapCompleted
ActCompleted
DifficultyUnlocked
BossDefeated
```

## Save

```text
SaveRequested
SaveCompleted
SaveFailed
```

## Companion

```text
CompanionMessageQueued
MoraleChanged
```

Eventos devem carregar dados estruturados.

A UI transforma eventos em texto.

O domínio não deve gerar frases prontas para o usuário.

---

# View State

A aplicação deve expor um modelo de leitura para a UI.

Esse modelo não é persistido.

Deve conter:

* herói;
* HP;
* XP;
* nível;
* ouro;
* mapa atual;
* ato atual;
* dificuldade;
* inimigo atual;
* estado do encontro;
* equipamentos;
* eventos recentes;
* Power;
* Build Score.

A UI lê o View State.

A UI não calcula regra de jogo.

---

# Fluxo Principal

## Inicialização

```text
main
↓
bootstrap
↓
carregar conteúdo
↓
carregar GameState
↓
aplicar migrações
↓
criar GameSession
↓
criar UI
↓
StartSession
```

---

## Tick

```text
UI chama AdvanceTick
↓
GameSession recebe comando
↓
EncounterSystem garante encontro ativo
↓
CombatSystem avança combate
↓
RewardSystem processa vitória, se existir
↓
ProgressionSystem aplica progresso
↓
SaveCoordinator avalia persistência
↓
GameSession retorna eventos + view state
↓
UI apresenta
```

---

## Vitória

```text
MonsterDefeated
↓
RewardSystem
↓
LootSystem
↓
EquipmentSystem
↓
ProgressionSystem
↓
EncounterSystem prepara próximo encontro
↓
SaveCoordinator marca save
```

---

## Persistência

```text
Evento importante ou autosave
↓
SaveCoordinator
↓
GameStateRepository
↓
save temporário
↓
validação
↓
save principal
↓
backup
```

---

# Estrutura Futura de Pastas

Direção recomendada:

```text
src/
├── main.py
├── bootstrap.py
├── domain/
│   ├── game_state.py
│   ├── hero/
│   │   ├── hero.py
│   │   ├── attributes.py
│   │   ├── hero_class.py
│   │   ├── race.py
│   │   └── loadout.py
│   ├── combat/
│   │   ├── combatant.py
│   │   ├── encounter.py
│   │   ├── damage.py
│   │   └── events.py
│   ├── items/
│   │   ├── item_base.py
│   │   ├── item_instance.py
│   │   ├── item_slot.py
│   │   ├── rarity.py
│   │   └── affix.py
│   ├── monsters/
│   │   ├── monster_definition.py
│   │   ├── monster_instance.py
│   │   └── boss_definition.py
│   ├── world/
│   │   ├── campaign_progress.py
│   │   ├── world_definition.py
│   │   ├── act_definition.py
│   │   ├── map_definition.py
│   │   └── difficulty_definition.py
│   └── economy/
│       ├── wallet.py
│       └── transaction.py
├── application/
│   ├── game_session.py
│   ├── commands.py
│   ├── events.py
│   ├── views.py
│   ├── ports/
│   │   ├── game_state_repository.py
│   │   ├── content_repository.py
│   │   ├── random_source.py
│   │   ├── clock.py
│   │   └── balance_service.py
│   └── systems/
│       ├── encounter_system.py
│       ├── combat_system.py
│       ├── reward_system.py
│       ├── loot_system.py
│       ├── equipment_system.py
│       ├── progression_system.py
│       ├── economy_system.py
│       ├── attribute_system.py
│       ├── class_system.py
│       └── save_coordinator.py
├── infrastructure/
│   ├── persistence/
│   │   ├── json_game_state_repository.py
│   │   ├── save_mapper.py
│   │   └── migrations.py
│   ├── content/
│   │   ├── python_content_repository.py
│   │   ├── content_validator.py
│   │   └── definitions/
│   ├── random/
│   │   └── python_random_source.py
│   └── time/
│       └── system_clock.py
└── presentation/
    └── taskbar/
        ├── main_window.py
        ├── presenter.py
        ├── event_formatter.py
        └── components/
```

Essa estrutura é direção, não obrigação imediata.

Não criar arquivos vazios apenas para cumprir a árvore.

---

# Mapeamento da Implementação Atual

| Atual            | Destino Futuro              | Observação                           |
| ---------------- | --------------------------- | ------------------------------------ |
| `hero.Hero`      | `domain.hero.Hero`          | Remover serialização direta          |
| `enemies.Enemy`  | `MonsterInstance`           | Separar definição e instância        |
| `generate_enemy` | `EncounterSystem`           | Usar mapa, ato e dificuldade         |
| `items.Item`     | `ItemBase` + `ItemInstance` | Separar base e item gerado           |
| `LOOT_TABLE`     | `ContentRepository`         | Catálogo fora da regra               |
| `roll_loot`      | `LootSystem`                | Receber contexto                     |
| `CombatEngine`   | `CombatSystem` + sistemas   | Separar combate, reward e progressão |
| `SaveManager`    | `JsonGameStateRepository`   | Persistir GameState versionado       |
| `MainWindow`     | Presentation + Presenter    | UI não decide regra                  |
| `main.py`        | `bootstrap.py` + `main.py`  | Compor dependências                  |

---

# Ordem Recomendada de Migração

1. Introduzir `GameState`.
2. Introduzir `WorldProgress`.
3. Centralizar save em repositório versionado.
4. Separar `MonsterDefinition` de `MonsterInstance`.
5. Extrair recompensa do `CombatEngine`.
6. Extrair progressão do `CombatEngine`.
7. Criar `EncounterSystem`.
8. Criar `Wallet`.
9. Separar `ItemBase` de `ItemInstance`.
10. Criar `LootSystem`.
11. Criar `EquipmentSystem`.
12. Introduzir atributos STR, DEX, INT e CON.
13. Introduzir `class_id` e `race_id` com defaults.
14. Adaptar UI para consumir eventos e View State.

Cada etapa deve manter o jogo executável.

---

# Testabilidade

O domínio e a aplicação devem funcionar sem interface gráfica.

Testes prioritários:

* carregar save antigo;
* migrar save;
* salvar e carregar `GameState`;
* gerar encontro por mapa;
* resolver combate;
* conceder XP;
* conceder ouro;
* gerar loot;
* equipar item;
* avançar mapa;
* derrotar chefe;
* desbloquear ato;
* desbloquear dificuldade;
* simular resultado com RandomSource controlado.

---

# Regras de Dependência

* Apresentação depende da Aplicação.
* Aplicação depende do Domínio e das Portas.
* Infraestrutura implementa Portas.
* Domínio não depende de UI.
* Domínio não depende de Infraestrutura.
* Nenhuma entidade lê ou grava arquivo.
* Nenhum widget decide regra de jogo.
* Nenhuma fórmula fica escondida na UI.

---

# Fonte de Verdade

| Tipo               | Fonte                     |
| ------------------ | ------------------------- |
| Regras de produto  | Documentos de domínio     |
| Fórmulas           | Fórmulas de Balanceamento |
| Contratos de dados | Modelo de Dados           |
| Persistência       | Sistema de Save           |
| Estrutura técnica  | Arquitetura Técnica       |
| Conteúdo           | Repositório de conteúdo   |

---

# Estado e Conteúdo

## Estado

Mutável e persistente.

Exemplos:

* Hero;
* Inventory;
* Equipment;
* WorldProgress;
* Wallet;
* Statistics.

---

## Conteúdo

Imutável e carregado.

Exemplos:

* mapas;
* atos;
* dificuldades;
* monstros;
* chefes;
* itens base;
* classes;
* raças.

---

# Compatibilidade

Toda mudança persistente exige:

* default;
* migração;
* fallback seguro;
* teste de save antigo.

Identificadores persistidos devem ser estáveis.

Não renomear IDs publicados sem migração.

---

# Decisões de Escopo

Não usar na fase atual:

* banco de dados;
* framework pesado de injeção de dependência;
* barramento global obrigatório;
* ECS genérico;
* herança profunda;
* cloud save;
* multiplayer real;
* persistência online.

Dataclasses, protocolos, enums, serviços pequenos e composição explícita são suficientes.

---

# Fora do Escopo

Este documento não define:

* fórmulas finais;
* valores de balanceamento;
* conteúdo completo de mapas;
* sprites;
* animações;
* tabelas finais de loot;
* cloud save;
* multiplayer;
* anticheat.

---

# Critérios de Sucesso

A arquitetura será considerada saudável quando:

* o jogo continuar executável após cada migração;
* a UI não decidir regras de gameplay;
* o save persistir `GameState` versionado;
* conteúdo e estado estiverem separados;
* sistemas puderem ser testados sem CustomTkinter;
* Codex conseguir implementar sem misturar responsabilidades;
* novas fases puderem entrar sem quebrar o núcleo;
* estratégia de combate legada estiver removida ou ignorada com segurança.

---

# Pendências

* Definir esquema inicial final de `GameState`.
* Definir formato oficial do `ContentRepository`.
* Definir migração do save atual.
* Definir se encontro atual será persistido ou recriado.
* Definir sequência final dos sistemas após vitória.
* Definir contratos técnicos de eventos.
* Criar testes de round-trip do save.
* Remover referências ativas a estratégia de combate.
* Preparar defaults de `class_id`, `race_id` e atributos.

---

# Histórico de Alterações

* 2026-06-10: criada arquitetura técnica inicial.
* 2026-06-10: definida separação em Domínio, Aplicação, Infraestrutura e Apresentação.
* 2026-06-10: `GameState` definido como agregado persistente principal.
* 2026-06-10: removida estratégia de combate como sistema ativo.
* 2026-06-10: adicionada direção de migração incremental.
