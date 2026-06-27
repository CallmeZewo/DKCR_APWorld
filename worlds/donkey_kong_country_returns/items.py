from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Dict

from BaseClasses import Item, ItemClassification as IC

from worlds.donkey_kong_country_returns.DKCRNameConstants import Item as I

import random

if TYPE_CHECKING:
    from . import DKCRWorld

@dataclass
class ItemData:
    code: int
    classification: IC = IC.progression
    amount: int = 1

WorldOffset = 0x1000
ItemOffset = 0x2000
KeyOffset = 0x3000
OrbOffset = 0x4000
AbilityOffset = 0x5000

item_table: Dict[str, ItemData] = {
    I.PUZZLE_PIECE: ItemData(code=0x1 + ItemOffset, amount=371),
    I.Kong_Letter.KONG_LETTER_JUNGLE: ItemData(code=0x05 + WorldOffset, amount=24),
    I.Kong_Letter.KONG_LETTER_BEACH: ItemData(code=0x00 + WorldOffset, amount=28),
    I.Kong_Letter.KONG_LETTER_RUINS: ItemData(code=0x06 + WorldOffset, amount=24),
    I.Kong_Letter.KONG_LETTER_CAVE: ItemData(code=0x01 + WorldOffset, amount=20),
    I.Kong_Letter.KONG_LETTER_FOREST: ItemData(code=0x04 + WorldOffset, amount=32),
    I.Kong_Letter.KONG_LETTER_CLIFF: ItemData(code=0x02 + WorldOffset, amount=32),
    I.Kong_Letter.KONG_LETTER_FACTORY: ItemData(code=0x03 + WorldOffset, amount=28),
    I.Kong_Letter.KONG_LETTER_VOLCANO: ItemData(code=0x07 + WorldOffset, amount=28),
    I.BALLOONX1: ItemData(code=0x26, classification=IC.filler),
    I.BALLOONX3: ItemData(code=0x27, classification=IC.filler),
    I.BALLOONX7: ItemData(code=0x28, classification=IC.filler),
    I.BANANA: ItemData(code=0x29, classification=IC.filler),
    I.BANANA_BUNCH: ItemData(code=0x30, classification=IC.filler),
    I.BIG_BANANA_BUNCH: ItemData(code=0x31, classification=IC.filler),
    I.BANANA_COIN: ItemData(code=0x32, classification=IC.filler),
    I.HEART: ItemData(code=0x33, classification=IC.filler),
    #I.Key.JUNGLE_KEY: ItemData(code=10),
    #I.Key.Beach_KEY: ItemData(code=11),
    #I.Key.Ruins_KEY: ItemData(code=12),
    #I.Key.CAVE_KEY: ItemData(code=13),
    #I.Key.FOREST_KEY: ItemData(code=14),
    #I.Key.CLIFF_KEY: ItemData(code=15),
    #I.Key.FACTORY_KEY: ItemData(code=16),
    #I.Key.VOLCANO_KEY: ItemData(code=17),
    #I.Rare_Orb.GREEN_ORB_JUNGLE: ItemData(code=18),
    #I.Rare_Orb.BLUE_ORB_BEACH: ItemData(code=19),
    #I.Rare_Orb.WHITE_ORB_RUINS: ItemData(code=20),
    #I.Rare_Orb.MAGENTA_ORB_CAVE: ItemData(code=21),
    #I.Rare_Orb.YELLOW_ORB_FOREST: ItemData(code=22),
    #I.Rare_Orb.ORANGE_ORB_CLIFF: ItemData(code=23),
    #I.Rare_Orb.GRAY_ORB_FACTORY: ItemData(code=24),
    #I.Rare_Orb.RED_ORB_VOLCANO: ItemData(code=25),
    #I.Unlockables.Moves.ROLL: ItemData(code=29),
    #I.Unlockables.Moves.GRAB: ItemData(code=30),
    #I.Unlockables.Moves.BLOW: ItemData(code=31),
    #I.Unlockables.Moves.GROUND_POUND: ItemData(code=32),
    #I.Unlockables.MISC.ROCKET_BARREL_FUEL: ItemData(code=33),
    #I.Unlockables.MISC.MINECART_PASS: ItemData(code=34),
    #I.Unlockables.MISC.RAMBIS_SADDLE: ItemData(code=35),
    #I.Unlockables.MISC.KONG_BARREL: ItemData(code=36),
    #I.Unlockables.MIRROR_SHARD: ItemData(code=37),
    #I.PROGRESSIVE_FACTORY_BUTTON: ItemData(code=38, amount=3)
}

ITEM_NAME_TO_ID = {key: value.code for key, value in item_table.items()}

class DKCRItem(Item):
    game: str = "Donkey Kong Country Returns"

def get_random_filler_item_name(world: DKCRWorld) -> str:
    filler_list = [I.BALLOONX1, I.BALLOONX3, I.BALLOONX7, I.BANANA, I.BANANA_BUNCH, I.BIG_BANANA_BUNCH, I.BANANA_COIN]
    return filler_list[random.randrange(0, len(filler_list))]

def create_item_with_correct_classification(world: DKCRWorld, name: str) -> DKCRItem:
    classification = item_table[name].classification
    id = item_table[name].code

    return DKCRItem(name, classification, id, world.player)

def create_all_items(world: DKCRWorld) -> None:
    itempool: list[DKCRItem] = []
    for item in item_table:
        for _ in range(item_table[item].amount):
            itempool.append(world.create_item(item))

    number_of_items = len(itempool)

    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))

    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items

    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]

    world.multiworld.itempool += itempool