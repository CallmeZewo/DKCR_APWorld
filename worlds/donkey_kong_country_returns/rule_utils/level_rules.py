from rule_builder.field_resolvers import FromOption
from rule_builder.rules import Has
from ..option_utils.options import *

can_enter_Lift_Off_Launch = Has("Progressive Factory Button", FromOption(FactoryButtons))
