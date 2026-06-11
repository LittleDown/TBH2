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
        self.assertEqual(scene.world_speed_factor, 0)

    def test_encounter_decelerates_world_and_stops_hero_walk(self) -> None:
        scene = JourneySceneController(rng=Random(1))
        scene.encounter_distance = 1
        scene.update(0.05)

        self.assertEqual(scene.phase, "encounter")
        self.assertEqual(scene.hero_frame, "idle")
        self.assertEqual(scene.world_speed_percent, 100)

        scroll_steps = []
        for _ in range(15):
            before = scene.background_scroll
            scene.update(0.05)
            scroll_steps.append(scene.background_scroll - before)

        self.assertGreater(scroll_steps[0], scroll_steps[-1])
        self.assertEqual(scene.world_speed_percent, 0)

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

    def test_ambient_event_spawns_only_during_active_exploration(self) -> None:
        scene = JourneySceneController(rng=Random(4))
        scene.next_ambient_event = 0
        scene.update(0.05)

        self.assertGreater(len(scene.ambient_particles), 0)
        first_x = scene.ambient_particles[0].x
        scene.update(0.05)
        self.assertLess(scene.ambient_particles[0].x, first_x)

        scene.phase = "fight"
        scene.ambient_particles.clear()
        scene.next_ambient_event = 0
        scene.update(0.05)
        self.assertEqual(scene.ambient_particles, [])

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
            update_events = scene.update(0.05)
            events.extend(update_events)
            if "explore" in update_events:
                break
        self.assertIn("explore", events)
        self.assertEqual(scene.phase, "explore")
        self.assertEqual(scene.world_speed_percent, 0)

        scene.update(0.05)
        self.assertGreater(scene.world_speed_percent, 0)
        self.assertLess(scene.world_speed_percent, 100)


if __name__ == "__main__":
    unittest.main()
