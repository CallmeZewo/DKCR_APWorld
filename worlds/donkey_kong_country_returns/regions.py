from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Entrance, Region

from .strings import Region as R, RegionConnection as RC

if TYPE_CHECKING:
    from .world import DKCRWorld

def create_and_connect_regions(world: DKCRWorld) -> None:
    create_all_regions(world)
    connect_regions(world)

def create_all_regions(world: DKCRWorld) -> None:
    # Jungle
    Jungle = create_all_regions_helper(R.JUNGLE, world)
    Jungle_Shop = create_all_regions_helper(R.JUNGLE_SHOP, world)
    Jungle_Hijinxs = create_all_regions_helper(R.JUNGLE_HIJINXS, world)
    King_of_Cling = create_all_regions_helper(R.KING_OF_CLING, world)
    Tree_Top_Bop = create_all_regions_helper(R.TREE_TOP_BOP, world)
    Sunset_Shore = create_all_regions_helper(R.SUNSET_SHORE, world)
    Canopy_Cannons = create_all_regions_helper(R.CANOPY_CANNONS, world)
    Crazy_Cart = create_all_regions_helper(R.CRAZY_CART, world)
    Muglys_Mound = create_all_regions_helper(R.MUGLYS_MOUND, world)
    Platform_Panic = create_all_regions_helper(R.PLATFORM_PANIC, world)

    # Beach
    Beach = create_all_regions_helper(R.BEACH, world)
    Beach_Shop = create_all_regions_helper(R.BEACH_SHOP, world)
    Poppin_Planks = create_all_regions_helper(R.POPPIN_PLANKS, world)
    Sloppy_Sands = create_all_regions_helper(R.SLOPPY_SANDS, world)
    Peaceful_Pier = create_all_regions_helper(R.PEACEFUL_PIER, world)
    Cannon_Cluster = create_all_regions_helper(R.CANNON_CLUSTER, world)
    Stormy_Shore = create_all_regions_helper(R.STORMY_SHORE, world)
    Blowhole_Bound = create_all_regions_helper(R.BLOWHOLE_BOUND, world)
    Tidal_Terror = create_all_regions_helper(R.TIDAL_TERROR, world)
    Pinchin_Pirates = create_all_regions_helper(R.PINCHIN_PIRATES, world)
    Tumblin_Temple = create_all_regions_helper(R.TUMBLIN_TEMPLE, world)

    # Ruins
    Ruins = create_all_regions_helper(R.RUINS, world)
    Ruins_Shop = create_all_regions_helper(R.RUINS_SHOP, world)
    Wonky_Waterway = create_all_regions_helper(R.WONKY_WATERWAY, world)
    Button_Bash = create_all_regions_helper(R.BUTTON_BASH, world)
    Mast_Blast = create_all_regions_helper(R.MAST_BLAST, world)
    Damp_Dungeon = create_all_regions_helper(R.DAMP_DUNGEON, world)
    Itty_Bitty_Biters = create_all_regions_helper(R.ITTY_BITTY_BITERS, world)
    Temple_Topple = create_all_regions_helper(R.TEMPLE_TOPPLE, world)
    Ruined_Roost = create_all_regions_helper(R.RUINED_ROOST, world)
    Shifty_Smashers = create_all_regions_helper(R.SHIFTY_SMASHERS, world)

    # Cave
    Cave = create_all_regions_helper(R.CAVE, world)
    Cave_Shop = create_all_regions_helper(R.CAVE_SHOP, world)
    Rickety_Rails = create_all_regions_helper(R.RICKETY_RAILS, world)
    Grip_n_Trip = create_all_regions_helper(R.GRIP_N_TRIP, world)
    Bombs_Away = create_all_regions_helper(R.BOMBS_AWAY, world)
    Mole_Patrol = create_all_regions_helper(R.MOLE_PATROL, world)
    Crowded_Cavern = create_all_regions_helper(R.CROWDED_CAVERN, world)
    The_Mole_Train = create_all_regions_helper(R.THE_MOLE_TRAIN, world)
    Jagged_Jewels = create_all_regions_helper(R.JAGGED_JEWELS, world)

    # Forest
    Forest = create_all_regions_helper(R.FOREST, world)
    Forest_Shop = create_all_regions_helper(R.FOREST_SHOP, world)
    Vine_Valley = create_all_regions_helper(R.VINE_VALLEY, world)
    Clingy_Swingy = create_all_regions_helper(R.CLINGY_SWINGY, world)
    Flutter_Flyaway = create_all_regions_helper(R.FLUTTER_FLYAWAY, world)
    Tippin_Totems = create_all_regions_helper(R.TIPPIN_TOTEMS, world)
    Longshot_Launch = create_all_regions_helper(R.LONGSHOT_LAUNCH, world)
    Springy_Spores = create_all_regions_helper(R.SPRINGY_SPORES, world)
    Wigglevine_Wonders = create_all_regions_helper(R.WIGGLEVINE_WONDERS, world)
    Muncher_Marathon = create_all_regions_helper(R.MUNCHER_MARATHON, world)
    Mangoruby_Run = create_all_regions_helper(R.MANGORUBY_RUN, world)
    Blast_n_Bounce = create_all_regions_helper(R.BLAST_N_BOUNCE, world)

    # Cliff
    Cliff = create_all_regions_helper(R.CLIFF, world)
    Cliff_Shop = create_all_regions_helper(R.CLIFF_SHOP, world)
    Sticky_Situation = create_all_regions_helper(R.STICKY_SITUATION, world)
    Prehistoric_Path = create_all_regions_helper(R.PREHISTORIC_PATH, world)
    Weighty_Way = create_all_regions_helper(R.WEIGHTY_WAY, world)
    Boulder_Roller = create_all_regions_helper(R.BOULDER_ROLLER, world)
    Precarious_Plateau = create_all_regions_helper(R.PRECARIOUS_PLATEAU, world)
    Crumble_Canyon = create_all_regions_helper(R.CRUMBLE_CANYON, world)
    Tippy_Shippy = create_all_regions_helper(R.TIPPY_SHIPPY, world)
    Clifftop_Climb = create_all_regions_helper(R.CLIFFTOP_CLIMB, world)
    Thuglys_Highrise = create_all_regions_helper(R.THUGLYS_HIGHRISE, world)
    Perilous_Passage = create_all_regions_helper(R.PERILOUS_PASSAGE, world)

    # Factory
    Factory = create_all_regions_helper(R.FACTORY, world)
    Factory_Shop = create_all_regions_helper(R.FACTORY_SHOP, world)
    Foggy_Fumes = create_all_regions_helper(R.FOGGY_FUMES, world)
    Slammin_Steel = create_all_regions_helper(R.SLAMMIN_STEEL, world)
    Handy_Hazards = create_all_regions_helper(R.HANDY_HAZARDS, world)
    Gear_Getaway = create_all_regions_helper(R.GEAR_GETAWAY, world)
    Cog_Jog = create_all_regions_helper(R.COG_JOG, world)
    Switcheroo = create_all_regions_helper(R.SWITCHEROO, world)
    Music_Madness = create_all_regions_helper(R.MUSIC_MADNESS, world)
    Lift_Off_Launch = create_all_regions_helper(R.LIFT_OFF_LAUNCH, world)
    Feather_Fiend = create_all_regions_helper(R.FEATHER_FIEND, world)
    Treacherous_Track = create_all_regions_helper(R.TREACHEROUS_TRACK, world)

    # Volcano
    Volcano = create_all_regions_helper(R.VOLCANO, world)
    Volcano_Shop = create_all_regions_helper(R.VOLCANO_SHOP, world)
    Furious_Fire = create_all_regions_helper(R.FURIOUS_FIRE, world)
    Hot_Rocket = create_all_regions_helper(R.HOT_ROCKET, world)
    Roasting_Rails = create_all_regions_helper(R.ROASTING_RAILS, world)
    Smokey_Peak = create_all_regions_helper(R.SMOKEY_PEAK, world)
    Bobbing_Basalt = create_all_regions_helper(R.BOBBING_BASALT, world)
    Moving_Melters = create_all_regions_helper(R.MOVING_MELTERS, world)
    Red_Red_Rising = create_all_regions_helper(R.RED_RED_RISING, world)
    Tiki_Tong_Terror = create_all_regions_helper(R.TIKI_TONG_TERROR, world)
    Five_Monkey_Trial = create_all_regions_helper(R.FIVE_MONKEY_TRIAL, world)

    regions = [
        Jungle,
        Jungle_Shop,
        Jungle_Hijinxs,
        King_of_Cling,
        Tree_Top_Bop,
        Sunset_Shore,
        Canopy_Cannons,
        Crazy_Cart,
        Muglys_Mound,
        Platform_Panic,

        Beach,
        Beach_Shop,
        Poppin_Planks,
        Sloppy_Sands,
        Peaceful_Pier,
        Cannon_Cluster,
        Stormy_Shore,
        Blowhole_Bound,
        Tidal_Terror,
        Pinchin_Pirates,
        Tumblin_Temple,

        Ruins,
        Ruins_Shop,
        Wonky_Waterway,
        Button_Bash,
        Mast_Blast,
        Damp_Dungeon,
        Itty_Bitty_Biters,
        Temple_Topple,
        Ruined_Roost,
        Shifty_Smashers,

        Cave,
        Cave_Shop,
        Rickety_Rails,
        Grip_n_Trip,
        Bombs_Away,
        Mole_Patrol,
        Crowded_Cavern,
        The_Mole_Train,
        Jagged_Jewels,

        Forest,
        Forest_Shop,
        Vine_Valley,
        Clingy_Swingy,
        Flutter_Flyaway,
        Tippin_Totems,
        Longshot_Launch,
        Springy_Spores,
        Wigglevine_Wonders,
        Muncher_Marathon,
        Mangoruby_Run,
        Blast_n_Bounce,

        Cliff,
        Cliff_Shop,
        Sticky_Situation,
        Prehistoric_Path,
        Weighty_Way,
        Boulder_Roller,
        Precarious_Plateau,
        Crumble_Canyon,
        Tippy_Shippy,
        Clifftop_Climb,
        Thuglys_Highrise,
        Perilous_Passage,

        Factory,
        Factory_Shop,
        Foggy_Fumes,
        Slammin_Steel,
        Handy_Hazards,
        Gear_Getaway,
        Cog_Jog,
        Switcheroo,
        Music_Madness,
        Lift_Off_Launch,
        Feather_Fiend,
        Treacherous_Track,

        Volcano,
        Volcano_Shop,
        Furious_Fire,
        Hot_Rocket,
        Roasting_Rails,
        Smokey_Peak,
        Bobbing_Basalt,
        Moving_Melters,
        Red_Red_Rising,
        Tiki_Tong_Terror,
        Five_Monkey_Trial
    ]

    if world.options.golden_temple:
        Golden_Temple = create_all_regions_helper(R.GOLDEN_TEMPLE, world)
        regions.append(Golden_Temple)

    world.multiworld.regions += regions

