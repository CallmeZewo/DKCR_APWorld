from rule_builder.options import OptionFilter
from rule_builder.rules import Has
from ..option_utils.options import *

has_jungle_key = Has("Jungle Key", options=[OptionFilter(SunsetShoreKey, 1)], filtered_resolution=False)
has_beach_key = Has("Beach Key", options=[OptionFilter(BlowholeBoundKey, 1)], filtered_resolution=False)
has_ruins_key = Has("Ruins Key", options=[OptionFilter(DampDungeonKey, 1)], filtered_resolution=False)
has_cave_key = Has("Cave Key", options=[OptionFilter(MolePatrolKey, 1)], filtered_resolution=False)
has_forest_key = Has("Forest Key", options=[OptionFilter(SpringySporesKey, 1)], filtered_resolution=False)
has_cliff_key = Has("Cliff Key", options=[OptionFilter(PrecariousPlateauKey, 1)], filtered_resolution=False)
has_factory_key = Has("Factory Key", options=[OptionFilter(HandyHazardsKey, 1)], filtered_resolution=False)
has_volcano_key = Has("Volcano Key", options=[OptionFilter(SmokeyPeakKey, 1)], filtered_resolution=False)
