# Fórmulas de Balanceamento

## Objetivo

Centralizar fórmulas, parâmetros numéricos e convenções de cálculo do TBH2 sem misturá-los aos documentos de conteúdo.

Este documento define como os valores são calculados.

Ele não define conteúdo narrativo, mapas, monstros, itens ou chefes específicos.

---

## Status

Draft

---

## Dependências

* Progressão
* Combate
* Loot e Economia
* Sistema de Itens
* Sistema de Monstros
* Dificuldades
* Modelo de Dados

---

# Visão Geral

As fórmulas de balanceamento existem para garantir consistência entre os sistemas principais do jogo.

Sistemas afetados:

* herói;
* monstros;
* equipamentos;
* loot;
* experiência;
* ouro;
* dificuldades;
* chefes;
* elites;
* mapas;
* atos.

O objetivo é evitar que cada sistema crie seus próprios números isoladamente.

---

# Filosofia de Balanceamento

O TBH2 deve seguir três princípios:

1. Progressão clara.
2. Crescimento controlado.
3. Recompensa proporcional ao desafio.

O jogador deve sentir que está ficando mais forte.

Mas o jogo não deve escalar de forma descontrolada.

---

# Prioridade de Poder

A fonte de poder do personagem deve seguir esta ordem:

1. Equipamentos
2. Atributos
3. Habilidades
4. Classe
5. Nível

O nível representa crescimento constante.

Os equipamentos representam a principal fonte de salto de poder.

---

# Convenções Gerais

## Valores Internos

Cálculos internos podem usar números decimais.

Exibição para o jogador deve usar inteiros arredondados.

---

## Arredondamento

Regra padrão:

* HP: arredondar para cima.
* Dano: arredondar para baixo.
* XP: arredondar para baixo.
* Ouro: arredondar para baixo.
* Power: arredondar para inteiro.
* Build Score: arredondar para inteiro.

---

## Valor Mínimo

Nenhuma fórmula de combate deve retornar valor menor que 1 quando houver acerto válido.

Exemplo:

```text
final_damage = max(1, calculated_damage)
```

---

## Multiplicadores

Multiplicadores devem ser aplicados de forma explícita.

Formato recomendado:

```text
final_value = base_value * level_multiplier * category_multiplier * difficulty_multiplier
```

Evitar fórmulas ocultas ou misturadas diretamente no código.

---

# HP do Herói

## Objetivo

Definir vida máxima do herói.

A vida do herói deve crescer com:

* nível;
* Constitution;
* equipamentos;
* bônus futuros.

---

## Fórmula Conceitual

```text
hero_max_hp =
    base_hp
    + level_hp_bonus
    + constitution_hp_bonus
    + equipment_hp_bonus
    + passive_hp_bonus
```

---

## Fórmula Inicial Recomendada

```text
hero_max_hp =
    base_hp
    + (level - 1) * hp_per_level
    + constitution * hp_per_constitution
    + equipment_hp_bonus
```

---

## Regras

* Constitution deve ser o principal atributo defensivo base.
* Equipamentos podem superar o bônus de nível.
* HP não deve crescer rápido demais no início.
* HP deve permitir leitura clara de sobrevivência.

---

# HP de Monstros

## Objetivo

Definir vida de monstros comuns, elites e chefes.

A vida dos monstros deve escalar com:

* nível do mapa;
* categoria do monstro;
* ato;
* dificuldade;
* modificadores especiais.

---

## Fórmula Conceitual

```text
monster_max_hp =
    base_monster_hp
    * level_multiplier
    * category_multiplier
    * act_multiplier
    * difficulty_multiplier
    * modifier_multiplier
```

---

## Categoria

Multiplicadores por categoria:

```text
Comum      = baixo
Campeão    = médio
Elite      = alto
Chefe      = muito alto
```

Valores finais serão definidos após testes.

---

## Regras

* Monstros comuns devem morrer em tempo razoável.
* Elites devem durar mais que comuns.
* Chefes devem funcionar como teste real de progressão.
* HP não deve ser usado sozinho para criar dificuldade.

---

# Attack do Herói

## Objetivo

Definir ataque base do herói.

O ataque do herói deve ser influenciado por:

* arma equipada;
* atributo principal;
* nível;
* habilidades;
* bônus de item.

---

## Fórmula Conceitual

```text
hero_attack =
    weapon_damage
    + attribute_damage_bonus
    + level_damage_bonus
    + equipment_damage_bonus
    + passive_damage_bonus
```

---

