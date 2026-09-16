from rule_builder.field_resolvers import FromOption
from rule_builder.rules import Has, True_
from ..data.constants.item_constants import ItemName as In
from ..option_utils.options import *

def can_enter_muglys_mound():
    return Has(In.PUZZLE_PIECE.value, count=FromOption(JungleBossAccess)) | Has(In.PROGRESSIVE_BOSS_UNLOCK.value, 1)


def can_enter_pinchin_pirates():
    return Has(In.PUZZLE_PIECE.value, count=FromOption(BeachBossAccess)) | Has(In.PROGRESSIVE_BOSS_UNLOCK.value, 2)


def can_enter_ruined_roost():
    return Has(In.PUZZLE_PIECE.value, count=FromOption(RuinsBossAccess)) | Has(In.PROGRESSIVE_BOSS_UNLOCK.value, 3)


def can_enter_the_mole_train():
    return Has(In.PUZZLE_PIECE.value, count=FromOption(CaveBossAccess)) | Has(In.PROGRESSIVE_BOSS_UNLOCK.value, 4)


def can_enter_mangoruby_run():
    return Has(In.PUZZLE_PIECE.value, count=FromOption(ForestBossAccess)) | Has(In.PROGRESSIVE_BOSS_UNLOCK.value, 5)


def can_enter_thuglys_highrise():
    return Has(In.PUZZLE_PIECE.value, count=FromOption(CliffBossAccess)) | Has(In.PROGRESSIVE_BOSS_UNLOCK.value, 6)


def can_enter_feather_fiend():
    if FromOption(LiftOffLaunch) == 1:
        return (Has(In.PUZZLE_PIECE.value, count=FromOption(FactoryBossAccess)) & can_access_feathery_fiend) | Has(In.PROGRESSIVE_BOSS_UNLOCK.value, 7)
    return Has(In.PUZZLE_PIECE.value, count=FromOption(FactoryBossAccess)) | Has(In.PROGRESSIVE_BOSS_UNLOCK.value, 7)

def can_enter_tiki_tong_terror():
    return Has(In.PUZZLE_PIECE.value, count=FromOption(VolcanoBossAccess)) | Has(In.PROGRESSIVE_BOSS_UNLOCK.value, 8)

beaten_boss_jungle = Has("Jungle boss beaten")
beaten_boss_beach = Has("Beach boss beaten")
beaten_boss_ruins = Has("Ruins boss beaten")
beaten_boss_cave = Has("Cave boss beaten")
beaten_boss_forest = Has("Forest boss beaten")
beaten_boss_cliff = Has("Cliff boss beaten")
beaten_boss_factory = Has("Factory boss beaten")
beaten_boss_volcano = Has("Volcano boss beaten") if FromOption(GoldenTemple) == 1 else True_()

can_access_feathery_fiend = Has("Cleared 7-R")