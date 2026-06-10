from __future__ import annotations

from dataclasses import asdict, dataclass
from random import Random
from typing import Any, Literal

ItemSlot = Literal["weapon", "armor"]
Rarity = Literal["Comum", "Raro", "Épico"]


@dataclass(frozen=True)
class Item:
    name: str
    rarity: Rarity
    slot: ItemSlot
    attack_bonus: int = 0
    defense_bonus: int = 0

    @property
    def power(self) -> int:
        return self.attack_bonus + self.defense_bonus

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Item:
        return cls(
            name=str(data["name"]),
            rarity=data["rarity"],
            slot=data["slot"],
            attack_bonus=int(data.get("attack_bonus", 0)),
            defense_bonus=int(data.get("defense_bonus", 0)),
        )


LOOT_TABLE: dict[Rarity, tuple[Item, ...]] = {
    "Comum": (
        Item("Espada Enferrujada", "Comum", "weapon", attack_bonus=2),
        Item("Escudo de Madeira", "Comum", "armor", defense_bonus=1),
    ),
    "Raro": (
        Item("Machado do Caçador", "Raro", "weapon", attack_bonus=5),
        Item("Armadura de Couro", "Raro", "armor", defense_bonus=4),
    ),
    "Épico": (
        Item("Lâmina Carmesim", "Épico", "weapon", attack_bonus=10),
        Item("Armadura do Guardião", "Épico", "armor", defense_bonus=8),
    ),
}


def roll_loot(rng: Random | None = None) -> Item | None:
    randomizer = rng or Random()
    roll = randomizer.random()
    if roll < 0.70:
        return None
    if roll < 0.90:
        rarity: Rarity = "Comum"
    elif roll < 0.98:
        rarity = "Raro"
    else:
        rarity = "Épico"
    return randomizer.choice(LOOT_TABLE[rarity])