## Fórmula Inicial Recomendada

```text
hero_attack =
    weapon_damage
    + primary_attribute * attribute_damage_factor
    + (level - 1) * attack_per_level
    + flat_damage_bonus
```

---

## Regras

* Arma deve ser a principal fonte ofensiva.
* Atributo principal deve reforçar a build.
* Nível deve adicionar crescimento estável, mas não dominante.
* Habilidades podem multiplicar ou modificar o dano.

---

# Attack de Monstros

## Objetivo

Definir dano base dos monstros.

O ataque dos monstros deve escalar com:

* nível;
* categoria;
* arquétipo;
* dificuldade;
* modificadores.

---

## Fórmula Conceitual

```text
monster_attack =
    base_attack
    * level_multiplier
    * archetype_multiplier
    * category_multiplier
    * difficulty_multiplier
    * modifier_multiplier
```

---

## Regras

* Predadores podem ter ataque menor e frequência maior.
* Brutamontes podem ter ataque maior e frequência menor.
* Conjuradores podem usar ataque mágico.
* Chefes podem possuir multiplicadores próprios.

---

# Defense

## Objetivo

Definir mitigação de dano físico e mágico.

O sistema deve evitar reduções absolutas que tornem o dano irrelevante.

---

# Armor

Armor reduz dano físico.

## Fórmula Recomendada

```text
physical_damage_taken =
    raw_physical_damage * (100 / (100 + armor))
```

---

# Spell Armor

Spell Armor reduz dano mágico.

## Fórmula Recomendada

```text
magic_damage_taken =
    raw_magic_damage * (100 / (100 + spell_armor))
```

---

# Pure Damage

Dano puro ignora Armor e Spell Armor.

```text
pure_damage_taken = raw_pure_damage
```

---

# Regras de Defesa

* Armor não deve reduzir dano a zero.
* Spell Armor não deve reduzir dano a zero.
* Dano puro deve ser raro.
* Defesa deve suavizar dano, não anular combate.
* Equipamentos defensivos devem ser relevantes.

---

# Dano Final

## Ordem de Cálculo

Fluxo base:

```text
base_damage
↓
modificadores ofensivos
↓
crítico
↓
categoria de dano
↓
mitigação defensiva
↓
dano final
```

---

## Fórmula Conceitual

```text
final_damage =
    max(1, mitigated_damage)
```

---

# Crítico

## Objetivo

Definir golpes críticos futuros.

Crítico deve ser uma forma de especialização ofensiva, principalmente para builds baseadas em Dexterity.

---

## Fórmula Conceitual

```text
critical_damage =
    base_damage * critical_multiplier
```

---

## Regras

* Crítico deve ser limitado.
* Dexterity pode aumentar chance crítica.
* Itens podem aumentar chance ou dano crítico.
* Crítico não deve ser obrigatório para todas as builds.

---

# Evasion

## Objetivo

Definir evasão futura.

Evasion representa chance de evitar completamente um ataque.

---

## Fórmula Conceitual

```text
hit_success = random_roll > evasion_chance
```

---

## Regras

* Evasion deve ter limite máximo.
* Evasion deve ser mais comum em builds leves.
* Evasion não deve substituir defesa completamente.
* Chefes podem possuir regras especiais contra evasão excessiva.

---

# Parry

## Objetivo

Definir aparo futuro.

Parry representa chance de reduzir ou evitar parcialmente dano físico.

---

## Fórmula Conceitual

```text
parried_damage =
    incoming_damage * parry_reduction
```

---

## Regras

* Parry deve ser mais ligado a armas, escudos e classes físicas.
* Parry não deve anular todo tipo de dano.
* Parry deve ser diferente de Evasion.

---

# XP Necessária para Subir de Nível

## Objetivo

Definir curva de experiência do herói.

A progressão deve ser rápida no início, moderada no meio e lenta no final.

---

## Fases de Progressão

```text
Níveis 1-10     = tutorial rápido
Níveis 11-30    = progressão inicial
Níveis 31-60    = progressão média
Níveis 61-90    = progressão avançada
Níveis 91-100+  = progressão lenta
```

---

## Fórmula Conceitual

```text
xp_required_for_next_level =
    base_xp
    * level_growth
    * phase_multiplier
```

---

## Fórmula Inicial Recomendada

```text
xp_required =
    base_xp * (level ^ xp_growth_power) * phase_multiplier
```

---

## Regras

