from __future__ import annotations

from typing import Final, Literal, TypeAlias, cast

ClassId: TypeAlias = Literal["warrior", "archer"]

DEFAULT_CLASS_ID: Final[ClassId] = "warrior"
SUPPORTED_CLASS_IDS: Final[frozenset[str]] = frozenset(
    {"warrior", "archer"}
)
CLASS_DISPLAY_NAMES: Final[dict[ClassId, str]] = {
    "warrior": "Guerreiro",
    "archer": "Arqueiro",
}


def normalize_class_id(value: object) -> ClassId:
    candidate = str(value).strip().lower() if value is not None else ""
    if candidate in SUPPORTED_CLASS_IDS:
        return cast(ClassId, candidate)
    return DEFAULT_CLASS_ID


def class_display_name(value: object) -> str:
    return CLASS_DISPLAY_NAMES[normalize_class_id(value)]
