from . import ItemTypeEnum
from BaseClasses import ItemClassification
from .constants import (
    ItemName as In,
    ItemOffset as Io
)

class GameItems(ItemTypeEnum):
    PUZZLE_PIECE = (In.PUZZLE_PIECE.value, Io.COLLECTABLES.value + Io.PUZZLE_PIECE.value, ItemClassification.progression, 371)
    KONG_LETTER_JUNGLE = (In.KONG_LETTER_JUNGLE.value, Io.COLLECTABLES.value + Io.JUNGLE.value + Io.KONG_LETTER.value, ItemClassification.progression, 24)
    KONG_LETTER_BEACH = (In.KONG_LETTER_BEACH.value, Io.COLLECTABLES.value + Io.BEACH.value + Io.KONG_LETTER.value, ItemClassification.progression, 28)
    KONG_LETTER_RUINS = (In.KONG_LETTER_RUINS.value, Io.COLLECTABLES.value + Io.RUINS.value + Io.KONG_LETTER.value, ItemClassification.progression, 24)
    KONG_LETTER_CAVE = (In.KONG_LETTER_CAVE.value, Io.COLLECTABLES.value + Io.CAVE.value + Io.KONG_LETTER.value, ItemClassification.progression, 20)
    KONG_LETTER_FOREST = (In.KONG_LETTER_FOREST.value, Io.COLLECTABLES.value + Io.FOREST.value + Io.KONG_LETTER.value, ItemClassification.progression, 32)
    KONG_LETTER_CLIFF = (In.KONG_LETTER_CLIFF.value, Io.COLLECTABLES.value + Io.CLIFF.value + Io.KONG_LETTER.value, ItemClassification.progression, 32)
    KONG_LETTER_FACTORY = (In.KONG_LETTER_FACTORY.value, Io.COLLECTABLES.value + Io.FACTORY.value + Io.KONG_LETTER.value, ItemClassification.progression, 28)
    KONG_LETTER_VOLCANO = (In.KONG_LETTER_VOLCANO.value, Io.COLLECTABLES.value + Io.VOLCANO.value + Io.KONG_LETTER.value, ItemClassification.progression, 28)
    JUNGLE_KEY = (In.JUNGLE_KEY.value, Io.JUNGLE.value + Io.KEY.value, ItemClassification.progression)
    BEACH_KEY = (In.BEACH_KEY.value, Io.BEACH.value + Io.KEY.value, ItemClassification.progression)
    RUINS_KEY = (In.RUINS_KEY.value, Io.RUINS.value + Io.KEY.value, ItemClassification.progression)
    CAVE_KEY = (In.CAVE_KEY.value, Io.CAVE.value + Io.KEY.value, ItemClassification.progression)
    FOREST_KEY = (In.FOREST_KEY.value, Io.FOREST.value + Io.KEY.value, ItemClassification.progression)
    CLIFF_KEY = (In.CLIFF_KEY.value, Io.CLIFF.value + Io.KEY.value, ItemClassification.progression)
    FACTORY_KEY = (In.FACTORY_KEY.value, Io.FACTORY.value + Io.KEY.value, ItemClassification.progression)
    VOLCANO_KEY = (In.VOLCANO_KEY.value, Io.VOLCANO.value + Io.KEY.value, ItemClassification.progression)
    RARE_ORB = (In.RARE_ORB.value, Io.ORB.value, ItemClassification.progression, 8)
    PROGRESSIVE_FACTORY_BUTTON = (In.PROGRESSIVE_FACTORY_BUTTON.value, Io.UNLOCK.value + Io.PROGRESSIVE_FACTORY_BUTTON.value, ItemClassification.progression)
    PROGRESSIVE_BOSS_UNLOCK = (In.PROGRESSIVE_BOSS_UNLOCK.value, Io.UNLOCK.value + Io.PROGRESSIVE_BOSS_UNLOCK.value, ItemClassification.progression, 8)
    MIRROR_SHARD = (In.MIRROR_SHARD.value, Io.UNLOCK.value + Io.MIRROR_SHARD.value,ItemClassification.progression)
    MIRROR_MODE = (In.MIRROR_MODE.value, Io.UNLOCK.value + Io.MIRROR_MODE.value,ItemClassification.progression)
    SQUAWKS = (In.SQUAWKS.value, Io.SHOP.value + Io.SQUAWKS.value, ItemClassification.useful)
    BALLOONX1 = (In.BALLOONX1.value, Io.FILLER.value + Io.BALLOONX1.value, ItemClassification.filler)
    BALLOONX3 = (In.BALLOONX3.value, Io.FILLER.value + Io.BALLOONX3.value, ItemClassification.filler)
    BALLOONX7 = (In.BALLOONX7.value, Io.FILLER.value + Io.BALLOONX7.value, ItemClassification.filler)
    BANANA = (In.BANANA.value, Io.FILLER.value + Io.BANANA.value, ItemClassification.filler)
    BANANA_BUNCH = (In.BANANA_BUNCH.value, Io.FILLER.value + Io.BANANA_BUNCH.value, ItemClassification.filler)
    BIG_BANANA_BUNCH = (In.BIG_BANANA_BUNCH.value, Io.FILLER.value + Io.BIG_BANANA_BUNCH.value, ItemClassification.filler)
    BANANA_COIN = (In.BANANA_COIN.value, Io.FILLER.value + Io.BANANA_COIN.value, ItemClassification.filler)
    RECOVERY_HEART = (In.RECOVERY_HEART.value, Io.FILLER.value + Io.RECOVERY_HEART.value, ItemClassification.filler)