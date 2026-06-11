from __future__ import annotations

from random import Random

from application.encounter import EncounterSystem
from application.loot import LootSystem
from application.progression import ProgressionSystem
from application.rewards import RewardSystem
from combat.combat import CombatEvent, CombatSystem
from game_state import GameState


class GameSession:
    def __init__(self, state: GameState, rng: Random | None = None) -> None:
        self.state = state
        self.hero = state.hero
        self.rng = rng or Random()
        self.combat_system = CombatSystem()
        self.encounter_system = EncounterSystem(state.campaign, self.rng)
        self.reward_system = RewardSystem(LootSystem(self.rng))
        self.progression_system = ProgressionSystem(state.campaign)
        self.enemy = self.encounter_system.create_encounter()
        self.hero_turn = True

    def tick(self) -> list[CombatEvent]:
        combat_events = self.combat_system.resolve_turn(
            self.hero,
            self.enemy,
            self.hero_turn,
        )
        if any(event.kind == "victory" for event in combat_events):
            attack_events = [
                event for event in combat_events if event.kind == "hero_attack"
            ]
            return attack_events + self._handle_victory()
        if any(event.kind == "defeat" for event in combat_events):
            attack_events = [
                event for event in combat_events if event.kind == "enemy_attack"
            ]
            return attack_events + self._handle_defeat()

        self.hero_turn = not self.hero_turn
        return combat_events

    def _handle_victory(self) -> list[CombatEvent]:
        defeated_enemy = self.enemy
        events = self.reward_system.grant(self.hero, defeated_enemy)
        events.extend(
            self.progression_system.register_victory(defeated_enemy)
        )
        self.enemy = self.encounter_system.create_encounter()
        self.hero_turn = True
        events.append(CombatEvent("new_enemy", self._appearance_message()))
        return events

    def _handle_defeat(self) -> list[CombatEvent]:
        self.hero.revive()
        self.enemy = self.encounter_system.create_encounter()
        self.hero_turn = True
        return [
            CombatEvent(
                "defeat",
                f"{self.hero.name} caiu e renasceu com vida cheia.",
            ),
            CombatEvent("new_enemy", self._appearance_message()),
        ]

    def _appearance_message(self) -> str:
        if self.enemy.is_boss:
            return f"Chefe {self.enemy.name} apareceu!"
        category = "Elite " if self.enemy.is_elite else ""
        return (
            f"{category}{self.enemy.name} nível {self.enemy.level} apareceu."
        )
