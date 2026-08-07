from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Dict

from BaseClasses import Item, ItemClassification as IC

from worlds.donkey_kong_country_returns.DKCRNameConstants import Item as I

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
UnlockableOffset = 0x6000
ProgressiveOffset = 0x7000
ShopOffset = 0x8000

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
    I.RECOVERY_HEART: ItemData(code=0x33, classification=IC.filler),
    I.Key.JUNGLE_KEY: ItemData(code=0x8 + KeyOffset),
    I.Key.Beach_KEY: ItemData(code=0x7 + KeyOffset),
    I.Key.Ruins_KEY: ItemData(code=0x6 + KeyOffset),
    I.Key.CAVE_KEY: ItemData(code=0x5 + KeyOffset),
    I.Key.FOREST_KEY: ItemData(code=0x4 + KeyOffset),
    I.Key.CLIFF_KEY: ItemData(code=0x3 + KeyOffset),
    I.Key.FACTORY_KEY: ItemData(code=0x2 + KeyOffset),
    I.Key.VOLCANO_KEY: ItemData(code=0x1 + KeyOffset),
    I.Rare_Orb.GREEN_ORB_JUNGLE: ItemData(code=0x18 + OrbOffset),
    I.Rare_Orb.BLUE_ORB_BEACH: ItemData(code=0x19 + OrbOffset),
    I.Rare_Orb.WHITE_ORB_RUINS: ItemData(code=0x20 + OrbOffset),
    I.Rare_Orb.MAGENTA_ORB_CAVE: ItemData(code=0x21 + OrbOffset),
    I.Rare_Orb.YELLOW_ORB_FOREST: ItemData(code=0x22 + OrbOffset),
    I.Rare_Orb.ORANGE_ORB_CLIFF: ItemData(code=0x23 + OrbOffset),
    I.Rare_Orb.GRAY_ORB_FACTORY: ItemData(code=0x24 + OrbOffset),
    I.Rare_Orb.RED_ORB_VOLCANO: ItemData(code=0x25 + OrbOffset),
    #I.Unlockables.Moves.ROLL: ItemData(code=29),
    #I.Unlockables.Moves.GRAB: ItemData(code=30),
    #I.Unlockables.Moves.BLOW: ItemData(code=31),
    #I.Unlockables.Moves.GROUND_POUND: ItemData(code=32),
    #I.Unlockables.MISC.ROCKET_BARREL_FUEL: ItemData(code=33),
    #I.Unlockables.MISC.MINECART_PASS: ItemData(code=34),
    #I.Unlockables.MISC.RAMBIS_SADDLE: ItemData(code=35),
    #I.Unlockables.MISC.KONG_BARREL: ItemData(code=36),
    I.Unlockables.MIRROR_SHARD: ItemData(code=UnlockableOffset + 0x1),
    I.Unlockables.MIRROR_MODE: ItemData(code=UnlockableOffset + 0x2),
    I.PROGRESSIVE_FACTORY_BUTTON: ItemData(code=38 + ProgressiveOffset),
    I.Shop.SQUAWKS: ItemData(code=1 + ShopOffset)
}

filler_dict = {
    I.BALLOONX1: 5,
    I.BALLOONX3: 3,
    I.BALLOONX7: 1,
    I.BANANA: 25,
    I.BANANA_BUNCH: 20,
    I.BIG_BANANA_BUNCH: 10,
    I.BANANA_COIN: 15,
    I.RECOVERY_HEART: 20,
}

ITEM_NAME_TO_ID = {key: value.code for key, value in item_table.items()}

class DKCRItem(Item):
    game: str = "Donkey Kong Country Returns"

def get_random_filler_item_name(world: DKCRWorld) -> str:
    filler_list = [I.BALLOONX1, I.BALLOONX3, I.BALLOONX7, I.BANANA, I.BANANA_BUNCH, I.BIG_BANANA_BUNCH, I.BANANA_COIN]
    return filler_list[world.random.randrange(0, len(filler_list))]

def create_item_with_correct_classification(world: DKCRWorld, name: str) -> DKCRItem:
    classification = item_table[name].classification
    id = item_table[name].code

    return DKCRItem(name, classification, id, world.player)

def create_all_items(world: DKCRWorld) -> None:
    itempool: list[DKCRItem] = []
    for item in item_table.keys():
        if item == I.Key.JUNGLE_KEY and world.options.sunset_shore_key == 0:
            continue
        if item == I.Key.Beach_KEY and world.options.blowhole_bound_key == 0:
            continue
        if item == I.Key.Ruins_KEY and world.options.damp_dungeon_key == 0:
            continue
        if item == I.Key.CAVE_KEY and world.options.mole_patrol_key == 0:
            continue
        if item == I.Key.FOREST_KEY and world.options.springy_spores_key == 0:
            continue
        if item == I.Key.CLIFF_KEY and world.options.precarious_plateau_key == 0:
            continue
        if item == I.Key.FACTORY_KEY and world.options.handy_hazards_key == 0:
            continue
        if item == I.Key.VOLCANO_KEY and world.options.smokey_peak_key == 0:
            continue
        if item in filler_dict.keys():
            continue
        if item == I.Shop.SQUAWKS and (world.options.squawks == 0):
            continue
        if item == I.Unlockables.MIRROR_MODE and (world.options.mirror_mode_shards.value > 0 or world.options.mirror_mode == 0):
            continue
        if item == I.Unlockables.MIRROR_SHARD:
            if world.options.mirror_mode == 0:
                continue
            for _ in range(world.options.mirror_mode_shards.value):
                itempool.append(world.create_item(item))
            continue
        if item == I.PROGRESSIVE_FACTORY_BUTTON:
            for _ in range(world.options.factory_buttons):
                itempool.append(world.create_item(item))
            continue
        for _ in range(item_table[item].amount):
            itempool.append(world.create_item(item))

    number_of_items = len(itempool)

    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))

    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items

    fillers = world.random.choices(
        population=list(filler_dict.keys()),
        weights=list(filler_dict.values()),
        k=needed_number_of_filler_items
    )

    for filler in fillers:
        itempool.append(world.create_item(filler))

    world.multiworld.itempool += itempool