from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import CollectionState
from rule_builder.rules import HasAllCounts

from worlds.donkey_kong_country_returns.DKCRNameConstants import RegionConnection as RC, Item as I, Location as L

if TYPE_CHECKING:
    from . import DKCRWorld

def set_all_rules(world: DKCRWorld) -> None:
    set_completion_condition(world)

has_all_jungle_letters = {I.Kong_Letter.KONG_LETTER_JUNGLE: 24}
has_all_beach_letters = {I.Kong_Letter.KONG_LETTER_BEACH: 28}
has_all_ruins_letters = {I.Kong_Letter.KONG_LETTER_RUINS: 24}
has_all_cave_letters = {I.Kong_Letter.KONG_LETTER_CAVE: 20}
has_all_forest_letters = {I.Kong_Letter.KONG_LETTER_FOREST: 32}
has_all_cliff_letters = {I.Kong_Letter.KONG_LETTER_CLIFF: 32}
has_all_factory_letters = {I.Kong_Letter.KONG_LETTER_FACTORY: 28}
has_all_volcano_letters = {I.Kong_Letter.KONG_LETTER_VOLCANO: 28}

has_enough_pp_jungle = {I.PUZZLE_PIECE: 20}
has_enough_pp_beach = {I.PUZZLE_PIECE: 50}
has_enough_pp_ruins = {I.PUZZLE_PIECE: 80}
has_enough_pp_cave = {I.PUZZLE_PIECE: 110}
has_enough_pp_forest = {I.PUZZLE_PIECE: 150}
has_enough_pp_cliff = {I.PUZZLE_PIECE: 200}
has_enough_pp_factory = {I.PUZZLE_PIECE: 260}
has_enough_pp_volcano = {I.PUZZLE_PIECE: 320}


def set_completion_condition(world: DKCRWorld) -> None:
    world.multiworld.completion_condition[world.player] = lambda state: state.can_reach_location(L.TIKI_TONG_TERROR_CLEARED, world.player)