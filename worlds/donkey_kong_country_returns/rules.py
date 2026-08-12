from __future__ import annotations

import dataclasses
from typing import TYPE_CHECKING, override

from BaseClasses import CollectionState
from rule_builder.field_resolvers import FromOption
from rule_builder.rules import Has, Rule, True_
from worlds.donkey_kong_country_returns.DKCRNameConstants import Item as I, Generic as G
from .data.indexes import *
from .options import *

if TYPE_CHECKING:
    from . import DKCRWorld


def set_all_rules(world: DKCRWorld) -> None:
    set_completion_condition(world)


# @dataclasses.dataclass(kw_only=True)
# class BossAccess(Rule[DKCRWorld], game=G.GAME_NAME):
#     world_index: int
#
#     @override
#     def _instantiate(self, world: DKCRWorld) -> Rule.Resolved:
#         # caching_enabled only needs to be passed in when your world inherits from CachedRuleBuilderWorld
#         boss_access_options = {
#             JUNGLE_WORLD_INDEX: world.options.jungle_boss_access.value,
#             BEACH_WORLD_INDEX: world.options.beach_boss_access.value,
#             RUINS_WORLD_INDEX: world.options.ruins_boss_access.value,
#             CAVE_WORLD_INDEX: world.options.cave_boss_access.value,
#             FOREST_WORLD_INDEX: world.options.forest_boss_access.value,
#             CLIFF_WORLD_INDEX: world.options.cliff_boss_access.value,
#             FACTORY_WORLD_INDEX: world.options.factory_boss_access.value,
#             VOLCANO_WORLD_INDEX: world.options.volcano_boss_access.value,
#         }
#
#         puzzle_pieces_requirement = boss_access_options[self.world_index]
#
#         return Has(I.PUZZLE_PIECE, count=puzzle_pieces_requirement).resolve(world=world)


def CanEnterMuglysMound():
    return Has(I.PUZZLE_PIECE, count=FromOption(JungleBossAccess))


def CanEnterPinchinPirates():
    return Has(I.PUZZLE_PIECE, count=FromOption(BeachBossAccess))


def CanEnterRuinedRoost():
    return Has(I.PUZZLE_PIECE, count=FromOption(RuinsBossAccess))


def CanEnterTheMoleTrain():
    return Has(I.PUZZLE_PIECE, count=FromOption(CaveBossAccess))


def CanEnterMangorubyRun():
    return Has(I.PUZZLE_PIECE, count=FromOption(ForestBossAccess))


def CanEnterThuglysHighrise():
    return Has(I.PUZZLE_PIECE, count=FromOption(CliffBossAccess))


def CanEnterFeatherFiend():
    if FromOption(LiftOffLaunch) == 1:
        return Has(I.PUZZLE_PIECE, count=FromOption(FactoryBossAccess)) & can_access_feathery_fiend
    return Has(I.PUZZLE_PIECE, count=FromOption(FactoryBossAccess))

def CanEnterTikiTongTerror():
    return Has(I.PUZZLE_PIECE, count=FromOption(VolcanoBossAccess))

def CanEnterGoldenTemple():
    return beaten_boss_volcano

def SmogBlocksFactory():
    if FromOption(SmogClear) == 1:
        return can_access_factory
    return None

