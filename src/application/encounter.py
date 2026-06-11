from __future__ import annotations

from random import Random

from enemies.enemies import Enemy, generate_enemy
from maps.campaign import CampaignProgress


class EncounterSystem:
    def __init__(
        self,
        campaign: CampaignProgress,
        rng: Random | None = None,
    ) -> None:
        self.campaign = campaign
        self.rng = rng or Random()

    def create_encounter(self) -> Enemy:
        return generate_enemy(self.campaign, self.rng)
