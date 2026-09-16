from __future__ import annotations
from typing import TYPE_CHECKING
from ..data.connection import CONNECTIONS
from .get_region import get_region_type
from ..data.worlds import GameWorlds
from ..data.constants.level_constants import LevelName as Ln

if TYPE_CHECKING:
    from ..world import DKCRWorld

def connect_all_regions(dkcr_world: DKCRWorld):
    for region in dkcr_world.get_regions():
        region_type = get_region_type(region.name)
        for connection in CONNECTIONS.get(region_type, []):

            if (dkcr_world.options.golden_temple.value == 0
                    and connection.target.display_name == GameWorlds.GOLDEN_TEMPLE_WORLD.display_name):
                continue

            if (dkcr_world.options.k_level.value == 0
                    and connection.target.display_name in [
                        Ln.PLATFORM_PANIC, Ln.TUMBLIN_TEMPLE, Ln.SHIFTY_SMASHERS, Ln.JAGGED_JEWELS,
                        Ln.BLAST_N_BOUNCE, Ln.PERILOUS_PASSAGE, Ln.TREACHEROUS_TRACK, Ln.FIVE_MONKEY_TRIAL
                ]):
                continue

            target_region = dkcr_world.get_region(connection.target.display_name)
            region.connect(target_region, f"From {region.name} to {target_region.name}", connection.rule)