from __future__ import annotations

from dataclasses import dataclass, field
from random import Random
from typing import Any, Literal
from uuid import uuid4

from balance import EncounterCategory, LOOT_DROP_CHANCE

ItemSlot = Literal["weapon", "armor", "accessory"]
Rarity = Literal["Comum", "Raro", "Épico"]


@dataclass(frozen=True)
class ItemBaseDefinition:
    item_base_id: str
    name: str
    rarity: Rarity
    slot: ItemSlot
    base_power: int


@dataclass(frozen=True)
class ItemInstance:
    name: str
    rarity: Rarity
    slot: ItemSlot
    power: int
    attack_bonus: int = 0
    defense_bonus: int = 0
    item_id: str = field(default_factory=lambda: uuid4().hex[:12])
    item_base_id: str = ""
    favorite: bool = False
    locked: bool = False

    @property
    def build_score(self) -> int:
        return self.power

    def to_dict(self) -> dict[str, Any]:
        return {
            "item_id": self.item_id,
            "item_base_id": self.item_base_id,
            "name": self.name,
            "rarity": self.rarity,
            "slot": self.slot,
            "power": self.power,
            "attack_bonus": self.attack_bonus,
            "defense_bonus": self.defense_bonus,
            "favorite": self.favorite,
            "locked": self.locked,
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> ItemInstance:
        attack_bonus = int(data.get("attack_bonus", 0))
        defense_bonus = int(data.get("defense_bonus", 0))
        rarity = str(data.get("rarity", "Comum"))
        if rarity in {"Ã‰pico", "Epico"}:
            rarity = "Épico"
        if rarity not in {"Comum", "Raro", "Épico"}:
            rarity = "Comum"
        slot = str(data.get("slot", "weapon"))
        if slot not in {"weapon", "armor", "accessory"}:
            slot = "weapon"
        return cls(
            name=str(data.get("name", "Item desconhecido")),
            rarity=rarity,
            slot=slot,
            power=max(1, int(data.get("power", attack_bonus + defense_bonus or 1))),
            attack_bonus=attack_bonus,
            defense_bonus=defense_bonus,
            item_id=str(data.get("item_id") or uuid4().hex[:12]),
            item_base_id=str(data.get("item_base_id", "")),
            favorite=bool(data.get("favorite", False)),
            locked=bool(data.get("locked", False)),
        )


Item = ItemInstance


ITEM_BASES: dict[str, ItemBaseDefinition] = {
    "rusty_sword": ItemBaseDefinition(
        "rusty_sword", "Espada Enferrujada", "Comum", "weapon", 2
    ),
    "wooden_shield": ItemBaseDefinition(
        "wooden_shield", "Escudo de Madeira", "Comum", "armor", 2
    ),
    "hunter_axe": ItemBaseDefinition(
        "hunter_axe", "Machado do Caçador", "Raro", "weapon", 5
    ),
    "leather_armor": ItemBaseDefinition(
        "leather_armor", "Armadura de Couro", "Raro", "armor", 5
    ),
    "crimson_blade": ItemBaseDefinition(
        "crimson_blade", "Lâmina Carmesim", "Épico", "weapon", 10
    ),
    "guardian_armor": ItemBaseDefinition(
        "guardian_armor", "Armadura do Guardião", "Épico", "armor", 10
    ),
}


def _rarity_for_roll(
    roll: float,
    category: EncounterCategory,
) -> Rarity:
    rare_threshold = 0.80 if category == "common" else 0.65
    epic_threshold = 0.96 if category == "common" else 0.90
    if category == "boss":
        rare_threshold = 0.35
        epic_threshold = 0.75
    if roll < rare_threshold:
        return "Comum"
    if roll < epic_threshold:
        return "Raro"
    return "Épico"


def roll_loot(
    reference_level: int,
    rng: Random | None = None,
    category: EncounterCategory = "common",
    difficulty_id: str = "normal",
) -> Item | None:
    del difficulty_id  # Reserved for the next difficulty tier.
    randomizer = rng or Random()
    if randomizer.random() >= LOOT_DROP_CHANCE[category]:
        return None

    rarity = _rarity_for_roll(randomizer.random(), category)
    candidates = [
        definition
        for definition in ITEM_BASES.values()
        if definition.rarity == rarity
    ]
    definition = randomizer.choice(candidates)
    power = definition.base_power + max(0, reference_level - 1)
    return Item(
        name=definition.name,
        rarity=definition.rarity,
        slot=definition.slot,
        power=power,
        attack_bonus=power if definition.slot == "weapon" else 0,
        defense_bonus=power if definition.slot == "armor" else 0,
        item_base_id=definition.item_base_id,
    )
