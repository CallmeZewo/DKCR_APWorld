from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import ItemClassification
from ..data.items import GameItems
from .generate_filler import generate_filler
from .dkcr_item import DKCRItem

if TYPE_CHECKING:
    from ..world import DKCRWorld

def generate_all_items(dkcr_world: DKCRWorld):
    itempool: list[DKCRItem] = []

    for item in GameItems:
        amount = get_item_amount(dkcr_world, item)

        for _ in range(amount):
            itempool.append(
                create_item_with_correct_classification(
                    dkcr_world,
                    item.display_name
                )
            )

    generate_filler(
        len(dkcr_world.multiworld.get_unfilled_locations(dkcr_world.player)) - len(itempool),
        dkcr_world
    )

    dkcr_world.multiworld.itempool += itempool


def create_item_with_correct_classification(world:DKCRWorld, item_name: str) -> DKCRItem:
    item = GameItems.from_display_name(item_name)
    classification = item.classification
    code = item.code
    return DKCRItem(item_name, classification, code, world.player)

def generate_item_name_to_id():
    item_name_to_id: dict[str, int] = {}
    for item in GameItems:
        item_name_to_id[item.display_name] = item.code
    return item_name_to_id

def get_item_amount(dkcr_world: DKCRWorld, item: GameItems) -> int:
    if item.classification == ItemClassification.filler:
        return 0

    if item.display_name == GameItems.SQUAWKS.display_name:
        if dkcr_world.options.squawks.value == 0:
            return 0

    if item.display_name == GameItems.PROGRESSIVE_FACTORY_BUTTON.display_name:
        return dkcr_world.options.factory_buttons.value

    if item.display_name == GameItems.MIRROR_SHARD.display_name:
        if "Mirror Mode" not in dkcr_world.selected_clear_types:
            return 0
        return dkcr_world.options.mirror_mode_shards.value

    if item.display_name == GameItems.MIRROR_MODE.display_name:
        if (
            dkcr_world.options.mirror_mode_shards.value != 0
            or "Mirror Mode" not in dkcr_world.selected_clear_types
        ):
            return 0

    if "Kong Letter" in item.display_name:
        if dkcr_world.options.kong_letter.value == 0:
            return 0

    if item.display_name == GameItems.RARE_ORB.display_name:
        if dkcr_world.options.goal.value == 1:
            return dkcr_world.options.rare_orbs.value
        else:
            return 0

    if item.display_name == GameItems.PUZZLE_PIECE.display_name:
        if dkcr_world.options.puzzle_pieces.value == 0:
            return 0

    if item.display_name == GameItems.PROGRESSIVE_BOSS_UNLOCK.display_name:
        if dkcr_world.options.puzzle_pieces.value == 1:
            return 0

    if item.display_name == GameItems.PROGRESSIVE_K_LEVEL_UNLOCK.display_name:
        if dkcr_world.options.kong_letter.value == 1:
            return 0

    if item.display_name == GameItems.JUNGLE_KEY.display_name:
        if dkcr_world.options.sunset_shore_key.value == 0:
            return 0

    if item.display_name == GameItems.BEACH_KEY.display_name:
        if dkcr_world.options.blowhole_bound_key.value == 0:
            return 0

    if item.display_name == GameItems.RUINS_KEY.display_name:
        if dkcr_world.options.damp_dungeon_key.value == 0:
            return 0

    if item.display_name == GameItems.CAVE_KEY.display_name:
        if dkcr_world.options.mole_patrol_key.value == 0:
            return 0

    if item.display_name == GameItems.FOREST_KEY.display_name:
        if dkcr_world.options.springy_spores_key.value == 0:
            return 0

    if item.display_name == GameItems.CLIFF_KEY.display_name:
        if dkcr_world.options.precarious_plateau_key.value == 0:
            return 0

    if item.display_name == GameItems.FACTORY_KEY.display_name:
        if dkcr_world.options.handy_hazards_key.value == 0:
            return 0

    if item.display_name == GameItems.VOLCANO_KEY.display_name:
        if dkcr_world.options.smokey_peak_key.value == 0:
            return 0

    return item.amount
