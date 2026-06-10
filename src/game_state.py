from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from hero.hero import Hero
from maps.campaign import CampaignProgress

SAVE_VERSION = 2


@dataclass
class GameState:
    hero: Hero = field(default_factory=Hero)
    campaign: CampaignProgress = field(default_factory=CampaignProgress)
    version: int = SAVE_VERSION

    def to_dict(self) -> dict[str, Any]:
        return {
            "version": SAVE_VERSION,
            "hero": self.hero.to_dict(),
            "campaign": self.campaign.to_dict(),
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> GameState:
        if "hero" not in data:
            return cls(hero=Hero.from_dict(data))
        return cls(
            hero=Hero.from_dict(data.get("hero", {})),
            campaign=CampaignProgress.from_dict(data.get("campaign", {})),
            version=SAVE_VERSION,
        )
