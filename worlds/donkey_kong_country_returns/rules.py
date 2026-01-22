from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import CollectionState
from worlds.generic.Rules import add_rule, set_rule

from .strings import RegionConnection as RC

if TYPE_CHECKING:
    from .world import DKCRWorld

def set_all_rules(world: DKCRWorld) -> None:
    set_all_entrance_rules(world)
    set_all_location_rules(world)
    set_completion_condition(world)

def set_all_entrance_rules(world: DKCRWorld) -> None:

    jungle_to_muglys_mound = world.get_entrance(RC.JUNGLE_TO_MUGLYS_MOUND)
    jungle_to_platform_panic = world.get_entrance(RC.JUNGLE_TO_PLATFORM_PANIC)
    muglys_mound_to_beach = world.get_entrance(RC.MUGLYS_MOUND_TO_BEACH)

    beach_to_pinchin_pirates = world.get_entrance(RC.BEACH_TO_PINCHIN_PIRATES)
    beach_to_tumblin_temple = world.get_entrance(RC.BEACH_TO_TUMBLIN_TEMPLE)
    pinchin_pirates_to_ruins = world.get_entrance(RC.PINCHIN_PIRATES_TO_RUINS)

    ruins_to_ruined_roost = world.get_entrance(RC.RUINS_TO_RUINED_ROOST)
    ruins_to_shifty_smashers = world.get_entrance(RC.RUINS_TO_SHIFTY_SMASHERS)
    ruined_roost_to_cave = world.get_entrance(RC.RUINED_ROOST_TO_CAVE)

    cave_to_the_mole_train = world.get_entrance(RC.CAVE_TO_THE_MOLE_TRAIN)
    cave_to_jagged_jewels = world.get_entrance(RC.CAVE_TO_JAGGED_JEWELS)
    the_mole_train_to_forest = world.get_entrance(RC.THE_MOLE_TRAIN_TO_FOREST)

    forest_to_mangoruby_run = world.get_entrance(RC.FOREST_TO_MANGORUBY_RUN)
    forest_to_blast_n_bounce = world.get_entrance(RC.FOREST_TO_BLAST_N_BOUNCE)
    mangoruby_run_to_cliff = world.get_entrance(RC.MANGORUBY_RUN_TO_CLIFF)

    cliff_to_thuglys_highrise = world.get_entrance(RC.CLIFF_TO_THUGLYS_HIGHRISE)
    cliff_to_perilous_passage = world.get_entrance(RC.CLIFF_TO_PERILOUS_PASSAGE)
    thuglys_highrise_to_factory = world.get_entrance(RC.THUGLYS_HIGHRISE_TO_FACTORY)

    factory_to_lift_off_launch = world.get_entrance(RC.FACTORY_TO_LIFT_OFF_LAUNCH)
    factory_to_treacherous_track = world.get_entrance(RC.FACTORY_TO_TREACHEROUS_TRACK)
    lift_off_launch_to_feather_fiend = world.get_entrance(RC.LIFT_OFF_LAUNCH_TO_FEATHER_FIEND)
    feather_fiend_to_volcano = world.get_entrance(RC.FEATHER_FIEND_TO_VOLCANO)

    volcano_to_tiki_tong_terror = world.get_entrance(RC.VOLCANO_TO_TIKI_TONG_TERROR)
    volcano_to_five_monkey_trial = world.get_entrance(RC.VOLCANO_TO_FIVE_MONKEY_TRIAL)

    if world.options.golden_temple:
        tiki_tong_terror_to_golden_temple = world.get_entrance(RC.TIKI_TONG_TERROR_TO_GOLDEN_TEMPLE)


def set_all_location_rules(world: DKCRWorld) -> None:
    pass

def set_completion_condition(world: DKCRWorld) -> None:
    if world.options.golden_temple:
        world.multiworld.completion_condition[world.player] = lambda state: state.has("Puzzle Piece", world.player)
    else:
        world.multiworld.completion_condition[world.player] = lambda state: state.has("Puzzle Piece", world.player)