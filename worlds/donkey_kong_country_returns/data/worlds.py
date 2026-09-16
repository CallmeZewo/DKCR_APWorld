from . import WorldTypeEnum
from .levels import GameLevels
from .constants import (
    WorldName as Wn,
    WorldIndex as Wi,
    WorldKey as Wk,
    WorldOrb as Wo
)


class GameWorlds(WorldTypeEnum):
    JUNGLE = (Wn.JUNGLE, Wi.JUNGLE_WORLD_INDEX, Wk.WORLD_MAP_KEY_JUNGLE, Wo.RARE_ORB_JUNGLE,
        {
            GameLevels.JUNGLE_HIJINXS: GameLevels.JUNGLE_HIJINXS,
            GameLevels.KING_OF_CLING: GameLevels.KING_OF_CLING,
            GameLevels.TREE_TOP_BOP: GameLevels.TREE_TOP_BOP,
            GameLevels.SUNSET_SHORE: GameLevels.SUNSET_SHORE,
            GameLevels.CANOPY_CANNONS: GameLevels.CANOPY_CANNONS,
            GameLevels.CRAZY_CART: GameLevels.CRAZY_CART,
            GameLevels.PLATFORM_PANIC: GameLevels.PLATFORM_PANIC,
            GameLevels.MUGLYS_MOUND: GameLevels.MUGLYS_MOUND,
            GameLevels.JUNGLE_SHOP: GameLevels.JUNGLE_SHOP,
        })
    BEACH = (Wn.BEACH, Wi.BEACH_WORLD_INDEX, Wk.WORLD_MAP_KEY_BEACH, Wo.RARE_ORB_BEACH,
        {
            GameLevels.POPPIN_PLANKS: GameLevels.POPPIN_PLANKS,
            GameLevels.SLOPPY_SANDS: GameLevels.SLOPPY_SANDS,
            GameLevels.PEACEFUL_PIER: GameLevels.PEACEFUL_PIER,
            GameLevels.CANNON_CLUSTER: GameLevels.CANNON_CLUSTER,
            GameLevels.STORMY_SHORE: GameLevels.STORMY_SHORE,
            GameLevels.BLOWHOLE_BOUND: GameLevels.BLOWHOLE_BOUND,
            GameLevels.TIDAL_TERROR: GameLevels.TIDAL_TERROR,
            GameLevels.TUMBLIN_TEMPLE: GameLevels.TUMBLIN_TEMPLE,
            GameLevels.PINCHIN_PIRATES: GameLevels.PINCHIN_PIRATES,
            GameLevels.BEACH_SHOP: GameLevels.BEACH_SHOP,
        })
    RUINS = (Wn.RUINS, Wi.RUINS_WORLD_INDEX, Wk.WORLD_MAP_KEY_RUINS, Wo.RARE_ORB_RUINS,
        {
            GameLevels.WONKY_WATERWAY: GameLevels.WONKY_WATERWAY,
            GameLevels.BUTTON_BASH: GameLevels.BUTTON_BASH,
            GameLevels.MAST_BLAST: GameLevels.MAST_BLAST,
            GameLevels.DAMP_DUNGEON: GameLevels.DAMP_DUNGEON,
            GameLevels.ITTY_BITTY_BITERS: GameLevels.ITTY_BITTY_BITERS,
            GameLevels.TEMPLE_TOPPLE: GameLevels.TEMPLE_TOPPLE,
            GameLevels.SHIFTY_SMASHERS: GameLevels.SHIFTY_SMASHERS,
            GameLevels.RUINED_ROOST: GameLevels.RUINED_ROOST,
            GameLevels.RUINS_SHOP: GameLevels.RUINS_SHOP,
        })
    CAVE = (Wn.CAVE, Wi.CAVE_WORLD_INDEX, Wk.WORLD_MAP_KEY_CAVE, Wo.RARE_ORB_CAVE,
        {
            GameLevels.RICKETY_RAILS: GameLevels.RICKETY_RAILS,
            GameLevels.GRIP_N_TRIP: GameLevels.GRIP_N_TRIP,
            GameLevels.BOMBS_AWAY: GameLevels.BOMBS_AWAY,
            GameLevels.MOLE_PATROL: GameLevels.MOLE_PATROL,
            GameLevels.CROWDED_CAVERN: GameLevels.CROWDED_CAVERN,
            GameLevels.JAGGED_JEWELS: GameLevels.JAGGED_JEWELS,
            GameLevels.THE_MOLE_TRAIN: GameLevels.THE_MOLE_TRAIN,
            GameLevels.CAVE_SHOP: GameLevels.CAVE_SHOP,
        })
    FOREST = (Wn.FOREST, Wi.FOREST_WORLD_INDEX, Wk.WORLD_MAP_KEY_FOREST, Wo.RARE_ORB_FOREST,
        {
            GameLevels.VINE_VALLEY: GameLevels.VINE_VALLEY,
            GameLevels.CLINGY_SWINGY: GameLevels.CLINGY_SWINGY,
            GameLevels.FLUTTER_FLYAWAY: GameLevels.FLUTTER_FLYAWAY,
            GameLevels.TIPPIN_TOTEMS: GameLevels.TIPPIN_TOTEMS,
            GameLevels.LONGSHOT_LAUNCH: GameLevels.LONGSHOT_LAUNCH,
            GameLevels.SPRINGY_SPORES: GameLevels.SPRINGY_SPORES,
            GameLevels.WIGGLEVINE_WONDERS: GameLevels.WIGGLEVINE_WONDERS,
            GameLevels.MUNCHER_MARATHON: GameLevels.MUNCHER_MARATHON,
            GameLevels.BLAST_N_BOUNCE: GameLevels.BLAST_N_BOUNCE,
            GameLevels.MANGORUBY_RUN: GameLevels.MANGORUBY_RUN,
            GameLevels.FOREST_SHOP: GameLevels.FOREST_SHOP,
        })
    CLIFF = (Wn.CLIFF, Wi.CLIFF_WORLD_INDEX, Wk.WORLD_MAP_KEY_CLIFF, Wo.RARE_ORB_CLIFF,
        {
            GameLevels.STICKY_SITUATION: GameLevels.STICKY_SITUATION,
            GameLevels.PREHISTORIC_PATH: GameLevels.PREHISTORIC_PATH,
            GameLevels.WEIGHTY_WAY: GameLevels.WEIGHTY_WAY,
            GameLevels.BOULDER_ROLLER: GameLevels.BOULDER_ROLLER,
            GameLevels.PRECARIOUS_PLATEAU: GameLevels.PRECARIOUS_PLATEAU,
            GameLevels.CRUMBLE_CANYON: GameLevels.CRUMBLE_CANYON,
            GameLevels.TIPPY_SHIPPY: GameLevels.TIPPY_SHIPPY,
            GameLevels.CLIFFTOP_CLIMB: GameLevels.CLIFFTOP_CLIMB,
            GameLevels.PERILOUS_PASSAGE: GameLevels.PERILOUS_PASSAGE,
            GameLevels.THUGLYS_HIGHRISE: GameLevels.THUGLYS_HIGHRISE,
            GameLevels.CLIFF_SHOP: GameLevels.CLIFF_SHOP,
        })
    FACTORY = (Wn.FACTORY, Wi.FACTORY_WORLD_INDEX, Wk.WORLD_MAP_KEY_FACTORY, Wo.RARE_ORB_FACTORY,
        {
            GameLevels.FOGGY_FUMES: GameLevels.FOGGY_FUMES,
            GameLevels.SLAMMIN_STEEL: GameLevels.SLAMMIN_STEEL,
            GameLevels.HANDY_HAZARDS: GameLevels.HANDY_HAZARDS,
            GameLevels.GEAR_GETAWAY: GameLevels.GEAR_GETAWAY,
            GameLevels.COG_JOG: GameLevels.COG_JOG,
            GameLevels.SWITCHEROO: GameLevels.SWITCHEROO,
            GameLevels.MUSIC_MADNESS: GameLevels.MUSIC_MADNESS,
            GameLevels.LIFT_OFF_LAUNCH: GameLevels.LIFT_OFF_LAUNCH,
            GameLevels.TREACHEROUS_TRACK: GameLevels.TREACHEROUS_TRACK,
            GameLevels.FEATHER_FIEND: GameLevels.FEATHER_FIEND,
            GameLevels.FACTORY_SHOP: GameLevels.FACTORY_SHOP,
        })
    VOLCANO = (Wn.VOLCANO, Wi.VOLCANO_WORLD_INDEX, Wk.WORLD_MAP_KEY_VOLCANO, Wo.RARE_ORB_VOLCANO,
        {
            GameLevels.FURIOUS_FIRE: GameLevels.FURIOUS_FIRE,
            GameLevels.HOT_ROCKET: GameLevels.HOT_ROCKET,
            GameLevels.ROASTING_RAILS: GameLevels.ROASTING_RAILS,
            GameLevels.SMOKEY_PEAK: GameLevels.SMOKEY_PEAK,
            GameLevels.BOBBING_BASALT: GameLevels.BOBBING_BASALT,
            GameLevels.MOVING_MELTERS: GameLevels.MOVING_MELTERS,
            GameLevels.RED_RED_RISING: GameLevels.RED_RED_RISING,
            GameLevels.FIVE_MONKEY_TRIAL: GameLevels.FIVE_MONKEY_TRIAL,
            GameLevels.TIKI_TONG_TERROR: GameLevels.TIKI_TONG_TERROR,
            GameLevels.VOLCANO_SHOP: GameLevels.VOLCANO_SHOP,
        })
    GOLDEN_TEMPLE_WORLD = (Wn.GOLDEN_TEMPLE_WORLD, Wi.GOLDEN_TEMPLE_WORLD_INDEX, None, None,
        {
            GameLevels.GOLDEN_TEMPLE: GameLevels.GOLDEN_TEMPLE,
        })
