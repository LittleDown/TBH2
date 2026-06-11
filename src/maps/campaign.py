from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from maps.world import (
    ACT_ONE_ID,
    ACT_ONE_MAPS,
    ACT_ONE_NAME,
    NORMAL_DIFFICULTY_ID,
    get_map_definition,
)

ACT_NAME = ACT_ONE_NAME
MAP_NAMES = tuple(map_definition.name for map_definition in ACT_ONE_MAPS)
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
    current_act_id: str = ACT_ONE_ID
    current_difficulty_id: str = NORMAL_DIFFICULTY_ID

    @property
    def current_map(self) -> str:
        return get_map_definition(self.map_index).name

    @property
    def current_map_id(self) -> str:
        return get_map_definition(self.map_index).map_id

    @property
    def map_number(self) -> int:
        return self.map_index + 1

    @property
    def target(self) -> int:
        if self.map_index == len(ACT_ONE_MAPS) - 1:
            return 1
        return VICTORIES_PER_MAP

    @property
    def next_encounter_is_boss(self) -> bool:
        return not self.act_completed and get_map_definition(
            self.map_index
        ).boss_id is not None

    def register_victory(self, is_boss: bool = False) -> ProgressResult:
        if self.act_completed:
            return ProgressResult()

        if self.map_index == len(ACT_ONE_MAPS) - 1:
            if not is_boss:
                return ProgressResult()
            self.victories = 1
            self.act_completed = True
            return ProgressResult(
                map_completed=True,
                act_completed=True,
                completed_map=self.current_map,
            )

        self.victories = min(VICTORIES_PER_MAP, self.victories + 1)
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
            "act_id": self.current_act_id,
            "act_name": ACT_NAME,
            "difficulty_id": self.current_difficulty_id,
            "map_index": self.map_index,
            "map_id": self.current_map_id,
            "map_name": self.current_map,
            "victories": self.victories,
            "target": self.target,
            "act_completed": self.act_completed,
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> CampaignProgress:
        map_index = max(
            0,
            min(len(ACT_ONE_MAPS) - 1, int(data.get("map_index", 0))),
        )
        act_completed = bool(data.get("act_completed", False))
        if map_index == len(ACT_ONE_MAPS) - 1:
            victories = 1 if act_completed else 0
        else:
            victories = max(
                0,
                min(VICTORIES_PER_MAP, int(data.get("victories", 0))),
            )
        return cls(
            map_index=map_index,
            victories=victories,
            act_completed=act_completed,
            current_act_id=str(data.get("act_id", ACT_ONE_ID)),
            current_difficulty_id=str(
                data.get("difficulty_id", NORMAL_DIFFICULTY_ID)
            ),
        )
