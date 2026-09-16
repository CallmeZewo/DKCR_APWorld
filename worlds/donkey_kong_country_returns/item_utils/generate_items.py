from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import ItemClassification
from ..data.items import GameItems
from .generate_filler import generate_filler
from .dkcr_item import DKCRItem

if TYPE_CHECKING:
    from ..world import DKCRWorld

def generate_all_items(dkcr_world: DKCRWorld):
    itempool = dkcr_world.multiworld.itempool

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
            print("no")
            return 0

    if item.display_name == GameItems.PROGRESSIVE_FACTORY_BUTTON.display_name:
        return dkcr_world.options.factory_buttons.value

    if item.display_name == GameItems.MIRROR_SHARD.display_name:
        if "Mirror Mode" not in dkcr_world.selected_clear_types:
            return 0
        return dkcr_world.options.mirror_mode_shards.value

    if item.display_name == GameItems.MIRROR_MODE.display_name:
        if (
            dkcr_world.options.mirror_mode_shards.value == 0
            and "Mirror Mode" in dkcr_world.selected_clear_types
        ):
            return 0

    if "Kong Letter" in item.display_name:
        if dkcr_world.options.k_level.value == 0:
            return 0

    if item.display_name == GameItems.PUZZLE_PIECE.display_name:
        if dkcr_world.options.puzzle_pieces.value == 0:
            return 0

        if dkcr_world.options.k_level.value == 0:
            if dkcr_world.options.golden_temple.value == 0:
                return item.amount - 45
            return item.amount - 40


    if item.display_name == GameItems.PROGRESSIVE_BOSS_UNLOCK.display_name:
        if dkcr_world.options.puzzle_pieces.value == 1:
            return 0

    return item.amount
