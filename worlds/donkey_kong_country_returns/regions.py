from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Entrance, Region

if TYPE_CHECKING:
    from .world import DKCRWorld

def create_and_connect_regions(world: DKCRWorld) -> None:
    create_all_regions(world)
    connect_regions(world)

def create_all_regions(world: DKCRWorld) -> None:
    Jungle = Region("Jungle", world.player, world.multiworld)
    Jungle_Shop = Region("Jungle Shop", world.player, world.multiworld)
    Jungle_Hijinxs = Region("Jungle Hijinxs", world.player, world.mutliworld)
    King_of_Cling = Region("King of Cling", world.player, world.multiworld)
    Tree_Top_Bop = Region("Tree Top Bot", world.player, world.multiworld)
    Sunset_Shore = Region("Sunset Shore", world.player, world.multiworld)
    Canopy_Cannons = Region("Canopy Cannons", world.player, world.multiworld)
    Crazy_Cart = Region("Crazy Cart", world.player, world.mutltiworld)
    Muglys_Mound = Region("Mugly's Mound", world.player, world.multiworld)
    Platform_Panic = Region("Platform Panic", world.player, world.multiworld)

    Beach = Region("Beach", world.player, world.multiworld)
    Beach_Shop = Region("Beach Shop", world.player, world.multiworld)
    Poppin_Planks = Region("Poppin' Planks", world.player, world.multiworld)
    Sloppy_Sands = Region("Sloppy Sands", world.player, world.multiworld)
    Peaceful_Pier = Region("Peaceful Pier",  world.player, world.multiworld)
    Cannon_Cluster = Region("Cannon Cluster", world.player, world.multiworld)
    Stormy_Shore = Region("Stormy Shore", world.player, world.multiworld)
    Blowhole_Bound = Region("Blowhole Bound", world.player, world.multiworld)
    Tidal_Terror = Region("Tidal Terror", world.player, world.multiworld)
    Pichin_Pirates = Region("Pinchin' Pirates", world.player, world.multiworld)
    Tumblin_Temple = Region("Tumblin' Temple", world.player, world.multiworld)

    Ruins = Region("Ruins", world.player, world.multiworld)
    Ruins_Shop = Region("Runs Shop", world.player, world.multiworld)
    Wonky_Waterway = Region("Wonky Waterway", world.player, world.multiworld)
    Button_Bash = Region("Button Bash", world.player, world.multiworld)
    Mast_Blast = Region("Mast Blast", world.player, world.multiworld)
    Damp_Dungeon = Region("Damp Dungeon", world.player, world.multiworld)
    Itty_Bitty_Biters = Region("Itty Bitty Biters", world.player, world.multiworld)
    Temple_Topple = Region("Temple Topple", world.player, world.multiworld)
    Ruined_Roost = Region("Ruined Roost", world.player, world.multiworld)
    Shifty_Smashers = Region("Shifty Smashers", world.player, world.multiworld)

    Cave = Region("Cave", world.player, world.multiworld)
    Cave_Shop = Region("Cave Shop", world.player, world.multiworld)
    Rickety_Rails = Region("Rickety Rails", world.player, world.multiworld)
    Grip_n_Trip = Region("Grip 'n' Trip", world.player, world.multiworld)
    Bombs_Away = Region("Bombs Away", world.player, world.multiworld)
    Mole_Patrol = Region("Mole Patrol", world.player, world.multiworld)
    Crowded_Cavers = Region("Crowded Cavern", world.player, world.multiworld)
    The_Mole_Train = Region("The Mole Train", world.player, world.multiworld)
    Jegged_Jewels = Region("Jagged Jewels", world.player, world.multiworld)

    Forest = Region("Forest", world.player, world.multiworld)
    Forest_Shop = Region("Forest Shop", world.player, world.multiworld)
    Vine_Valley = Region("Vine Valley", world.player, world.multiworld)
    Clingy_Swingy = Region("Clingy Swingy", world.player, world.multiworld)
    Flutter_Flyaway = Region("Flutter Flyaway", world.player, world.multiworld)
    Tippin_Totems = Region("Tippin' Totems", world.player, world.multiworld)
    Longshot_Launch = Region("Longshot Launch", world.player, world.multiworld)
    Springy_Spores = Region("Springy Spores", world.player, world.multiworld)
    Wigglevine_Wonders = Region("Wigglevine Wonders", world.player, world.multiworld)
    Muncher_Marathon = Region("Muncher Marathon", world.player, world.multiworld)
    Mangoruby_Run = Region("Mangoruby Run", world.player, world.multiworld)
    Blast_n_Bounce = Region("Blast 'n' Bounce", world.player, world.multiworld)

    Cliff = Region("Cliff", world.player, world.multiworld)
    Cliff_Shop = Region("Cliff Shop", world.player, world.multiworld)
    Sticky_Situation = Region("Sticky Situation", world.player, world.multiworld)
    Prehistoric_Path = Region("Prehistoric Path", world.player, world.multiworld)
    Weighty_Way = Region("Weighty Way", world.player, world.multiworld)
    Boulder_Roller = Region("Boulder Roller", world.player, world.multiworld)
    Precarious_Plateau = Region("Precarious Plateau", world.player, world.multiworld)
    Crumble_Canyon = Region("Crumble Canyon", world.player, world.multiworld)
    Trippy_Shippy = Region("Trippy Shippy", world.player, world.multiworld)
    Clifftop_Climb = Region("Clifftop Climb", world.player, world.multiworld)
    Thuglys_Highrise = Region("Thugly's Highrise", world.player, world.multiworld)
    Perilous_Passage = Region("Perilous Passage", world.player, world.multiworld)

    Factory = Region("Factory", world.player, world.multiworld)
    Factory_Shop = Region("Factory Shop", world.player, world.multiworld)
    Foggy_Fumes = Region("Foggy Fumes", world.player, world.multiworld)
    Slammin_Steel = Region("Slammin' Steel", world.player, world.multiworld)
    Handy_Hazards = Region("Handy Hazards", world.player, world.multiworld)
    Gear_Getaway = Region("Gear Getaway", world.player, world.multiworld)
    Cog_Jog = Region("Cog Jog", world.player, world.multiworld)
    Switcheroo = Region("Switcheroo", world.player, world.multiworld)
    Music_Madness = Region("Music Madness", world.player, world.multiworld)
    Lift_Off_Launch = Region("Lift-Off_Launch", world.player, world.multiworld)
    Feather_Fiend = Region("Feather Fiend", world.player, world.multiworld)
    Treacherous_Track = Region("Treacherous_Track", world.player, world.multiworld)

    Volcano = Region("Volcano", world.player, world.multiworld)
    Volcano_Shop = Region("Volcano Shop", world.player, world.multiworld)
    Furious_Fire = Region("Furious Fire", world.player, world.multiworld)
    Hot_Rocket = Region("Hot Rocket", world.player, world.multiworld)
    Roasting_Rails = Region("Roasting Rails", world.player, world.multiworld)
    Smokey_Peak = Region("Smokey Peak", world.player, world.multiworld)
    Bobbing_Basalt = Region("Bobbing Basalt", world.player, world.multiworld)
    Moving_Melters = Region("Moving Melters", world.player, world.multiworld)
    Red_Red_Rising = Region("Red Red Rising", world.player, world.multiworld)
    Tikit_Tong_Terror = Region("Tikit Tong Terror", world.player, world.multiworld)
    Five_Monkey_Trial = Region("Five Monkey Trial", world.player, world.mutltiworld)

    regions = [
        Jungle,
        King_of_Cling,
        Tree_Top_Bop,
        Sunset_Shore,
        Canopy_Cannons,
        Crazy_Cart,
        Muglys_Mound,
        Platform_Panic,
        Beach,
        Poppin_Planks,
        Blowhole_Bound,
        Ruins,
        Damp_Dungeon,
        Cave,
        Mole_Patrol,
        Forest,
        Springy_Spores,
        Cliff,
        Precarious_Plateau,
        Factory,
        Handy_Hazards,
        Volcano,
        Smokey_Peak
    ]

    if world.options.golden_temple:
        Golden_Temple = Region("Golden Temple", world.player, world.multiworld)
        regions.append(Golden_Temple)

    world.multiworld.regions += regions

