from dataclasses import dataclass
from random import Random


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

    def receive_damage(self, raw_damage: int) -> int:
        applied = max(1, raw_damage - self.defense)
        self.current_hp = max(0, self.current_hp - applied)
        return applied


ENEMY_TYPES = (
    ("Goblin", 42, 7, 1, 34, 8),
    ("Lobo", 36, 9, 0, 38, 10),
    ("Esqueleto", 50, 6, 2, 42, 12),
)


def generate_enemy(
    hero_level: int,
    map_index: int = 0,
    rng: Random | None = None,
    boss: bool = False,
) -> Enemy:
    randomizer = rng or Random()
    if boss:
        level = max(1, hero_level + 2)
        max_hp = 180 + (level - 1) * 24
        attack = 13 + (level - 1) * 2
        defense = 3 + level // 3
        return Enemy(
            "Capitão Ossonegro",
            level,
            max_hp,
            max_hp,
            attack,
            defense,
            250 + level * 30,
            100 + level * 12,
            True,
        )

    level = max(1, hero_level + map_index // 3 + randomizer.choice((-1, 0, 1)))
    name, base_hp, base_attack, base_defense, base_xp, base_gold = (
        randomizer.choice(ENEMY_TYPES)
    )
    max_hp = base_hp + (level - 1) * 12 + map_index * 4
    attack = base_attack + (level - 1) * 2 + map_index // 2
    defense = base_defense + map_index // 3
    xp_reward = base_xp + (level - 1) * 8 + map_index * 3
    gold_reward = base_gold + level * 2 + map_index
    return Enemy(
        name,
        level,
        max_hp,
        max_hp,
        attack,
        defense,
        xp_reward,
        gold_reward,
    )
