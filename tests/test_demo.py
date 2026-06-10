from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path
from random import Random

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from combat.combat import CombatEngine
from enemies.enemies import Enemy
from game_state import GameState
from hero.hero import Hero
from items.items import Item
from maps.campaign import CampaignProgress
from save.save_manager import SaveManager


class HeroTests(unittest.TestCase):
    def test_strategies_modify_effective_attributes(self) -> None:
        hero = Hero()

        hero.set_strategy("Agressivo")
        self.assertEqual((hero.attack, hero.defense), (12, 4))

        hero.set_strategy("Defensivo")
        self.assertEqual((hero.attack, hero.defense), (8, 6))

        hero.set_strategy("Balanceado")
        self.assertEqual((hero.attack, hero.defense), (10, 5))

    def test_manual_equipment_uses_inventory_item(self) -> None:
        hero = Hero()
        sword = Item(
            "Espada de Teste",
            "Raro",
            "weapon",
            power=7,
            attack_bonus=7,
        )
        hero.add_item(sword)

        equipped = hero.equip(sword.item_id)

        self.assertIs(equipped, sword)
        self.assertTrue(hero.is_equipped(sword))
        self.assertEqual(hero.attack, 17)
        self.assertIn("accessory", hero.equipment)
        self.assertIsNone(hero.equipment["accessory"])


class CampaignTests(unittest.TestCase):
    def test_act_one_advances_through_maps_and_boss(self) -> None:
        campaign = CampaignProgress()

        for _ in range(9):
            for _ in range(10):
                campaign.register_victory()

        self.assertEqual(campaign.map_index, 9)
        self.assertEqual(campaign.victories, 0)

        for _ in range(9):
            campaign.register_victory()

        self.assertTrue(campaign.next_encounter_is_boss)
        result = campaign.register_victory(is_boss=True)
        self.assertTrue(result.act_completed)
        self.assertTrue(campaign.act_completed)


class CombatTests(unittest.TestCase):
    def test_victory_grants_rewards_and_map_progress(self) -> None:
        state = GameState()
        engine = CombatEngine(state, Random(3))
        engine.enemy = Enemy(
            name="Alvo",
            level=1,
            max_hp=1,
            current_hp=1,
            attack=0,
            defense=0,
            xp_reward=25,
            gold_reward=11,
        )

        events = engine.tick()

        self.assertEqual(state.hero.xp, 25)
        self.assertEqual(state.hero.gold, 11)
        self.assertEqual(state.hero.enemies_defeated, 1)
        self.assertEqual(state.campaign.victories, 1)
        self.assertIn("victory", {event.kind for event in events})
        self.assertEqual(events[0].amount, 10)

    def test_boss_is_created_on_final_map_threshold(self) -> None:
        state = GameState(campaign=CampaignProgress(map_index=9, victories=9))
        engine = CombatEngine(state, Random(1))

        self.assertTrue(engine.enemy.is_boss)
        self.assertEqual(engine.enemy.name, "Capitão Ossonegro")

    def test_defeating_boss_completes_act_one(self) -> None:
        state = GameState(campaign=CampaignProgress(map_index=9, victories=9))
        engine = CombatEngine(state, Random(1))
        engine.enemy.current_hp = 1

        events = engine.tick()

        self.assertTrue(state.campaign.act_completed)
        self.assertEqual(state.hero.bosses_defeated, 1)
        self.assertIn("act_complete", {event.kind for event in events})


class SaveTests(unittest.TestCase):
    def test_old_save_is_migrated_and_round_trips(self) -> None:
        old_save = {
            "name": "Aventureiro",
            "level": 2,
            "xp": 15,
            "max_hp": 120,
            "current_hp": 90,
            "base_attack": 13,
            "base_defense": 7,
            "equipment": {"weapon": None, "armor": None},
            "statistics": {"enemies_defeated": 4, "deaths": 1},
        }

        with tempfile.TemporaryDirectory() as temporary_directory:
            save_path = Path(temporary_directory) / "save.json"
            save_path.write_text(
                json.dumps(old_save, ensure_ascii=False),
                encoding="utf-8",
            )
            manager = SaveManager(save_path)

            state = manager.load()
            state.hero.gold = 42
            state.campaign.victories = 3
            manager.save(state)
            loaded_again = manager.load()

        self.assertEqual(loaded_again.version, 2)
        self.assertEqual(loaded_again.hero.level, 2)
        self.assertEqual(loaded_again.hero.gold, 42)
        self.assertIn("accessory", loaded_again.hero.equipment)
        self.assertIsNone(loaded_again.hero.equipment["accessory"])
        self.assertEqual(loaded_again.campaign.victories, 3)


if __name__ == "__main__":
    unittest.main()