def connect_regions(world: DKCRWorld) -> None:
    Jungle = world.get_region("Jungle")
    Sunset_Shore = world.get_region("Sunset Shore")
    Beach = world.get_region("Beach")
    Blowhole_Bound = world.get_region("Blowhole Bound")
    Ruins = world.get_region("Ruins")
    Damp_Dungeon = world.get_region("Damp Dungeon")
    Cave = world.get_region("Cave")
    Mole_Patrol = world.get_region("Mole Patrol")
    Forest = world.get_region("Forest")
    Springy_Spores = world.get_region("Springy Spores")
    Cliff = world.get_region("Cliff")
    Precarious_Plateau = world.get_region("Precarious Plateau")
    Factory = world.get_region("Factory")
    Handy_Hazards = world.get_region("Handy Hazards")
    Volcano = world.get_region("Volcano")
    Smokey_Peak = world.get_region("Smokey Peak")

    Jungle_to_Beach = Entrance(world.player, "Jungle to Beach", parent=Jungle)
    Jungle.exits.append(Jungle_to_Beach)
    Jungle_to_Beach.connect(Beach)

    Jungle_to_SunsetShore = Entrance(world.player, "Jungle to Sunset Shore", parent=Jungle)
    Jungle.exits.append(Jungle_to_SunsetShore)
    Jungle_to_SunsetShore.connect(Sunset_Shore)

    Beach_to_Ruins = Entrance(world.player, "Beach to Ruins", parent=Beach)
    Beach.exits.append(Beach_to_Ruins)
    Beach_to_Ruins.connect(Ruins)

    Beach_to_BlowholeBound = Entrance(world.player, "Beach to Blowhole Bound", parent=Beach)
    Beach.exits.append(Beach_to_BlowholeBound)
    Beach_to_BlowholeBound.connect(Blowhole_Bound)

    Ruins_to_Cave = Entrance(world.player, "Ruins to Cave", parent=Ruins)
    Ruins.exits.append(Ruins_to_Cave)
    Ruins_to_Cave.connect(Cave)

    Ruins_to_DampDungeon = Entrance(world.player, "Ruins to Damp Dungeon", parent=Ruins)
    Ruins.exits.append(Ruins_to_DampDungeon)
    Ruins_to_DampDungeon.connect(Damp_Dungeon)

    Cave_to_Forest = Entrance(world.player, "Cave to Forest", parent=Cave)
    Cave.exits.append(Cave_to_Forest)
    Cave_to_Forest.connect(Forest)

    Cave_to_MolePatrol = Entrance(world.player, "Cave to Mole Patrol", parent=Cave)
    Cave.exits.append(Cave_to_MolePatrol)
    Cave_to_MolePatrol.connect(Mole_Patrol)

    Forest_to_Cliff = Entrance(world.player, "Forest to Cliff", parent=Forest)
    Cave.exits.append(Forest_to_Cliff)
    Forest_to_Cliff.connect(Cliff)

    Forest_to_SpringySpores = Entrance(world.player, "Forest to Springy Spores", parent=Forest)
    Forest.exits.append(Forest_to_SpringySpores)
    Forest_to_SpringySpores.connect(Springy_Spores)

    Cliff_to_Factory = Entrance(world.player, "Cliff to Factory", parent=Cliff)
    Cliff.exits.append(Cliff_to_Factory)
    Cliff_to_Factory.connect(Factory)

    Cliff_to_PrecariousPlateau = Entrance(world.player, "Cliff to Precarious Plateau", parent=Cliff)
    Cliff.exits.append(Cliff_to_PrecariousPlateau)
    Cliff_to_PrecariousPlateau.connect(Precarious_Plateau)

    Factory_to_Volcano = Entrance(world.player, "Factory to Volcano", parent=Factory)
    Factory.exits.append(Factory_to_Volcano)
    Factory_to_Volcano.connect(Volcano)

    Factory_to_HandyHazards = Entrance(world.player, "Factory to Handy Hazards", parent=Factory)
    Factory.exits.append(Factory_to_HandyHazards)
    Factory_to_HandyHazards.connect(Handy_Hazards)

    Volcano_to_SmokeyPeak = Entrance(world.player, "Volcano to Smokey Peak", parent=Volcano)
    Volcano.exits.append(Volcano_to_SmokeyPeak)
    Volcano_to_SmokeyPeak.connect(Smokey_Peak)

    if world.options.golden_temple:
        Golden_Temple = world.get_region("Golden Temple")

        Volcano_to_GoldenTemple = Entrance(world.player, "Volcano to Golden Temple", parent=Volcano)
        Volcano.exits.append(Volcano_to_GoldenTemple)
        Volcano_to_GoldenTemple.connect(Golden_Temple)



