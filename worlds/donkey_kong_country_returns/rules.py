from __future__ import annotations

from typing import TYPE_CHECKING

from rule_builder.field_resolvers import FromOption
from rule_builder.rules import Has
from worlds.donkey_kong_country_returns.DKCRNameConstants import Item as I
from .options import JungleBossAccess, BeachBossAccess, RuinsBossAccess, CaveBossAccess, ForestBossAccess, \
    CliffBossAccess, FactoryBossAccess, VolcanoBossAccess

if TYPE_CHECKING:
    from . import DKCRWorld


def set_all_rules(world: DKCRWorld) -> None:
    set_completion_condition(world)


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
    return Has(I.PUZZLE_PIECE, count=FromOption(FactoryBossAccess))


def CanEnterTikiTongTerror():
    return Has(I.PUZZLE_PIECE, count=FromOption(VolcanoBossAccess))


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

has_all_jungle_letters = Has(I.Kong_Letter.KONG_LETTER_JUNGLE, 24)
has_all_beach_letters = Has(I.Kong_Letter.KONG_LETTER_BEACH, 28)
has_all_ruins_letters = Has(I.Kong_Letter.KONG_LETTER_RUINS, 24)
has_all_cave_letters = Has(I.Kong_Letter.KONG_LETTER_CAVE, 20)
has_all_forest_letters = Has(I.Kong_Letter.KONG_LETTER_FOREST, 32)
has_all_cliff_letters = Has(I.Kong_Letter.KONG_LETTER_CLIFF, 32)
has_all_factory_letters = Has(I.Kong_Letter.KONG_LETTER_FACTORY, 28)
has_all_volcano_letters = Has(I.Kong_Letter.KONG_LETTER_VOLCANO, 28)

beaten_boss_jungle = Has("Jungle boss beaten")
beaten_boss_beach = Has("Beach boss beaten")
beaten_boss_ruins = Has("Ruins boss beaten")
beaten_boss_cave = Has("Cave boss beaten")
beaten_boss_forest = Has("Forest boss beaten")
beaten_boss_cliff = Has("Cliff boss beaten")
beaten_boss_factory = Has("Factory boss beaten")
beaten_boss_volcano = Has("Volcano boss beaten")


def set_completion_condition(world: DKCRWorld) -> None:
    world.set_completion_rule(Has("Volcano boss beaten"))