* Primeiros níveis devem ser rápidos.
* Níveis intermediários devem sustentar a jornada.
* Níveis finais devem exigir tempo e otimização.
* A curva deve ser testada por tempo médio de progressão.

---

# XP Concedida por Monstro

## Objetivo

Definir experiência recebida por combate.

---

## Fórmula Conceitual

```text
xp_reward =
    base_xp_by_level
    * monster_category_multiplier
    * difficulty_xp_multiplier
    * event_multiplier
```

---

## Regras

* Monstros comuns sustentam XP base.
* Elites concedem XP superior.
* Chefes concedem XP relevante.
* Dificuldades maiores podem aumentar XP.
* XP não deve substituir loot como fonte principal de poder.

---

# Gold

## Objetivo

Definir ouro recebido por monstros, elites, chefes e eventos.

O ouro deve ser útil durante todo o jogo.

---

## Fórmula Conceitual

```text
gold_reward =
    base_gold_by_level
    * monster_category_multiplier
    * difficulty_gold_multiplier
    * random_variation
```

---

## Variação Aleatória

Variação recomendada:

```text
random_variation = 0.85 até 1.15
```

Valores finais podem ser ajustados.

---

## Regras

* Ouro deve crescer com nível e dificuldade.
* Chefes e elites devem conceder mais ouro.
* Ouro não deve inflacionar sem sinks.
* Custos de upgrade devem acompanhar geração de ouro.

---

# Power

## Objetivo

Definir indicador geral de força do herói.

Power é uma leitura simplificada.

Ele não substitui Build Score.

---

## Fórmula Conceitual

```text
power =
    offensive_score
    + defensive_score
    + attribute_score
    + item_score
```

---

## Componentes

```text
offensive_score = attack + critical_value + attack_speed_value

defensive_score = max_hp_value + armor_value + spell_armor_value

attribute_score = strength_value + dexterity_value + intelligence_value + constitution_value

item_score = equipment_power_total
```

---

## Regras

* Power deve ser fácil de entender.
* Power pode ser usado para leitura geral.
* Power não deve decidir sozinho se um item é melhor.
* Power pode ser salvo como cache, mas deve ser recalculável.

---

# Build Score

## Objetivo

Definir valor real de um item ou build para o personagem atual.

Build Score representa sinergia.

---

## Fórmula Conceitual

```text
build_score =
    power_value
    + class_synergy
    + attribute_synergy
    + skill_synergy
    + tag_synergy
    + special_effect_value
```

---

## Regras

* Build Score depende do herói atual.
* Dois personagens podem avaliar o mesmo item de forma diferente.
* Build Score deve ser recalculável.
* Auto-equip deve priorizar Build Score, não apenas Power.

---

# Scaling por Mapa

## Objetivo

Definir progressão numérica entre mapas.

---

## Fórmula Conceitual

```text
map_level =
    act_base_level + map_order
```

---

## Exemplo Conceitual

```text
Ato I, Mapa 1  = nível 1
Ato I, Mapa 10 = nível 10
Ato II, Mapa 1 = nível 11
Ato II, Mapa 10 = nível 20
```

A estrutura final pode ser ajustada conforme curva de progressão.

---

## Regras

* Mapas posteriores devem ser mais difíceis.
* Boss maps devem representar pico de dificuldade.
* O nível do mapa define nível base dos monstros.
* Dificuldade altera multiplicadores, não identidade do mapa.

---

# Scaling por Ato

## Objetivo

Definir crescimento entre atos.

---

## Fórmula Conceitual

```text
act_multiplier =
    1 + (act_index - 1) * act_growth_factor
```

---

## Regras

* Atos posteriores devem exigir personagem mais forte.
* Cada ato deve introduzir inimigos mais perigosos.
* O salto entre atos deve ser perceptível, mas não quebrar progressão.

---

# Scaling por Dificuldade

## Objetivo

Definir modificadores por dificuldade.

---

## Dificuldades Planejadas

```text
Normal
Veterano
Pesadelo
Infernal
```

---

## Multiplicadores Conceituais

Cada dificuldade pode modificar:

```text
monster_hp_multiplier
monster_damage_multiplier
xp_multiplier
gold_multiplier
loot_quality_multiplier
elite_spawn_multiplier
boss_reward_multiplier
```

---

## Regras

* Dificuldade maior aumenta desafio e recompensa.
* Dificuldade não deve ser apenas HP e dano.
* Dificuldade deve aumentar potencial de loot.
* Valores finais dependem de teste da dificuldade Normal.

---

# Loot Quality

## Objetivo

