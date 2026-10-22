from __future__ import annotations
from typing import TYPE_CHECKING

from ..data.constants import LevelName
from ..rule_utils import *

if TYPE_CHECKING:
    from ..world import DKCRWorld

key_levels = [LevelName.SUNSET_SHORE, LevelName.BLOWHOLE_BOUND, LevelName.DAMP_DUNGEON, LevelName.MOLE_PATROL,
              LevelName.SPRINGY_SPORES, LevelName.PRECARIOUS_PLATEAU, LevelName.HANDY_HAZARDS, LevelName.SMOKEY_PEAK]

def create_location_rules(dkcr_world: DKCRWorld):
    locations = dkcr_world.get_locations()
    for location in locations:
        if "(Mirror)" in location.name:
            dkcr_world.set_rule(location, has_mirror_mode)