from dataclasses import dataclass
from random import Random
from typing import Literal

from enemies.enemies import Enemy, generate_enemy
from hero.hero import Hero
from items.items import Item, roll_loot

EventKind = Literal[
    "hero_attack",
    "enemy_attack",
    "victory",
    "defeat",
    "level_up",
    "loot",
    "new_enemy",
]


@dataclass(frozen=True)
class CombatEvent:
    kind: EventKind
    message: str
    item: Item | None = None


class CombatEngine:
    def __init__(self, hero: Hero, rng: Random | None = None) -> None:
        self.hero = hero
        self.rng = rng or Random()
        self.enemy: Enemy = generate_enemy(hero.level, self.rng)
        self.hero_turn = True

    def tick(self) -> list[CombatEvent]:
        if self.hero_turn:
            events = self._hero_attack()
        else:
            events = self._enemy_attack()
        self.hero_turn = not self.hero_turn
        return events

    def _hero_attack(self) -> list[CombatEvent]:
        damage = self.enemy.receive_damage(self.hero.attack)
        events = [
            CombatEvent(
                "hero_attack",
                f"{self.hero.name} causa {damage} de dano em {self.enemy.name}.",
            )
        ]
        if self.enemy.current_hp == 0:
            events.extend(self._handle_victory())
        return events

    def _enemy_attack(self) -> list[CombatEvent]:
        damage = self.hero.receive_damage(self.enemy.attack)
        events = [
            CombatEvent(
                "enemy_attack",
                f"{self.enemy.name} causa {damage} de dano em {self.hero.name}.",
            )
        ]
        if self.hero.current_hp == 0:
            events.extend(self._handle_defeat())
        return events

    def _handle_victory(self) -> list[CombatEvent]:
        reward = self.enemy.xp_reward
        defeated_name = self.enemy.name
        self.hero.enemies_defeated += 1
        events = [
            CombatEvent(
                "victory",
                f"{defeated_name} derrotado. +{reward} XP.",
            )
        ]
        for level in self.hero.gain_xp(reward):
            events.append(
                CombatEvent("level_up", f"Nível {level} alcançado! Atributos aumentados.")
            )

        item = roll_loot(self.rng)
        if item:
            equipped = self.hero.equip_if_better(item)
            result = "equipado" if equipped else "mantido no chão"
            events.append(
                CombatEvent(
                    "loot",
                    f"{item.rarity}: {item.name} encontrado e {result}.",
                    item,
                )
            )
        else:
            events.append(CombatEvent("loot", "Nenhum item encontrado."))

        self.enemy = generate_enemy(self.hero.level, self.rng)
        self.hero_turn = False
        events.append(
            CombatEvent(
                "new_enemy",
                f"Um {self.enemy.name} nível {self.enemy.level} apareceu.",
            )
        )
        return events

    def _handle_defeat(self) -> list[CombatEvent]:
        self.hero.revive()
        self.enemy = generate_enemy(self.hero.level, self.rng)
        self.hero_turn = False
        return [
            CombatEvent("defeat", f"{self.hero.name} caiu e renasceu com vida cheia."),
            CombatEvent(
                "new_enemy",
                f"Um {self.enemy.name} nível {self.enemy.level} apareceu.",
            ),
        ]

