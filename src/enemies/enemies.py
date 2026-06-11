from __future__ import annotations

from dataclasses import dataclass
from random import Random

from balance import (
    ELITE_ENCOUNTER_CHANCE,
    EncounterCategory,
    enemy_rewards,
    enemy_stats,
)
from maps.campaign import CampaignProgress
from maps.world import get_map_definition


@dataclass(frozen=True)
class MonsterDefinition:
    monster_id: str
    name: str
    hp_modifier: float = 1.0
    attack_modifier: float = 1.0
    defense_modifier: float = 1.0
    sprite_key: str = "skeleton"


@dataclass
class Enemy:
    name: str
    level: int
    max_hp: int
    current_hp: int
    attack: int
    defense: int
    xp_reward: int
    gold_reward: int
    is_boss: bool = False
    definition_id: str = ""
    category: EncounterCategory = "common"
    act_id: str = "act_1"
    map_id: str = "abandoned_road"
    difficulty_id: str = "normal"
    sprite_key: str = "skeleton"

    @property
    def is_elite(self) -> bool:
        return self.category == "elite"

    def receive_damage(self, raw_damage: int) -> int:
        applied = max(1, raw_damage - self.defense)
        self.current_hp = max(0, self.current_hp - applied)
        return applied


MONSTER_CATALOG: dict[str, MonsterDefinition] = {
    "giant_rat": MonsterDefinition(
        "giant_rat", "Rato Gigante", 0.80, 0.90, 0.80, "goblin"
    ),
    "hostile_crow": MonsterDefinition(
        "hostile_crow", "Corvo Hostil", 0.70, 1.10, 0.60, "goblin"
    ),
    "gray_wolf": MonsterDefinition(
        "gray_wolf", "Lobo Cinzento", 0.90, 1.15, 0.80, "wolf"
    ),
    "giant_spider": MonsterDefinition(
        "giant_spider", "Aranha Gigante", 1.00, 1.00, 0.90, "goblin"
    ),
    "raider": MonsterDefinition(
        "raider", "Saqueador", 1.00, 1.05, 1.00, "goblin"
    ),
    "bandit": MonsterDefinition(
        "bandit", "Bandido", 1.05, 1.00, 1.05, "goblin"
    ),
    "veteran_bandit": MonsterDefinition(
        "veteran_bandit", "Bandido Veterano", 1.10, 1.10, 1.10, "goblin"
    ),
    "alpha_wolf": MonsterDefinition(
        "alpha_wolf", "Lobo Alfa", 1.15, 1.15, 0.90, "wolf"
    ),
    "skeleton_warrior": MonsterDefinition(
        "skeleton_warrior", "Esqueleto Guerreiro", 1.10, 1.00, 1.20
    ),
    "wandering_spirit": MonsterDefinition(
        "wandering_spirit", "Espírito Errante", 0.90, 1.15, 0.80
    ),
    "cultist": MonsterDefinition(
        "cultist", "Cultista", 1.00, 1.15, 0.90
    ),
    "undead": MonsterDefinition(
        "undead", "Morto-Vivo", 1.20, 0.95, 1.10
    ),
    "skeleton_guardian": MonsterDefinition(
        "skeleton_guardian", "Guardião Esquelético", 1.20, 1.00, 1.25
    ),
    "dead_archer": MonsterDefinition(
        "dead_archer", "Arqueiro Morto", 0.90, 1.20, 0.90
    ),
    "skeleton_knight": MonsterDefinition(
        "skeleton_knight", "Cavaleiro Esquelético", 1.25, 1.10, 1.25
    ),
    "necromancer": MonsterDefinition(
        "necromancer", "Necromante", 0.95, 1.25, 0.90
    ),
    "elite_undead": MonsterDefinition(
        "elite_undead", "Elite Morto-Vivo", 1.30, 1.10, 1.20
    ),
    "lord_of_bones_guard": MonsterDefinition(
        "lord_of_bones_guard",
        "Guarda do Senhor dos Ossos",
        1.20,
        1.15,
        1.20,
    ),
    "lord_of_bones": MonsterDefinition(
        "lord_of_bones",
        "Senhor dos Ossos",
        1.25,
        1.10,
        1.25,
        "boss",
    ),
}


def generate_enemy(
    campaign: CampaignProgress,
    rng: Random | None = None,
    category: EncounterCategory | None = None,
) -> Enemy:
    randomizer = rng or Random()
    map_definition = get_map_definition(campaign.map_index)
    is_boss = campaign.next_encounter_is_boss

    if is_boss:
        category = "boss"
        monster_id = map_definition.boss_id or "lord_of_bones"
    else:
        if category is None:
            category = (
                "elite"
                if randomizer.random() < ELITE_ENCOUNTER_CHANCE
                else "common"
            )
        monster_id = randomizer.choice(map_definition.monster_pool)

    definition = MONSTER_CATALOG[monster_id]
    max_hp, attack, defense = enemy_stats(
        map_definition.recommended_level,
        definition.hp_modifier,
        definition.attack_modifier,
        definition.defense_modifier,
        category,
        campaign.current_difficulty_id,
    )
    xp_reward, gold_reward = enemy_rewards(
        map_definition.recommended_level,
        category,
        campaign.current_difficulty_id,
        randomizer.uniform(0.85, 1.15),
    )
    return Enemy(
        name=definition.name,
        level=map_definition.recommended_level,
        max_hp=max_hp,
        current_hp=max_hp,
        attack=attack,
        defense=defense,
        xp_reward=xp_reward,
        gold_reward=gold_reward,
        is_boss=is_boss,
        definition_id=definition.monster_id,
        category=category,
        act_id=campaign.current_act_id,
        map_id=map_definition.map_id,
        difficulty_id=campaign.current_difficulty_id,
        sprite_key=definition.sprite_key,
    )
