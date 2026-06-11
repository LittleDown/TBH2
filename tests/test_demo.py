from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path
from random import Random

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from application.game_session import GameSession
from balance import enemy_rewards, xp_required_for_level
from combat.combat import CombatSystem
from enemies.enemies import Enemy, generate_enemy
from game_state import SAVE_VERSION, GameState
from hero.hero import Hero
from items.items import Item, roll_loot
from maps.campaign import CampaignProgress, MAP_NAMES
from save.save_manager import SaveManager


class HeroTests(unittest.TestCase):
    def test_legacy_strategy_is_ignored(self) -> None:
        hero = Hero.from_dict({"strategy": "Agressivo"})

        self.assertEqual((hero.attack, hero.defense), (10, 5))
        self.assertNotIn("strategy", hero.to_dict())

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
        self.assertEqual(hero.equipment_power, 7)
        self.assertIn("accessory", hero.equipment)

    def test_autoequip_preserves_favorite_or_locked_item(self) -> None:
        hero = Hero()
        protected = Item(
            "Espada Favorita",
            "Comum",
            "weapon",
            power=2,
            attack_bonus=2,
            favorite=True,
        )
        stronger = Item(
            "Espada Forte",
            "Raro",
            "weapon",
            power=8,
            attack_bonus=8,
        )
        hero.add_item(protected)

        equipped = hero.add_item(stronger)

        self.assertFalse(equipped)
        self.assertIs(hero.equipment["weapon"], protected)


class CampaignTests(unittest.TestCase):
    def test_act_one_uses_official_maps_and_boss_gate(self) -> None:
        campaign = CampaignProgress()
        self.assertEqual(MAP_NAMES[3], "Colinas da Fronteira")
        self.assertEqual(MAP_NAMES[-1], "Covil do Senhor dos Ossos")

        for _ in range(9):
            for _ in range(10):
                campaign.register_victory()

        self.assertEqual(campaign.map_index, 9)
        self.assertEqual(campaign.victories, 0)
        self.assertEqual(campaign.target, 1)
        self.assertTrue(campaign.next_encounter_is_boss)

        ignored = campaign.register_victory(is_boss=False)
        self.assertFalse(ignored.act_completed)
        result = campaign.register_victory(is_boss=True)
        self.assertTrue(result.act_completed)
        self.assertTrue(campaign.act_completed)

    def test_legacy_final_map_progress_keeps_boss_pending(self) -> None:
        campaign = CampaignProgress.from_dict(
            {"map_index": 9, "victories": 9, "act_completed": False}
        )

        self.assertEqual(campaign.victories, 0)
        self.assertEqual(campaign.target, 1)
        self.assertTrue(campaign.next_encounter_is_boss)


class EncounterTests(unittest.TestCase):
    def test_encounter_comes_from_current_map_pool(self) -> None:
        campaign = CampaignProgress(map_index=0)

        enemy = generate_enemy(campaign, Random(2), category="common")

        self.assertIn(enemy.definition_id, {"giant_rat", "hostile_crow"})
        self.assertEqual(enemy.level, 1)
        self.assertEqual(enemy.map_id, "abandoned_road")

    def test_final_map_creates_official_boss(self) -> None:
        campaign = CampaignProgress(map_index=9)

        enemy = generate_enemy(campaign, Random(1))

        self.assertTrue(enemy.is_boss)
        self.assertEqual(enemy.name, "Senhor dos Ossos")
        self.assertEqual(enemy.category, "boss")


