from ..DKCRNameConstants import Level as L

EU_OFFSET = -0x1000
US_REV_1_0_OFFSET = -0x2000

# Static Adresses across versions?
MEM = 0x80000000
GAME_ID = 0x0000
REV_NUMBER = 0x0007

# Every Address is from US Revision 1.1, this version is used as the main

GAME_STATE = 0x5AA660  # 32-bit
# 0x00 = In level
# 0x01 = World map
# 0x02 = Quitting from game over (briefly)
# 0x03 = World map (After quitting from a level)
# 0x04 = Startup / Title screen
# 0x05 = Super Guide
# 0x06 = Time Attack

P1_INPUTS = 0x5CBCEA  # 8-bit
P1_INPUTFIELD = 0x5CBCEB  # 8-bit
# Bit0 = Down
# Bit1 = Up
# Bit2 = Right
# Bit3 = Left

P1_CONTROLTYPE = 0x5CBD47  # 8-bit
# 0x01 = Horizontal
# 0x04 = Nunchuck

P1_ANALOG = 0x5cbd48 #

# P2_INPUTS = 0x5cc373  # 8-bit
P2_INPUTFIELD = 0x5cc373  # 8-bit
# Bit0 = Down
# Bit1 = Up
# Bit2 = Right
# Bit3 = Left

P2_CONTROLTYPE = 0x5cc3cf  # 8-bit
# 0x01 = Horizontal
# 0x04 = Nunchuck

P2_ANALOG = 0x5cc3d0 #

PLAYABLE_CHARACTER_PTR = 0x617864
# +0x4154 | Donkey Kong's Pointers
# .+0xe0
# ..+0x70
# ...+0xd0 = [32-bit BE] DK's Animation state.
# .+0x2BC
# ..+0x2B8 | Important DK Data
# ...+0x7C | [Float BE] DK Position X
# ...+0x80 = [Float BE] DK's Y Position (depth)
# ...+0x84 = [Float BE] DK's Z Position (height)
# ...+0x8c = [Bit2] DK is on the ground
# ...+0x8c = [Bit3] DK is NOT mounted on Rambi
# .+0x2d4
# ..+0xf8 Useful DK Data
# ...+0xf0 = [32-bit BE] DK's Jump combo counter (Single Player)
# ..+0x100 | Co-Op Only DK Pointers
# ...+0xf0 = [32-bit BE] DK's Coop Jump Combo
# +0x4158 | Diddy Kong's Pointers
# .+0xe0
# ..+0x70
# ...+0xd0 = [32-bit BE] Diddy's Animation state.
# .+0x2BC
# ..+0x2B8 | Important Diddy's Data
# ...+0x7C | [Float BE] Diddy's Position X
# ...+0x80 = [Float BE] Diddy's Y Position (depth)
# ...+0x84 = [Float BE] Diddy's Z Position (height)
# ...+0x8c = [Bit2] Diddy is on the ground
# ...+0x8c = [Bit3] Diddy is NOT mounted on Rambi or DK
# .+0x2d4
# ..+0xf8 | Useful Diddy Data
# ...+0xf0 = [32-bit BE] Diddy's Jump combo counter

IS_LEVEL_PAUSED = 0x617ecc

IN_PRE_RENDERED_CUTSCENE = 0x61fbf8

CUTSCENE_IDENTIFIER = 0x61fc04
# 0x315b20 = Tiki Tong reveal (Solo DK)
# 0x317360 = Tiki Tong reveal (DK & Diddy or Solo Diddy)
# 0x319120 = Golden Temple (Solo DK)
# 0x319220 = Golden Temple (DK & Diddy or Solo Diddy)
# 0x31a740 = Golden Temple reveal
# 0x31b100 = Victory (Solo DK)
# 0x31b380 = Game start
# 0x31b900 = Victory (DK & Diddy or Solo Diddy)


# WORLD_MAP_POS = 0x630B64
# (See also 0x62ffbc)
# +0x740
# ++0x48
# +++0xb2c = (Typically in MEM2)
# ++++0xd50 + 80823e3c = 80f421c0
# +++++0x288 80f40400
# +++++0x1e0 No pointer (back: 80decee0)
# ++++++0x34c = [32-bit BE] Location selected on world map 0x1=Freelook, 0x2-9 = Worlds in alphabetical order, 0xa = Golden Temple, 0xb = Zooming

