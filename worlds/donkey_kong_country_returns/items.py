from __future__ import annotations

from typing import TYPE_CHECKING, NamedTuple, Optional, Dict

from BaseClasses import Item, ItemClassification as IC

from strings import Item as I

if TYPE_CHECKING:
    from .world import DKCRWorld

class ItemData(NamedTuple):
    code: Optional[int]
    classification: IC
    amount: Optional[int] = 1

item_table: Dict[str, ItemData] = {
    I.PUZZLE_PIECE: ItemData(1, IC.progression, 366),
    I.Kong_Letter.KONG_LETTER_JUNGLE: ItemData(2, IC.progression, 24),
    I.Kong_Letter.KONG_LETTER_BEACH: ItemData(3, IC.progression, 28),
    I.Kong_Letter.KONG_LETTER_RUINS: ItemData(4, IC.progression, 24),
    I.Kong_Letter.KONG_LETTER_CAVE: ItemData(5, IC.progression, 20),
    I.Kong_Letter.KONG_LETTER_FOREST: ItemData(6, IC.progression, 32),
    I.Kong_Letter.KONG_LETTER_CLIFF: ItemData(7, IC.progression, 32),
    I.Kong_Letter.KONG_LETTER_FACTORY: ItemData(8, IC.progression, 28),
    I.Kong_Letter.KONG_LETTER_VOLCANO: ItemData(9, IC.progression, 28),
    I.Key.JUNGLE_KEY: ItemData(10, IC.progression),
    I.Key.Beach_KEY: ItemData(11, IC.progression),
    I.Key.Ruins_KEY: ItemData(12, IC.progression),
    I.Key.CAVE_KEY: ItemData(13, IC.progression),
    I.Key.FOREST_KEY: ItemData(14, IC.progression),
    I.Key.CLIFF_KEY: ItemData(15, IC.progression),
    I.Key.FACTORY_KEY: ItemData(16, IC.progression),
    I.Key.VOLCANO_KEY: ItemData(17, IC.progression),
    I.Rare_Orb.GREEN_ORB_JUNGLE: ItemData(18, IC.progression),
    I.Rare_Orb.BLUE_ORB_BEACH: ItemData(19, IC.progression),
    I.Rare_Orb.WHITE_ORB_RUINS: ItemData(20, IC.progression),
    I.Rare_Orb.MAGENTA_ORB_CAVE: ItemData(21, IC.progression),
    I.Rare_Orb.YELLOW_ORB_FOREST: ItemData(22, IC.progression),
    I.Rare_Orb.ORANGE_ORB_CLIFF: ItemData(23, IC.progression),
    I.Rare_Orb.GRAY_ORB_FACTORY: ItemData(24, IC.progression),
    I.Rare_Orb.RED_ORB_VOLCANO: ItemData(25, IC.progression),
    I.Shop.BALLOONX1: ItemData(26, IC.useful, 8),
    I.Shop.BALLOONX3: ItemData(27, IC.useful, 8),
    I.Shop.BALLOONX7: ItemData(28, IC.useful, 8),
    I.Shop.SQUAWKS: ItemData(29, IC.useful, 8),
    I.Shop.HEART_BOOST: ItemData(30, IC.useful, 8),
    I.Shop.BANANA_JUICE: ItemData(31, IC.useful, 8),
    I.Unlockables.Moves.RUN: ItemData(32, IC.progression),
    I.Unlockables.Moves.ROLL: ItemData(33, IC.progression),
    I.Unlockables.Moves.GRAB: ItemData(34, IC.progression),
    I.Unlockables.Moves.BLOW: ItemData(35, IC.progression),
    I.Unlockables.Moves.GROUND_POUND: ItemData(36, IC.progression),
    I.Unlockables.MISC.ROCKET_BARREL_FUEL: ItemData(37, IC.progression),
    I.Unlockables.MISC.MINECART_PASS: ItemData(38, IC.progression),
    I.Unlockables.MISC.RAMBIS_SADDLE: ItemData(39, IC.progression),
    I.Unlockables.MISC.KONG_BARREL: ItemData(40, IC.progression),
    I.Unlockables.MIRROR_SHARD: ItemData(41, IC.progression)
}

ITEM_NAME_TO_ID: Dict[str, int] = {}

DEFAULT_ITEM_CLASSIFICATIONS = {

}

class DKCRItem(Item):
    game = "Donkey Kong Country Returns"

def get_random_filler_item_name(world: DKCRWorld) -> str:
    return "Balloon"

def create_item_with_correct_classification(world: DKCRWorld, name: str) -> DKCRItem:
    classification = DEFAULT_ITEM_CLASSIFICATIONS[name]

    return DKCRItem(name, classification, ITEM_NAME_TO_ID[name], world.player)

def create_all_items(world: DKCRWorld) -> None:
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