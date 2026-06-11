from __future__ import annotations

from dataclasses import dataclass
from typing import Literal, Sequence

from items.items import Item
from maps.campaign import CampaignProgress
from maps.world import ACT_ONE_MAPS

InventoryFilter = Literal["Todos", "Armas", "Armaduras", "Acessórios"]
MapStatus = Literal["completed", "current", "locked"]


@dataclass(frozen=True)
class ItemComparison:
    power_delta: int
    attack_delta: int
    defense_delta: int
    is_equipped: bool
    is_upgrade: bool


def filter_inventory(
    items: Sequence[Item],
    selected_filter: InventoryFilter,
) -> list[Item]:
    slot_by_filter = {
        "Armas": "weapon",
        "Armaduras": "armor",
        "Acessórios": "accessory",
    }
    slot = slot_by_filter.get(selected_filter)
    if slot is None:
        return list(items)
    return [item for item in items if item.slot == slot]


def compare_item(
    selected: Item,
    equipped: Item | None,
) -> ItemComparison:
    equipped_power = equipped.power if equipped else 0
    equipped_attack = equipped.attack_bonus if equipped else 0
    equipped_defense = equipped.defense_bonus if equipped else 0
    is_equipped = (
        equipped is not None and selected.item_id == equipped.item_id
    )
    return ItemComparison(
        power_delta=selected.power - equipped_power,
        attack_delta=selected.attack_bonus - equipped_attack,
        defense_delta=selected.defense_bonus - equipped_defense,
        is_equipped=is_equipped,
        is_upgrade=selected.power > equipped_power,
    )


def map_status(campaign: CampaignProgress, map_index: int) -> MapStatus:
    if map_index < campaign.map_index or campaign.act_completed:
        return "completed"
    if map_index == campaign.map_index:
        return "current"
    return "locked"


def next_objective(campaign: CampaignProgress) -> str:
    if campaign.act_completed:
        return (
            "Ato I concluído. Free Farm e dificuldade Veterano "
            "estão em preparação."
        )
    if campaign.next_encounter_is_boss:
        return "Próximo objetivo: derrotar o Senhor dos Ossos."
    return (
        f"Próximo objetivo: concluir {campaign.current_map} "
        f"({campaign.victories}/{campaign.target})."
    )


def current_map_summary(campaign: CampaignProgress) -> str:
    map_definition = ACT_ONE_MAPS[campaign.map_index]
    if campaign.act_completed:
        return f"{map_definition.name} · Chefe derrotado"
    return (
        f"{map_definition.name} · "
        f"{campaign.victories}/{campaign.target}"
    )

