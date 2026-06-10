from __future__ import annotations

from dataclasses import dataclass, field
from random import Random
from typing import Any, Literal
from uuid import uuid4

ItemSlot = Literal["weapon", "armor"]
Rarity = Literal["Comum", "Raro", "Épico"]


@dataclass(frozen=True)
class Item:
    name: str
    rarity: Rarity
    slot: ItemSlot
    power: int
    attack_bonus: int = 0
    defense_bonus: int = 0
    item_id: str = field(default_factory=lambda: uuid4().hex[:12])

    def to_dict(self) -> dict[str, Any]:
        return {
            "item_id": self.item_id,
            "name": self.name,
            "rarity": self.rarity,
            "slot": self.slot,
            "power": self.power,
            "attack_bonus": self.attack_bonus,
            "defense_bonus": self.defense_bonus,
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Item:
        attack_bonus = int(data.get("attack_bonus", 0))
        defense_bonus = int(data.get("defense_bonus", 0))
        return cls(
            name=str(data["name"]),
            rarity=data["rarity"],
            slot=data["slot"],
            power=max(1, int(data.get("power", attack_bonus + defense_bonus or 1))),
            attack_bonus=attack_bonus,
            defense_bonus=defense_bonus,
            item_id=str(data.get("item_id") or uuid4().hex[:12]),
        )


ITEM_BASES: dict[Rarity, tuple[tuple[str, ItemSlot, int], ...]] = {
    "Comum": (
        ("Espada Enferrujada", "weapon", 2),
        ("Escudo de Madeira", "armor", 2),
    ),
    "Raro": (
        ("Machado do Caçador", "weapon", 5),
        ("Armadura de Couro", "armor", 5),
    ),
    "Épico": (
        ("Lâmina Carmesim", "weapon", 10),
        ("Armadura do Guardião", "armor", 10),
    ),
}


def roll_loot(hero_level: int, rng: Random | None = None) -> Item | None:
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

    name, slot, base_power = randomizer.choice(ITEM_BASES[rarity])
    power = base_power + max(0, hero_level - 1)
    return Item(
        name=name,
        rarity=rarity,
        slot=slot,
        power=power,
        attack_bonus=power if slot == "weapon" else 0,
        defense_bonus=power if slot == "armor" else 0,
    )
