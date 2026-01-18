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
    Sunset_Shore = Region("Sunset Shore", world.player, world.multiworld)
    Beach = Region("Beach", world.player, world.multiworld)
    Blowhole_Bound = Region("Blowhole Bound", world.player, world.multiworld)
    Ruins = Region("Ruins", world.player, world.multiworld)
    Damp_Dungeon = Region("Damp Dungeon", world.player, world.multiworld)
    Cave = Region("Cave", world.player, world.multiworld)
    Mole_Patrol = Region("Mole Patrol", world.player, world.multiworld)
    Forest = Region("Forest", world.player, world.multiworld)
    Springy_Spores = Region("Springy Spores", world.player, world.multiworld)
    Cliff = Region("Cliff", world.player, world.multiworld)
    Precarious_Plateau = Region("Precarious Plateau", world.player, world.multiworld)
    Factory = Region("Factory", world.player, world.multiworld)
    Handy_Hazards = Region("Handy Hazards", world.player, world.multiworld)
    Volcano = Region("Volcano", world.player, world.multiworld)
    Smokey_Peak = Region("Smokey Peak", world.player, world.multiworld)

    regions = [
        Jungle,
        Sunset_Shore,
        Beach,
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



