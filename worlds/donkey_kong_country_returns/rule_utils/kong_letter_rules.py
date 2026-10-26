from rule_builder.field_resolvers import FromOption
from rule_builder.options import OptionFilter
from rule_builder.rules import Has
from ..option_utils.options import *
from ..data.constants.item_constants import ItemName as In

has_all_jungle_letters = Has(In.KONG_LETTER_JUNGLE.value, count=FromOption(JungleKLevelAccess),
                             options=[OptionFilter(KongLetterUnlockKLevel, 1, operator="eq")], filtered_resolution=False)
has_all_beach_letters = Has(In.KONG_LETTER_BEACH.value, count=FromOption(BeachKLevelAccess),
                            options=[OptionFilter(KongLetterUnlockKLevel, 1, operator="eq")], filtered_resolution=False)
has_all_ruins_letters = Has(In.KONG_LETTER_RUINS.value, count=FromOption(RuinsKLevelAccess),
                            options=[OptionFilter(KongLetterUnlockKLevel, 1, operator="eq")], filtered_resolution=False)
has_all_cave_letters = Has(In.KONG_LETTER_CAVE.value, count=FromOption(CaveKLevelAccess),
                           options=[OptionFilter(KongLetterUnlockKLevel, 1, operator="eq")], filtered_resolution=False)
has_all_forest_letters = Has(In.KONG_LETTER_FOREST.value, count=FromOption(ForestKLevelAccess),
                             options=[OptionFilter(KongLetterUnlockKLevel, 1, operator="eq")], filtered_resolution=False)
has_all_cliff_letters = Has(In.KONG_LETTER_CLIFF.value, count=FromOption(CliffKLevelAccess),
                            options=[OptionFilter(KongLetterUnlockKLevel, 1, operator="eq")], filtered_resolution=False)
has_all_factory_letters = Has(In.KONG_LETTER_FACTORY.value, count=FromOption(FactoryKLevelAccess),
                              options=[OptionFilter(KongLetterUnlockKLevel, 1, operator="eq")], filtered_resolution=False)
has_all_volcano_letters = Has(In.KONG_LETTER_VOLCANO.value, count=FromOption(VolcanoKLevelAccess),
                              options=[OptionFilter(KongLetterUnlockKLevel, 1, operator="eq")], filtered_resolution=False)
