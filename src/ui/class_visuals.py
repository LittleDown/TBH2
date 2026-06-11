from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Final, Literal, TypeAlias

from hero.classes import ClassId, normalize_class_id

VisualAction: TypeAlias = Literal[
    "idle",
    "walk",
    "combat_idle",
    "attack_melee",
    "attack_ranged",
    "hit",
    "victory",
    "defeat",
]
AttackVisualAction: TypeAlias = Literal["attack_melee", "attack_ranged"]

VISUAL_ACTION_FRAMES: Final[dict[VisualAction, tuple[str, ...]]] = {
    "idle": ("idle",),
    "walk": ("walk1", "walk2"),
    "combat_idle": ("combat_idle",),
    "attack_melee": ("attack1", "attack2"),
    "attack_ranged": ("attack1", "attack2"),
    "hit": ("hit",),
    "victory": ("victory",),
    "defeat": ("defeat",),
}
RENDER_FRAME_NAMES: Final[tuple[str, ...]] = (
    "idle",
    "walk1",
    "walk2",
    "combat_idle",
    "attack1",
    "attack2",
    "hit",
    "victory",
    "defeat",
)
FRAME_FILE_ALIASES: Final[dict[str, tuple[str, ...]]] = {
    "idle": ("idle.png",),
    "walk1": ("walk1.png",),
    "walk2": ("walk2.png",),
    "combat_idle": ("combat_idle.png", "idle.png"),
    "attack1": ("attack1.png",),
    "attack2": ("attack2.png",),
    "hit": ("hit.png",),
    "victory": ("victory.png",),
    "defeat": ("defeat.png", "dead.png"),
    "front": ("front.png",),
}


@dataclass(frozen=True)
class ClassVisualProfile:
    class_id: ClassId
    asset_directory: str
    attack_action: AttackVisualAction


CLASS_VISUAL_PROFILES: Final[dict[ClassId, ClassVisualProfile]] = {
    "warrior": ClassVisualProfile(
        class_id="warrior",
        asset_directory="warrior",
        attack_action="attack_melee",
    ),
    "archer": ClassVisualProfile(
        class_id="archer",
        asset_directory="archer",
        attack_action="attack_ranged",
    ),
}


def visual_profile_for(class_id: object) -> ClassVisualProfile:
    return CLASS_VISUAL_PROFILES[normalize_class_id(class_id)]


def frame_names_for_action(action: VisualAction) -> tuple[str, ...]:
    return VISUAL_ACTION_FRAMES[action]


def resolve_visual_asset(
    asset_root: Path,
    class_id: object,
    frame_name: str,
) -> Path | None:
    profile = visual_profile_for(class_id)
    default_profile = CLASS_VISUAL_PROFILES["warrior"]
    aliases = FRAME_FILE_ALIASES.get(
        frame_name,
        (f"{frame_name}.png",),
    )

    search_directories = [profile.asset_directory]
    if profile.class_id != default_profile.class_id:
        search_directories.append(default_profile.asset_directory)

    for directory in search_directories:
        for file_name in aliases:
            path = asset_root / directory / file_name
            if path.is_file():
                return path

    for directory in search_directories:
        idle_path = asset_root / directory / "idle.png"
        if idle_path.is_file():
            return idle_path
    return None