WORLD_OF_CURRENT_LEVEL = 0x80b000
# [32-bit BE] (EU) World of current level, updates on entry / file select. Worlds are in alphabetical order instead of numerical-except for Golden Temple
# 0x00 = Beach (2)
# 0x01 = Cave (4)
# 0x02 = Cliff (6)
# 0x03 = Factory (7)
# 0x04 = Forest (5)
# 0x05 = Jungle (1)
# 0x06 = Ruins (3)
# 0x07 = Volcano (8)
# 0x08 = Golden Temple (9)
CURRENT_LEVEL = 0x80b004
# [32-bit BE] (EU) Level number, updates on level entry / file select
# Normal level = Level Number+1
# Boss = 0x01
# Temple level = 0x00
# 7-R = 0x0a
# Shops dont change the number they have custom one in apworld code but not in emulator
LEVEL_DATA_POINTER = 0x80b028
# [32-bit BE] (EU) Pointer for level data. Levels seem to always be in the same order. Individual level data seems to all be structured the same.
# ++0x38 = [Float BE] Best recorded speedrun time
# ++0x3d = [8-bit] Medal earned. 0x03 = Shiny gold, 0x02 = Gold, 0x01 = Silver, 0x00 = Bronze, 0xff = no medal
# ++0x3e = [Bit7] Level available
# ++0x3e = [Bit6] Level cleared
# ++0x3e = [Bit5] Flag to play level clear animation
# ++0x3e = [Bit4] All puzzle pieces collected
# ++0x3e = [Bit3] KONG collected
# ++0x3e = [Bit2] Cleared with Super Guide
# ++0x3e = [Bit0] Mirror Mode cleared

RECORD_TIME_OFFSET = 0x38
MEDAL_OFFSET = 0x3d
LEVEL_DATA_FLAGS_OFFSET = 0x3e

PLATFORM_PANIC_POINTER = 0x071c
MUGLYS_MOUND_POINTER = 0x0e1c
JUNGLE_HIJINXS_POINTER = 0x0284
KING_OF_CLING_POINTER = 0x086c
TREE_TOP_BOP_POINTER = 0x0984
SUNSET_SHORE_POINTER = 0x07c4
CANOPY_CANNONS_POINTER = 0x0a9c
CRAZY_CART_POINTER = 0x0214
JUNGLE_SHOP_POINTER = 0x024c

TUMBLIN_TEMPLE_POINTER = 0x0d74
PINCHIN_PIRATES_POINTER = 0x0c5c
POPPIN_PLANKS_POINTER = 0x078c
SLOPPY_SANDS_POINTER = 0x055c
PEACEFUL_PIER_POINTER = 0x039c
CANNON_CLUSTER_POINTER = 0x11d4
STORMY_SHORE_POINTER = 0x0674
BLOWHOLE_BOUND_POINTER = 0x001c
TIDAL_TERROR_POINTER = 0x104c
BEACH_SHOP_POINTER = 0x06ac

SHIFTY_SMASHERS_POINTER = 0x00c4
RUINED_ROOST_POINTER = 0x0ccc
WONKY_WATERWAY_POINTER = 0x0834
BUTTON_BASH_POINTER = 0x032c
MAST_BLAST_POINTER = 0x1164
DAMP_DUNGEON_POINTER = 0x1084
ITTY_BITTY_BITERS_POINTER = 0x119c
TEMPLE_TOPPLE_POINTER = 0x1014
RUINS_SHOP_POINTER = 0x02f4

JAGGED_JEWELS_POINTER = 0x0b0c
THE_MOLE_TRAIN_POINTER = 0x0b44
RICKETY_RAILS_POINTER = 0x0754
GRIP_N_TRIP_POINTER = 0x0444
BOMBS_AWAY_POINTER = 0x0134
MOLE_PATROL_POINTER = 0x0604
CROWDED_CAVERN_POINTER = 0x0ec4
CAVE_SHOP_POINTER = 0x0364

BLAST_N_BOUNCE_POINTER = 0x0fa4
MANGORUBY_RUN_POINTER = 0x0d3c
VINE_VALLEY_POINTER = 0x08a4
CLINGY_SWINGY_POINTER = 0x07fc
FLUTTER_FLYAWAY_POINTER = 0x0bec
TIPPIN_TOTEMS_POINTER = 0x0efc
LONGSHOT_LAUNCH_POINTER = 0x0dac
SPRINGY_SPORES_POINTER = 0x0fdc
WIGGLEVINE_WONDERS_POINTER = 0x05cc
MUNCHER_MARATHON_POINTER = 0x0ad4
FOREST_SHOP_POINTER = 0x09bc

PERILOUS_PASSAGE_POINTER = 0x00fc
THUGLYS_HIGHRISE_POINTER = 0x063c
STICKY_SITUATION_POINTER = 0x0a64
PREHISTORIC_PATH_POINTER = 0x0c24
WEIGHTY_WAY_POINTER = 0x0bb4
BOULDER_ROLLER_POINTER = 0x0c94
PRECARIOUS_PLATEAU_POINTER = 0x02bc
CRUMBLE_CANYON_POINTER = 0x0054
TIPPY_SHIPPY_POINTER = 0x016c
CLIFFTOP_CLIMB_POINTER = 0x04b4
CLIFF_SHOP_POINTER = 0x0f6c

