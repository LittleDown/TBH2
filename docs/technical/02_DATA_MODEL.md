# Modelo de Dados

## Objetivo

Definir as entidades, relações, contratos e regras de persistência dos dados do TBH2.

O Modelo de Dados serve como referência central para implementação, save, migrações e comunicação entre sistemas.

Este documento não define balanceamento.

Ele define estrutura.

---

## Status

Draft

---

## Dependências

* Sistema de Save
* Sistema de Herói
* Sistema de Monstros
* Sistema de Itens
* Estrutura do Mundo
* Progressão
* Loot e Economia
* Arquitetura Técnica

---

# Visão Geral

O TBH2 utiliza dois tipos principais de dados:

1. Dados persistentes
2. Dados de definição

Dados persistentes são salvos no arquivo do jogador.

Dados de definição fazem parte do conteúdo do jogo e não devem ser duplicados no save.

---

# Filosofia do Modelo

O save deve armazenar apenas o que pertence ao progresso do jogador.

O conteúdo estático do jogo deve ser referenciado por identificadores.

Exemplo:

O save não armazena todos os dados da classe Guerreiro.

O save armazena apenas:

```text
class_id = "warrior"
```

A definição completa da classe pertence aos arquivos ou módulos de conteúdo.

---

# Convenções Gerais

## Identificadores

Toda entidade referenciável deve possuir identificador estável.

Exemplos:

```text
hero_id
item_id
class_id
race_id
monster_id
map_id
act_id
difficulty_id
```

Identificadores não devem mudar após publicação.

---

## Referências

O save deve utilizar referências simples.

Exemplo recomendado:

```text
equipped_weapon_id = "item_0001"
```

Evitar salvar objetos inteiros dentro de outros objetos quando uma referência for suficiente.

---

## Versionamento

Todo SaveData deve possuir versão.

Exemplo:

```text
save_version = 1
```

O versionamento permite migrações futuras sem perda de progresso.

---

# Tipos de Dados

## Dados Persistentes

São salvos no SaveData.

Exemplos:

* Hero
* Inventory
* Equipment
* WorldProgress
* SessionState
* DailyState
* CompanionState
* DungeonRun futura

---

## Dados de Definição

Não são salvos integralmente.

São carregados a partir do conteúdo do jogo.

Exemplos:

* RaceDefinition
* ClassDefinition
* MonsterDefinition
* ItemBaseDefinition
* MapDefinition
* DungeonDefinition
* BossDefinition
* DifficultyDefinition

---

# SaveData

## Objetivo

Representar o estado completo persistente do jogador.

SaveData é o agregado principal do sistema de save.

---

## Campos Planejados

```text
save_version
created_at
updated_at
last_saved_at
hero
inventory
equipment
world_progress
session_state
daily_state
companion_state
settings_reference
```

---

## Campos Futuros

```text
dungeon_run
party_state
achievements
statistics
offline_progress
```

---

## Regras

* Deve possuir versão.
* Deve possuir timestamps básicos.
* Deve ser compatível com migrações.
* Não deve duplicar conteúdo estático.
* Deve armazenar apenas progresso do jogador.

---

# Hero

## Objetivo

Representar o personagem principal do jogador.

O Hero é uma entidade persistente.

---

## Campos Planejados

```text
hero_id
name
level
xp
gold
current_hp
max_hp
base_damage
armor
spell_armor
strength
dexterity
intelligence
constitution
race_id
class_id
equipment
statistics
```

---

## Campos Legados

```text
strategy
```

O campo `strategy` pode existir em saves antigos, mas não deve ser usado como sistema ativo.

A filosofia atual do combate remove modos como:

* agressivo;
* balanceado;
* defensivo.

O estilo de combate deve surgir de:

* equipamentos;
* atributos;
* classe;
* habilidades;
* efeitos especiais.

---

## Defaults de Migração

Para saves antigos:

```text
race_id = "human"
class_id = "warrior"
strength = 5
dexterity = 5
intelligence = 5
constitution = 5
```

Valores finais podem ser ajustados durante balanceamento.

---

## Regras

* Todo herói deve possuir classe.
* Todo herói deve possuir raça.
* Todo herói deve possuir atributos primários.
* Atributos ausentes devem receber defaults.
* Estratégia de combate não deve orientar o comportamento futuro.
* O poder do herói deve ser calculado a partir dos dados atuais, não salvo manualmente como verdade absoluta.

