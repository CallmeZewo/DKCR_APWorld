from enum import StrEnum, IntEnum

class LevelIndex(IntEnum):
    K_LEVEL_INDEX = 0x0
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

class LevelMapIndex(IntEnum):
    HANDY_HAZARDS = 0x0
    WONKY_WATERWAY = 0x1
    CLIFFTOP_CLIMB = 0x2
    SLAMMIN_STEEL = 0x3
    FOGGY_FUMES = 0x4
    MOVING_MELTERS = 0x5
    MUSIC_MADNESS = 0x6
    TIKI_TONG_TERROR = 0x7
    KING_OF_CLING = 0x8
    SPRINGY_SPORES = 0x9
    BLOWHOLE_BOUND = 0xa
    CANNON_CLUSTER = 0xb
    GOLDEN_TEMPLE = 0xc
    JAGGED_JEWELS = 0xd
    DAMP_DUNGEON = 0xe
    BOMBS_AWAY = 0xf
    SWITCHEROO = 0x10
    STICKY_SITUATION = 0x11
    VINE_VALLEY = 0x12
    BOULDER_ROLLER = 0x13
    TUMBLIN_TEMPLE = 0x14
    FIVE_MONKEY_TRIAL = 0x15
    FOREST_SHOP = 0x16
    ITTY_BITTY_BITERS = 0x17
    SMOKEY_PEAK = 0x18
    TIDAL_TERROR = 0x19
    CRUMBLE_CANYON = 0x1a
    MAST_BLAST = 0x1b
    BLAST_N_BOUNCE = 0x1c
    TIPPIN_TOTEMS = 0x1d
    HOT_ROCKET = 0x1e
    RUINS_SHOP = 0x1f
    MOLE_PATROL = 0x20
    GEAR_GETAWAY = 0x21
    TIPPY_SHIPPY = 0x22
    LIFT_OFF_LAUNCH = 0x23
    MUGLYS_MOUND = 0x24
    FURIOUS_FIRE = 0x25
    MUNCHER_MARATHON = 0x26
    SUNSET_SHORE = 0x27
    CLINGY_SWINGY = 0x28
    TREE_TOP_BOP = 0x29
    GRIP_N_TRIP = 0x2a
    FEATHER_FIEND = 0x2b
    BEACH_SHOP = 0x2c
    RUINED_ROOST = 0x2d
    JUNGLE_SHOP = 0x2e
    TEMPLE_TOPPLE = 0x2f
    TREACHEROUS_TRACK = 0x30
    WEIGHTY_WAY = 0x31
    JUNGLE_HIJINXS = 0x32
    PERILOUS_PASSAGE = 0x33
    STORMY_SHORE = 0x34
    VOLCANO_SHOP = 0x35
    CROWDED_CAVERN = 0x36
    ROASTING_RAILS = 0x37
    POPPIN_PLANKS = 0x38
    WIGGLEVINE_WONDERS = 0x39
    SLOPPY_SANDS = 0x3a
    PRECARIOUS_PLATEAU = 0x3b
    CAVE_SHOP = 0x3c
    RED_RED_RISING = 0x3d
    THE_MOLE_TRAIN = 0x3e
    MANGORUBY_RUN = 0x3f
    FACTORY_SHOP = 0x40
    BOBBING_BASALT = 0x41
    COG_JOG = 0x42
    PEACEFUL_PIER = 0x43
    PINCHIN_PIRATES = 0x44
    PLATFORM_PANIC = 0x45
    SHIFTY_SMASHERS = 0x46
    CRAZY_CART = 0x47
    CANOPY_CANNONS = 0x48
    CLIFF_SHOP = 0x49
    RICKETY_RAILS = 0x4a
    THUGLYS_HIGHRISE = 0x4b
    FLUTTER_FLYAWAY = 0x4c
    LONGSHOT_LAUNCH = 0x4d
    PREHISTORIC_PATH = 0x4e
    BUTTON_BASH = 0x4f


