from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from .world import DKCR

ITEM_NAME_TO_ID = {
    "Puzzle Piece": 1,
    "Kong Letter": 2,
    "Jungle Shop Key": 3,
    "Beach Shop Key": 4,
    "Ruins Shop Key": 5,
    "Cave Shop Key": 6,
    "Forest Shop Key": 7,
    "Cliff Shop Key": 8,
    "Factory Shop Key": 9,
    "Volcano Shop Key": 10,
    "Balloon": 11,
    "Defeated Boss 1": 12,
    "Defeated Boss 2": 13,
    "Defeated Boss 3": 14,
    "Defeated Boss 4": 15,
    "Defeated Boss 5": 16,
    "Defeated Boss 6": 17,
    "Defeated Boss 7": 18,
    "Defeated Boss 8": 19,
}

DEFAULT_ITEM_CLASSIFICATIONS = {
    "Puzzle Piece": ItemClassification.progression,
    "Kong Letter": ItemClassification.progression,
    "Jungle Shop Key": ItemClassification.progression,
    "Beach Shop Key": ItemClassification.progression,
    "Ruins Shop Key": ItemClassification.progression,
    "Cave Shop Key": ItemClassification.progression,
    "Forest Shop Key": ItemClassification.progression,
    "Cliff Shop Key": ItemClassification.progression,
    "Factory Shop Key": ItemClassification.progression,
    "Volcano Shop Key": ItemClassification.progression,
    "Balloon": ItemClassification.filler,
    "Defeated Boss 1": ItemClassification.progression,
    "Defeated Boss 2": ItemClassification.progression,
    "Defeated Boss 3": ItemClassification.progression,
    "Defeated Boss 4": ItemClassification.progression,
    "Defeated Boss 5": ItemClassification.progression,
    "Defeated Boss 6": ItemClassification.progression,
    "Defeated Boss 7": ItemClassification.progression,
    "Defeated Boss 8": ItemClassification.progression,
}

class DKCRItem(Item):
    game = "Donkey Kong Country Returns"

def get_random_filler_item_name(world: DKCR) -> str:
    return "Balloon"

def create_item_with_correct_classification(world: DKCR, name: str) -> DKCRItem:
    classification = DEFAULT_ITEM_CLASSIFICATIONS[name]

    return DKCRItem(name, classification, ITEM_NAME_TO_ID[name], world.player)

def create_all_items(world: DKCR) -> None:
    itempool: list[Item] = [
        world.create_item("Puzzle Piece"),
        world.create_item("Kong Letter"),
        world.create_item("Jungle Shop Key"),
        world.create_item("Beach Shop Key"),
        world.create_item("Ruins Shop Key"),
        world.create_item("Cave Shop Key"),
        world.create_item("Forest Shop Key"),
        world.create_item("Cliff Shop Key"),
        world.create_item("Factory Shop Key"),
        world.create_item("Volcano Shop Key"),
        world.create_item("Defeated Boss 1"),
        world.create_item("Defeated Boss 2"),
        world.create_item("Defeated Boss 3"),
        world.create_item("Defeated Boss 4"),
        world.create_item("Defeated Boss 5"),
        world.create_item("Defeated Boss 6"),
        world.create_item("Defeated Boss 7"),
        world.create_item("Defeated Boss 8"),
    ]

    number_of_Items = len(itempool)

    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))

    needed_number_of_filler_items = number_of_unfilled_locations - number_of_Items

    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]

    world.multiworld.itempool += itempool