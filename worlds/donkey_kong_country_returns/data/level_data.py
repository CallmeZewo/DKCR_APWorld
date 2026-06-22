import dataclasses
from typing import Mapping
from ..DKCRNameConstants import World as W, Level as LV
from ..rules import *


@dataclasses.dataclass(slots=True)
class LevelData:
    world_name: str
    pointer: int
    index: int | None = None
    puzzle_piece_amount: int | None = None
    kong_letter_amount: int | None = None
    connections: list[int | None  | list[int | Mapping[str, int]]] = None
    time_offset: int = 0x38
    medal_offset: int = 0x3d
    flags_offset: int = 0x3e


LEVEL_RAW = {
    LV.JUNGLE_SHOP: (W.JUNGLE, 0x024C, 0x0B, None, [0x3]),
    LV.JUNGLE_HIJINXS: (W.JUNGLE, 0x0284, 0x2, 9, [0x3]),
    LV.KING_OF_CLING: (W.JUNGLE, 0x086C, 0x3, 7, [0x2, 0x4, 0x0B, [0x0, has_all_jungle_letters]]),
    LV.TREE_TOP_BOP: (W.JUNGLE, 0x0984, 0x4, 5, [0x3, 0x5, 0x6]),
    LV.SUNSET_SHORE: (W.JUNGLE, 0x07C4, 0x5, 5, [0x4, 0x7]),
    LV.CANOPY_CANNONS: (W.JUNGLE, 0x0A9C, 0x6, 5, [0x4, 0x7]),
    LV.CRAZY_CART: (W.JUNGLE, 0x0214, 0x7, 5, [0x5, 0x6, [0x1, has_enough_pp_jungle]]),
    LV.MUGLYS_MOUND: (W.JUNGLE, 0x0E1C, 0x1, None, [0x7]),
    LV.PLATFORM_PANIC: (W.JUNGLE, 0x071C, 0x0, 5, [0x3]),
    LV.BEACH_SHOP: (W.BEACH, 0x06AC, 0x0B, None, [0x3]),
    LV.POPPIN_PLANKS: (W.BEACH, 0x078C, 0x2, 5, [0x3]),
    LV.SLOPPY_SANDS: (W.BEACH, 0x055C, 0x3, 7, [0x2, 0x4, 0x0B]),
    LV.PEACEFUL_PIER: (W.BEACH, 0x039C, 0x4, 5, [0x3, 0x5, 0x7]),
    LV.CANNON_CLUSTER: (W.BEACH, 0x11D4, 0x5, 7, [0x4, 0x6]),
    LV.STORMY_SHORE: (W.BEACH, 0x0674, 0x6, 5, [0x5, 0x7, 0x8]),
    LV.BLOWHOLE_BOUND: (W.BEACH, 0x001C, 0x7, 5, [0x4, 0x6]),
    LV.TIDAL_TERROR: (W.BEACH, 0x104C, 0x8, 5, [0x6, [0x0, has_all_beach_letters], [0x1, has_enough_pp_beach]]),
    LV.PINCHIN_PIRATES: (W.BEACH, 0x0C5C, 0x1, None, [0x8]),
    LV.TUMBLIN_TEMPLE: (W.BEACH, 0x0D74, 0x0, 5, [0x8]),
    LV.RUINS_SHOP: (W.RUINS, 0x02F4, 0x0B, None, [0x3]),
    LV.WONKY_WATERWAY: (W.RUINS, 0x0834, 0x2, 7, [0x3, 0x5]),
    LV.BUTTON_BASH: (W.RUINS, 0x032C, 0x3, 7, [0x2, 0x4, 0x0B]),
    LV.MAST_BLAST: (W.RUINS, 0x1164, 0x4, 7, [0x3, 0x5, 0x6]),
    LV.DAMP_DUNGEON: (W.RUINS, 0x1084, 0x5, 9, [0x2, 0x4, 0x7]),
    LV.ITTY_BITTY_BITERS: (W.RUINS, 0x119C, 0x6, 7, [0x4, 0x7, [0x0, has_all_ruins_letters]]),
    LV.TEMPLE_TOPPLE: (W.RUINS, 0x1014, 0x7, 5, [0x5, 0x6, [0x1, has_enough_pp_ruins]]),
    LV.RUINED_ROOST: (W.RUINS, 0x0CCC, 0x1, None, [0x7]),
    LV.SHIFTY_SMASHERS: (W.RUINS, 0x00C4, 0x0, 5, [0x6]),
    LV.CAVE_SHOP: (W.CAVE, 0x0364, 0x0B, None, [0x3, 0x4, 0x6]),
    LV.RICKETY_RAILS: (W.CAVE, 0x0754, 0x2, 5, [0x3, 0x4]),
    LV.GRIP_N_TRIP: (W.CAVE, 0x0444, 0x3, 5, [0x2, 0x5, 0x0B]),
    LV.BOMBS_AWAY: (W.CAVE, 0x0134, 0x4, 5, [0x2, 0x6, [0x0, has_all_cave_letters]]),
    LV.MOLE_PATROL: (W.CAVE, 0x0604, 0x5, 5, [0x3, [0x1, has_enough_pp_cave]]),
    LV.CROWDED_CAVERN: (W.CAVE, 0x0EC4, 0x6, 5, [0x4, 0x0B, [0x1, has_enough_pp_cave]]),
    LV.THE_MOLE_TRAIN: (W.CAVE, 0x0B44, 0x1, None, [0x5, 0x6]),
    LV.JAGGED_JEWELS: (W.CAVE, 0x0B0C, 0x0, 5, [0x4]),
    LV.FOREST_SHOP: (W.FOREST, 0x09BC, 0x0B, None, [0x4]),
    LV.VINE_VALLEY: (W.FOREST, 0x08A4, 0x2, 7, [0x3]),
    LV.CLINGY_SWINGY: (W.FOREST, 0x07FC, 0x3, 5, [0x2, 0x4, 0x7, [0x0, has_all_forest_letters]]),
    LV.FLUTTER_FLYAWAY: (W.FOREST, 0x0BEC, 0x4, 7, [0x3, 0x5, 0x0B]),
    LV.TIPPIN_TOTEMS: (W.FOREST, 0x0EFC, 0x5, 7, [0x4, 0x6]),
    LV.LONGSHOT_LAUNCH: (W.FOREST, 0x0DAC, 0x6, 7, [0x5, 0x9]),
    LV.SPRINGY_SPORES: (W.FOREST, 0x0FDC, 0x7, 7, [0x3, 0x8]),
    LV.WIGGLEVINE_WONDERS: (W.FOREST, 0x05CC, 0x8, 7, [0x7, 0x9]),
    LV.MUNCHER_MARATHON: (W.FOREST, 0x0AD4, 0x9, 5, [0x6, 0x7, [0x1, has_enough_pp_forest]]),
    LV.MANGORUBY_RUN: (W.FOREST, 0x0D3C, 0x1, None, [0x9]),
    LV.BLAST_N_BOUNCE: (W.FOREST, 0x0FA4, 0x0, 5, [0x3]),
    LV.CLIFF_SHOP: (W.CLIFF, 0x0F6C, 0x0B, None, [0x4]),
    LV.STICKY_SITUATION: (W.CLIFF, 0x0A64, 0x2, 9, [0x3]),
    LV.PREHISTORIC_PATH: (W.CLIFF, 0x0C24, 0x3, 5, [0x2, 0x4, [0x0, has_all_cliff_letters]]),
    LV.WEIGHTY_WAY: (W.CLIFF, 0x0BB4, 0x4, 5, [0x3, 0x5, 0x6, 0x0B]),
    LV.BOULDER_ROLLER: (W.CLIFF, 0x0C94, 0x5, 7, [0x4, 0x7]),
    LV.PRECARIOUS_PLATEAU: (W.CLIFF, 0x02BC, 0x6, 5, [0x4, 0x7]),
    LV.CRUMBLE_CANYON: (W.CLIFF, 0x0054, 0x7, 9, [0x5, 0x6, 0x8]),
    LV.TIPPY_SHIPPY: (W.CLIFF, 0x016C, 0x8, 5, [0x7, 0x9]),
    LV.CLIFFTOP_CLIMB: (W.CLIFF, 0x04B4, 0x9, 5, [0x8, [0x1, has_enough_pp_cliff]]),
    LV.THUGLYS_HIGHRISE: (W.CLIFF, 0x063C, 0x1, None, [0x9]),
    LV.PERILOUS_PASSAGE: (W.CLIFF, 0x00FC, 0x0, 5, [0x3]),
    LV.FACTORY_SHOP: (W.FACTORY, 0x01A4, 0x0B, None, [0x3]),
    LV.FOGGY_FUMES: (W.FACTORY, 0x008C, 0x2, 7, [0x3]),
    LV.SLAMMIN_STEEL: (W.FACTORY, 0x06E4, 0x3, 5, [0x2, 0x4, 0x5, 0x0B]),
    LV.HANDY_HAZARDS: (W.FACTORY, 0x094C, 0x4, 7, [0x3, 0x6, [0x0, has_all_factory_letters]]),
    LV.GEAR_GETAWAY: (W.FACTORY, 0x0DE4, 0x5, 7, [0x3, 0x6]),
    LV.COG_JOG: (W.FACTORY, 0x047C, 0x6, 9, [0x4, 0x5, 0x7, 0x8]),
    LV.SWITCHEROO: (W.FACTORY, 0x112C, 0x7, 5, [0x6, 0x8]),
    LV.MUSIC_MADNESS: (W.FACTORY, 0x0594, 0x8, 5, [0x6, 0x7, 0x0A]),
    LV.LIFT_OFF_LAUNCH: (W.FACTORY, 0x0F34, 0x0A, None, [0x8, [0x1, has_enough_pp_factory]]),
    LV.FEATHER_FIEND: (W.FACTORY, 0x0524, 0x1, None, [0x0A]),
    LV.TREACHEROUS_TRACK: (W.FACTORY, 0x040C, 0x0, 5, [0x4]),
    LV.VOLCANO_SHOP: (W.VOLCANO, 0x0914, 0x0B, None, [0x2]),
    LV.FURIOUS_FIRE: (W.VOLCANO, 0x04EC, 0x2, 5, [0x3, 0x0B]),
    LV.HOT_ROCKET: (W.VOLCANO, 0x03D4, 0x3, 5, [0x2, 0x4, 0x5]),
    LV.ROASTING_RAILS: (W.VOLCANO, 0x0E54, 0x4, 5, [0x3, 0x6]),
    LV.SMOKEY_PEAK: (W.VOLCANO, 0x0A2C, 0x5, 5, [0x3, 0x6]),
    LV.BOBBING_BASALT: (W.VOLCANO, 0x0B7C, 0x6, 7, [0x5, 0x7]),
    LV.MOVING_MELTERS: (W.VOLCANO, 0x08DC, 0x7, 5, [0x6, 0x8, [0x0, has_all_volcano_letters]]),
    LV.RED_RED_RISING: (W.VOLCANO, 0x01DC, 0x8, 5, [0x7, [0x1, has_enough_pp_volcano]]),
    LV.TIKI_TONG_TERROR: (W.VOLCANO, 0x0D04, 0x1, None, [0x8]),
    LV.FIVE_MONKEY_TRIAL: (W.VOLCANO, 0x10BC, 0x0, 5, [0x7]),
    LV.GOLDEN_TEMPLE: (W.GOLDEN_TEMPLE, 0x10F4, 0x0, 5, [None]),
}


def get_kong_letter_amount(index: int | None) -> int | None:
    if index is None:
        return None
    if 0x1 < index < 0x0A:
        return 4
    return None


Levels: dict[str, LevelData] = {
    name: LevelData(
        world_name=world,
        pointer=ptr,
        index=index,
        puzzle_piece_amount=pp,
        kong_letter_amount=get_kong_letter_amount(index),
        connections=connections
    )
    for name, (world, ptr, index, pp, connections) in LEVEL_RAW.items()
}

LEVELS_BY_WORLD: dict[str, list] = {}

for level in Levels.values():
    world = level.world_name
    if world not in LEVELS_BY_WORLD:
        LEVELS_BY_WORLD[world] = []

    LEVELS_BY_WORLD[world].append(level)