TREACHEROUS_TRACK_POINTER = 0x040c
FEATHER_FIEND_POINTER = 0x0524
FOGGY_FUMES_POINTER = 0x008c
SLAMMIN_STEEL_POINTER = 0x06e4
HANDY_HAZARDS_POINTER = 0x094c
GEAR_GETAWAY_POINTER = 0x0de4
COG_JOG_POINTER = 0x047c
SWITCHEROO_POINTER = 0x112c
MUSIC_MADNESS_POINTER = 0x0594
LIFT_OFF_LAUNCH_POINTER = 0x0f34
FACTORY_SHOP_POINTER = 0x01a4

FIVE_MONKEY_TRIAL_POINTER = 0x10bc
TIKI_TONG_TERROR_POINTER = 0x0d04
FURIOUS_FIRE_POINTER = 0x04ec
HOT_ROCKET_POINTER = 0x03d4
ROASTING_RAILS_POINTER = 0x0e54
SMOKEY_PEAK_POINTER = 0x0a2c
BOBBING_BASALT_POINTER = 0x0b7c
MOVING_MELTERS_POINTER = 0x08dc
RED_RED_RISING_POINTER = 0x01dc
VOLCANO_SHOP_POINTER = 0x0914

GOLDEN_TEMPLE_POINTER = 0x10f4

TIME_ATTACK_POINTER = 0x80c3c4
# [32-bit BE] (US 1.1) Pointer for time attack time
# +0xc = [Float BE] Current Time Attack run time

SUPER_KONG_COLORS = 0x80c497

BANANAS = 0x80dd84
BANANA_COINS = 0x80dd88
DK_HEALTH = 0x80dd8c
DIDDY_HEALTH = 0x80dd90
DK_JUICE_LEFT = 0x80dd94
DIDDY_JUICE_LEFT = 0x80dd98
LIVES = 0x80dd9c
PP_CURRENT_LEVEL = 0x80dda3
K_LETTER = 0x80dda7
O_LETTER = 0x80ddab
N_LETTER = 0x80ddaf
G_LETTER = 0x80ddb3
SQUAWKS = 0x80ddc0
HEART_BOOST_DK = 0x80ddc4
HEART_BOOST_DIDDY = 0x80ddc8
MIRROR = 0x80ddcc
RARE_ORB_JUNGLE = 0x80ddd0
RARE_ORB_BEACH = 0x80ddd4
RARE_ORB_RUINS = 0x80ddd8
RARE_ORB_CAVE = 0x80dddc
RARE_ORB_FOREST = 0x80dde0
RARE_ORB_CLIFF = 0x80dde4
RARE_ORB_FACTORY = 0x80dde8
RARE_ORB_VOLCANO = 0x80dddc
WORLD_MAP_KEY_BEACH = 0x80ddff
WORLD_MAP_KEY_CAVE = 0x80de03
WORLD_MAP_KEY_CLIFF = 0x80de07
WORLD_MAP_KEY_FACTORY = 0x80de0b
WORLD_MAP_KEY_FOREST = 0x80de0f
WORLD_MAP_KEY_JUNGLE = 0x80de13
WORLD_MAP_KEY_RUINS = 0x80de17
WORLD_MAP_KEY_VOLCANO = 0x80de1b
BANANA_JUICE_INV = 0x80de1f
SQUAWKS_INV = 0x80de23
HEART_BOOST_INV = 0x80de27
MIRROR_UNLOCKED = 0x80de28
ON_WORLD_MAP = 0x81ad60
PLAYER_COUNT = 0x84b1b4
SMTH_COUNTER_DIDDY_1 = 0x85428b
# [32-Bits BE] (US 1.1) Counter increases when jumping on a enemy or collecting anything as Diddy (or other elements like the pause menu appearing)
SMTH_COUNTER_DK = 0x856284
# [32-Bits BE] (US 1.1) Counter increases when jumping on a enemy or collecting anything as DK (or other elements like the pause menu appearing)
SMTH_COUNTER_DIDDY_2 = 0x85428b
# [32-Bits BE] (US 1.1) Counter increases when jumping on a enemy or collecting anything as Diddy (or other elements like the pause menu appearing)
CAM_X = 0x8562c8
# -500.0 = Game over
# -248.5 = Entering Golden Temple cutscene
# -112.0 = Entering some bonus rooms
# -101.0 = Playing bonus room
# -100.0 = Bonus room completion (victory or defeat)
# -99.5 = Entering some bonus rooms
# -1.0 = Cranky Kong's Shop
# 0.00 = Loading
# 1000.0 = Tiki Tong Fight initial, ending cutscene, credits (Fight takes place around this value too)
# Level complete scene, cutscenes maintain values around the trigger point
CAM_Y = 0x8562cc
CAM_Z = 0x8562d0
# -1000.0 = Game over
# -149.0 = Entering some bonus rooms (depends on room size?)
# -147.118454 = Some bonus room completions (victory or defeat)
# -143.301407 = Playing bonus room
# -141.118454 = Some bonus room completions
# 0.0 = Loading
# 25.0 = Golden Temple / Tiki Tong cutscenes (Tiki Tong fight occurs around -8)
# 851.0 = Cranky Kong's shop
LOADING_SCREEN_COUNTER = 0x856328