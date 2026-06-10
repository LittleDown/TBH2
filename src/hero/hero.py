from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from items.items import Item


@dataclass
class Hero:
    name: str = "Aventureiro"
    level: int = 1
    xp: int = 0
    max_hp: int = 100
    current_hp: int = 100
    base_attack: int = 10
    base_defense: int = 5
    equipment: dict[str, Item | None] = field(
        default_factory=lambda: {"weapon": None, "armor": None}
    )
    enemies_defeated: int = 0
    deaths: int = 0

    @property
    def attack(self) -> int:
        weapon = self.equipment.get("weapon")
        return self.base_attack + (weapon.attack_bonus if weapon else 0)

    @property
    def defense(self) -> int:
        armor = self.equipment.get("armor")
        return self.base_defense + (armor.defense_bonus if armor else 0)

    @property
    def xp_needed(self) -> int:
        return self.level * 100

    def receive_damage(self, raw_damage: int) -> int:
        damage = max(1, raw_damage - self.defense)
        self.current_hp = max(0, self.current_hp - damage)
        return damage

    def gain_xp(self, amount: int) -> list[int]:
        self.xp += amount
        levels_gained: list[int] = []
        while self.xp >= self.xp_needed:
            self.xp -= self.xp_needed
            self.level += 1
            self.max_hp += 20
            self.base_attack += 3
            self.base_defense += 2
            self.current_hp = self.max_hp
            levels_gained.append(self.level)
        return levels_gained

    def revive(self) -> None:
        self.deaths += 1
        self.current_hp = self.max_hp

    def equip_if_better(self, item: Item) -> bool:
        current = self.equipment.get(item.slot)
        if current is None or item.power > current.power:
            self.equipment[item.slot] = item
            return True
        return False

    def to_dict(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "level": self.level,
            "xp": self.xp,
            "max_hp": self.max_hp,
            "current_hp": self.current_hp,
            "base_attack": self.base_attack,
            "base_defense": self.base_defense,
            "equipment": {
                slot: item.to_dict() if item else None
                for slot, item in self.equipment.items()
            },
            "statistics": {
                "enemies_defeated": self.enemies_defeated,
                "deaths": self.deaths,
            },
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Hero:
        equipment_data = data.get("equipment", {})
        statistics = data.get("statistics", {})
        max_hp = int(data.get("max_hp", 100))
        current_hp = min(max_hp, max(1, int(data.get("current_hp", max_hp))))
        return cls(
            name=str(data.get("name", "Aventureiro")),
            level=max(1, int(data.get("level", 1))),
            xp=max(0, int(data.get("xp", 0))),
            max_hp=max_hp,
            current_hp=current_hp,
            base_attack=max(1, int(data.get("base_attack", 10))),
            base_defense=max(0, int(data.get("base_defense", 5))),
            equipment={
                "weapon": Item.from_dict(equipment_data["weapon"])
                if equipment_data.get("weapon")
                else None,
                "armor": Item.from_dict(equipment_data["armor"])
                if equipment_data.get("armor")
                else None,
            },
            enemies_defeated=max(0, int(statistics.get("enemies_defeated", 0))),
            deaths=max(0, int(statistics.get("deaths", 0))),
        )

