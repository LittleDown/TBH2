from dataclasses import dataclass
from random import Random
from typing import Literal

from enemies.enemies import Enemy, generate_enemy
from game_state import GameState
from items.items import Item, roll_loot

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


class CombatEngine:
    def __init__(self, state: GameState, rng: Random | None = None) -> None:
        self.state = state
        self.hero = state.hero
        self.rng = rng or Random()
        self.enemy = self._generate_enemy()
        self.hero_turn = True

    def _generate_enemy(self) -> Enemy:
        return generate_enemy(
            hero_level=self.hero.level,
            map_index=self.state.campaign.map_index,
            rng=self.rng,
            boss=self.state.campaign.next_encounter_is_boss,
        )

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
        gold_reward = self.enemy.gold_reward
        defeated_name = self.enemy.name
        self.hero.enemies_defeated += 1
        if self.enemy.is_boss:
            self.hero.bosses_defeated += 1
        self.hero.add_gold(gold_reward)
        events = [
            CombatEvent(
                "victory",
                f"{defeated_name} derrotado. +{reward} XP e +{gold_reward} ouro.",
            ),
            CombatEvent("gold", f"Tesouro atual: {self.hero.gold} ouro."),
        ]
        for level in self.hero.gain_xp(reward):
            events.append(
                CombatEvent("level_up", f"Nível {level} alcançado! Atributos aumentados.")
            )

        item = roll_loot(self.hero.level, self.rng)
        if item:
            equipped = self.hero.add_item(item)
            result = "autoequipado" if equipped else "guardado no inventário"
            events.append(
                CombatEvent(
                    "loot",
                    f"{item.rarity}: {item.name} encontrado e {result}.",
                    item,
                )
            )
        else:
            events.append(CombatEvent("loot", "Nenhum item encontrado."))

        progress = self.state.campaign.register_victory(self.enemy.is_boss)
        if progress.map_completed and not progress.act_completed:
            events.append(
                CombatEvent(
                    "map_complete",
                    f"{progress.completed_map} concluído. Rumo a {progress.new_map}.",
                )
            )
        if progress.act_completed:
            events.append(
                CombatEvent(
                    "act_complete",
                    "Ato I concluído. Capitão Ossonegro foi derrotado!",
                )
            )

        self.enemy = self._generate_enemy()
        self.hero_turn = False
        appearance = (
            f"Chefe {self.enemy.name} apareceu!"
            if self.enemy.is_boss
            else f"Um {self.enemy.name} nível {self.enemy.level} apareceu."
        )
        events.append(
            CombatEvent("new_enemy", appearance)
        )
        return events

    def _handle_defeat(self) -> list[CombatEvent]:
        self.hero.revive()
        self.enemy = self._generate_enemy()
        self.hero_turn = False
        return [
            CombatEvent("defeat", f"{self.hero.name} caiu e renasceu com vida cheia."),
            CombatEvent(
                "new_enemy",
                f"Um {self.enemy.name} nível {self.enemy.level} apareceu.",
            ),
        ]
