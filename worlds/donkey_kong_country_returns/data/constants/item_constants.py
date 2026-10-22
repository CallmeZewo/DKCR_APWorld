from enum import Enum, IntEnum

class ItemName(Enum):
    PUZZLE_PIECE = "Puzzle Piece"
    KONG_LETTER_JUNGLE = "Kong Letter Jungle"
    KONG_LETTER_BEACH = "Kong Letter Beach"
    KONG_LETTER_RUINS = "Kong Letter Ruins"
    KONG_LETTER_CAVE = "Kong Letter Cave"
    KONG_LETTER_FOREST = "Kong Letter Forest"
    KONG_LETTER_CLIFF = "Kong Letter Cliff"
    KONG_LETTER_FACTORY = "Kong Letter Factory"
    KONG_LETTER_VOLCANO = "Kong Letter Volcano"
    JUNGLE_KEY = "Jungle Key"
    BEACH_KEY = "Beach Key"
    RUINS_KEY = "Ruins Key"
    CAVE_KEY = "Cave Key"
    FOREST_KEY = "Forest Key"
    CLIFF_KEY = "Cliff Key"
    FACTORY_KEY = "Factory Key"
    VOLCANO_KEY = "Volcano Key"
    RARE_ORB = "Rare Orb"
    MIRROR_SHARD = "Mirror Shard"
    MIRROR_MODE = "Mirror Mode"
    PROGRESSIVE_FACTORY_BUTTON = "Progressive Factory Button"
    PROGRESSIVE_BOSS_UNLOCK = "Progressive Boss Unlock"
    PROGRESSIVE_K_LEVEL_UNLOCK = "Progressive K Level Unlock"
    ROCKET_BARREL_FUEL = "Rocket Barrel Fuel"
    MINECART_PASS = "Minecart Pass"
    RAMBIS_SADDLE = "Rambi's Saddle"
    KONG_BARREL = "Kong Barrel"
    SQUAWKS = "Squawks"
    RUN = "Run"
    ROLL = "Roll"
    GRAB = "Grab"
    BLOW = "Blow"
    GROUND_POUND = "Ground Pound"
    BALLOONX1 = "Balloons x 1"
    BALLOONX3 = "Balloons x 3"
    BALLOONX7 = "Balloons x 7"
    BANANA = "Banana"
    BANANA_BUNCH = "Banana Bunch"
    BIG_BANANA_BUNCH = "Big Banana Bunch"
    BANANA_COIN = "Banana Coin"
    RECOVERY_HEART = "Recovery Heart"

class ItemOffset(IntEnum):
    JUNGLE = 0x100
    BEACH = 0x200
    RUINS = 0x300
    CAVE = 0x400
    FOREST = 0x500
    CLIFF = 0x600
    FACTORY = 0x700
    VOLCANO = 0x800
    TEMPLE = 0x900

    COLLECTABLES = 0x1000 # Puzzle Pieces, Kong Letters
    PUZZLE_PIECE = COLLECTABLES + 0x1
    KONG_LETTER_JUNGLE = COLLECTABLES + JUNGLE + 0x2
    KONG_LETTER_BEACH = COLLECTABLES + BEACH + 0x2
    KONG_LETTER_RUINS = COLLECTABLES + RUINS + 0x2
    KONG_LETTER_CAVE = COLLECTABLES + CAVE + 0x2
    KONG_LETTER_FOREST = COLLECTABLES + FOREST + 0x2
    KONG_LETTER_CLIFF = COLLECTABLES + CLIFF + 0x2
    KONG_LETTER_FACTORY = COLLECTABLES + FACTORY + 0x2
    KONG_LETTER_VOLCANO = COLLECTABLES + VOLCANO + 0x2

    KEY = 0x2000 # Key Level Keys
    JUNGLE_KEY = KEY + JUNGLE
    BEACH_KEY = KEY + BEACH
    RUINS_KEY = KEY + RUINS
    CAVE_KEY = KEY + CAVE
    FOREST_KEY = KEY + FOREST
    CLIFF_KEY = KEY + CLIFF
    FACTORY_KEY = KEY + FACTORY
    VOLCANO_KEY = KEY + VOLCANO

    ORB = 0x3000 # Rare Orbs

    ABILITY = 0x4000 # Moves, Vehicles
    UNLOCK = 0x5000 # Mirror Mode, FACTORY BUTTON
    MIRROR_SHARD = UNLOCK + 0x1
    MIRROR_MODE = UNLOCK + 0x2
    PROGRESSIVE_FACTORY_BUTTON = UNLOCK + 0x3
    PROGRESSIVE_BOSS_UNLOCK = UNLOCK + 0x4
    PROGRESSIVE_K_LEVEL_UNLOCK = UNLOCK + 0x5

    SHOP = 0x6000 # Squawks
    SQUAWKS = SHOP + 0x1

    FILLER = 0x10000
    BALLOONX1 = FILLER + 0x1
    BALLOONX3 = FILLER + 0x2
    BALLOONX7 = FILLER + 0x3
    BANANA = FILLER + 0x4
    BANANA_BUNCH = FILLER + 0x5
    BIG_BANANA_BUNCH = FILLER + 0x6
    BANANA_COIN = FILLER + 0x7
    RECOVERY_HEART = FILLER + 0x8


