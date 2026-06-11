from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from hero.hero import Hero
from maps.campaign import CampaignProgress

SAVE_VERSION = 3


@dataclass
class GameState:
    hero: Hero = field(default_factory=Hero)
    campaign: CampaignProgress = field(default_factory=CampaignProgress)
    save_version: int = SAVE_VERSION

    @property
    def version(self) -> int:
        return self.save_version

    def to_dict(self) -> dict[str, Any]:
        return {
            "save_version": SAVE_VERSION,
            "hero": self.hero.to_core_dict(),
            "inventory": self.hero.inventory_to_dict(),
            "equipment": self.hero.equipment_to_dict(),
            "wallet": {"gold": self.hero.gold},
            "statistics": self.hero.statistics_to_dict(),
            "world_progress": self.campaign.to_dict(),
            "session_state": {},
            "daily_state": {},
            "companion_state": {},
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> GameState:
        if not isinstance(data, dict):
            raise TypeError("Save data must be a dictionary.")

        if "hero" not in data:
            return cls(
                hero=Hero.from_dict(data),
                campaign=CampaignProgress.from_dict(
                    data.get("campaign", {})
                    if isinstance(data.get("campaign", {}), dict)
                    else {}
                ),
            )

        raw_hero = data.get("hero", {})
        hero_data = dict(raw_hero) if isinstance(raw_hero, dict) else {}

        if "inventory" in data:
            hero_data["inventory"] = data.get("inventory", [])
        if "equipment" in data:
            hero_data["equipment"] = data.get("equipment", {})
        if "statistics" in data:
            hero_data["statistics"] = data.get("statistics", {})

        wallet = data.get("wallet", {})
        if isinstance(wallet, dict) and "gold" in wallet:
            hero_data["gold"] = wallet.get("gold", 0)

        progress_data = data.get("world_progress", data.get("campaign", {}))
        if not isinstance(progress_data, dict):
            progress_data = {}

        return cls(
            hero=Hero.from_dict(hero_data),
            campaign=CampaignProgress.from_dict(progress_data),
            save_version=SAVE_VERSION,
        )
