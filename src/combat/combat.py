from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from enemies.enemies import Enemy
from hero.hero import Hero
from items.items import Item

EventKind = Literal[
    "hero_attack",
    "enemy_attack",
    "victory",
    "defeat",
    "level_up",
    "gold",
    "loot",
    "map_complete",
    "act_complete",
    "new_enemy",
]


@dataclass(frozen=True)
class CombatEvent:
    kind: EventKind
    message: str
    item: Item | None = None
    amount: int | None = None


class CombatSystem:
    def resolve_turn(
        self,
        hero: Hero,
        enemy: Enemy,
        hero_turn: bool,
    ) -> list[CombatEvent]:
        if hero_turn:
            damage = enemy.receive_damage(hero.attack)
            events = [
                CombatEvent(
                    "hero_attack",
                    f"{hero.name} causa {damage} de dano em {enemy.name}.",
                    amount=damage,
                )
            ]
            if enemy.current_hp == 0:
                events.append(
                    CombatEvent("victory", f"{enemy.name} foi derrotado.")
                )
            return events

        damage = hero.receive_damage(enemy.attack)
        events = [
            CombatEvent(
                "enemy_attack",
                f"{enemy.name} causa {damage} de dano em {hero.name}.",
                amount=damage,
            )
        ]
        if hero.current_hp == 0:
            events.append(
                CombatEvent("defeat", f"{hero.name} caiu em combate.")
            )
        return events
