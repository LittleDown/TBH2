from __future__ import annotations

from random import Random

from enemies.enemies import Enemy
from items.items import Item, roll_loot


class LootSystem:
    def __init__(self, rng: Random | None = None) -> None:
        self.rng = rng or Random()

    def roll(self, enemy: Enemy) -> Item | None:
        return roll_loot(
            reference_level=enemy.level,
            rng=self.rng,
            category=enemy.category,
            difficulty_id=enemy.difficulty_id,
        )
