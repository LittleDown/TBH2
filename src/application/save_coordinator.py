from __future__ import annotations

from collections.abc import Iterable

from combat.combat import CombatEvent
from game_state import GameState
from save.save_manager import SaveManager

IMPORTANT_EVENT_KINDS = {
    "victory",
    "defeat",
    "level_up",
    "loot",
    "map_complete",
    "act_complete",
}


class SaveCoordinator:
    def __init__(self, state: GameState, save_manager: SaveManager) -> None:
        self.state = state
        self.save_manager = save_manager

    def handle_events(self, events: Iterable[CombatEvent]) -> None:
        if any(event.kind in IMPORTANT_EVENT_KINDS for event in events):
            self.save_now()

    def save_now(self) -> None:
        self.save_manager.save(self.state)
