from dataclasses import dataclass
from random import Random


@dataclass
class Enemy:
    name: str
    level: int
    max_hp: int
    current_hp: int
    attack: int
    xp_reward: int

    def receive_damage(self, damage: int) -> int:
        applied = max(1, damage)
        self.current_hp = max(0, self.current_hp - applied)
        return applied


ENEMY_TYPES = (
    ("Goblin", 42, 7, 34),
    ("Lobo", 36, 9, 38),
    ("Esqueleto", 50, 6, 42),
)


def generate_enemy(hero_level: int, rng: Random | None = None) -> Enemy:
    randomizer = rng or Random()
    level = max(1, hero_level + randomizer.choice((-1, 0, 1)))
    name, base_hp, base_attack, base_xp = randomizer.choice(ENEMY_TYPES)
    max_hp = base_hp + (level - 1) * 12
    attack = base_attack + (level - 1) * 2
    xp_reward = base_xp + (level - 1) * 8
    return Enemy(name, level, max_hp, max_hp, attack, xp_reward)

