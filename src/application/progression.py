from __future__ import annotations

from combat.combat import CombatEvent
from enemies.enemies import Enemy
from maps.campaign import CampaignProgress


class ProgressionSystem:
    def __init__(self, campaign: CampaignProgress) -> None:
        self.campaign = campaign

    def register_victory(self, enemy: Enemy) -> list[CombatEvent]:
        progress = self.campaign.register_victory(enemy.is_boss)
        events: list[CombatEvent] = []
        if progress.map_completed and not progress.act_completed:
            events.append(
                CombatEvent(
                    "map_complete",
                    (
                        f"{progress.completed_map} concluído. "
                        f"Rumo a {progress.new_map}."
                    ),
                )
            )
        if progress.act_completed:
            events.append(
                CombatEvent(
                    "act_complete",
                    "Ato I concluído. O Senhor dos Ossos foi derrotado!",
                )
            )
        return events