class CombatTests(unittest.TestCase):
    @staticmethod
    def target_enemy(**overrides: object) -> Enemy:
        values = {
            "name": "Alvo",
            "level": 1,
            "max_hp": 1,
            "current_hp": 1,
            "attack": 0,
            "defense": 0,
            "xp_reward": 25,
            "gold_reward": 11,
        }
        values.update(overrides)
        return Enemy(**values)

    def test_combat_system_only_resolves_the_fight(self) -> None:
        hero = Hero()
        enemy = self.target_enemy()

        events = CombatSystem().resolve_turn(hero, enemy, hero_turn=True)

        self.assertEqual(hero.xp, 0)
        self.assertEqual(hero.gold, 0)
        self.assertIn("victory", {event.kind for event in events})
        self.assertEqual(events[0].amount, 10)

    def test_session_grants_rewards_and_map_progress(self) -> None:
        state = GameState()
        session = GameSession(state, Random(3))
        session.enemy = self.target_enemy()

        events = session.tick()

        self.assertEqual(state.hero.xp, 25)
        self.assertEqual(state.hero.gold, 11)
        self.assertEqual(state.hero.enemies_defeated, 1)
        self.assertEqual(state.campaign.victories, 1)
        self.assertIn("victory", {event.kind for event in events})

    def test_defeat_revives_hero_without_advancing_map(self) -> None:
        state = GameState()
        session = GameSession(state, Random(4))
        session.enemy = self.target_enemy(
            current_hp=100,
            max_hp=100,
            attack=500,
        )
        session.hero_turn = False

        events = session.tick()

        self.assertEqual(state.hero.deaths, 1)
        self.assertEqual(state.hero.current_hp, state.hero.max_hp)
        self.assertEqual(state.campaign.victories, 0)
        self.assertIn("defeat", {event.kind for event in events})

    def test_defeating_boss_completes_act_one(self) -> None:
        state = GameState(campaign=CampaignProgress(map_index=9))
        session = GameSession(state, Random(1))
        session.enemy.current_hp = 1

        events = session.tick()

        self.assertTrue(state.campaign.act_completed)
        self.assertEqual(state.hero.bosses_defeated, 1)
        self.assertIn("act_complete", {event.kind for event in events})


class BalanceTests(unittest.TestCase):
    def test_xp_curve_is_monotonic_and_slows_progression(self) -> None:
        requirements = [xp_required_for_level(level) for level in range(1, 21)]
        self.assertEqual(requirements, sorted(requirements))
        self.assertGreater(requirements[-1], requirements[0] * 30)

        hero = Hero()
        for map_level in range(1, 10):
            xp_reward, _ = enemy_rewards(
                map_level,
                "common",
                "normal",
                variation=1.0,
            )
            hero.gain_xp(xp_reward * 10)
        self.assertGreaterEqual(hero.level, 4)
        self.assertLessEqual(hero.level, 7)

    def test_boss_always_rolls_loot(self) -> None:
        item = roll_loot(10, Random(5), category="boss")
        self.assertIsNotNone(item)

    def test_campaign_can_defeat_the_final_boss_across_seeds(self) -> None:
        for seed in range(20):
            state = GameState()
            session = GameSession(state, Random(seed))

            for _ in range(3000):
                session.tick()
                if state.campaign.act_completed:
                    break

            self.assertTrue(state.campaign.act_completed, f"seed {seed}")
            self.assertEqual(state.hero.bosses_defeated, 1)
            self.assertLess(state.hero.level, 10)


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
            "strategy": "Defensivo",
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
            saved_data = json.loads(save_path.read_text(encoding="utf-8"))

        self.assertEqual(loaded_again.save_version, SAVE_VERSION)
        self.assertEqual(loaded_again.hero.class_id, "warrior")
        self.assertEqual(loaded_again.hero.level, 2)
        self.assertEqual(loaded_again.hero.gold, 42)
        self.assertEqual(loaded_again.campaign.victories, 3)
        self.assertEqual(saved_data["save_version"], SAVE_VERSION)
        self.assertEqual(saved_data["hero"]["class_id"], "warrior")
        self.assertNotIn("strategy", saved_data["hero"])
        self.assertIn("world_progress", saved_data)

    def test_version_two_nested_save_is_migrated(self) -> None:
        old_save = {
            "version": 2,
            "hero": {
                "name": "Veterano",
                "level": 8,
                "gold": 90,
                "strategy": "Agressivo",
            },
            "campaign": {"map_index": 4, "victories": 6},
        }

        state = GameState.from_dict(old_save)

        self.assertEqual(state.hero.name, "Veterano")
        self.assertEqual(state.hero.level, 8)
        self.assertEqual(state.hero.attack, 10)
        self.assertEqual(state.campaign.map_index, 4)

    def test_corrupt_primary_save_recovers_from_backup(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            save_path = Path(temporary_directory) / "save.json"
            manager = SaveManager(save_path)
            state = GameState()
            state.hero.gold = 7
            manager.save(state)
            state.hero.gold = 9
            manager.save(state)
            save_path.write_text("{corrompido", encoding="utf-8")

            recovered = manager.load()
            restored_data = json.loads(save_path.read_text(encoding="utf-8"))

        self.assertEqual(recovered.hero.gold, 7)
        self.assertEqual(restored_data["wallet"]["gold"], 7)


if __name__ == "__main__":
    unittest.main()
