from __future__ import annotations

from dataclasses import dataclass

ACT_ONE_ID = "act_1"
ACT_ONE_NAME = "Fronteira Esquecida"
NORMAL_DIFFICULTY_ID = "normal"


@dataclass(frozen=True)
class MapDefinition:
    map_id: str
    name: str
    recommended_level: int
    monster_pool: tuple[str, ...]
    boss_id: str | None = None


ACT_ONE_MAPS = (
    MapDefinition(
        "abandoned_road",
        "Estrada Abandonada",
        1,
        ("giant_rat", "hostile_crow"),
    ),
    MapDefinition(
        "whispering_woods",
        "Bosque dos Sussurros",
        2,
        ("gray_wolf", "giant_spider"),
    ),
    MapDefinition(
        "raided_camp",
        "Acampamento Saqueado",
        3,
        ("raider", "bandit"),
    ),
    MapDefinition(
        "frontier_hills",
        "Colinas da Fronteira",
        4,
        ("veteran_bandit", "alpha_wolf"),
    ),
    MapDefinition(
        "vigil_cemetery",
        "Cemitério da Vigília",
        5,
        ("skeleton_warrior", "wandering_spirit"),
    ),
    MapDefinition(
        "monastery_ruins",
        "Ruínas do Mosteiro",
        6,
        ("cultist", "undead"),
    ),
    MapDefinition(
        "broken_bridge",
        "Ponte Quebrada",
        7,
        ("skeleton_guardian", "dead_archer"),
    ),
    MapDefinition(
        "ruined_fortress",
        "Fortaleza Arruinada",
        8,
        ("skeleton_knight", "necromancer"),
    ),
    MapDefinition(
        "hall_of_the_fallen",
        "Salão dos Caídos",
        9,
        ("elite_undead", "lord_of_bones_guard"),
    ),
    MapDefinition(
        "lord_of_bones_lair",
        "Covil do Senhor dos Ossos",
        10,
        ("lord_of_bones_guard",),
        boss_id="lord_of_bones",
    ),
)


def get_map_definition(map_index: int) -> MapDefinition:
    safe_index = max(0, min(len(ACT_ONE_MAPS) - 1, map_index))
    return ACT_ONE_MAPS[safe_index]

