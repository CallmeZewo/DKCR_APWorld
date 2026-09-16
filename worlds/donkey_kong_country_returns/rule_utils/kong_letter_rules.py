from rule_builder.field_resolvers import FromOption
from rule_builder.rules import Has
from ..option_utils.options import *
from ..data.constants.item_constants import ItemName as In

has_all_jungle_letters = Has(In.KONG_LETTER_JUNGLE.value, FromOption(JungleKLevelAccess))
has_all_beach_letters = Has(In.KONG_LETTER_BEACH.value, FromOption(BeachKLevelAccess))
has_all_ruins_letters = Has(In.KONG_LETTER_RUINS.value, FromOption(RuinsKLevelAccess))
has_all_cave_letters = Has(In.KONG_LETTER_CAVE.value, FromOption(CaveKLevelAccess))
has_all_forest_letters = Has(In.KONG_LETTER_FOREST.value, FromOption(ForestKLevelAccess))
has_all_cliff_letters = Has(In.KONG_LETTER_CLIFF.value, FromOption(CliffKLevelAccess))
has_all_factory_letters = Has(In.KONG_LETTER_FACTORY.value, FromOption(FactoryKLevelAccess))
has_all_volcano_letters = Has(In.KONG_LETTER_VOLCANO.value, FromOption(VolcanoKLevelAccess))
