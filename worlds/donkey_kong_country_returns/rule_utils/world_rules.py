from rule_builder.field_resolvers import FromOption
from rule_builder.rules import Has
from .boss_rules import beaten_boss_volcano
from ..data.constants import ItemName
from ..option_utils.options import *


def smog_blocks_factory():
    if FromOption(SmogClear) == 1:
        return can_access_factory
    return None

def can_enter_golden_temple():
    return beaten_boss_volcano & Has(ItemName.RARE_ORB.value, count=FromOption(RareOrbs))

can_access_factory = Has("Cleared smog")