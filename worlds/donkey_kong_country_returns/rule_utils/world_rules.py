from rule_builder.field_resolvers import FromOption
from rule_builder.options import OptionFilter
from rule_builder.rules import Has
from .boss_rules import beaten_boss_volcano
from ..data.constants import ItemName
from ..option_utils.options import *


def smog_blocks_factory():
    return Has("Cleared smog", options=[OptionFilter(SmogClear, 1, operator= "eq")], filtered_resolution=True)

def can_enter_golden_temple():
    return beaten_boss_volcano & Has(ItemName.RARE_ORB.value, count=FromOption(RareOrbs))

can_access_factory = Has("Cleared smog")