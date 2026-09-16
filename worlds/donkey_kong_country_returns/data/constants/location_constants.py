from enum import StrEnum, IntEnum


class LocationOffset(IntEnum):
    WorldOffset = 0x10000
    LevelOffset = 0x100


class PPIndex(IntEnum):
    PUZZLE_PIECE_BASE = 0x0
    PUZZLE_PIECE_SET = 0xA
    PUZZLE_PIECE_BUNDLE = 0xB


class KongLetterIndex(IntEnum):
    KONG_LETTER_K = 0x11
    KONG_LETTER_O = 0x12
    KONG_LETTER_N = 0x13
    KONG_LETTER_G = 0x14
    KONG_LETTER_SET = 0x1A
    KONG_LETTER_BUNDLE = 0x1B


class ClearTypeIndex(IntEnum):
    CLEARED = 0x21
    CLEARED_MIRROR = 0x22
    MIRROR_MODE_UNLOCK = 0x23
    CLEARED_TIME_ATTACK_BRONZE = 0x24
    CLEARED_TIME_ATTACK_SILVER = 0x25
    CLEARED_TIME_ATTACK_GOLD = 0x26
    CLEARED_TIME_ATTACK_SHINY_GOLD = 0x27


class SpecialIndex(IntEnum):
    RARE_ORB = 0x31
    SHOP_KEY = 0x41
    MIRROR_MODE_UNLOCK = 0x51


class LevelIndex(IntEnum):
    K_LEVEL_INDEX = 0x0
    GOLDEN_TEMPLE_LEVEL_INDEX = 0x0
    BOSS_LEVEL_INDEX = 0x1
    FIRST_LEVEL_INDEX = 0x2
    SECOND_LEVEL_INDEX = 0x3
    THIRD_LEVEL_INDEX = 0x4
    FOURTH_LEVEL_INDEX = 0x5
    FIFTH_LEVEL_INDEX = 0x6
    SIXTH_LEVEL_INDEX = 0x7
    SEVENTH_LEVEL_INDEX = 0x8
    EIGHTH_LEVEL_INDEX = 0x9
    LIFT_OFF_LAUNCH_LEVEL_INDEX = 0xA
    SHOP_LEVEL_INDEX = 0xB


class WorldIndex(IntEnum):
    BEACH_WORLD_INDEX = 0x0
    CAVE_WORLD_INDEX = 0x1
    CLIFF_WORLD_INDEX = 0x2
    FACTORY_WORLD_INDEX = 0x3
    FOREST_WORLD_INDEX = 0x4
    JUNGLE_WORLD_INDEX = 0x5
    RUINS_WORLD_INDEX = 0x6
    VOLCANO_WORLD_INDEX = 0x7
    GOLDEN_TEMPLE_WORLD_INDEX = 0x8


class LocationName(StrEnum):
    PUZZLE_PIECE = "Puzzle Piece"
    PUZZLE_PIECE_SET = "Puzzle Piece Set"
    PUZZLE_BUNDLE = "Puzzle Bundle"
    KONG_LETTER_K = "Kong Letter (K)"
    KONG_LETTER_O = "Kong Letter (O)"
    KONG_LETTER_N = "Kong Letter (N)"
    KONG_LETTER_G = "Kong Letter (G)"
    KONG_LETTER_SET = "Kong Letter Set"
    KONG_BUNDLE = "Kong Bundle"
    CLEARED = "Cleared"
    CLEARED_MIRROR = "Cleared (Mirror)"
    CLEARED_TIME_ATTACK_BRONZE = "Cleared (Time Attack) [Bronze]"
    CLEARED_TIME_ATTACK_SILVER = "Cleared (Time Attack) [Silver]"
    CLEARED_TIME_ATTACK_GOLD = "Cleared (Time Attack) [Gold]"
    CLEARED_TIME_ATTACK_SHINY_GOLD = "Cleared (Time Attack) [Shiny Gold]"
    KEY = "Key"
    RARE_ORB = "Rare Orb"
    MIRROR_MODE_UNLOCK = "Mirror Mode Unlock"


KONG_LETTER_MAPPING: list[tuple[LocationName, KongLetterIndex]] = [
    (LocationName.KONG_LETTER_K, KongLetterIndex.KONG_LETTER_K),
    (LocationName.KONG_LETTER_O, KongLetterIndex.KONG_LETTER_O),
    (LocationName.KONG_LETTER_N, KongLetterIndex.KONG_LETTER_N),
    (LocationName.KONG_LETTER_G, KongLetterIndex.KONG_LETTER_G),
]

CLEAR_LOCATION_MAPPING: list[tuple[LocationName, ClearTypeIndex]] = [
    (LocationName.CLEARED, ClearTypeIndex.CLEARED),
    (LocationName.CLEARED_MIRROR, ClearTypeIndex.CLEARED_MIRROR),
    (LocationName.CLEARED_TIME_ATTACK_BRONZE, ClearTypeIndex.CLEARED_TIME_ATTACK_BRONZE),
    (LocationName.CLEARED_TIME_ATTACK_SILVER, ClearTypeIndex.CLEARED_TIME_ATTACK_SILVER),
    (LocationName.CLEARED_TIME_ATTACK_GOLD, ClearTypeIndex.CLEARED_TIME_ATTACK_GOLD),
    (LocationName.CLEARED_TIME_ATTACK_SHINY_GOLD, ClearTypeIndex.CLEARED_TIME_ATTACK_SHINY_GOLD),
]