Definir influência da dificuldade e categoria do inimigo na qualidade do loot.

---

## Fórmula Conceitual

```text
loot_quality_score =
    base_loot_score
    + monster_category_bonus
    + difficulty_bonus
    + boss_bonus
    + event_bonus
```

---

## Regras

* Loot Quality aumenta potencial, não garante item específico.
* Chefes e elites devem ter bônus claros.
* Dificuldades superiores devem liberar ou favorecer raridades superiores.
* Loot deve permanecer imprevisível, mas justo.

---

# Tempo de Combate

## Objetivo

Definir metas de duração para encontros.

O tempo de combate é uma métrica de validação do balanceamento.

---

## Metas Conceituais

```text
Monstro comum  = curto
Campeão        = médio
Elite          = médio/longo
Chefe          = longo
```

---

## Regras

* Combates comuns não devem travar o fluxo.
* Elites devem quebrar a rotina.
* Chefes devem parecer eventos especiais.
* Se todo combate for longo, o idle perde ritmo.
* Se todo combate for curto, progressão perde peso.

---

# Processo de Aprovação

Nenhuma fórmula deve ser considerada final sem testes.

Processo recomendado:

1. Definir objetivo da fórmula.
2. Criar cenário de teste.
3. Simular valores.
4. Validar sensação de progressão.
5. Ajustar constantes.
6. Registrar alteração no histórico.

---

# Cenários de Teste Obrigatórios

## Cenário 1

Herói nível 1 contra monstro comum do Mapa 1.

Objetivo:

Validar tutorial.

---

## Cenário 2

Herói nível 5 contra monstro comum do Mapa 5.

Objetivo:

Validar progressão inicial.

---

## Cenário 3

Herói nível 10 contra chefe do Ato I.

Objetivo:

Validar primeiro bloqueio real.

---

## Cenário 4

Herói nível 30 em dificuldade Veterano.

Objetivo:

Validar início da segunda progressão.

---

## Cenário 5

Herói nível 60 em Pesadelo.

Objetivo:

Validar necessidade de build.

---

## Cenário 6

Herói nível 90 em Infernal.

Objetivo:

Validar endgame.

---

# Regras

* Fórmulas devem ficar centralizadas.
* Não usar números mágicos espalhados no código.
* Todo multiplicador deve possuir nome claro.
* Valores finais devem ser definidos após teste.
* Power e Build Score devem ser recalculáveis.
* Fórmulas devem favorecer equipamentos como principal fonte de poder.
* Dificuldade Normal deve ser validada antes das demais.
* O balanceamento deve explicar derrotas de forma compreensível.
* Fórmulas não devem ser misturadas em documentos de conteúdo.

---

# Fora do Escopo

Este documento não define:

* lista final de monstros;
* lista final de itens;
* tabelas finais de loot;
* valores finais de afixos;
* arte;
* narrativa;
* mapas específicos;
* implementação de código.

---

# Dados Planejados

Possível arquivo técnico futuro:

```text
balance_config.py
```

Ou:

```text
balance_config.json
```

Deve conter:

```text
base_hp
hp_per_level
hp_per_constitution
attack_per_level
attribute_damage_factor
xp_base
xp_growth_power
gold_base
difficulty_multipliers
category_multipliers
act_growth_factor
map_growth_factor
```

---

# Critérios de Sucesso

As fórmulas serão consideradas saudáveis quando:

* o início do jogo for rápido e compreensível;
* equipamentos gerarem impacto perceptível;
* chefes funcionarem como bloqueios justos;
* elites forem perigosos e recompensadores;
* dificuldades superiores criarem novos ciclos;
* ouro permanecer útil;
* Power for legível;
* Build Score representar melhor a build real;
* o jogo puder ser balanceado sem reescrever sistemas inteiros.

---

# Pendências

* Definir constantes iniciais.
* Criar simulações de combate.
* Definir metas de tempo por encontro.
* Definir XP necessária por nível.
* Definir gold médio por mapa.
* Definir multiplicadores por dificuldade.
* Definir multiplicadores por categoria de monstro.
* Definir fórmula final de Power.
* Definir fórmula final de Build Score.
* Criar cenários de teste automatizados.

---

# Histórico de Alterações

* 2026-06-10: criado template modular.
* 2026-06-10: adicionadas fórmulas conceituais de HP, Attack, Defense, XP, Gold, Power e Scaling.
* 2026-06-10: definida separação entre fórmulas e documentos de conteúdo.
* 2026-06-10: adicionados critérios de teste e aprovação.
