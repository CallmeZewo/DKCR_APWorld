from __future__ import annotations
from typing import TYPE_CHECKING, Mapping

from .generate_locations import generate_world_location, generate_level_location
from ..data.levels import GameLevels
from ..data.worlds import GameWorlds
from ..data.constants import LevelIndex

if TYPE_CHECKING:
    from .. import DKCRWorld

def get_locations_for_world(dkcr_world: DKCRWorld, world: GameWorlds) -> Mapping[str, int | None]:
    locations_for_region: dict[str, int | None] = {}
    locations_for_world = generate_world_location(world)
    for location_name, code in locations_for_world.items():
        if "Puzzle Bundle" in location_name and dkcr_world.options.world_puzzle_piece_bundle == 0:
            continue
        elif "Kong Bundle" in location_name and dkcr_world.options.world_kong_bundle == 0:
            continue
        elif "[Bronze]" in location_name:
            if "Bronze" not in dkcr_world.selected_medals or dkcr_world.options.world_cleared_time_attack == 0:
                continue
        elif "[Silver]" in location_name:
            if "Silver" not in dkcr_world.selected_medals or dkcr_world.options.world_cleared_time_attack == 0:
                continue
        elif "[Gold]" in location_name:
            if "Gold" not in dkcr_world.selected_medals or dkcr_world.options.world_cleared_time_attack == 0:
                continue
        elif "[Shiny Gold]" in location_name:
            if "Shiny Gold" not in dkcr_world.selected_medals or dkcr_world.options.world_cleared_time_attack == 0:
                continue
        elif "(Mirror)" in location_name:
            if "Mirror Mode" in dkcr_world.selected_clear_types or dkcr_world.options.world_cleared_mirror == 0:
                continue
        elif "Cleared" in location_name:
            if "Normal" not in dkcr_world.selected_clear_types or dkcr_world.options.world_cleared == 0:
                continue
        locations_for_region[location_name] = code
    return locations_for_region

def get_locations_for_level(dkcr_world: DKCRWorld, world: GameWorlds, level: GameLevels) -> Mapping[str, int | None]:
    locations_for_region: dict[str, int | None] = {}
    locations_for_level = generate_level_location(world, level)
    for location_name, code in locations_for_level.items():
        if "[Bronze]" in location_name:
            if "Bronze" not in dkcr_world.selected_medals or "Time Attack" not in dkcr_world.selected_clear_types:
                continue
        elif "[Silver]" in location_name:
            if "Silver" not in dkcr_world.selected_medals or "Time Attack" not in dkcr_world.selected_clear_types:
                continue
        elif "[Gold]" in location_name:
            if "Gold" not in dkcr_world.selected_medals or "Time Attack" not in dkcr_world.selected_clear_types:
                continue
        elif "[Shiny Gold]" in location_name:
            if "Shiny Gold" not in dkcr_world.selected_medals or "Time Attack" not in dkcr_world.selected_clear_types:
                continue
        elif "(Mirror)" in location_name and "Mirror Mode" not in dkcr_world.selected_clear_types:
            continue
        elif "Cleared" in location_name and "Normal" not in dkcr_world.selected_clear_types and level.level_index != LevelIndex.BOSS_LEVEL_INDEX:
            continue
        elif "Kong Letter" in location_name and dkcr_world.options.k_level.value == 0:
            continue
        elif "Puzzle Piece" in location_name and dkcr_world.options.puzzle_pieces == 0:
            continue
        locations_for_region[location_name] = code
    return locations_for_region