---

# RaceDefinition

## Objetivo

Definir raças disponíveis para personagens.

RaceDefinition é dado de conteúdo.

O save armazena apenas `race_id`.

---

## Campos Planejados

```text
race_id
name
description
attribute_bonus
passive_effect_id
visual_reference
```

---

## Exemplos

```text
human
elf
dwarf
half_orc
```

---

## Regras

* Raças não devem ser salvas integralmente no SaveData.
* Alterações em raças devem respeitar compatibilidade.
* `race_id` deve possuir fallback seguro.

---

# ClassDefinition

## Objetivo

Definir classes jogáveis, funções e crescimento.

ClassDefinition é dado de conteúdo.

O save armazena apenas `class_id`.

---

## Campos Planejados

```text
class_id
name
role
primary_attribute
secondary_attribute
growth_profile
skill_ids
allowed_weapon_types
allowed_armor_types
visual_reference
```

---

## Exemplos

```text
warrior
archer
mage
healer
```

---

## Regras

* Classes definem identidade de build.
* Classes não devem ser duplicadas no save.
* Habilidades devem ser referenciadas por identificadores.
* Alterações futuras devem ser migráveis.

---

# Attributes

## Objetivo

Definir atributos primários usados por heróis e sistemas futuros.

---

## Atributos Primários

```text
strength
dexterity
intelligence
constitution
```

---

## Função Esperada

Strength:

* dano físico;
* armas pesadas;
* resistência física futura.

Dexterity:

* precisão;
* velocidade;
* crítico;
* evasão futura.

Intelligence:

* dano mágico;
* cura;
* efeitos arcanos.

Constitution:

* vida;
* resistência;
* sustentação.

---

## Regras

* Todo herói possui todos os atributos.
* Classes priorizam atributos diferentes.
* Atributos devem influenciar Build Score.
* Atributos não substituem equipamentos como fonte principal de poder.

---

# Equipment

## Objetivo

Representar itens equipados pelo herói.

Equipment é persistente.

---

## Slots Planejados

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

## Regras

* Cada slot referencia um item do inventário ou item equipado.
* Armas de duas mãos ocupam `weapon` e `offhand`.
* Rings devem permitir dois slots separados.
* Equipamentos favoritos ou bloqueados não devem ser removidos por auto-equip.

---

# Inventory

## Objetivo

Representar itens possuídos pelo jogador.

Inventory é persistente.

---

## Campos Planejados

```text
items
capacity
gold_reference
locked_items
favorite_items
```

---

## Regras

* Cada item deve possuir identificador único.
* O inventário armazena instâncias de itens, não apenas definições.
* Itens gerados por loot devem preservar seus atributos.
* Itens vendidos ou destruídos devem ser removidos do inventário.

---

# Item

## Objetivo

Representar uma instância concreta de item obtida pelo jogador.

Item é persistente.

---

## Campos Planejados

```text
item_id
base_item_id
name
slot
rarity
item_level
power
build_score
affixes
tags
is_equipped
is_locked
is_favorite
created_at
```

---

## Regras

* `item_id` identifica a instância.
* `base_item_id` referencia o tipo base do item.
* `rarity` define potencial e complexidade.
* `power` é indicador geral.
* `build_score` depende do herói atual e pode ser recalculado.
* Afixos gerados devem ser persistidos.

---

# ItemBaseDefinition

## Objetivo

Definir tipos base de itens.

ItemBaseDefinition é dado de conteúdo.

---

## Campos Planejados

```text
base_item_id
name
slot
weapon_type
armor_type
allowed_classes
base_tags
visual_reference
```

---

## Regras

* Não deve ser salvo integralmente no SaveData.
* Deve ser referenciado por `base_item_id`.
* Mudanças devem preservar compatibilidade com itens existentes.

---

# Monster

## Objetivo

Representar inimigos gerados durante encontros.

Monstros comuns podem ser gerados a partir de definições.

Nem todo monstro precisa ser persistido.

---

## Campos Planejados

```text
monster_id
monster_definition_id
name
category
archetype
level
current_hp
max_hp
attack
armor
spell_armor
modifiers
loot_table_id
xp_reward
gold_reward
```