class LevelOffset(IntEnum):
    PLATFORM_PANIC = 0x071c
    MUGLYS_MOUND = 0x0e1c
    JUNGLE_HIJINXS = 0x0284
    KING_OF_CLING = 0x086c
    TREE_TOP_BOP = 0x0984
    SUNSET_SHORE = 0x07c4
    CANOPY_CANNONS = 0x0a9c
    CRAZY_CART = 0x0214
    JUNGLE_SHOP = 0x024c

    TUMBLIN_TEMPLE = 0x0d74
    PINCHIN_PIRATES = 0x0c5c
    POPPIN_PLANKS = 0x078c
    SLOPPY_SANDS = 0x055c
    PEACEFUL_PIER = 0x039c
    CANNON_CLUSTER = 0x11d4
    STORMY_SHORE = 0x0674
    BLOWHOLE_BOUND = 0x001c
    TIDAL_TERROR = 0x104c
    BEACH_SHOP = 0x06ac

    SHIFTY_SMASHERS = 0x00c4
    RUINED_ROOST = 0x0ccc
    WONKY_WATERWAY = 0x0834
    BUTTON_BASH = 0x032c
    MAST_BLAST = 0x1164
    DAMP_DUNGEON = 0x1084
    ITTY_BITTY_BITERS = 0x119c
    TEMPLE_TOPPLE = 0x1014
    RUINS_SHOP = 0x02f4

    JAGGED_JEWELS = 0x0b0c
    THE_MOLE_TRAIN = 0x0b44
    RICKETY_RAILS = 0x0754
    GRIP_N_TRIP = 0x0444
    BOMBS_AWAY = 0x0134
    MOLE_PATROL = 0x0604
    CROWDED_CAVERN = 0x0ec4
    CAVE_SHOP = 0x0364

    BLAST_N_BOUNCE = 0x0fa4
    MANGORUBY_RUN = 0x0d3c
    VINE_VALLEY = 0x08a4
    CLINGY_SWINGY = 0x07fc
    FLUTTER_FLYAWAY = 0x0bec
    TIPPIN_TOTEMS = 0x0efc
    LONGSHOT_LAUNCH = 0x0dac
    SPRINGY_SPORES = 0x0fdc
    WIGGLEVINE_WONDERS = 0x05cc
    MUNCHER_MARATHON = 0x0ad4
    FOREST_SHOP = 0x09bc

    PERILOUS_PASSAGE = 0x00fc
    THUGLYS_HIGHRISE = 0x063c
    STICKY_SITUATION = 0x0a64
    PREHISTORIC_PATH = 0x0c24
    WEIGHTY_WAY = 0x0bb4
    BOULDER_ROLLER = 0x0c94
    PRECARIOUS_PLATEAU = 0x02bc
    CRUMBLE_CANYON = 0x0054
    TIPPY_SHIPPY = 0x016c
    CLIFFTOP_CLIMB = 0x04b4
    CLIFF_SHOP = 0x0f6c

    TREACHEROUS_TRACK = 0x040c
    FEATHER_FIEND = 0x0524
    FOGGY_FUMES = 0x008c
    SLAMMIN_STEEL = 0x06e4
    HANDY_HAZARDS = 0x094c
    GEAR_GETAWAY = 0x0de4
    COG_JOG = 0x047c
    SWITCHEROO = 0x112c
    MUSIC_MADNESS = 0x0594
    LIFT_OFF_LAUNCH = 0x0f34
    FACTORY_SHOP = 0x01a4

    FIVE_MONKEY_TRIAL = 0x10bc
    TIKI_TONG_TERROR = 0x0d04
    FURIOUS_FIRE = 0x04ec
    HOT_ROCKET = 0x03d4
    ROASTING_RAILS = 0x0e54
    SMOKEY_PEAK = 0x0a2c
    BOBBING_BASALT = 0x0b7c
    MOVING_MELTERS = 0x08dc
    RED_RED_RISING = 0x01dc
    VOLCANO_SHOP = 0x0914

    GOLDEN_TEMPLE = 0x10f4

class PPAmount(IntEnum):
    PP_0 = 0x0
    PP_5 = 0x5
    PP_7 = 0x7
    PP_9 = 0x9

