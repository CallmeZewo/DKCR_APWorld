from __future__ import annotations
from typing import TYPE_CHECKING

from ..location_utils import get_locations_for_world
from ..location_utils import get_locations_for_level
from ..location_utils.dkcr_location import DKCRLocation
from ..data.worlds import GameWorlds

if TYPE_CHECKING:
    from ..world import DKCRWorld

def fill_all_regions(dkcr_world: DKCRWorld):
    regions = {
        region.name: region
        for region in dkcr_world.get_regions()
    }

    for world in GameWorlds:
        if region := regions.get(world.display_name):
            region.add_locations(
                get_locations_for_world(dkcr_world, world),
                DKCRLocation
            )
        for level in world.level_list:
            if region := regions.get(level.display_name):
                region.add_locations(
                    get_locations_for_level(dkcr_world, world, level),
                    DKCRLocation
                )