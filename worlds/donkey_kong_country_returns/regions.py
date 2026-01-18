from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Entrance, Region

if TYPE_CHECKING:
    from .world import DKCR

def create_and_connect_regions(world: DKCR) -> None:
    create_all_regions(world)
    connect_regions(world)

def create_all_regions(world: DKCR) -> None:
    Jungle = Region("Jungle", world.player, world.multiworld)
    SunsetShore = Region("Sunset Shore", world.player, world.multiworld)
    Beach = Region("Beach", world.player, world.multiworld)
    BlowholeBound = Region("Blowhole Bound", world.player, world.multiworld)
    Ruins = Region("Ruins", world.player, world.multiworld)
    DampDungeon = Region("Damp Dungeon", world.player, world.multiworld)
    Cave = Region("Cave", world.player, world.multiworld)
    MolePatrol = Region("Mole Patrol", world.player, world.multiworld)
    Forest = Region("Forest", world.player, world.multiworld)
    SpringySpores = Region("Springy Spores", world.player, world.multiworld)
    Cliff = Region("Cliff", world.player, world.multiworld)
    PrecariousPlateau = Region("Precarious Plateau", world.player, world.multiworld)
    Factory = Region("Factory", world.player, world.multiworld)
    HandyHazards = Region("Handy Hazards", world.player, world.multiworld)
    Volcano = Region("Volcano", world.player, world.multiworld)
    SmokeyPeak = Region("Smokey Peak", world.player, world.multiworld)

    regions = [
        Jungle,
        SunsetShore,
        Beach,
        BlowholeBound,
        Ruins,
        DampDungeon,
        Cave,
        MolePatrol,
        Forest,
        SpringySpores,
        Cliff,
        PrecariousPlateau,
        Factory,
        HandyHazards,
        Volcano,
        SmokeyPeak
    ]

    if world.options.golden_temple:
        GoldenTemple = Region("Golden Temple", world.player, world.multiworld)
        regions.append(GoldenTemple)

    world.multiworld.regions += regions

def connect_regions(world: DKCR) -> None:
    Jungle = world.get_region("Jungle")
    SunsetShore = world.get_region("Sunset Shore")
    Beach = world.get_region("Beach")
    BlowholeBound = world.get_region("Blowhole Bound")
    Ruins = world.get_region("Ruins")
    DampDungeon = world.get_region("Damp Dungeon")
    Cave = world.get_region("Cave")
    MolePatrol = world.get_region("Mole Patrol")
    Forest = world.get_region("Forest")
    SpringySpores = world.get_region("Springy Spores")
    Cliff = world.get_region("Cliff")
    PrecariousPlateau = world.get_region("Precarious Plateau")
    Factory = world.get_region("Factory")
    HandyHazards = world.get_region("Handy Hazards")
    Volcano = world.get_region("Volcano")
    SmokeyPeak = world.get_region("Smokey Peak")

    Jungle_to_Beach = Entrance(world.player, "Jungle to Beach", parent=Jungle)
    Jungle.exits.append(Jungle_to_Beach)
    Jungle_to_Beach.connect(Beach)

    Jungle_to_SunsetShore = Entrance(world.player, "Jungle to Sunset Shore", parent=Jungle)
    Jungle.exits.append(Jungle_to_SunsetShore)
    Jungle_to_SunsetShore.connect(SunsetShore)

    Beach_to_Ruins = Entrance(world.player, "Beach to Ruins", parent=Beach)
    Beach.exits.append(Beach_to_Ruins)
    Beach_to_Ruins.connect(Ruins)

    Beach_to_BlowholeBound = Entrance(world.player, "Beach to Blowhole Bound", parent=Beach)
    Beach.exits.append(Beach_to_BlowholeBound)
    Beach_to_BlowholeBound.connect(BlowholeBound)

    Ruins_to_Cave = Entrance(world.player, "Ruins to Cave", parent=Ruins)
    Ruins.exits.append(Ruins_to_Cave)
    Ruins_to_Cave.connect(Cave)

    Ruins_to_DampDungeon = Entrance(world.player, "Ruins to Damp Dungeon", parent=Ruins)
    Ruins.exits.append(Ruins_to_DampDungeon)
    Ruins_to_DampDungeon.connect(DampDungeon)

    Cave_to_Forest = Entrance(world.player, "Cave to Forest", parent=Cave)
    Cave.exits.append(Cave_to_Forest)
    Cave_to_Forest.connect(Forest)

    Cave_to_MolePatrol = Entrance(world.player, "Cave to Mole Patrol", parent=Cave)
    Cave.exits.append(Cave_to_MolePatrol)
    Cave_to_MolePatrol.connect(MolePatrol)

    Forest_to_Cliff = Entrance(world.player, "Forest to Cliff", parent=Forest)
    Cave.exits.append(Forest_to_Cliff)
    Forest_to_Cliff.connect(Cliff)

    Forest_to_SpringySpores = Entrance(world.player, "Forest to Springy Spores", parent=Forest)
    Forest.exits.append(Forest_to_SpringySpores)
    Forest_to_SpringySpores.connect(SpringySpores)

    Cliff_to_Factory = Entrance(world.player, "Cliff to Factory", parent=Cliff)
    Cliff.exits.append(Cliff_to_Factory)
    Cliff_to_Factory.connect(Factory)

    Cliff_to_PrecariousPlateau = Entrance(world.player, "Cliff to Precarious Plateau", parent=Cliff)
    Cliff.exits.append(Cliff_to_PrecariousPlateau)
    Cliff_to_PrecariousPlateau.connect(PrecariousPlateau)

    Factory_to_Volcano = Entrance(world.player, "Factory to Volcano", parent=Factory)
    Factory.exits.append(Factory_to_Volcano)
    Factory_to_Volcano.connect(Volcano)

    Factory_to_HandyHazards = Entrance(world.player, "Factory to Handy Hazards", parent=Factory)
    Factory.exits.append(Factory_to_HandyHazards)
    Factory_to_HandyHazards.connect(HandyHazards)

    Volcano_to_SmokeyPeak = Entrance(world.player, "Volcano to Smokey Peak", parent=Volcano)
    Volcano.exits.append(Volcano_to_SmokeyPeak)
    Volcano_to_SmokeyPeak.connect(SmokeyPeak)

    if world.options.golden_temple:
        GoldenTemple = world.get_region("Golden Temple")

        Volcano_to_GoldenTemple = Entrance(world.player, "Volcano to Golden Temple", parent=Volcano)
        Volcano.exits.append(Volcano_to_GoldenTemple)
        Volcano_to_GoldenTemple.connect(GoldenTemple)



