from __future__ import annotations

from typing import TYPE_CHECKING, Dict

from BaseClasses import Item, ItemClassification as IC

from .strings import Item as I

if TYPE_CHECKING:
    from .world import DKCRWorld

class ItemData:
    def __init__(self, code, classification: IC = IC.progression, amount=1):
        self.code = code
        self.classification = classification
        self.amount = amount

item_table: Dict[str, ItemData] = {
    I.PUZZLE_PIECE: ItemData(code=1, amount=366),
    I.Kong_Letter.KONG_LETTER_JUNGLE: ItemData(code=2, amount=24),
    I.Kong_Letter.KONG_LETTER_BEACH: ItemData(code=3, amount=28),
    I.Kong_Letter.KONG_LETTER_RUINS: ItemData(code=4, amount=24),
    I.Kong_Letter.KONG_LETTER_CAVE: ItemData(code=5, amount=20),
    I.Kong_Letter.KONG_LETTER_FOREST: ItemData(code=6, amount=32),
    I.Kong_Letter.KONG_LETTER_CLIFF: ItemData(code=7, amount=32),
    I.Kong_Letter.KONG_LETTER_FACTORY: ItemData(code=8, amount=28),
    I.Kong_Letter.KONG_LETTER_VOLCANO: ItemData(code=9, amount=28),
    I.Key.JUNGLE_KEY: ItemData(code=10),
    I.Key.Beach_KEY: ItemData(code=11),
    I.Key.Ruins_KEY: ItemData(code=12),
    I.Key.CAVE_KEY: ItemData(code=13),
    I.Key.FOREST_KEY: ItemData(code=14),
    I.Key.CLIFF_KEY: ItemData(code=15),
    I.Key.FACTORY_KEY: ItemData(code=16),
    I.Key.VOLCANO_KEY: ItemData(code=17),
    I.Rare_Orb.GREEN_ORB_JUNGLE: ItemData(code=18),
    I.Rare_Orb.BLUE_ORB_BEACH: ItemData(code=19),
    I.Rare_Orb.WHITE_ORB_RUINS: ItemData(code=20),
    I.Rare_Orb.MAGENTA_ORB_CAVE: ItemData(code=21),
    I.Rare_Orb.YELLOW_ORB_FOREST: ItemData(code=22),
    I.Rare_Orb.ORANGE_ORB_CLIFF: ItemData(code=23),
    I.Rare_Orb.GRAY_ORB_FACTORY: ItemData(code=24),
    I.Rare_Orb.RED_ORB_VOLCANO: ItemData(code=25),
    I.Shop.BALLOONX1: ItemData(code=26, classification=IC.filler, amount=8),
    I.Shop.BALLOONX3: ItemData(code=27, classification=IC.filler, amount=8),
    I.Shop.BALLOONX7: ItemData(code=28, classification=IC.filler, amount=8),
    I.Unlockables.Moves.RUN: ItemData(code=29),
    I.Unlockables.Moves.ROLL: ItemData(code=30),
    I.Unlockables.Moves.GRAB: ItemData(code=31),
    I.Unlockables.Moves.BLOW: ItemData(code=32),
    I.Unlockables.Moves.GROUND_POUND: ItemData(code=33),
    I.Unlockables.MISC.ROCKET_BARREL_FUEL: ItemData(code=34),
    I.Unlockables.MISC.MINECART_PASS: ItemData(code=34),
    I.Unlockables.MISC.RAMBIS_SADDLE: ItemData(code=35),
    I.Unlockables.MISC.KONG_BARREL: ItemData(code=37),
    I.Unlockables.MIRROR_SHARD: ItemData(code=38),
}

ITEM_NAME_TO_ID: Dict[str, int] = {}

DEFAULT_ITEM_CLASSIFICATIONS = {

}

class DKCRItem(Item):
    game = "Donkey Kong Country Returns"

def get_random_filler_item_name(world: DKCRWorld) -> str:
    return I.Shop.BALLOONX1

def create_item_with_correct_classification(world: DKCRWorld, name: str) -> DKCRItem:
    classification = item_table[name].classification
    id = item_table[name].code

    return DKCRItem(name, classification, id, world.player)

def create_all_items(world: DKCRWorld) -> None:
    itempool: list[Item] = []
    for item in item_table:
        for _ in range(item_table[item].amount):
            itempool.append(world.create_item(item))

    number_of_Items = len(itempool)

    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))

    needed_number_of_filler_items = number_of_unfilled_locations - number_of_Items

    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]

    world.multiworld.itempool += itempool