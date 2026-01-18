from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import CollectionState
from worlds.generic.Rules import add_rule, set_rule

if TYPE_CHECKING:
    from .world import DKCRWorld

def set_all_rules(world: DKCRWorld) -> None:
    set_all_entrance_rules(world)
    set_all_location_rules(world)
    set_completion_condition(world)

def set_all_entrance_rules(world: DKCRWorld) -> None:
    Jungle_to_Beach = world.get_entrance("Jungle to Beach")
    Jungle_to_SunsetShore = world.get_entrance("Jungle to Sunset Shore")
    Beach_to_Ruins = world.get_entrance("Beach to Ruins")
    Beach_to_BlowholeBound = world.get_entrance("Beach to Blowhole Bound")
    Ruins_to_Cave = world.get_entrance("Ruins to Cave")
    Ruins_to_DampDungeon = world.get_entrance("Ruins to Damp Dungeon")
    Cave_to_Forest = world.get_entrance("Cave to Forest")
    Cave_to_MolePatrol = world.get_entrance("Cave to Mole Patrol")
    Forest_to_Cliff = world.get_entrance("Forest to Cliff")
    Forest_to_SpringySpores = world.get_entrance("Forest to Springy Spores")
    Cliff_to_Factory = world.get_entrance("Cliff to Factory")
    Cliff_to_PrecariousPlateau = world.get_entrance("Cliff to Precarious Plateau")
    Factory_to_Volcano = world.get_entrance("Factory to Volcano")
    Factory_to_HandyHazards = world.get_entrance("Factory to Handy Hazards")

    if world.options.golden_temple:
        Volcano_to_GoldenTemple = world.get_entrance("Volcano to Golden Temple")
        set_rule(Volcano_to_GoldenTemple, lambda state: state.has("Defeated Boss 8", world.player))

    set_rule(Jungle_to_Beach, lambda state: state.has("Defeated Boss 1", world.player))
    set_rule(Jungle_to_SunsetShore, lambda state: state.has("Jungle Shop Key", world.player))
    set_rule(Beach_to_Ruins, lambda state: state.has("Defeated Boss 2", world.player))
    set_rule(Beach_to_BlowholeBound, lambda state: state.has("Beach Shop Key", world.player))
    set_rule(Ruins_to_Cave, lambda state: state.has("Defeated Boss 3", world.player))
    set_rule(Ruins_to_DampDungeon, lambda state: state.has("Ruins Shop Key", world.player))
    set_rule(Cave_to_Forest, lambda state: state.has("Defeated Boss 4", world.player))
    set_rule(Cave_to_MolePatrol, lambda state: state.has("Cave Shop Key", world.player))
    set_rule(Forest_to_Cliff, lambda state: state.has("Defeated Boss 5", world.player))
    set_rule(Forest_to_SpringySpores, lambda state: state.has("Forest Shop Key", world.player))
    set_rule(Cliff_to_Factory, lambda state: state.has("Defeated Boss 6", world.player))
    set_rule(Cliff_to_PrecariousPlateau, lambda state: state.has("Cliff Shop Key", world.player))
    set_rule(Factory_to_Volcano, lambda state: state.has("Defeated Boss 7", world.player))
    set_rule(Factory_to_HandyHazards, lambda state: state.has("Factory Shop Key", world.player))
    set_rule(Factory_to_Volcano, lambda state: state.has("Volcano Shop Key", world.player))

def set_all_location_rules(world: DKCRWorld) -> None:
    pass

def set_completion_condition(world: DKCRWorld) -> None:
    if world.options.golden_temple:
        world.multiworld.completion_condition[world.player] = lambda state: state.has("Defeated Boss 8", world.player)
    else:
        world.multiworld.completion_condition[world.player] = lambda state: state.has("9-1 Golden Temple cleared", world.player)