from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..world import DKCRWorld

def set_letter_percentage(dkcr_world: DKCRWorld):
    total_jungle_pp = dkcr_world.options.jungle_kong_letter_amount.value
    total_beach_pp = dkcr_world.options.beach_kong_letter_amount.value
    total_ruins_pp = dkcr_world.options.ruins_kong_letter_amount.value
    total_cave_pp = dkcr_world.options.cave_kong_letter_amount.value
    total_forest_pp = dkcr_world.options.forest_kong_letter_amount.value
    total_cliff_pp = dkcr_world.options.cliff_kong_letter_amount.value
    total_factory_pp = dkcr_world.options.factory_kong_letter_amount.value
    total_volcano_pp = dkcr_world.options.volcano_kong_letter_amount.value

    dkcr_world.options.jungle_k_level_access.value = dkcr_world.options.jungle_k_level_access.value * total_jungle_pp // 100
    dkcr_world.options.beach_k_level_access.value = dkcr_world.options.beach_k_level_access.value * total_beach_pp // 100
    dkcr_world.options.ruins_k_level_access.value = dkcr_world.options.ruins_k_level_access.value * total_ruins_pp // 100
    dkcr_world.options.cave_k_level_access.value = dkcr_world.options.cave_k_level_access.value * total_cave_pp // 100
    dkcr_world.options.forest_k_level_access.value = dkcr_world.options.forest_k_level_access.value * total_forest_pp // 100
    dkcr_world.options.cliff_k_level_access.value = dkcr_world.options.cliff_k_level_access.value * total_cliff_pp // 100
    dkcr_world.options.factory_k_level_access.value = dkcr_world.options.factory_k_level_access.value * total_factory_pp // 100
    dkcr_world.options.volcano_k_level_access.value = dkcr_world.options.volcano_k_level_access.value * total_volcano_pp // 100