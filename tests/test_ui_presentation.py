from __future__ import annotations

import sys
import unittest
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from items.items import Item
from maps.campaign import CampaignProgress
from ui.presentation import (
    compare_item,
    filter_inventory,
    map_status,
    next_objective,
)


class InventoryPresentationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.weapon = Item(
            "Espada",
            "Comum",
            "weapon",
            power=8,
            attack_bonus=8,
        )
        self.armor = Item(
            "Armadura",
            "Raro",
            "armor",
            power=12,
            defense_bonus=12,
        )

    def test_filters_inventory_by_official_category(self) -> None:
        items = [self.weapon, self.armor]

        self.assertEqual(filter_inventory(items, "Todos"), items)
        self.assertEqual(filter_inventory(items, "Armas"), [self.weapon])
        self.assertEqual(filter_inventory(items, "Armaduras"), [self.armor])
        self.assertEqual(filter_inventory(items, "Acessórios"), [])

    def test_comparison_uses_equipped_item_from_same_slot(self) -> None:
        stronger = Item(
            "Espada Melhor",
            "Raro",
            "weapon",
            power=13,
            attack_bonus=13,
        )

        comparison = compare_item(stronger, self.weapon)

        self.assertEqual(comparison.power_delta, 5)
        self.assertEqual(comparison.attack_delta, 5)
        self.assertTrue(comparison.is_upgrade)
        self.assertFalse(comparison.is_equipped)


class MapPresentationTests(unittest.TestCase):
    def test_map_status_separates_completed_current_and_locked(self) -> None:
        campaign = CampaignProgress(map_index=3, victories=4)

        self.assertEqual(map_status(campaign, 2), "completed")
        self.assertEqual(map_status(campaign, 3), "current")
        self.assertEqual(map_status(campaign, 4), "locked")

    def test_post_boss_state_always_exposes_next_direction(self) -> None:
        campaign = CampaignProgress(
            map_index=9,
            victories=1,
            act_completed=True,
        )

        objective = next_objective(campaign)

        self.assertIn("Ato I concluído", objective)
        self.assertIn("Free Farm", objective)
        self.assertIn("Veterano", objective)


if __name__ == "__main__":
    unittest.main()