class LevelName(StrEnum):
    # Jungle
    PLATFORM_PANIC = "Platform Panic"
    MUGLYS_MOUND = "Mugly's Mound"
    JUNGLE_HIJINXS = "Jungle Hijinxs"
    KING_OF_CLING = "King of Cling"
    TREE_TOP_BOP = "Tree Top Bop"
    SUNSET_SHORE = "Sunset Shore"
    CANOPY_CANNONS = "Canopy Cannons"
    CRAZY_CART = "Crazy Cart"
    JUNGLE_SHOP = "Jungle Shop"

    # Beach
    TUMBLIN_TEMPLE = "Tumblin' Temple"
    PINCHIN_PIRATES = "Pinchin' Pirates"
    POPPIN_PLANKS = "Poppin' Planks"
    SLOPPY_SANDS = "Sloppy Sands"
    PEACEFUL_PIER = "Peaceful Pier"
    CANNON_CLUSTER = "Cannon Cluster"
    STORMY_SHORE = "Stormy Shore"
    BLOWHOLE_BOUND = "Blowhole Bound"
    TIDAL_TERROR = "Tidal Terror"
    BEACH_SHOP = "Beach Shop"

    # Ruins
    SHIFTY_SMASHERS = "Shifty Smashers"
    RUINED_ROOST = "Ruined Roost"
    WONKY_WATERWAY = "Wonky Waterway"
    BUTTON_BASH = "Button Bash"
    MAST_BLAST = "Mast Blast"
    DAMP_DUNGEON = "Damp Dungeon"
    ITTY_BITTY_BITERS = "Itty Bitty Biters"
    TEMPLE_TOPPLE = "Temple Topple"
    RUINS_SHOP = "Ruins Shop"

    # Cave
    JAGGED_JEWELS = "Jagged Jewels"
    THE_MOLE_TRAIN = "The Mole Train"
    RICKETY_RAILS = "Rickety Rails"
    GRIP_N_TRIP = "Grip 'n' Trip"
    BOMBS_AWAY = "Bombs Away"
    MOLE_PATROL = "Mole Patrol"
    CROWDED_CAVERN = "Crowded Cavern"
    CAVE_SHOP = "Cave Shop"

    # Forest
    BLAST_N_BOUNCE = "Blast 'n' Bounce"
    MANGORUBY_RUN = "Mangoruby Run"
    VINE_VALLEY = "Vine Valley"
    CLINGY_SWINGY = "Clingy Swingy"
    FLUTTER_FLYAWAY = "Flutter Flyaway"
    TIPPIN_TOTEMS = "Tippin' Totems"
    LONGSHOT_LAUNCH = "Longshot Launch"
    SPRINGY_SPORES = "Springy Spores"
    WIGGLEVINE_WONDERS = "Wigglevine Wonders"
    MUNCHER_MARATHON = "Muncher Marathon"
    FOREST_SHOP = "Forest Shop"

    # Cliff
    PERILOUS_PASSAGE = "Perilous Passage"
    THUGLYS_HIGHRISE = "Thugly's Highrise"
    STICKY_SITUATION = "Sticky Situation"
    PREHISTORIC_PATH = "Prehistoric Path"
    WEIGHTY_WAY = "Weighty Way"
    BOULDER_ROLLER = "Boulder Roller"
    PRECARIOUS_PLATEAU = "Precarious Plateau"
    CRUMBLE_CANYON = "Crumble Canyon"
    TIPPY_SHIPPY = "Tippy Shippy"
    CLIFFTOP_CLIMB = "Clifftop Climb"
    CLIFF_SHOP = "Cliff Shop"

    # Factory
    TREACHEROUS_TRACK = "Treacherous Track"
    FEATHER_FIEND = "Feather Fiend"
    FOGGY_FUMES = "Foggy Fumes"
    SLAMMIN_STEEL = "Slammin' Steel"
    HANDY_HAZARDS = "Handy Hazards"
    GEAR_GETAWAY = "Gear Getaway"
    COG_JOG = "Cog Jog"
    SWITCHEROO = "Switcheroo"
    MUSIC_MADNESS = "Music Madness"
    LIFT_OFF_LAUNCH = "Lift-Off Launch"
    FACTORY_SHOP = "Factory Shop"

    # Volcano
    FIVE_MONKEY_TRIAL = "Five Monkey Trial"
    TIKI_TONG_TERROR = "Tiki Tong Terror"
    FURIOUS_FIRE = "Furious Fire"
    HOT_ROCKET = "Hot Rocket"
    ROASTING_RAILS = "Roasting Rails"
    SMOKEY_PEAK = "Smokey Peak"
    BOBBING_BASALT = "Bobbing Basalt"
    MOVING_MELTERS = "Moving Melters"
    RED_RED_RISING = "Red Red Rising"
    VOLCANO_SHOP = "Volcano Shop"

    # Golden Temple
    GOLDEN_TEMPLE_LEVEL = "Golden Temple Level"