def create_all_regions_helper(name: str, world: DKCRWorld) -> Region:
    return Region(name, world.player, world.multiworld)

def connect_regions(world: DKCRWorld) -> None:
    Jungle = world.get_region(R.JUNGLE)
    Jungle_Shop = world.get_region(R.JUNGLE_SHOP)
    Jungle_Hijinxs = world.get_region(R.JUNGLE_HIJINXS)
    King_of_Cling = world.get_region(R.KING_OF_CLING)
    Tree_Top_Bop = world.get_region(R.TREE_TOP_BOP)
    Sunset_Shore = world.get_region(R.SUNSET_SHORE)
    Canopy_Cannons = world.get_region(R.CANOPY_CANNONS)
    Crazy_Cart = world.get_region(R.CRAZY_CART)
    Muglys_Mound = world.get_region(R.MUGLYS_MOUND)
    Platform_Panic = world.get_region(R.PLATFORM_PANIC)

    Beach = world.get_region(R.BEACH)
    Beach_Shop = world.get_region(R.BEACH_SHOP)
    Poppin_Planks = world.get_region(R.POPPIN_PLANKS)
    Sloppy_Sands = world.get_region(R.SLOPPY_SANDS)
    Peaceful_Pier = world.get_region(R.PEACEFUL_PIER)
    Cannon_Cluster = world.get_region(R.CANNON_CLUSTER)
    Stormy_Shore = world.get_region(R.STORMY_SHORE)
    Blowhole_Bound = world.get_region(R.BLOWHOLE_BOUND)
    Tidal_Terror = world.get_region(R.TIDAL_TERROR)
    Pinchin_Pirates = world.get_region(R.PINCHIN_PIRATES)
    Tumblin_Temple = world.get_region(R.TUMBLIN_TEMPLE)

    Ruins = world.get_region(R.RUINS)
    Ruins_Shop = world.get_region(R.RUINS_SHOP)
    Wonky_Waterways = world.get_region(R.WONKY_WATERWAY)
    Button_Bash = world.get_region(R.BUTTON_BASH)
    Mast_Blast = world.get_region(R.MAST_BLAST)
    Damp_Dungeon = world.get_region(R.DAMP_DUNGEON)
    Itty_Bitty_Biters = world.get_region(R.ITTY_BITTY_BITERS)
    Temple_Topple = world.get_region(R.TEMPLE_TOPPLE)
    Ruined_Roost = world.get_region(R.RUINED_ROOST)
    Shifty_Smashers = world.get_region(R.SHIFTY_SMASHERS)

    Cave = world.get_region(R.CAVE)
    Cave_Shop = world.get_region(R.CAVE_SHOP)
    Rickety_Rails = world.get_region(R.RICKETY_RAILS)
    Grip_n_Trip = world.get_region(R.GRIP_N_TRIP)
    Bombs_Away = world.get_region(R.BOMBS_AWAY)
    Mole_Patrol = world.get_region(R.MOLE_PATROL)
    Crowded_Cavern = world.get_region(R.CROWDED_CAVERN)
    The_Mole_Train = world.get_region(R.THE_MOLE_TRAIN)
    Jagged_Jewels = world.get_region(R.JAGGED_JEWELS)

    Forest = world.get_region(R.FOREST)
    Forest_Shop = world.get_region(R.FOREST_SHOP)
    Vine_Valley = world.get_region(R.VINE_VALLEY)
    Clingy_Swingy = world.get_region(R.CLINGY_SWINGY)
    Flutter_Flyaway = world.get_region(R.FLUTTER_FLYAWAY)
    Tippin_Totems = world.get_region(R.TIPPIN_TOTEMS)
    Longshot_Launch = world.get_region(R.LONGSHOT_LAUNCH)
    Springy_Spores = world.get_region(R.SPRINGY_SPORES)
    Wigglevine_Wonders = world.get_region(R.WIGGLEVINE_WONDERS)
    Muncher_Marathon = world.get_region(R.MUNCHER_MARATHON)
    Mangoruby_Run = world.get_region(R.MANGORUBY_RUN)
    Blast_n_Bounce = world.get_region(R.BLAST_N_BOUNCE)

    Cliff = world.get_region(R.CLIFF)
    Cliff_Shop = world.get_region(R.CLIFF_SHOP)
    Sticky_Situation = world.get_region(R.STICKY_SITUATION)
    Prehistoric_Path = world.get_region(R.PREHISTORIC_PATH)
    Weighty_Way = world.get_region(R.WEIGHTY_WAY)
    Boulder_Roller = world.get_region(R.BOULDER_ROLLER)
    Precarious_Plateau = world.get_region(R.PRECARIOUS_PLATEAU)
    Crumble_Canyon = world.get_region(R.CRUMBLE_CANYON)
    Tippy_Shippy = world.get_region(R.TIPPY_SHIPPY)
    Clifftop_Climb = world.get_region(R.CLIFFTOP_CLIMB)
    Thuglys_Highrise = world.get_region(R.THUGLYS_HIGHRISE)
    Perilous_Passage = world.get_region(R.PERILOUS_PASSAGE)

    Factory = world.get_region(R.FACTORY)
    Factory_Shop = world.get_region(R.FACTORY_SHOP)
    Foggy_Fumes = world.get_region(R.FOGGY_FUMES)
    Slammin_Steel = world.get_region(R.SLAMMIN_STEEL)
    Handy_Hazards = world.get_region(R.HANDY_HAZARDS)
    Gear_Getaway = world.get_region(R.GEAR_GETAWAY)
    Cog_Jog = world.get_region(R.COG_JOG)
    Switcheroo = world.get_region(R.SWITCHEROO)
    Music_Madness = world.get_region(R.MUSIC_MADNESS)
    Lift_Off_Launch = world.get_region(R.LIFT_OFF_LAUNCH)
    Feather_Fiend = world.get_region(R.FEATHER_FIEND)
    Treacherous_Track = world.get_region(R.TREACHEROUS_TRACK)

    Volcano = world.get_region(R.VOLCANO)
    Volcano_Shop = world.get_region(R.VOLCANO_SHOP)
    Furious_Fire = world.get_region(R.FURIOUS_FIRE)
    Hot_Rocket = world.get_region(R.HOT_ROCKET)
    Roasting_Rails = world.get_region(R.ROASTING_RAILS)
    Smokey_Peak = world.get_region(R.SMOKEY_PEAK)
    Bobbing_Basalt = world.get_region(R.BOBBING_BASALT)
    Moving_Melters = world.get_region(R.MOVING_MELTERS)
    Red_Red_Rising = world.get_region(R.RED_RED_RISING)
    Tiki_Tong_Terror = world.get_region(R.TIKI_TONG_TERROR)
    Five_Monkey_Trial = world.get_region(R.FIVE_MONKEY_TRIAL)

    # Jungle
    connect_regions_helper(world, RC.JUNGLE_TO_JUNGLE_HIJINXS, Jungle, Jungle_Hijinxs)
    connect_regions_helper(world, RC.JUNGLE_TO_KING_OF_CLING, Jungle, King_of_Cling)
    connect_regions_helper(world, RC.JUNGLE_TO_TREE_TOP_BOP, Jungle, Tree_Top_Bop)
    connect_regions_helper(world, RC.JUNGLE_TO_SUNSET_SHORE, Jungle, Sunset_Shore)
    connect_regions_helper(world, RC.JUNGLE_TO_CANOPY_CANNONS, Jungle, Canopy_Cannons)
    connect_regions_helper(world, RC.JUNGLE_TO_CRAZY_CART, Jungle, Crazy_Cart)
    connect_regions_helper(world, RC.JUNGLE_TO_MUGLYS_MOUND, Jungle, Muglys_Mound)
    connect_regions_helper(world, RC.JUNGLE_TO_PLATFORM_PANIC, Jungle, Platform_Panic)
    connect_regions_helper(world, RC.JUNGLE_TO_JUNGLE_SHOP, Jungle, Jungle_Shop)

    # Mugly's Mound
    connect_regions_helper(world, RC.MUGLYS_MOUND_TO_BEACH, Muglys_Mound, Beach)

    # Beach
    connect_regions_helper(world, RC.BEACH_TO_POPPIN_PLANKS, Beach, Poppin_Planks)
    connect_regions_helper(world, RC.BEACH_TO_SLOPPY_SANDS, Beach, Sloppy_Sands)
    connect_regions_helper(world, RC.BEACH_TO_PEACEFUL_PIER, Beach, Peaceful_Pier)
    connect_regions_helper(world, RC.BEACH_TO_CANNON_CLUSTER, Beach, Cannon_Cluster)
    connect_regions_helper(world, RC.BEACH_TO_STORMY_SHORE, Beach, Stormy_Shore)
    connect_regions_helper(world, RC.BEACH_TO_BLOWHOLE_BOUND, Beach, Blowhole_Bound)
    connect_regions_helper(world, RC.BEACH_TO_TIDAL_TERROR, Beach, Tidal_Terror)
    connect_regions_helper(world, RC.BEACH_TO_PINCHIN_PIRATES, Beach, Pinchin_Pirates)
    connect_regions_helper(world, RC.BEACH_TO_TUMBLIN_TEMPLE, Beach, Tumblin_Temple)
    connect_regions_helper(world, RC.BEACH_TO_BEACH_SHOP, Beach, Beach_Shop)

    # Pinchin' Pirates
    connect_regions_helper(world, RC.PINCHIN_PIRATES_TO_RUINS, Pinchin_Pirates, Ruins)

    # Ruins
    connect_regions_helper(world, RC.RUINS_TO_WONKY_WATERWAY, Ruins, Wonky_Waterways)
    connect_regions_helper(world, RC.RUINS_TO_BUTTON_BASH, Ruins, Button_Bash)
    connect_regions_helper(world, RC.RUINS_TO_MAST_BLAST, Ruins, Mast_Blast)
    connect_regions_helper(world, RC.RUINS_TO_DAMP_DUNGEON, Ruins, Damp_Dungeon)
    connect_regions_helper(world, RC.RUINS_TO_ITTY_BITTY_BITERS, Ruins, Itty_Bitty_Biters)
    connect_regions_helper(world, RC.RUINS_TO_TEMPLE_TOPPLE, Ruins, Temple_Topple)
    connect_regions_helper(world, RC.RUINS_TO_RUINED_ROOST, Ruins, Ruined_Roost)
    connect_regions_helper(world, RC.RUINS_TO_SHIFTY_SMASHERS, Ruins, Shifty_Smashers)
    connect_regions_helper(world, RC.RUINS_TO_RUINS_SHOP, Ruins, Ruins_Shop)

    # Ruined Roost
    connect_regions_helper(world, RC.RUINED_ROOST_TO_CAVE, Ruined_Roost, Cave)

    # Cave
    connect_regions_helper(world, RC.CAVE_TO_RICKETY_RAILS, Cave, Rickety_Rails)
    connect_regions_helper(world, RC.CAVE_TO_GRIP_N_TRIP, Cave, Grip_n_Trip)
    connect_regions_helper(world, RC.CAVE_TO_BOMBS_AWAY, Cave, Bombs_Away)
    connect_regions_helper(world, RC.CAVE_TO_MOLE_PATROL, Cave, Mole_Patrol)
    connect_regions_helper(world, RC.CAVE_TO_CROWDED_CAVERN, Cave, Crowded_Cavern)
    connect_regions_helper(world, RC.CAVE_TO_THE_MOLE_TRAIN, Cave, The_Mole_Train)
    connect_regions_helper(world, RC.CAVE_TO_JAGGED_JEWELS, Cave, Jagged_Jewels)
    connect_regions_helper(world, RC.CAVE_TO_CAVE_SHOP, Cave, Cave_Shop)

    # The Mole Train
    connect_regions_helper(world, RC.THE_MOLE_TRAIN_TO_FOREST, The_Mole_Train, Forest)

    # Forest
    connect_regions_helper(world, RC.FOREST_TO_VINE_VALLEY, Forest, Vine_Valley)
    connect_regions_helper(world, RC.FOREST_TO_CLINGY_SWINGY, Forest, Clingy_Swingy)
    connect_regions_helper(world, RC.FOREST_TO_FLUTTER_FLYAWAY, Forest, Flutter_Flyaway)
    connect_regions_helper(world, RC.FOREST_TO_TIPPIN_TOTEMS, Forest, Tippin_Totems)
    connect_regions_helper(world, RC.FOREST_TO_LONGSHOT_LAUNCH, Forest, Longshot_Launch)
    connect_regions_helper(world, RC.FOREST_TO_SPRINGY_SPORES, Forest, Springy_Spores)
    connect_regions_helper(world, RC.FOREST_TO_WIGGLEVINE_WONDERS, Forest, Wigglevine_Wonders)
    connect_regions_helper(world, RC.FOREST_TO_MUNCHER_MARATHON, Forest, Muncher_Marathon)
    connect_regions_helper(world, RC.FOREST_TO_MANGORUBY_RUN, Forest, Mangoruby_Run)
    connect_regions_helper(world, RC.FOREST_TO_BLAST_N_BOUNCE, Forest, Blast_n_Bounce)
    connect_regions_helper(world, RC.FOREST_TO_FOREST_SHOP, Forest, Forest_Shop)

    # Mangoruby Run
    connect_regions_helper(world, RC.MANGORUBY_RUN_TO_CLIFF, Mangoruby_Run, Cliff)

    # Cliff
    connect_regions_helper(world, RC.CLIFF_TO_STICKY_SITUATION, Cliff, Sticky_Situation)
    connect_regions_helper(world, RC.CLIFF_TO_PREHISTORIC_PATH, Cliff, Prehistoric_Path)
    connect_regions_helper(world, RC.CLIFF_TO_WEIGHTY_WAY, Cliff, Weighty_Way)
    connect_regions_helper(world, RC.CLIFF_TO_BOULDER_ROLLER, Cliff, Boulder_Roller)
    connect_regions_helper(world, RC.CLIFF_TO_PRECARIOUS_PLATEAU, Cliff, Precarious_Plateau)
    connect_regions_helper(world, RC.CLIFF_TO_CRUMBLE_CANYON, Cliff, Crumble_Canyon)
    connect_regions_helper(world, RC.CLIFF_TO_TIPPY_SHIPPY, Cliff, Tippy_Shippy)
    connect_regions_helper(world, RC.CLIFF_TO_CLIFFTOP_CLIMB, Cliff, Clifftop_Climb)
    connect_regions_helper(world, RC.CLIFF_TO_THUGLYS_HIGHRISE, Cliff, Thuglys_Highrise)
    connect_regions_helper(world, RC.CLIFF_TO_PERILOUS_PASSAGE, Cliff, Perilous_Passage)
    connect_regions_helper(world, RC.CLIFF_TO_CLIFF_SHOP, Cliff, Cliff_Shop)

    # Thugly's Highrise
    connect_regions_helper(world, RC.THUGLYS_HIGHRISE_TO_FACTORY, Thuglys_Highrise, Factory)

    # Factory
    connect_regions_helper(world, RC.FACTORY_TO_FOGGY_FUMES, Factory, Foggy_Fumes)
    connect_regions_helper(world, RC.FACTORY_TO_SLAMMIN_STEEL, Factory, Slammin_Steel)
    connect_regions_helper(world, RC.FACTORY_TO_HANDY_HAZARDS, Factory, Handy_Hazards)
    connect_regions_helper(world, RC.FACTORY_TO_GEAR_GETAWAY, Factory, Gear_Getaway)
    connect_regions_helper(world, RC.FACTORY_TO_COG_JOG, Factory, Cog_Jog)
    connect_regions_helper(world, RC.FACTORY_TO_SWITCHEROO, Factory, Switcheroo)
    connect_regions_helper(world, RC.FACTORY_TO_MUSIC_MADNESS, Factory, Music_Madness)
    connect_regions_helper(world, RC.FACTORY_TO_LIFT_OFF_LAUNCH, Factory, Lift_Off_Launch)
    connect_regions_helper(world, RC.FACTORY_TO_TREACHEROUS_TRACK, Factory, Treacherous_Track)
    connect_regions_helper(world, RC.FACTORY_TO_FACTORY_SHOP, Factory, Factory_Shop)

    # Lift-Off Launch
    connect_regions_helper(world, RC.LIFT_OFF_LAUNCH_TO_FEATHER_FIEND, Lift_Off_Launch, Feather_Fiend)

    # Feather Fiend
    connect_regions_helper(world, RC.FEATHER_FIEND_TO_VOLCANO, Feather_Fiend, Volcano)

    # Volcano
    connect_regions_helper(world, RC.VOLCANO_TO_FURIOUS_FIRE, Volcano, Furious_Fire)
    connect_regions_helper(world, RC.VOLCANO_TO_HOT_ROCKET, Volcano, Hot_Rocket)
    connect_regions_helper(world, RC.VOLCANO_TO_ROASTING_RAILS, Volcano, Roasting_Rails)
    connect_regions_helper(world, RC.VOLCANO_TO_SMOKEY_PEAK, Volcano, Smokey_Peak)
    connect_regions_helper(world, RC.VOLCANO_TO_BOBBING_BASALT, Volcano, Bobbing_Basalt)
    connect_regions_helper(world, RC.VOLCANO_TO_MOVING_MELTERS, Volcano, Moving_Melters)
    connect_regions_helper(world, RC.VOLCANO_TO_RED_RED_RISING, Volcano, Red_Red_Rising)
    connect_regions_helper(world, RC.VOLCANO_TO_TIKI_TONG_TERROR, Volcano, Tiki_Tong_Terror)
    connect_regions_helper(world, RC.VOLCANO_TO_FIVE_MONKEY_TRIAL, Volcano, Five_Monkey_Trial)
    connect_regions_helper(world, RC.VOLCANO_TO_VOLCANO_SHOP, Volcano, Volcano_Shop)

    if world.options.golden_temple:
        Golden_Temple = world.get_region(R.GOLDEN_TEMPLE)

        connect_regions_helper(world, RC.TIKI_TONG_TERROR_TO_GOLDEN_TEMPLE, Tiki_Tong_Terror, Golden_Temple)

def connect_regions_helper(world:DKCRWorld, name: str, parent: Region, target: Region) -> None:
    entrance = Entrance(world.player, name, parent=parent)
    parent.exits.append(entrance)
    entrance.connect(target)
