from .levels import GameLevels
from .worlds import GameWorlds
from ..rule_utils import *

class Connection:
    def __init__(self, target, rule = None):
        self.target = target
        self.rule = rule

CONNECTIONS = {
    GameLevels.JUNGLE_HIJINXS: [
        Connection(GameLevels.KING_OF_CLING),
        Connection(GameWorlds.JUNGLE),
    ],
    GameLevels.KING_OF_CLING: [
        Connection(GameLevels.JUNGLE_HIJINXS),
        Connection(GameLevels.TREE_TOP_BOP),
        Connection(GameLevels.JUNGLE_SHOP),
        Connection(GameLevels.PLATFORM_PANIC, rule=has_all_jungle_letters),
    ],
    GameLevels.TREE_TOP_BOP: [
        Connection(GameLevels.KING_OF_CLING),
        Connection(GameLevels.CANOPY_CANNONS),
        Connection(GameLevels.SUNSET_SHORE, rule=has_jungle_key),
    ],
    GameLevels.SUNSET_SHORE: [
        Connection(GameLevels.TREE_TOP_BOP),
        Connection(GameLevels.CRAZY_CART),
    ],
    GameLevels.CANOPY_CANNONS: [
        Connection(GameLevels.TREE_TOP_BOP),
        Connection(GameLevels.CRAZY_CART),
    ],
    GameLevels.CRAZY_CART: [
        Connection(GameLevels.CANOPY_CANNONS),
        Connection(GameLevels.SUNSET_SHORE, rule=has_jungle_key),
        Connection(GameLevels.MUGLYS_MOUND, rule=can_enter_muglys_mound()),
    ],
    GameLevels.PLATFORM_PANIC: [
        Connection(GameLevels.KING_OF_CLING),
    ],
    GameLevels.MUGLYS_MOUND: [
        Connection(GameLevels.CRAZY_CART),
    ],
    GameLevels.JUNGLE_SHOP: [
        Connection(GameLevels.KING_OF_CLING),
    ],
    GameWorlds.JUNGLE: [
        Connection(GameLevels.JUNGLE_HIJINXS),
        Connection(GameWorlds.BEACH, rule=beaten_boss_jungle),
    ],
    GameLevels.POPPIN_PLANKS: [
        Connection(GameLevels.SLOPPY_SANDS),
        Connection(GameWorlds.BEACH),
    ],
    GameLevels.SLOPPY_SANDS: [
        Connection(GameLevels.POPPIN_PLANKS),
        Connection(GameLevels.BEACH_SHOP),
        Connection(GameLevels.PEACEFUL_PIER),
    ],
    GameLevels.PEACEFUL_PIER: [
        Connection(GameLevels.SLOPPY_SANDS),
        Connection(GameLevels.CANNON_CLUSTER),
        Connection(GameLevels.BLOWHOLE_BOUND, rule=has_beach_key),
    ],
    GameLevels.CANNON_CLUSTER: [
        Connection(GameLevels.PEACEFUL_PIER),
        Connection(GameLevels.STORMY_SHORE),
    ],
    GameLevels.STORMY_SHORE: [
        Connection(GameLevels.CANNON_CLUSTER),
        Connection(GameLevels.TIDAL_TERROR),
        Connection(GameLevels.BLOWHOLE_BOUND, rule=has_beach_key),
    ],
    GameLevels.BLOWHOLE_BOUND: [
        Connection(GameLevels.PEACEFUL_PIER),
        Connection(GameLevels.STORMY_SHORE),
    ],
    GameLevels.TIDAL_TERROR: [
        Connection(GameLevels.STORMY_SHORE),
        Connection(GameLevels.PINCHIN_PIRATES, rule=can_enter_pinchin_pirates()),
        Connection(GameLevels.TUMBLIN_TEMPLE, rule=has_all_beach_letters),
    ],
    GameLevels.TUMBLIN_TEMPLE: [
        Connection(GameLevels.TIDAL_TERROR),
    ],
    GameLevels.PINCHIN_PIRATES: [
        Connection(GameLevels.TIDAL_TERROR),
    ],
    GameLevels.BEACH_SHOP: [
        Connection(GameLevels.SLOPPY_SANDS),
    ],
    GameWorlds.BEACH: [
        Connection(GameLevels.POPPIN_PLANKS),
        Connection(GameWorlds.RUINS, rule=beaten_boss_beach),
    ],
    GameLevels.WONKY_WATERWAY: [
        Connection(GameLevels.BUTTON_BASH),
        Connection(GameWorlds.RUINS),
        Connection(GameLevels.DAMP_DUNGEON, rule=has_ruins_key),
    ],
    GameLevels.BUTTON_BASH: [
        Connection(GameLevels.WONKY_WATERWAY),
        Connection(GameLevels.RUINS_SHOP),
        Connection(GameLevels.MAST_BLAST),
    ],
    GameLevels.MAST_BLAST: [
        Connection(GameLevels.BUTTON_BASH),
        Connection(GameLevels.ITTY_BITTY_BITERS),
        Connection(GameLevels.DAMP_DUNGEON, rule=has_ruins_key),
    ],
    GameLevels.DAMP_DUNGEON: [
        Connection(GameLevels.WONKY_WATERWAY),
        Connection(GameLevels.MAST_BLAST),
        Connection(GameLevels.TEMPLE_TOPPLE),
    ],
    GameLevels.ITTY_BITTY_BITERS: [
        Connection(GameLevels.MAST_BLAST),
        Connection(GameLevels.TEMPLE_TOPPLE),
        Connection(GameLevels.SHIFTY_SMASHERS, rule=has_all_ruins_letters),
    ],
    GameLevels.TEMPLE_TOPPLE: [
        Connection(GameLevels.ITTY_BITTY_BITERS),
        Connection(GameLevels.DAMP_DUNGEON, rule=has_ruins_key),
        Connection(GameLevels.RUINED_ROOST, rule=can_enter_ruined_roost()),
    ],
    GameLevels.SHIFTY_SMASHERS: [
        Connection(GameLevels.ITTY_BITTY_BITERS),
    ],
    GameLevels.RUINED_ROOST: [
        Connection(GameLevels.TEMPLE_TOPPLE),
    ],
    GameLevels.RUINS_SHOP: [
        Connection(GameLevels.BUTTON_BASH),
    ],
    GameWorlds.RUINS: [
        Connection(GameLevels.WONKY_WATERWAY),
        Connection(GameWorlds.CAVE, rule=beaten_boss_ruins),
    ],
    GameLevels.RICKETY_RAILS: [
        Connection(GameLevels.GRIP_N_TRIP),
        Connection(GameLevels.BOMBS_AWAY),
        Connection(GameWorlds.CAVE),
    ],
    GameLevels.GRIP_N_TRIP: [
        Connection(GameLevels.RICKETY_RAILS),
        Connection(GameLevels.CAVE_SHOP),
        Connection(GameLevels.MOLE_PATROL, rule=has_cave_key),
    ],
    GameLevels.BOMBS_AWAY: [
        Connection(GameLevels.RICKETY_RAILS),
        Connection(GameLevels.CAVE_SHOP),
        Connection(GameLevels.CROWDED_CAVERN),
        Connection(GameLevels.JAGGED_JEWELS, rule=has_all_cave_letters),
    ],
    GameLevels.MOLE_PATROL: [
        Connection(GameLevels.GRIP_N_TRIP),
        Connection(GameLevels.THE_MOLE_TRAIN, rule=can_enter_the_mole_train()),
    ],
    GameLevels.CROWDED_CAVERN: [
        Connection(GameLevels.BOMBS_AWAY),
        Connection(GameLevels.CAVE_SHOP),
        Connection(GameLevels.THE_MOLE_TRAIN, rule=can_enter_the_mole_train()),
    ],
    GameLevels.JAGGED_JEWELS: [
        Connection(GameLevels.BOMBS_AWAY),
    ],
    GameLevels.THE_MOLE_TRAIN: [
        Connection(GameLevels.CROWDED_CAVERN),
        Connection(GameLevels.MOLE_PATROL, rule=has_cave_key),
    ],
    GameLevels.CAVE_SHOP: [
        Connection(GameLevels.GRIP_N_TRIP),
        Connection(GameLevels.BOMBS_AWAY),
        Connection(GameLevels.CROWDED_CAVERN),
    ],
    GameWorlds.CAVE: [
        Connection(GameLevels.RICKETY_RAILS),
        Connection(GameWorlds.FOREST, rule=beaten_boss_cave),
    ],
    GameLevels.VINE_VALLEY: [
        Connection(GameLevels.CLINGY_SWINGY),
        Connection(GameWorlds.FOREST),
    ],
    GameLevels.CLINGY_SWINGY: [
        Connection(GameLevels.VINE_VALLEY),
        Connection(GameLevels.FLUTTER_FLYAWAY),
        Connection(GameLevels.BLAST_N_BOUNCE, rule=has_all_forest_letters),
        Connection(GameLevels.SPRINGY_SPORES, rule=has_forest_key),
    ],
    GameLevels.FLUTTER_FLYAWAY: [
        Connection(GameLevels.CLINGY_SWINGY),
        Connection(GameLevels.FOREST_SHOP),
        Connection(GameLevels.TIPPIN_TOTEMS),
    ],
    GameLevels.TIPPIN_TOTEMS: [
        Connection(GameLevels.FLUTTER_FLYAWAY),
        Connection(GameLevels.LONGSHOT_LAUNCH),
    ],
    GameLevels.LONGSHOT_LAUNCH: [
        Connection(GameLevels.TIPPIN_TOTEMS),
        Connection(GameLevels.MUNCHER_MARATHON),
    ],
    GameLevels.SPRINGY_SPORES: [
        Connection(GameLevels.CLINGY_SWINGY),
        Connection(GameLevels.WIGGLEVINE_WONDERS),
    ],
    GameLevels.WIGGLEVINE_WONDERS: [
        Connection(GameLevels.MUNCHER_MARATHON),
        Connection(GameLevels.SPRINGY_SPORES),
    ],
    GameLevels.MUNCHER_MARATHON: [
        Connection(GameLevels.LONGSHOT_LAUNCH),
        Connection(GameLevels.MANGORUBY_RUN, rule=can_enter_mangoruby_run()),
        Connection(GameLevels.WIGGLEVINE_WONDERS, rule=has_forest_key),
    ],
    GameLevels.BLAST_N_BOUNCE: [
        Connection(GameLevels.CLINGY_SWINGY),
    ],
    GameLevels.MANGORUBY_RUN: [
        Connection(GameLevels.MUNCHER_MARATHON),
    ],
    GameLevels.FOREST_SHOP: [
        Connection(GameLevels.FLUTTER_FLYAWAY),
    ],
    GameWorlds.FOREST: [
        Connection(GameLevels.VINE_VALLEY),
        Connection(GameWorlds.CLIFF, rule=beaten_boss_forest),
    ],
    GameLevels.STICKY_SITUATION: [
        Connection(GameLevels.PREHISTORIC_PATH),
        Connection(GameWorlds.CLIFF),
    ],
    GameLevels.PREHISTORIC_PATH: [
        Connection(GameLevels.STICKY_SITUATION),
        Connection(GameLevels.WEIGHTY_WAY),
        Connection(GameLevels.PERILOUS_PASSAGE, rule=has_all_cliff_letters),
    ],
    GameLevels.WEIGHTY_WAY: [
        Connection(GameLevels.PREHISTORIC_PATH),
        Connection(GameLevels.CLIFF_SHOP),
        Connection(GameLevels.BOULDER_ROLLER),
        Connection(GameLevels.PRECARIOUS_PLATEAU, rule=has_cliff_key),
    ],
    GameLevels.BOULDER_ROLLER: [
        Connection(GameLevels.WEIGHTY_WAY),
        Connection(GameLevels.CRUMBLE_CANYON),
    ],
    GameLevels.PRECARIOUS_PLATEAU: [
        Connection(GameLevels.WEIGHTY_WAY),
        Connection(GameLevels.CRUMBLE_CANYON),
    ],
    GameLevels.CRUMBLE_CANYON: [
        Connection(GameLevels.BOULDER_ROLLER),
        Connection(GameLevels.TIPPY_SHIPPY),
        Connection(GameLevels.PRECARIOUS_PLATEAU, rule=has_cliff_key),
    ],
    GameLevels.TIPPY_SHIPPY: [
        Connection(GameLevels.CRUMBLE_CANYON),
        Connection(GameLevels.CLIFFTOP_CLIMB),
    ],
    GameLevels.CLIFFTOP_CLIMB: [
        Connection(GameLevels.TIPPY_SHIPPY),
        Connection(GameLevels.THUGLYS_HIGHRISE, rule=can_enter_thuglys_highrise()),
    ],
    GameLevels.PERILOUS_PASSAGE: [
        Connection(GameLevels.PREHISTORIC_PATH),
    ],
    GameLevels.THUGLYS_HIGHRISE: [
        Connection(GameLevels.CLIFFTOP_CLIMB),
    ],
    GameLevels.CLIFF_SHOP: [
        Connection(GameLevels.WEIGHTY_WAY),
    ],
    GameWorlds.CLIFF: [
        Connection(GameLevels.STICKY_SITUATION),
        Connection(GameWorlds.FACTORY, rule=beaten_boss_cliff),
    ],
    GameLevels.FOGGY_FUMES: [
        Connection(GameWorlds.FACTORY),
        Connection(GameLevels.SLAMMIN_STEEL, rule=smog_blocks_factory()),
    ],
    GameLevels.SLAMMIN_STEEL: [
        Connection(GameLevels.FOGGY_FUMES),
        Connection(GameLevels.FACTORY_SHOP),
        Connection(GameLevels.GEAR_GETAWAY),
        Connection(GameLevels.HANDY_HAZARDS, rule=has_factory_key),
    ],
    GameLevels.HANDY_HAZARDS: [
        Connection(GameLevels.SLAMMIN_STEEL),
        Connection(GameLevels.COG_JOG),
        Connection(GameLevels.TREACHEROUS_TRACK, rule=has_all_factory_letters),
    ],
    GameLevels.GEAR_GETAWAY: [
        Connection(GameLevels.SLAMMIN_STEEL),
        Connection(GameLevels.COG_JOG),
    ],
    GameLevels.COG_JOG: [
        Connection(GameLevels.GEAR_GETAWAY),
        Connection(GameLevels.SWITCHEROO),
        Connection(GameLevels.MUSIC_MADNESS),
        Connection(GameLevels.HANDY_HAZARDS, rule=has_factory_key),
    ],
    GameLevels.SWITCHEROO: [
        Connection(GameLevels.COG_JOG),
        Connection(GameLevels.MUSIC_MADNESS),
    ],
    GameLevels.MUSIC_MADNESS: [
        Connection(GameLevels.SWITCHEROO),
        Connection(GameLevels.COG_JOG),
        Connection(GameLevels.LIFT_OFF_LAUNCH, rule=can_enter_Lift_Off_Launch),
    ],
    GameLevels.LIFT_OFF_LAUNCH: [
        Connection(GameLevels.MUSIC_MADNESS),
        Connection(GameLevels.FEATHER_FIEND, rule=can_enter_feather_fiend()),
    ],
    GameLevels.TREACHEROUS_TRACK: [
        Connection(GameLevels.HANDY_HAZARDS),
    ],
    GameLevels.FEATHER_FIEND: [
        Connection(GameLevels.LIFT_OFF_LAUNCH),
    ],
    GameLevels.FACTORY_SHOP: [
        Connection(GameLevels.SLAMMIN_STEEL),
    ],
    GameWorlds.FACTORY: [
        Connection(GameLevels.FOGGY_FUMES),
        Connection(GameWorlds.VOLCANO, rule=beaten_boss_factory),
    ],
    GameLevels.FURIOUS_FIRE: [
        Connection(GameLevels.VOLCANO_SHOP),
        Connection(GameLevels.HOT_ROCKET),
        Connection(GameWorlds.VOLCANO),
    ],
    GameLevels.HOT_ROCKET: [
        Connection(GameLevels.ROASTING_RAILS),
        Connection(GameLevels.SMOKEY_PEAK, rule=has_volcano_key),
    ],
    GameLevels.SMOKEY_PEAK: [
        Connection(GameLevels.HOT_ROCKET),
        Connection(GameLevels.BOBBING_BASALT),
    ],
    GameLevels.BOBBING_BASALT: [
        Connection(GameLevels.ROASTING_RAILS),
        Connection(GameLevels.MOVING_MELTERS),
        Connection(GameLevels.SMOKEY_PEAK, rule=has_volcano_key),
    ],
    GameLevels.MOVING_MELTERS: [
        Connection(GameLevels.BOBBING_BASALT),
        Connection(GameLevels.RED_RED_RISING),
        Connection(GameLevels.FIVE_MONKEY_TRIAL, rule=has_all_volcano_letters),
    ],
    GameLevels.RED_RED_RISING: [
        Connection(GameLevels.MOVING_MELTERS),
        Connection(GameLevels.TIKI_TONG_TERROR, rule=can_enter_tiki_tong_terror()),
    ],
    GameLevels.FIVE_MONKEY_TRIAL:[
        Connection(GameLevels.MOVING_MELTERS),
    ],
    GameLevels.TIKI_TONG_TERROR: [
        Connection(GameLevels.RED_RED_RISING),
    ],
    GameLevels.VOLCANO_SHOP: [
        Connection(GameLevels.FURIOUS_FIRE),
    ],
    GameWorlds.VOLCANO: [
        Connection(GameLevels.FURIOUS_FIRE),
        Connection(GameWorlds.GOLDEN_TEMPLE_WORLD, rule=can_enter_golden_temple()),
    ],
    GameWorlds.GOLDEN_TEMPLE_WORLD: [
        Connection(GameLevels.GOLDEN_TEMPLE),
        Connection(GameWorlds.JUNGLE),
    ],
    GameLevels.GOLDEN_TEMPLE: [
        Connection(GameWorlds.GOLDEN_TEMPLE_WORLD),
    ],
}