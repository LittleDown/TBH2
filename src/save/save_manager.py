import json
from pathlib import Path

from hero.hero import Hero


class SaveManager:
    def __init__(self, save_path: Path) -> None:
        self.save_path = save_path

    def load(self) -> Hero:
        if not self.save_path.exists():
            return Hero()
        try:
            data = json.loads(self.save_path.read_text(encoding="utf-8"))
            return Hero.from_dict(data)
        except (OSError, ValueError, KeyError, TypeError):
            return Hero()

    def save(self, hero: Hero) -> None:
        temporary_path = self.save_path.with_suffix(".tmp")
        temporary_path.write_text(
            json.dumps(hero.to_dict(), ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        temporary_path.replace(self.save_path)

