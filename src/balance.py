from __future__ import annotations

from typing import Literal

EncounterCategory = Literal["common", "elite", "boss"]

HERO_LEVEL_HP_GAIN = 12
HERO_LEVEL_ATTACK_GAIN = 1
HERO_DEFENSE_GAIN_INTERVAL = 3

ELITE_ENCOUNTER_CHANCE = 0.05

CATEGORY_STAT_MULTIPLIERS: dict[
    EncounterCategory, tuple[float, float, float, float]
] = {
    "common": (1.0, 1.0, 1.0, 1.0),
    "elite": (2.2, 1.35, 1.25, 2.5),
    "boss": (0.55, 0.65, 1.0, 5.0),
}

DIFFICULTY_MULTIPLIERS: dict[str, tuple[float, float, float]] = {
    "normal": (1.0, 1.0, 1.0),
}

LOOT_DROP_CHANCE: dict[EncounterCategory, float] = {
    "common": 0.30,
    "elite": 0.65,
    "boss": 1.0,
}


def xp_required_for_level(level: int) -> int:
    """Return the XP needed to advance from the given level."""
    safe_level = max(1, level)
    if safe_level <= 10:
        phase_multiplier = 1.0
    elif safe_level <= 30:
        phase_multiplier = 1.15
    elif safe_level <= 60:
        phase_multiplier = 1.35
    else:
        phase_multiplier = 1.6
    return max(1, round(120 * (safe_level**1.3) * phase_multiplier))


def hero_level_growth(new_level: int) -> tuple[int, int, int]:
    defense_gain = 1 if new_level % HERO_DEFENSE_GAIN_INTERVAL == 0 else 0
    return HERO_LEVEL_HP_GAIN, HERO_LEVEL_ATTACK_GAIN, defense_gain


def enemy_stats(
    map_level: int,
    hp_modifier: float,
    attack_modifier: float,
    defense_modifier: float,
    category: EncounterCategory,
    difficulty_id: str,
) -> tuple[int, int, int]:
    safe_level = max(1, map_level)
    category_hp, category_attack, category_defense, _ = (
        CATEGORY_STAT_MULTIPLIERS[category]
    )
    difficulty_hp, difficulty_attack, _ = DIFFICULTY_MULTIPLIERS.get(
        difficulty_id,
        DIFFICULTY_MULTIPLIERS["normal"],
    )
    base_hp = 36 + (safe_level - 1) * 14
    base_attack = 7 + (safe_level - 1) * 2
    base_defense = (safe_level - 1) // 3
    return (
        max(1, round(base_hp * hp_modifier * category_hp * difficulty_hp)),
        max(
            1,
            round(
                base_attack
                * attack_modifier
                * category_attack
                * difficulty_attack
            ),
        ),
        max(0, round(base_defense * defense_modifier * category_defense)),
    )


def enemy_rewards(
    map_level: int,
    category: EncounterCategory,
    difficulty_id: str,
    variation: float,
) -> tuple[int, int]:
    safe_level = max(1, map_level)
    _, _, _, category_reward = CATEGORY_STAT_MULTIPLIERS[category]
    _, _, difficulty_reward = DIFFICULTY_MULTIPLIERS.get(
        difficulty_id,
        DIFFICULTY_MULTIPLIERS["normal"],
    )
    reward_multiplier = category_reward * difficulty_reward
    xp = round((14 + safe_level * 3) * reward_multiplier * variation)
    gold = round((3 + safe_level * 2) * reward_multiplier * variation)
    return max(1, xp), max(0, gold)
