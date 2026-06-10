import json
from pathlib import Path

from game_state import GameState


class SaveManager:
    def __init__(self, save_path: Path) -> None:
        self.save_path = save_path

    def load(self) -> GameState:
        if not self.save_path.exists():
            return GameState()
        try:
            data = json.loads(self.save_path.read_text(encoding="utf-8"))
            return GameState.from_dict(data)
        except (OSError, ValueError, KeyError, TypeError):
            return GameState()

    def save(self, state: GameState) -> None:
        self.save_path.parent.mkdir(parents=True, exist_ok=True)
        temporary_path = self.save_path.with_suffix(".tmp")
        temporary_path.write_text(
            json.dumps(state.to_dict(), ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        temporary_path.replace(self.save_path)
