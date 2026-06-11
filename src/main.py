from argparse import ArgumentParser, Namespace
from pathlib import Path
from typing import Sequence

from hero.classes import SUPPORTED_CLASS_IDS
from save.save_manager import SaveManager
from ui.main_window import MainWindow


def parse_args(argv: Sequence[str] | None = None) -> Namespace:
    parser = ArgumentParser(description="TBH2 - TaskBar Hero 2")
    parser.add_argument(
        "--class-id",
        choices=sorted(SUPPORTED_CLASS_IDS),
        help=(
            "Define e persiste a classe do heroi atual. "
            "Uso tecnico enquanto a selecao em UI nao existe."
        ),
    )
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> None:
    args = parse_args(argv)
    project_root = Path(__file__).resolve().parent.parent
    save_manager = SaveManager(project_root / "save.json")
    state = save_manager.load()
    if args.class_id is not None:
        state.hero.class_id = args.class_id
        save_manager.save(state)
    app = MainWindow(state, save_manager)
    app.mainloop()


if __name__ == "__main__":
    main()
