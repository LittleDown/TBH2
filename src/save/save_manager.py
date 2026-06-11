from __future__ import annotations

import json
from pathlib import Path
from shutil import copy2
from typing import Any

from game_state import GameState


class SaveManager:
    def __init__(self, save_path: Path) -> None:
        self.save_path = save_path
        self.backup_path = save_path.with_name(
            f"{save_path.stem}.backup{save_path.suffix}"
        )

    def load(self) -> GameState:
        state = self._load_path(self.save_path)
        if state is not None:
            return state

        recovered_state = self._load_path(self.backup_path)
        if recovered_state is not None:
            self._atomic_write(recovered_state.to_dict(), preserve_backup=True)
            return recovered_state
        return GameState()

    def save(self, state: GameState) -> None:
        self._atomic_write(state.to_dict())

    def _load_path(self, path: Path) -> GameState | None:
        if not path.exists():
            return None
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            return GameState.from_dict(data)
        except (OSError, ValueError, KeyError, TypeError):
            return None

    def _atomic_write(
        self,
        data: dict[str, Any],
        preserve_backup: bool = False,
    ) -> None:
        self.save_path.parent.mkdir(parents=True, exist_ok=True)
        temporary_path = self.save_path.with_suffix(
            f"{self.save_path.suffix}.tmp"
        )
        temporary_path.write_text(
            json.dumps(data, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )

        validation_data = json.loads(temporary_path.read_text(encoding="utf-8"))
        GameState.from_dict(validation_data)

        if (
            not preserve_backup
            and self.save_path.exists()
            and self._load_path(self.save_path) is not None
        ):
            copy2(self.save_path, self.backup_path)

        temporary_path.replace(self.save_path)
        if not self.backup_path.exists():
            copy2(self.save_path, self.backup_path)
