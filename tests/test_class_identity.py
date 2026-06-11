from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from game_state import SAVE_VERSION, GameState
from hero.hero import Hero
from ui.class_visuals import (
    RENDER_FRAME_NAMES,
    frame_names_for_action,
    resolve_visual_asset,
    visual_profile_for,
)
from ui.journey_scene import JourneySceneController


class HeroClassIdentityTests(unittest.TestCase):
    def test_new_hero_defaults_to_warrior(self) -> None:
        hero = Hero()

        self.assertEqual(hero.class_id, "warrior")
        self.assertEqual(hero.to_core_dict()["class_id"], "warrior")

    def test_archer_can_be_constructed_and_serialized(self) -> None:
        hero = Hero(class_id="archer")

        restored = Hero.from_dict(hero.to_dict())

        self.assertEqual(hero.class_id, "archer")
        self.assertEqual(restored.class_id, "archer")

    def test_unknown_class_falls_back_to_warrior(self) -> None:
        self.assertEqual(Hero(class_id="necromancer").class_id, "warrior")
        self.assertEqual(
            Hero.from_dict({"class_id": "unknown"}).class_id,
            "warrior",
        )

    def test_old_save_migrates_without_losing_progress(self) -> None:
        old_save = {
            "version": 2,
            "hero": {
                "name": "Veterano",
                "level": 8,
                "gold": 90,
                "inventory": [
                    {
                        "item_id": "legacy_sword",
                        "name": "Espada Antiga",
                        "rarity": "Comum",
                        "slot": "weapon",
                        "power": 7,
                        "attack_bonus": 7,
                        "defense_bonus": 0,
                    }
                ],
                "equipment": {
                    "weapon": {
                        "item_id": "legacy_sword",
                        "name": "Espada Antiga",
                        "rarity": "Comum",
                        "slot": "weapon",
                        "power": 7,
                        "attack_bonus": 7,
                        "defense_bonus": 0,
                    }
                },
            },
            "campaign": {"map_index": 4, "victories": 6},
        }

        state = GameState.from_dict(old_save)
        serialized = state.to_dict()

        self.assertEqual(state.save_version, SAVE_VERSION)
        self.assertEqual(state.hero.class_id, "warrior")
        self.assertEqual(state.hero.gold, 90)
        self.assertEqual(len(state.hero.inventory), 1)
        self.assertIsNotNone(state.hero.equipment["weapon"])
        self.assertEqual(state.campaign.map_index, 4)
        self.assertEqual(state.campaign.victories, 6)
        self.assertEqual(serialized["hero"]["class_id"], "warrior")


class ClassVisualMappingTests(unittest.TestCase):
    def test_archer_profile_prepares_ranged_attack(self) -> None:
        profile = visual_profile_for("archer")
        controller = JourneySceneController(
            hero_attack_action=profile.attack_action
        )
        controller.phase = "fight"

        controller.trigger_attack("hero_attack", 10)
        controller.update(0.05)

        self.assertEqual(profile.attack_action, "attack_ranged")
        self.assertEqual(controller.hero_action, "attack_ranged")
        self.assertIn(
            controller.hero_frame,
            frame_names_for_action("attack_ranged"),
        )

    def test_missing_class_or_animation_falls_back_to_warrior(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            asset_root = Path(temporary_directory)
            warrior_dir = asset_root / "warrior"
            warrior_dir.mkdir()
            warrior_victory = warrior_dir / "victory.png"
            warrior_victory.write_bytes(b"placeholder")

            missing_archer = resolve_visual_asset(
                asset_root,
                "archer",
                "victory",
            )
            unknown_class = resolve_visual_asset(
                asset_root,
                "unknown",
                "victory",
            )

        self.assertEqual(missing_archer, warrior_victory)
        self.assertEqual(unknown_class, warrior_victory)

    def test_required_frames_resolve_for_supported_classes(self) -> None:
        asset_root = PROJECT_ROOT / "src" / "assets"

        for class_id in ("warrior", "archer"):
            for frame_name in (*RENDER_FRAME_NAMES, "front"):
                with self.subTest(
                    class_id=class_id,
                    frame_name=frame_name,
                ):
                    self.assertIsNotNone(
                        resolve_visual_asset(
                            asset_root,
                            class_id,
                            frame_name,
                        )
                    )


class ArchitectureRegressionTests(unittest.TestCase):
    def test_manual_strategy_dependencies_are_not_in_source(self) -> None:
        forbidden_names = (
            "StrategySystem",
            "CombatStrategy",
            "ChangeCombatStrategy",
        )
        source = "\n".join(
            path.read_text(encoding="utf-8")
            for path in (PROJECT_ROOT / "src").rglob("*.py")
        )

        for name in forbidden_names:
            self.assertNotIn(name, source)


if __name__ == "__main__":
    unittest.main()
