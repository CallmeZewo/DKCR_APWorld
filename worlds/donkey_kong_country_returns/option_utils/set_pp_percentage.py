from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..world import DKCRWorld

def set_pp_percentage(dkcr_world: DKCRWorld):
    total_pp = dkcr_world.options.puzzle_piece_amount.value

    dkcr_world.options.jungle_boss_access.value = dkcr_world.options.jungle_boss_access.value * total_pp // 100
    dkcr_world.options.beach_boss_access.value = dkcr_world.options.beach_boss_access.value * total_pp // 100
    dkcr_world.options.ruins_boss_access.value = dkcr_world.options.ruins_boss_access.value * total_pp // 100
    dkcr_world.options.cave_boss_access.value = dkcr_world.options.cave_boss_access.value * total_pp // 100
    dkcr_world.options.forest_boss_access.value = dkcr_world.options.forest_boss_access.value * total_pp // 100
    dkcr_world.options.cliff_boss_access.value = dkcr_world.options.cliff_boss_access.value * total_pp // 100
    dkcr_world.options.factory_boss_access.value = dkcr_world.options.factory_boss_access.value * total_pp // 100
    dkcr_world.options.volcano_boss_access.value = dkcr_world.options.volcano_boss_access.value * total_pp // 100