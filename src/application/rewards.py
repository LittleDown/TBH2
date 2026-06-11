from __future__ import annotations

from application.loot import LootSystem
from combat.combat import CombatEvent
from enemies.enemies import Enemy
from hero.hero import Hero


class RewardSystem:
    def __init__(self, loot_system: LootSystem) -> None:
        self.loot_system = loot_system

    def grant(self, hero: Hero, enemy: Enemy) -> list[CombatEvent]:
        hero.enemies_defeated += 1
        if enemy.is_boss:
            hero.bosses_defeated += 1
        hero.add_gold(enemy.gold_reward)

        events = [
            CombatEvent(
                "victory",
                (
                    f"{enemy.name} derrotado. +{enemy.xp_reward} XP e "
                    f"+{enemy.gold_reward} ouro."
                ),
            ),
            CombatEvent("gold", f"Tesouro atual: {hero.gold} ouro."),
        ]
        for level in hero.gain_xp(enemy.xp_reward):
            events.append(
                CombatEvent(
                    "level_up",
                    f"Nível {level} alcançado. Atributos aumentados.",
                )
            )

        item = self.loot_system.roll(enemy)
        if item is None:
            events.append(CombatEvent("loot", "Nenhum item encontrado."))
            return events

        equipped = hero.add_item(item)
        result = "autoequipado" if equipped else "guardado no inventário"
        events.append(
            CombatEvent(
                "loot",
                f"{item.rarity}: {item.name} encontrado e {result}.",
                item=item,
            )
        )
        return events
