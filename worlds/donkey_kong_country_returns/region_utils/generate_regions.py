from __future__ import annotations
from typing import TYPE_CHECKING
from BaseClasses import Region

from ..data.worlds import GameWorlds
from ..data.constants import WorldIndex as Wi, LevelIndex as Li

if TYPE_CHECKING:
    from ..world import DKCRWorld

def generate_all_regions(dkcr_world: DKCRWorld):
    regions = dkcr_world.multiworld.regions
    for world in GameWorlds:
        if world.world_index == Wi.GOLDEN_TEMPLE_WORLD_INDEX and dkcr_world.options.golden_temple.value == 0:
            continue
        regions.append(create_region(world.display_name, dkcr_world))
        for level in world.level_list:
            if level.level_index == Li.K_LEVEL_INDEX and dkcr_world.options.k_level.value == 0 and "Gold" not in level.display_name:
                continue
            regions.append(create_region(level.display_name, dkcr_world))


def create_region(name: str, dkcr_world: DKCRWorld) -> Region:
    return Region(name, dkcr_world.player, dkcr_world.multiworld)