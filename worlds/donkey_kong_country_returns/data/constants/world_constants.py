from enum import StrEnum, IntEnum

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

class WorldKey(IntEnum):
    WORLD_MAP_KEY_BEACH = 0x80ddff
    WORLD_MAP_KEY_CAVE = 0x80de03
    WORLD_MAP_KEY_CLIFF = 0x80de07
    WORLD_MAP_KEY_FACTORY = 0x80de0b
    WORLD_MAP_KEY_FOREST = 0x80de0f
    WORLD_MAP_KEY_JUNGLE = 0x80de13
    WORLD_MAP_KEY_RUINS = 0x80de17
    WORLD_MAP_KEY_VOLCANO = 0x80de1b

class WorldOrb(IntEnum):
    RARE_ORB_JUNGLE = 0x80ddd0
    RARE_ORB_BEACH = 0x80ddd4
    RARE_ORB_RUINS = 0x80ddd8
    RARE_ORB_CAVE = 0x80dddc
    RARE_ORB_FOREST = 0x80dde0
    RARE_ORB_CLIFF = 0x80dde4
    RARE_ORB_FACTORY = 0x80dde8
    RARE_ORB_VOLCANO = 0x80dddc

class WorldName(StrEnum):
    JUNGLE = "Jungle"
    BEACH = "Beach"
    RUINS = "Ruins"
    CAVE = "Cave"
    FOREST = "Forest"
    CLIFF = "Cliff"
    FACTORY = "Factory"
    VOLCANO = "Volcano"
    GOLDEN_TEMPLE_WORLD = "Golden Temple World"