from pathlib import Path

from save.save_manager import SaveManager
from ui.main_window import MainWindow


def main() -> None:
    project_root = Path(__file__).resolve().parent.parent
    save_manager = SaveManager(project_root / "save.json")
    hero = save_manager.load()
    app = MainWindow(hero, save_manager)
    app.mainloop()


if __name__ == "__main__":
    main()

