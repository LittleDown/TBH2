from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from items.items import Item

STRATEGY_MODIFIERS: dict[str, tuple[float, float]] = {
    "Agressivo": (1.20, 0.80),
    "Balanceado": (1.00, 1.00),
    "Defensivo": (0.80, 1.20),
}


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
        default_factory=lambda: {
            "weapon": None,
            "armor": None,
            "accessory": None,
        }
    )
    inventory: list[Item] = field(default_factory=list)
    gold: int = 0
    strategy: str = "Balanceado"
    enemies_defeated: int = 0
    deaths: int = 0
    bosses_defeated: int = 0

    @property
    def attack(self) -> int:
        weapon = self.equipment.get("weapon")
        base_value = self.base_attack + (weapon.attack_bonus if weapon else 0)
        attack_modifier, _ = STRATEGY_MODIFIERS[self.strategy]
        return max(1, int(base_value * attack_modifier))

    @property
    def defense(self) -> int:
        armor = self.equipment.get("armor")
        base_value = self.base_defense + (armor.defense_bonus if armor else 0)
        _, defense_modifier = STRATEGY_MODIFIERS[self.strategy]
        return max(0, int(base_value * defense_modifier))

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

    def set_strategy(self, strategy: str) -> bool:
        if strategy not in STRATEGY_MODIFIERS or strategy == self.strategy:
            return False
        self.strategy = strategy
        return True

    def add_gold(self, amount: int) -> None:
        self.gold += max(0, amount)

    def add_item(self, item: Item) -> bool:
        self.inventory.append(item)
        return self.equip_if_better(item)

    def equip_if_better(self, item: Item) -> bool:
        current = self.equipment.get(item.slot)
        if current is None or item.power > current.power:
            self.equipment[item.slot] = item
            return True
        return False

    def equip(self, item_id: str) -> Item | None:
        item = next(
            (
                inventory_item
                for inventory_item in self.inventory
                if inventory_item.item_id == item_id
            ),
            None,
        )
        if item is not None:
            self.equipment[item.slot] = item
        return item

    def is_equipped(self, item: Item) -> bool:
        equipped = self.equipment.get(item.slot)
        return equipped is not None and equipped.item_id == item.item_id

    def to_dict(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "level": self.level,
            "xp": self.xp,
            "max_hp": self.max_hp,
            "current_hp": self.current_hp,
            "base_attack": self.base_attack,
            "base_defense": self.base_defense,
            "gold": self.gold,
            "strategy": self.strategy,
            "equipment": {
                slot: item.to_dict() if item else None
                for slot, item in self.equipment.items()
            },
            "inventory": [
                {**item.to_dict(), "equipped": self.is_equipped(item)}
                for item in self.inventory
            ],
            "statistics": {
                "enemies_defeated": self.enemies_defeated,
                "deaths": self.deaths,
                "bosses_defeated": self.bosses_defeated,
            },
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Hero:
        equipment_data = data.get("equipment", {})
        inventory = [
            Item.from_dict(item_data)
            for item_data in data.get("inventory", [])
            if isinstance(item_data, dict)
        ]
        equipment: dict[str, Item | None] = {
            "weapon": None,
            "armor": None,
            "accessory": None,
        }
        for slot in equipment:
            item_data = equipment_data.get(slot)
            if not item_data:
                continue
            equipped_item = Item.from_dict(item_data)
            matching_item = next(
                (item for item in inventory if item.item_id == equipped_item.item_id),
                None,
            )
            if matching_item is None:
                inventory.append(equipped_item)
                matching_item = equipped_item
            equipment[slot] = matching_item

        statistics = data.get("statistics", {})
        max_hp = int(data.get("max_hp", 100))
        current_hp = min(max_hp, max(1, int(data.get("current_hp", max_hp))))
        strategy = str(data.get("strategy", "Balanceado"))
        if strategy not in STRATEGY_MODIFIERS:
            strategy = "Balanceado"
        return cls(
            name=str(data.get("name", "Aventureiro")),
            level=max(1, int(data.get("level", 1))),
            xp=max(0, int(data.get("xp", 0))),
            max_hp=max_hp,
            current_hp=current_hp,
            base_attack=max(1, int(data.get("base_attack", 10))),
            base_defense=max(0, int(data.get("base_defense", 5))),
            equipment=equipment,
            inventory=inventory,
            gold=max(0, int(data.get("gold", 0))),
            strategy=strategy,
            enemies_defeated=max(0, int(statistics.get("enemies_defeated", 0))),
            deaths=max(0, int(statistics.get("deaths", 0))),
            bosses_defeated=max(0, int(statistics.get("bosses_defeated", 0))),
        )
