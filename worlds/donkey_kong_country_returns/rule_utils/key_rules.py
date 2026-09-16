from rule_builder.field_resolvers import FromOption
from rule_builder.rules import Has, True_
from ..option_utils.options import *

has_jungle_key = Has("Jungle Key") if FromOption(SunsetShoreKey) == 1 else True_()
has_beach_key = Has("Beach Key") if FromOption(BlowholeBoundKey) == 1 else True_()
has_ruins_key = Has("Ruins Key") if FromOption(DampDungeonKey) == 1 else True_()
has_cave_key = Has("Cave Key") if FromOption(MolePatrolKey) == 1 else True_()
has_forest_key = Has("Forest Key") if FromOption(SpringySporesKey) == 1 else True_()
has_cliff_key = Has("Cliff Key") if FromOption(PrecariousPlateauKey) == 1 else True_()
has_factory_key = Has("Factory Key") if FromOption(HandyHazardsKey) == 1 else True_()
has_volcano_key = Has("Volcano Key") if FromOption(SmokeyPeakKey) == 1 else True_()
