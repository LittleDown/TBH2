from __future__ import annotations

from dataclasses import dataclass
from typing import Any

ACT_NAME = "Fronteira Esquecida"
MAP_NAMES = (
    "Estrada Abandonada",
    "Bosque dos Sussurros",
    "Acampamento Saqueado",
    "Colinas Cinzentas",
    "Cemitério da Vigília",
    "Ponte Quebrada",
    "Ruínas do Posto Norte",
    "Trilha da Névoa",
    "Portões da Fortaleza",
    "Fortaleza Esquecida",
)
VICTORIES_PER_MAP = 10


@dataclass(frozen=True)
class ProgressResult:
    map_completed: bool = False
    act_completed: bool = False
    completed_map: str | None = None
    new_map: str | None = None


@dataclass
class CampaignProgress:
    map_index: int = 0
    victories: int = 0
    act_completed: bool = False

    @property
    def current_map(self) -> str:
        return MAP_NAMES[self.map_index]

    @property
    def map_number(self) -> int:
        return self.map_index + 1

    @property
    def target(self) -> int:
        return VICTORIES_PER_MAP

    @property
    def next_encounter_is_boss(self) -> bool:
        return (
            not self.act_completed
            and self.map_index == len(MAP_NAMES) - 1
            and self.victories >= VICTORIES_PER_MAP - 1
        )

    def register_victory(self, is_boss: bool = False) -> ProgressResult:
        if self.act_completed:
            return ProgressResult()

        self.victories = min(VICTORIES_PER_MAP, self.victories + 1)
        if self.map_index == len(MAP_NAMES) - 1:
            if is_boss and self.victories >= VICTORIES_PER_MAP:
                self.act_completed = True
                return ProgressResult(
                    map_completed=True,
                    act_completed=True,
                    completed_map=self.current_map,
                )
            return ProgressResult()

        if self.victories < VICTORIES_PER_MAP:
            return ProgressResult()

        completed_map = self.current_map
        self.map_index += 1
        self.victories = 0
        return ProgressResult(
            map_completed=True,
            completed_map=completed_map,
            new_map=self.current_map,
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "act": ACT_NAME,
            "map_index": self.map_index,
            "map_name": self.current_map,
            "victories": self.victories,
            "target": self.target,
            "act_completed": self.act_completed,
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> CampaignProgress:
        map_index = max(0, min(len(MAP_NAMES) - 1, int(data.get("map_index", 0))))
        victories = max(
            0, min(VICTORIES_PER_MAP, int(data.get("victories", 0)))
        )
        return cls(
            map_index=map_index,
            victories=victories,
            act_completed=bool(data.get("act_completed", False)),
        )
