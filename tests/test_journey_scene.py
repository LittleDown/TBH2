from __future__ import annotations

import sys
import unittest
from pathlib import Path
from random import Random

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from ui.journey_scene import JourneySceneController


class JourneySceneTests(unittest.TestCase):
    def test_explore_encounter_fight_flow_uses_delta_time(self) -> None:
        scene = JourneySceneController(rng=Random(1))
        scene.encounter_distance = 6

        events = scene.update(0.05)
        self.assertEqual(events, [])
        self.assertEqual(scene.phase, "explore")

        events = scene.update(0.05)
        self.assertEqual(events, ["encounter"])
        self.assertEqual(scene.phase, "encounter")

        for _ in range(40):
            events = scene.update(0.05)
            if "fight" in events:
                break
        self.assertEqual(scene.phase, "fight")
        self.assertEqual(scene.enemy_x, scene.enemy_home_x)

    def test_attack_has_lunge_hit_and_floating_damage(self) -> None:
        scene = JourneySceneController(rng=Random(1))
        scene.phase = "fight"
        scene.enemy_visible = True

        scene.trigger_attack("hero_attack", 17)
        scene.update(0.12)

        self.assertGreater(scene.hero_x, scene.hero_home_x)
        self.assertTrue(scene.enemy_hit_flash)
        self.assertEqual(scene.floaters[0].text, "-17")

        for _ in range(10):
            scene.update(0.05)
        self.assertEqual(scene.hero_x, scene.hero_home_x)

    def test_reward_death_returns_to_explore(self) -> None:
        scene = JourneySceneController(rng=Random(1))
        scene.phase = "fight"
        scene.enemy_visible = True
        scene.show_victory("+10 XP")

        for _ in range(10):
            scene.update(0.05)
        self.assertFalse(scene.enemy_visible)

        events: list[str] = []
        for _ in range(40):
            events.extend(scene.update(0.05))
        self.assertIn("explore", events)
        self.assertEqual(scene.phase, "explore")


if __name__ == "__main__":
    unittest.main()