---

## Regras

* Monstros comuns são temporários.
* Chefes derrotados devem ser registrados no progresso do mundo.
* Elites podem ser gerados por combinação de definição base + modificadores.
* O save não deve armazenar monstros temporários comuns após o combate.

---

# MonsterDefinition

## Objetivo

Definir monstros disponíveis no conteúdo do jogo.

MonsterDefinition é dado de conteúdo.

---

## Campos Planejados

```text
monster_definition_id
name
category
archetype
act_id
allowed_map_ids
base_stats
skills
loot_table_id
visual_reference
```

---

## Regras

* Define o modelo base do monstro.
* Não representa uma instância de combate.
* Pode ser reutilizado em campanha e dungeons.
* Deve possuir identidade visual clara.

---

# BossDefinition

## Objetivo

Definir chefes de campanha, dungeons e endgame.

BossDefinition é dado de conteúdo.

---

## Campos Planejados

```text
boss_id
name
act_id
map_id
recommended_level
base_stats
skills
loot_table_id
unlock_rules
visual_reference
```

---

## Regras

* Chefes bloqueiam avanço quando configurados para campanha.
* Chefes derrotados devem ser registrados em WorldProgress.
* Chefes possuem recompensas superiores.
* Chefes não devem ser tratados como monstros comuns com mais vida.

---

# WorldProgress

## Objetivo

Representar o progresso do jogador no mundo.

WorldProgress é persistente.

---

## Campos Planejados

```text
current_act_id
current_map_id
current_difficulty_id
unlocked_acts
unlocked_maps
unlocked_difficulties
defeated_bosses
completed_maps
```

---

## Regras

* O avanço de ato depende de chefe derrotado.
* O avanço de dificuldade depende da conclusão da dificuldade anterior.
* Mapas desbloqueados devem ser persistidos.
* Identidade visual dos mapas pertence às definições, não ao save.

---

# MapDefinition

## Objetivo

Definir mapas da campanha.

MapDefinition é dado de conteúdo.

---

## Campos Planejados

```text
map_id
act_id
name
order
theme
recommended_level
monster_pool
boss_id
loot_context_id
visual_kit_id
```

---

## Regras

* O save armazena progresso no mapa, não a definição completa.
* Cada mapa deve pertencer a um ato.
* Mapas de chefe devem possuir `boss_id`.
* Mapas devem usar pools de monstros compatíveis com o ato.

---

# DifficultyDefinition

## Objetivo

Definir dificuldades da campanha.

DifficultyDefinition é dado de conteúdo.

---

## Campos Planejados

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

## Regras

* O save armazena apenas `current_difficulty_id`.
* Multiplicadores pertencem à definição.
* Dificuldades devem ser desbloqueadas progressivamente.

---

# DungeonRun

## Objetivo

Representar o estado de uma dungeon em andamento.

DungeonRun é persistência futura e opcional.

Sua inclusão no save depende da decisão sobre retomada de runs.

---

## Campos Planejados

```text
dungeon_run_id
dungeon_id
current_floor
completed_floors
mid_boss_defeated
final_boss_defeated
participants
pending_rewards
started_at
last_updated_at
```

---

## Regras

* Só deve existir se progresso parcial de dungeon for salvo.
* Não deve criar progressão paralela.
* Deve reutilizar combate, loot e monstros existentes.
* Pode ser descartável caso dungeons sejam sempre concluídas em uma sessão.

---

# CompanionState

## Objetivo

Representar estado persistente do Companion.

---

## Campos Planejados

```text
personality_type
morale_state
last_message_id
last_message_at
recent_events
victory_count_recent
defeat_count_recent
```

---

## Regras

* Companion reage apenas a eventos internos do jogo.
* Não deve armazenar dados externos do computador.
* Moral não deve punir severamente o jogador.
* Mensagens podem ser reconstruídas por identificador.

---

# PartyState

## Objetivo

Representar composição futura de grupo.

Uso planejado para Party Dungeon e companheiros NPC.

---

## Campos Planejados

```text
members
active_slots
formation
shared_rewards
```

---

## Regras

* Sistema futuro.
* Deve suportar NPCs antes de multiplayer real.
* Cada membro deve possuir ownership claro de equipamentos.
* Party não deve exigir microgerenciamento constante.

