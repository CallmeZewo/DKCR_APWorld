from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import CollectionState
from worlds.generic.Rules import add_rule, set_rule

from worlds.donkey_kong_country_returns.DKCRNameConstants import RegionConnection as RC, Item as I, Location as L

if TYPE_CHECKING:
    from . import DKCRWorld

def set_all_rules(world: DKCRWorld) -> None:
    set_rules(world)
    set_completion_condition(world)

def get_rules(world: DKCRWorld):
    rules = {
        "entrances": {
            RC.JUNGLE_TO_MUGLYS_MOUND:
                lambda state:
                    state.has(I.PUZZLE_PIECE, world.player, world.options.jungle_boss_access.value),
            RC.BEACH_TO_PINCHIN_PIRATES:
                lambda state:
                    state.has(I.PUZZLE_PIECE, world.player, world.options.beach_boss_access.value),
            RC.RUINS_TO_RUINED_ROOST:
                lambda state:
                    state.has(I.PUZZLE_PIECE, world.player, world.options.ruins_boss_access.value),
            RC.CAVE_TO_THE_MOLE_TRAIN:
                lambda state:
                    state.has(I.PUZZLE_PIECE, world.player, world.options.cave_boss_access.value),
            RC.FOREST_TO_MANGORUBY_RUN:
                lambda state:
                    state.has(I.PUZZLE_PIECE, world.player, world.options.forest_boss_access.value),
            RC.CLIFF_TO_THUGLYS_HIGHRISE:
                lambda state:
                    state.has(I.PUZZLE_PIECE, world.player, world.options.cliff_boss_access.value),
            RC.LIFT_OFF_LAUNCH_TO_FEATHER_FIEND:
                lambda state:
                    state.has(I.PUZZLE_PIECE, world.player, world.options.factory_boss_access.value),
            RC.VOLCANO_TO_TIKI_TONG_TERROR:
                lambda state:
                    state.has(I.PUZZLE_PIECE, world.player, world.options.volcano_boss_access.value),
        }
    }
    return rules

def set_rules(world: DKCRWorld) -> None:
    rules_lookup = get_rules(world)
    for entrance_name, rule in rules_lookup["entrances"].items():
        try:
            world.get_entrance(entrance_name).access_rule = rule
        except KeyError:
            pass

def set_completion_condition(world: DKCRWorld) -> None:
    world.multiworld.completion_condition[world.player] = lambda state: state.can_reach_location(L.TIKI_TONG_TERROR_CLEARED, world.player)