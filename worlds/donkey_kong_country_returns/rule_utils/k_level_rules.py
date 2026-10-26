from rule_builder.rules import True_
from .kong_letter_rules import *
from ..option_utils.options import *


def can_enter_platform_panic():
    return has_all_jungle_letters | Has("Progressive K Level Unlock", 1)

def can_enter_tumblin_temple():
    return has_all_beach_letters | Has("Progressive K Level Unlock", 2)

def can_enter_shifty_smashers():
    return has_all_ruins_letters | Has("Progressive K Level Unlock", 3)

def can_enter_jagged_jewels():
    return has_all_cave_letters | Has("Progressive K Level Unlock", 4)

def can_enter_blast_n_bounce():
    return has_all_forest_letters | Has("Progressive K Level Unlock", 5)

def can_enter_perilous_passage():
    return has_all_cliff_letters | Has("Progressive K Level Unlock", 6)

def can_enter_treacherous_track():
    return has_all_factory_letters | Has("Progressive K Level Unlock", 7)

def can_enter_five_monkey_trial():
    return has_all_volcano_letters | Has("Progressive K Level Unlock", 8)