---

# SessionState

## Objetivo

Representar dados internos de sessão.

---

## Campos Planejados

```text
session_start_time
last_session_duration
total_play_time
session_milestones_claimed
daily_session_reward_claimed
```

---

## Regras

* Deve registrar apenas dados internos do jogo.
* Não deve monitorar aplicativos, sites ou arquivos.
* Recompensas devem possuir limite.

---

# DailyState

## Objetivo

Representar retornos diários e eventos por horário local.

---

## Campos Planejados

```text
last_opened_date
last_daily_reward_date
current_streak
best_streak
daily_reward_claimed
current_time_period
daily_event_seed
```

---

## Regras

* Ausência não deve gerar punição.
* Streak não deve conceder poder essencial.
* Horário local pode alterar atmosfera, não bloquear progresso.

---

# Statistics

## Objetivo

Registrar estatísticas úteis do jogador.

---

## Campos Planejados

```text
enemies_defeated
bosses_defeated
items_found
legendary_items_found
gold_earned_total
deaths
maps_completed
play_time_total
```

---

## Regras

* Estatísticas não devem ser fonte principal de poder.
* Podem alimentar conquistas futuras.
* Devem ser atualizadas por eventos internos.

---

# Propriedade dos Dados

## Herói

Pertence ao SaveData.

---

## Itens

Instâncias pertencem ao jogador.

Definições pertencem ao conteúdo do jogo.

---

## Mapas

Progresso pertence ao jogador.

Definição pertence ao conteúdo do jogo.

---

## Monstros

Instâncias de combate são temporárias.

Definições pertencem ao conteúdo do jogo.

---

## Chefes

Definição pertence ao conteúdo do jogo.

Estado de derrotado pertence ao progresso do jogador.

---

## Companheiros

Estado desbloqueado e equipamentos pertencem ao jogador.

Definição do companheiro pertence ao conteúdo do jogo.

---

# Regras Gerais

* Dados persistentes devem ser mínimos e suficientes.
* Dados de definição não devem ser duplicados no save.
* Identificadores devem ser estáveis.
* Saves antigos devem receber defaults.
* Campos obsoletos devem ser migrados ou ignorados com segurança.
* Poder calculado deve ser recalculável.
* O save deve armazenar estado, não lógica.
* Sistemas futuros devem ser adicionados sem quebrar saves antigos.
* Instâncias e definições devem permanecer separadas.

---

# Fora do Escopo

Não definir neste documento:

* fórmulas finais de dano;
* balanceamento final;
* arte final;
* tabelas completas de loot;
* implementação de banco de dados;
* cloud save;
* multiplayer persistente.

---

# Dados Planejados

Este documento define contratos conceituais.

A implementação técnica pode utilizar:

* dataclasses;
* classes Python;
* dicionários tipados;
* schemas de validação;
* JSON serializável.

A decisão final pertence ao documento de Arquitetura Técnica.

---

# Critérios de Sucesso

O Modelo de Dados será considerado bem-sucedido quando:

* o save conseguir persistir progresso sem duplicar conteúdo estático;
* novas entidades puderem ser adicionadas com migração simples;
* sistemas diferentes usarem os mesmos identificadores;
* itens, monstros, mapas e heróis tiverem ownership claro;
* Codex conseguir implementar sem espalhar estruturas incompatíveis;
* o projeto permanecer fácil de debugar.

---

# Pendências

* Definir defaults finais de raça.
* Expandir as definições de classe além dos identificadores iniciais.
* Definir valores iniciais dos atributos.
* Decidir se DungeonRun será persistido.
* Definir propriedade dos equipamentos de companheiros.
* Definir formato final de ItemInstance.
* Definir contrato entre SaveData e Settings.
* Definir schemas técnicos no documento de arquitetura.

---

# Histórico de Alterações

* 2026-06-10: criado template modular.
* 2026-06-10: entidades futuras da expansão registradas.
* 2026-06-10: separação entre dados persistentes e dados de definição estabelecida.
* 2026-06-10: estratégia de combate marcada como campo legado.
* 2026-06-10: contratos iniciais de Hero, Item, Monster, Map, SaveData e estados futuros definidos.
* 2026-06-11: `class_id` implementado com `warrior` padrão, suporte técnico a `archer` e fallback seguro.
