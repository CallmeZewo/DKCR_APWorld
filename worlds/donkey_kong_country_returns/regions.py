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
    Jagged_Jewels = Region("Jagged Jewels", world.player, world.multiworld)

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
    Tippy_Shippy = Region("Trippy Shippy", world.player, world.multiworld)
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
    Tiki_Tong_Terror = Region("Tikit Tong Terror", world.player, world.multiworld)
    Five_Monkey_Trial = Region("Five Monkey Trial", world.player, world.mutltiworld)

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
        Pichin_Pirates,
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
        Crowded_Cavers,
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
        Golden_Temple = Region("Golden Temple", world.player, world.multiworld)
        regions.append(Golden_Temple)

    world.multiworld.regions += regions

def connect_regions(world: DKCRWorld) -> None:
    Jungle = world.get_region("Jungle")
    Jungle_Shop = world.get_region("Jungle Shop")
    Jungle_Hijinxs = world.get_region("Jungle Hijinxs")
    King_of_Cling = world.get_region("King of CLing")
    Tree_Top_Bop = world.get_region("Tree Top Bop")
    Sunset_Shore = world.get_region("Sunset Shore")
    Canopy_Cannons = world.get_region("Canopy Cannons")
    Crazy_Cart = world.get_region("Crazy Cart")
    Muglys_Mound = world.get_region("Mugly's Mound")
    Platform_Panic = world.get_region("Platform Panic")

    Beach = world.get_region("Beach")
    Beach_Shop = world.get_region("Beach Shop")
    Poppin_Planks = world.get_region("Poppin' Planks")
    Sloppy_Sands = world.get_region("Sloppy Sands")
    Peaceful_Pier = world.get_region("Peaceful Pier")
    Cannon_Cluster = world.get_region("Cannon Cluster")
    Stormy_Shore = world.get_region("Stormy Shore")
    Blowhole_Bound = world.get_region("Blowhole Bound")
    Tidal_Terror = world.get_region("Tidal Terror")
    Pinchin_Pirates = world.get_region("Pinchin' Pirates")
    Tumblin_Temple = world.get_region("Tumlin' Temple")

    Ruins = world.get_region("Ruins")
    Ruins_Shop = world.get_region("Ruins Shop")
    Wonky_Waterways = world.get_region("Wonky Waterways")
    Button_Bash = world.get_region("Button Bash")
    Mast_Blast = world.get_region("Mast Blast")
    Damp_Dungeon = world.get_region("Damp Dungeon")
    Itty_Bitty_Biters = world.get_region("Itty Bitty Biters")
    Temple_Topple = world.get_region("Temple Topple")
    Ruined_Roost = world.get_region("Ruined Roost")
    Shifty_Smashers = world.get_region("Shifty Smashers")

    Cave = world.get_region("Cave")
    Cave_Shop = world.get_region("Cave Shop")
    Rickety_Rails = world.get_region("Rickety Rails")
    Grip_n_Trip = world.get_region("Grip 'n' Trip")
    Bombs_Away = world.get_region("Bombs Away")
    Mole_Patrol = world.get_region("Mole Patrol")
    Crowded_Cavern = world.get_region("Crowded Cavern")
    The_Mole_Train = world.get_region("The Mole Train")
    Jagged_Jewels = world.get_region("Jagged Jewels")

    Forest = world.get_region("Forest")
    Forest_Shop = world.get_region("Forest Shop")
    Vine_Valley = world.get_region("Vine Valley")
    Clingy_Swingy = world.get_region("Clingy Swingy")
    Flutter_Flyaway = world.get_region("Flutter Flyaway")
    Tippin_Totems = world.get_region("Tippin' Totems")
    Longshot_Launch = world.get_region("Longshot Launch")
    Springy_Spores = world.get_region("Springy Spores")
    Wigglevine_Wonders = world.get_region("Wigglevine Wonders")
    Muncher_Marathon = world.get_region("Muncher Marathon")
    Mangoruby_Run = world.get_region("Mangoruby Run")
    Blast_n_Bounce = world.get_region("Blast 'n' Bounce")

    Cliff = world.get_region("Cliff")
    Cliff_shop = world.get_region("Cliff Shop")
    Sticky_Situation = world.get_region("Sticky Situation")
    Prehistoric_Path = world.get_region("Prehistoric Path")
    Weighty_Way = world.get_region("Weighty Way")
    Boulder_Roller = world.get_region("Boulder Rollder")
    Precarious_Plateau = world.get_region("Precarious Plateau")
    Crumble_Canyon = world.get_region("Crumble Canyon")
    Tippy_Shippy = world.get_region("Tippy Shippy")
    Clifftop_Climb = world.get_region("Clifftop Climb")
    Thuglys_Highrise = world.get_region("Thugly's Highrise")
    Perilous_Passage = world.get_region("Perilous Passage")

    Factory = world.get_region("Factory")
    Factory_Shop = world.get_region("Factory Shop")
    Foggy_Fumes = world.get_region("Foggy Fumes")
    Slammin_Steel = world.get_region("Slammin' Steel")
    Handy_Hazards = world.get_region("Handy Hazards")
    Gear_Getaway = world.get_region("Gear Getaway")
    Cog_Jog = world.get_region("Cog Jog")
    Switcheroo = world.get_region("Switcheroo")
    Music_Madness = world.get_region("Music Madness")
    Lift_Off_Launch = world.get_region("Lift-Off_Launch")
    Feather_Fiend = world.get_region("Feather Fiend")
    Treacherous_Track = world.get_region("Treacherous Track")

    Volcano = world.get_region("Volcano")
    Volcano_Shop = world.get_region("Volcano Shop")
    Furious_Fire = world.get_region("Furious Fire")
    Hot_Rocket = world.get_region("Hot Rocket")
    Roasting_Rails = world.get_region("Roasting Rails")
    Smokey_Peak = world.get_region("Smokey Peak")
    Bobbing_Basalt = world.get_region("Bobbing Basalt")
    Moving_Melters = world.get_region("Moving Melters")
    Red_Red_Rising = world.get_region("Red Red Rising")
    Tiki_Tong_Terror = world.get_region("Wiki Tong Terror")
    Five_Monkey_Trial = world.get_region("Five Monkey Trial")

    Jungle_to_Jungle_Hijinxs = Entrance(world.player, "Jungle to Jungle Hijinxs", parent=Jungle)
    Jungle.exits.append(Jungle_to_Jungle_Hijinxs)
    Jungle_to_Jungle_Hijinxs.connect(Jungle_Hijinxs)

    Jungle_to_King_of_Cling = Entrance(world.player, "Jungle to King of Cling", parent=Jungle)
    Jungle.exits.append(Jungle_to_King_of_Cling)
    Jungle_to_King_of_Cling.connect(King_of_Cling)

    Jungle_to_Tree_Top_Bop = Entrance(world.player, "Jungle to Tree Top Bop", parent=Jungle)
    Jungle.exits.append(Jungle_to_Tree_Top_Bop)
    Jungle_to_Tree_Top_Bop.connect(Tree_Top_Bop)

    Jungle_to_SunsetShore = Entrance(world.player, "Jungle to Sunset Shore", parent=Jungle)
    Jungle.exits.append(Jungle_to_SunsetShore)
    Jungle_to_SunsetShore.connect(Sunset_Shore)

    Jungle_to_Canopy_Cannons = Entrance(world.player, "Jungle to Canopy Cannons", parent=Jungle)
    Jungle.exits.append(Jungle_to_Canopy_Cannons)
    Jungle_to_Canopy_Cannons.connect(Canopy_Cannons)

    Jungle_to_Crazy_Cart = Entrance(world.player, "Jungle to Crazy Cart", parent=Jungle)
    Jungle.exits.append(Jungle_to_Crazy_Cart)
    Jungle_to_Crazy_Cart.connect(Crazy_Cart)

    Jungle_to_Muglys_Mound = Entrance(world.player, "Jungle to Mugly's Mound", parent=Jungle)
    Jungle.exits.append(Jungle_to_Muglys_Mound)
    Jungle_to_Muglys_Mound.connect(Muglys_Mound)

    Jungle_to_Platform_Panic = Entrance(world.player, "Jungle to Platform Panic", parent=Jungle)
    Jungle.exits.append(Jungle_to_Platform_Panic)
    Jungle_to_Platform_Panic.connect(Platform_Panic)

    Jungle_to_Jungle_Shop = Entrance(world.player, "Jungle to Jungle Shop", parent=Jungle)
    Jungle.exits.append(Jungle_to_Jungle_Shop)
    Jungle_to_Jungle_Shop.connect(Jungle_Shop)

    Muglys_Mound_to_Beach = Entrance(world.player, "Mugly's Mound to Beach", parent=Muglys_Mound)
    Muglys_Mound.exits.append(Muglys_Mound_to_Beach)
    Muglys_Mound_to_Beach.connect(Beach)

    Beach_to_Poppin_Planks = Entrance(world.player, "Beach to Poppin' Planks", parent=Beach)
    Beach.exits.append(Beach_to_Poppin_Planks)
    Beach_to_Poppin_Planks.connect(Poppin_Planks)

    Beach_to_Sloppy_Sands = Entrance(world.player, "Beach to Sloppy Sands", parent=Beach)
    Beach.exits.append(Beach_to_Sloppy_Sands)
    Beach_to_Sloppy_Sands.connect(Sloppy_Sands)

    Beach_to_Peaceful_Pier = Entrance(world.player, "Beach to Peaceful Pier", parent=Beach)
    Beach.exits.append(Beach_to_Peaceful_Pier)
    Beach_to_Peaceful_Pier.connect(Peaceful_Pier)

    Beach_to_Cannon_Cluster = Entrance(world.player, "Beach to Cannon Cluster", parent=Beach)
    Beach.exits.append(Beach_to_Cannon_Cluster)
    Beach_to_Cannon_Cluster.connect(Cannon_Cluster)

    Beach_to_Stormy_Shore = Entrance(world.player, "Beach to Stormy Shore", parent=Beach)
    Beach.exits.append(Beach_to_Stormy_Shore)
    Beach_to_Stormy_Shore.connect(Stormy_Shore)

    Beach_to_BlowholeBound = Entrance(world.player, "Beach to Blowhole Bound", parent=Beach)
    Beach.exits.append(Beach_to_BlowholeBound)
    Beach_to_BlowholeBound.connect(Blowhole_Bound)

    Beach_to_Tidal_Terror = Entrance(world.player, "Beach to Tidal Terror", parent=Beach)
    Beach.exits.append(Beach_to_Tidal_Terror)
    Beach_to_Tidal_Terror.connect(Tidal_Terror)

    Beach_to_Pinchin_Pirates = Entrance(world.player, "Beach to Pinchin' Pirates", parent=Beach)
    Beach.exits.append(Beach_to_Pinchin_Pirates)
    Beach_to_Pinchin_Pirates.connect(Pinchin_Pirates)

    Beach_to_Tumblin_Temple = Entrance(world.player, "Beach to Tumblin' Temple", parent=Beach)
    Beach.exits.append(Beach_to_Tumblin_Temple)
    Beach_to_Tumblin_Temple.connect(Tumblin_Temple)

    Beach_to_Beach_Shop = Entrance(world.player, "Beach to Beach Shop", parent=Beach)
    Beach.exits.append(Beach_to_Beach_Shop)
    Beach_to_Beach_Shop.connect(Beach_Shop)

    Pinchin_Pirates_to_Ruins = Entrance(world.player, "Pinchin' Pirates to Ruins", parent=Pinchin_Pirates)
    Pinchin_Pirates.exits.append(Pinchin_Pirates_to_Ruins)
    Pinchin_Pirates_to_Ruins.connect(Ruins)

    Ruins_to_Wonky_Waterway = Entrance(world.player, "Ruins to Wonky Waterway", parent=Ruins)
    Ruins.exits.append(Ruins_to_Wonky_Waterway)
    Ruins_to_Wonky_Waterway.connect(Wonky_Waterways)

    Ruins_to_Button_Bash = Entrance(world.player, "Ruins to Button Bash", parent=Ruins)
    Ruins.exits.append(Ruins_to_Button_Bash)
    Ruins_to_Button_Bash.connect(Button_Bash)

    Ruins_to_Mast_Blast = Entrance(world.player, "Ruins to Mast Blast", parent=Ruins)
    Ruins.exits.append(Ruins_to_Mast_Blast)
    Ruins_to_Mast_Blast.connect(Mast_Blast)

    Ruins_to_DampDungeon = Entrance(world.player, "Ruins to Damp Dungeon", parent=Ruins)
    Ruins.exits.append(Ruins_to_DampDungeon)
    Ruins_to_DampDungeon.connect(Damp_Dungeon)

    Ruins_to_Itty_Bitty_Biters = Entrance(world.player, "Ruins to Itty Bitty Biters", parent=Ruins)
    Ruins.exits.append(Ruins_to_Itty_Bitty_Biters)
    Ruins_to_Itty_Bitty_Biters.connect(Itty_Bitty_Biters)

    Ruins_to_Temple_Topple = Entrance(world.player,"Ruins to Temple Topple", parent=Ruins)
    Ruins.exits.append(Ruins_to_Temple_Topple)
    Ruins_to_Temple_Topple.connect(Temple_Topple)

    Ruins_to_Ruined_Roost = Entrance(world.player, "Ruins to Ruined Roost", parent=Ruins)
    Ruins.exits.append(Ruins_to_Ruined_Roost)
    Ruins_to_Ruined_Roost.connect(Ruined_Roost)

    Ruins_to_Shifty_Smashers = Entrance(world.player, "Ruins to Shifty Smashers", parent=Ruins)
    Ruins.exits.append(Ruins_to_Shifty_Smashers)
    Ruins_to_Shifty_Smashers.connect(Shifty_Smashers)

    Ruins_to_Ruins_Shop = Entrance(world.player, "Ruins to Ruins Shop", parent=Ruins)
    Ruins.exits.append(Ruins_to_Ruins_Shop)
    Ruins_to_Ruins_Shop.connect(Ruins_Shop)

    Ruined_Roost_to_Cave = Entrance(world.player, "Ruined Roost to Cave", parent=Ruined_Roost)
    Ruined_Roost.exits.append(Ruined_Roost_to_Cave)
    Ruined_Roost_to_Cave.connect(Cave)

    Cave_to_Rickety_Rails = Entrance(world.player, "Cave to Rickety Rails", parent=Cave)
    Cave.exits.append(Cave_to_Rickety_Rails)
    Cave_to_Rickety_Rails.connect(Rickety_Rails)

    Cave_to_Grip_n_Trip = Entrance(world.player, "Cave to Grip 'n' Trip", parent=Cave)
    Cave.exits.append(Cave_to_Grip_n_Trip)
    Cave_to_Grip_n_Trip.connect(Grip_n_Trip)

    Cave_to_Boms_Away = Entrance(world.player, "Cave to Bombs Away", parent=Cave)
    Cave.exits.append(Cave_to_Boms_Away)
    Cave_to_Boms_Away.connect(Bombs_Away)

    Cave_to_MolePatrol = Entrance(world.player, "Cave to Mole Patrol", parent=Cave)
    Cave.exits.append(Cave_to_MolePatrol)
    Cave_to_MolePatrol.connect(Mole_Patrol)

    Cave_to_Crowded_Cavern = Entrance(world.player, "Cave to Crowded Cavern", parent=Cave)
    Cave.exits.append(Cave_to_Crowded_Cavern)
    Cave_to_Crowded_Cavern.connect(Crowded_Cavern)

    Cave_to_The_Mole_Train = Entrance(world.player, "Cave to The Mole Train", parent=Cave)
    Cave.exits.append(Cave_to_The_Mole_Train)
    Cave_to_The_Mole_Train.connect(The_Mole_Train)

    Cave_to_Jagged_Jewels = Entrance(world.player, "Cave to Jagged Jewels", parent=Cave)
    Cave.exits.append(Cave_to_Jagged_Jewels)
    Cave_to_Jagged_Jewels.connect(Jagged_Jewels)

    Cave_to_Cave_Shop = Entrance(world.player, "Cave to Cave Shop", parent=Cave)
    Cave.exits.append(Cave_to_Cave_Shop)
    Cave_to_Cave_Shop.connect(Cave_Shop)

    The_Mole_Train_to_Forest = Entrance(world.player, "The Mole Train to Forest", parent=The_Mole_Train)
    The_Mole_Train.exits.append(The_Mole_Train_to_Forest)
    The_Mole_Train_to_Forest.connect(Forest)

    Forest_to_Vine_Valley = Entrance(world.player, "Forest to Vine Valley", parent=Forest)
    Forest.exits.append(Forest_to_Vine_Valley)
    Forest_to_Vine_Valley.connect(Vine_Valley)

    Forest_to_Clingy_Swingy = Entrance(world.player, "Forest to Clingy Swingy", parent=Forest)
    Forest.exits.append(Forest_to_Clingy_Swingy)
    Forest_to_Clingy_Swingy.connect(Clingy_Swingy)

    Forest_to_Flutter_Flyaway = Entrance(world.player, "Forest to Flutter Flyaway", parent=Forest)
    Forest.exits.append(Forest_to_Flutter_Flyaway)
    Forest_to_Flutter_Flyaway.connect(Flutter_Flyaway)

    Forest_to_Tippin_Totems = Entrance(world.player, "Forest to Tippin' Totems", parent=Forest)
    Forest.exits.append(Forest_to_Tippin_Totems)
    Forest_to_Tippin_Totems.connect(Tippin_Totems)

    Forest_to_Longshot_Launch = Entrance(world.player, "Forest to Longshot Launch", parent=Forest)
    Forest.exits.append(Forest_to_Longshot_Launch)
    Forest_to_Longshot_Launch.connect(Longshot_Launch)

    Forest_to_SpringySpores = Entrance(world.player, "Forest to Springy Spores", parent=Forest)
    Forest.exits.append(Forest_to_SpringySpores)
    Forest_to_SpringySpores.connect(Springy_Spores)

    Forest_to_Wigglevine_Wonders = Entrance(world.player, "Forest to Wigglevine Wonders", parent=Forest)
    Forest.exits.append(Forest_to_Wigglevine_Wonders)
    Forest_to_Wigglevine_Wonders.connect(Wigglevine_Wonders)

    Forest_to_Muncher_Marathon = Entrance(world.player, "Forest to Muncher Marathon", parent=Forest)
    Forest.exits.append(Forest_to_Muncher_Marathon)
    Forest_to_Muncher_Marathon.connect(Muncher_Marathon)

    Forest_to_Mangoruby_Run = Entrance(world.player, "Forest to Mangoruby Run", parent=Forest)
    Forest.exits.append(Forest_to_Mangoruby_Run)
    Forest_to_Mangoruby_Run.connect(Mangoruby_Run)

    Forest_to_Blast_n_Bounce = Entrance(world.player, "Forest to Blast 'n' Bounce",parent=Forest)
    Forest.exits.append(Forest_to_Blast_n_Bounce)
    Forest_to_Blast_n_Bounce.connect(Blast_n_Bounce)

    Forest_to_Forest_Shop = Entrance(world.player, "Forest to Forest Shop", parent=Forest)
    Forest.exits.append(Forest_to_Forest_Shop)
    Forest_to_Forest_Shop.connect(Forest_Shop)

    Mangoruby_Run_to_Cliff = Entrance(world.player, "Mangoruby Run to Cliff", parent=Mangoruby_Run)
    Mangoruby_Run.exits.append(Mangoruby_Run_to_Cliff)
    Mangoruby_Run_to_Cliff.connect(Cliff)

    Cliff_to_Sticky_Situation = Entrance(world.player, "Cliff to Sticky Situation", parent=Cliff)
    Cliff.exits.append(Cliff_to_Sticky_Situation)
    Cliff_to_Sticky_Situation.connect(Sticky_Situation)

    Cliff_to_Prehistoric_Path = Entrance(world.player,"Cliff to Prehistoric Path", parent=Cliff)
    Cliff.exits.append(Cliff_to_Prehistoric_Path)
    Cliff_to_Prehistoric_Path.connect(Prehistoric_Path)

    Cliff_to_Weighty_Way = Entrance(world.player, "Cliff to Weighty Way", parent=Cliff)
    Cliff.exits.append(Cliff_to_Weighty_Way)
    Cliff_to_Weighty_Way.connect(Weighty_Way)

    Cliff_to_Boulder_Roller = Entrance(world.player, "Cliff to Boulder Roller", parent=Cliff)
    Cliff.exits.append(Cliff_to_Boulder_Roller)
    Cliff_to_Boulder_Roller.connect(Boulder_Roller)

    Cliff_to_Precarious_Plateau = Entrance(world.player, "Cliff to Precarious Plateau", parent=Cliff)
    Cliff.exits.append(Cliff_to_Precarious_Plateau)
    Cliff_to_Precarious_Plateau.connect(Precarious_Plateau)

    Cliff_to_Crumble_Canyon = Entrance(world.player, "Cliff to Crumble Canyon", parent=Cliff)
    Cliff.exits.append(Cliff_to_Crumble_Canyon)
    Cliff_to_Crumble_Canyon.connect(Crumble_Canyon)

    Cliff_to_Tippy_Shippy = Entrance(world.player, "Cliff to Tippy Shippy", parent=Cliff)
    Cliff.exits.append(Cliff_to_Tippy_Shippy)
    Cliff_to_Tippy_Shippy.connect(Tippy_Shippy)

    Cliff_to_Clifftop_Climb = Entrance(world.player, "Cliff to Clifftop Climb", parent=Cliff)
    Cliff.exits.append(Cliff_to_Clifftop_Climb)
    Cliff_to_Clifftop_Climb.connect(Clifftop_Climb)

    Cliff_to_Thuglys_Highrise = Entrance(world.player, "Cliff to Thugly's Highrise", parent=Cliff)
    Cliff.exits.append(Cliff_to_Thuglys_Highrise)
    Cliff_to_Thuglys_Highrise.connect(Thuglys_Highrise)

    Cliff_to_Perilous_Passage = Entrance(world.player, "Cliff to Perilous Passage", parent=Cliff)
    Cliff.exits.append(Cliff_to_Perilous_Passage)
    Cliff_to_Perilous_Passage.connect(Perilous_Passage)

    Cliff_to_Cliff_Shop = Entrance(world.player, "Cliff to Cliff Shop", parent=Cliff)
    Cliff.exits.append(Cliff_to_Cliff_Shop)
    Cliff_to_Cliff_Shop.connect(Cliff_shop)

    Thuglys_Highrise_to_Factory = Entrance(world.player, "Thugly's Highrise to Factory", parent=Thuglys_Highrise)
    Thuglys_Highrise.exits.append(Thuglys_Highrise_to_Factory)
    Thuglys_Highrise_to_Factory.connect(Factory)

    Factory_to_Foggy_Fumes = Entrance(world.player, "Factory to Foggy Fumes", parent=Factory)
    Factory.exits.append(Factory_to_Foggy_Fumes)
    Factory_to_Foggy_Fumes.connect(Foggy_Fumes)

    Factory_to_Slammin_Steel = Entrance(world.player, "Factory to Slammin' Steel", parent=Factory)
    Factory.exits.append(Factory_to_Slammin_Steel)
    Factory_to_Slammin_Steel.connect(Slammin_Steel)

    Factory_to_Handy_Hazards = Entrance(world.player, "Factory to Handy Hazards", parent=Factory)
    Factory.exits.append(Factory_to_Handy_Hazards)
    Factory_to_Handy_Hazards.connect(Handy_Hazards)

    Factory_to_Gear_Getaway = Entrance(world.player, "Factory to Gear Getaway", parent=Factory)
    Factory.exits.append(Factory_to_Gear_Getaway)
    Factory_to_Gear_Getaway.connect(Gear_Getaway)

    Factory_to_Cog_Jog = Entrance(world.player, "Factory to Cog Jog", parent=Factory)
    Factory.exits.append(Factory_to_Cog_Jog)
    Factory_to_Cog_Jog.connect(Cog_Jog)

    Factory_to_Switcheroo = Entrance(world.player, "Factory to Switcheroo", parent=Factory)
    Factory.exits.append(Factory_to_Switcheroo)
    Factory_to_Switcheroo.connect(Switcheroo)

    Factory_to_Music_Madness = Entrance(world.player, "Factory to Music Madness", parent=Factory)
    Factory.exits.append(Factory_to_Music_Madness)
    Factory_to_Music_Madness.connect(Music_Madness)

    Factory_to_Lift_Off_Launch = Entrance(world.player, "Factory to Lift-Off Launch", parent=Factory)
    Factory.exits.append(Factory_to_Lift_Off_Launch)
    Factory_to_Lift_Off_Launch.connect(Lift_Off_Launch)

    Lift_Off_Launch_to_Feather_Fiend = Entrance(world.player, "Lift-Off Launch_to_Feather_Fiend", parent=Lift_Off_Launch)
    Lift_Off_Launch.exits.append(Lift_Off_Launch_to_Feather_Fiend)
    Lift_Off_Launch_to_Feather_Fiend.connect(Feather_Fiend)

    Factory_to_Treacherous_Track = Entrance(world.player, "Factory to Treacherous Track", parent=Factory)
    Factory.exits.append(Factory_to_Treacherous_Track)
    Factory_to_Treacherous_Track.connect(Treacherous_Track)

    Feather_Fiend_to_Volcano = Entrance(world.player, "Feather Fiend to Volcano", parent=Feather_Fiend)
    Feather_Fiend.exits.append(Feather_Fiend_to_Volcano)
    Feather_Fiend_to_Volcano.connect(Volcano)

    Volcano_to_Furious_Fire = Entrance(world.player, "Volcano to Furious Fire", parent=Volcano)
    Volcano.exits.append(Volcano_to_Furious_Fire)
    Volcano_to_Furious_Fire.connect(Furious_Fire)

    Volcano_to_Hot_Rocket = Entrance(world.player, "Volcano to Hot Rocket", parent=Volcano)
    Volcano.exits.append(Volcano_to_Hot_Rocket)
    Volcano_to_Hot_Rocket.connect(Hot_Rocket)

    Volcano_to_Roasting_Rails = Entrance(world.player, "Volcano to Roasting Rails", parent=Volcano)
    Volcano.exits.append(Volcano_to_Roasting_Rails)
    Volcano_to_Roasting_Rails.connect(Roasting_Rails)

    Volcano_to_Smokey_Peak = Entrance(world.player, "Volcano to Smokey Peak", parent=Volcano)
    Volcano.exits.append(Volcano_to_Smokey_Peak)
    Volcano_to_Smokey_Peak.connect(Smokey_Peak)

    Volcano_to_Bobbing_Basalt = Entrance(world.player, "Volcano to Bobbing Basalt", parent=Volcano)
    Volcano.exits.append(Volcano_to_Bobbing_Basalt)
    Volcano_to_Bobbing_Basalt.connect(Bobbing_Basalt)

    Volcano_to_Moving_Melters = Entrance(world.player, "Volcano to Moving Melters", parent=Volcano)
    Volcano.exits.append(Volcano_to_Moving_Melters)
    Volcano_to_Moving_Melters.connect(Moving_Melters)

    Volcano_to_Red_Red_Rising = Entrance(world.player, "Volcano to Red Red Rising", parent=Volcano)
    Volcano.exits.append(Volcano_to_Red_Red_Rising)
    Volcano_to_Red_Red_Rising.connect(Red_Red_Rising)

    Volcano_to_Tiki_Tong_Terror = Entrance(world.player, "Volcano to Tiki Tong Terror", parent=Volcano)
    Volcano.exits.append(Volcano_to_Tiki_Tong_Terror)
    Volcano_to_Tiki_Tong_Terror.connect(Tiki_Tong_Terror)

    Volcano_to_Five_Monkey_Trial = Entrance(world.player, "Volcano to Five Monkey Trial", parent=Volcano)
    Volcano.exits.append(Volcano_to_Five_Monkey_Trial)
    Volcano_to_Five_Monkey_Trial.connect(Five_Monkey_Trial)

    if world.options.golden_temple:
        Golden_Temple = world.get_region("Golden Temple")

        Tiki_Tong_Terror_to_Golden_Temple = Entrance(world.player, "Tiki Tong Terror to Golden Temple", parent=Tiki_Tong_Terror)
        Tiki_Tong_Terror.exits.append(Tiki_Tong_Terror_to_Golden_Temple)
        Tiki_Tong_Terror_to_Golden_Temple.connect(Golden_Temple)

        Volcano_to_Golden_Temple = Entrance(world.player, "Volcano to Golden Temple", parent=Volcano)
        Volcano.exits.append(Volcano_to_Golden_Temple)
        Volcano_to_Golden_Temple.connect(Golden_Temple)