# @dataclasses.dataclass(kw_only=True)
# class CanEnterMuglysMounds(Rule[DKCRWorld], game=G.GAME_NAME):
#     @override
#     def _instantiate(self, world: DKCRWorld) -> Rule.Resolved:
#         Has(I.PUZZLE_PIECE, count=FromOption(JungleBossAccess))
#         return Has(I.PUZZLE_PIECE, world.options.jungle_boss_access.value).resolve(world)
#
# @dataclasses.dataclass(kw_only=True)
# class CanEnterPinchinPiratess(Rule[DKCRWorld], game=G.GAME_NAME):
#     @override
#     def _instantiate(self, world: DKCRWorld) -> Rule.Resolved:
#         return Has(I.PUZZLE_PIECE, world.options.beach_boss_access.value).resolve(world)
#
# @dataclasses.dataclass(kw_only=True)
# class CanEnterRuinedRoosts(Rule[DKCRWorld], game=G.GAME_NAME):
#     @override
#     def _instantiate(self, world: DKCRWorld) -> Rule.Resolved:
#         return Has(I.PUZZLE_PIECE, world.options.ruins_boss_access.value).resolve(world)
#
# @dataclasses.dataclass(kw_only=True)
# class CanEnterTheMoleTrains(Rule[DKCRWorld], game=G.GAME_NAME):
#     @override
#     def _instantiate(self, world: DKCRWorld) -> Rule.Resolved:
#         return Has(I.PUZZLE_PIECE, world.options.cave_boss_access.value).resolve(world)
#
# @dataclasses.dataclass(kw_only=True)
# class CanEnterMangorubysRun(Rule[DKCRWorld], game=G.GAME_NAME):
#     @override
#     def _instantiate(self, world: DKCRWorld) -> Rule.Resolved:
#         return Has(I.PUZZLE_PIECE, world.options.forest_boss_access.value).resolve(world)
#
# @dataclasses.dataclass(kw_only=True)
# class CanEnterThuglysHighrises(Rule[DKCRWorld], game=G.GAME_NAME):
#     @override
#     def _instantiate(self, world: DKCRWorld) -> Rule.Resolved:
#         return Has(I.PUZZLE_PIECE, world.options.cliff_boss_access.value).resolve(world)
#
# @dataclasses.dataclass(kw_only=True)
# class CanEnterFeatherFiends(Rule[DKCRWorld], game=G.GAME_NAME):
#     @override
#     def _instantiate(self, world: DKCRWorld) -> Rule.Resolved:
#         return Has(I.PUZZLE_PIECE, world.options.factory_boss_access.value).resolve(world)
#
# @dataclasses.dataclass(kw_only=True)
# class CanEnterTikiTongTerrors(Rule[DKCRWorld], game=G.GAME_NAME):
#     @override
#     def _instantiate(self, world: DKCRWorld) -> Rule.Resolved:
#         return Has(I.PUZZLE_PIECE, world.options.volcano_boss_access.value).resolve(world)

has_all_jungle_letters = Has(I.Kong_Letter.KONG_LETTER_JUNGLE, FromOption(JungleKLevelAccess))
has_all_beach_letters = Has(I.Kong_Letter.KONG_LETTER_BEACH, FromOption(BeachKLevelAccess))
has_all_ruins_letters = Has(I.Kong_Letter.KONG_LETTER_RUINS, FromOption(RuinsKLevelAccess))
has_all_cave_letters = Has(I.Kong_Letter.KONG_LETTER_CAVE, FromOption(CaveKLevelAccess))
has_all_forest_letters = Has(I.Kong_Letter.KONG_LETTER_FOREST, FromOption(ForestKLevelAccess))
has_all_cliff_letters = Has(I.Kong_Letter.KONG_LETTER_CLIFF, FromOption(CliffKLevelAccess))
has_all_factory_letters = Has(I.Kong_Letter.KONG_LETTER_FACTORY, FromOption(FactoryKLevelAccess))
has_all_volcano_letters = Has(I.Kong_Letter.KONG_LETTER_VOLCANO, FromOption(VolcanoKLevelAccess))

beaten_boss_jungle = Has("Jungle boss beaten")
beaten_boss_beach = Has("Beach boss beaten")
beaten_boss_ruins = Has("Ruins boss beaten")
beaten_boss_cave = Has("Cave boss beaten")
beaten_boss_forest = Has("Forest boss beaten")
beaten_boss_cliff = Has("Cliff boss beaten")
beaten_boss_factory = Has("Factory boss beaten")
beaten_boss_volcano = Has("Volcano boss beaten")

has_jungle_key = Has("Jungle Key") if FromOption(SunsetShoreKey) == 1 else True_()
has_beach_key = Has("Beach Key") if FromOption(BlowholeBoundKey) == 1 else True_()
has_ruins_key = Has("Ruins Key") if FromOption(DampDungeonKey) == 1 else True_()
has_cave_key = Has("Cave Key") if FromOption(MolePatrolKey) == 1 else True_()
has_forest_key = Has("Forest Key") if FromOption(SpringySporesKey) == 1 else True_()
has_cliff_key = Has("Cliff Key") if FromOption(PrecariousPlateauKey) == 1 else True_()
has_factory_key = Has("Factory Key") if FromOption(HandyHazardsKey) == 1 else True_()
has_volcano_key = Has("Volcano Key") if FromOption(SmokeyPeakKey) == 1 else True_()

has_all_mirror_shards = Has("Mirror Shard", FromOption(MirrorModeShards))
has_mirror_mode = Has("Mirror Mode")

can_enter_Lift_Off_Launch = Has("Progressive Factory Button", FromOption(FactoryButtons))
can_access_feathery_fiend = Has("Cleared 7-R")
can_access_factory = Has("Cleared smog")

def set_completion_condition(world: DKCRWorld) -> None:
    if FromOption(GoldenTemple) == 1:
        world.set_completion_rule(CanEnterGoldenTemple())
        return
    world.set_completion_rule(CanEnterTikiTongTerror())
