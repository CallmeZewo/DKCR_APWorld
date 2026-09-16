from rule_builder.field_resolvers import FromOption
from rule_builder.rules import Has
from ..option_utils.options import *

has_all_mirror_shards = Has("Mirror Shard", FromOption(MirrorModeShards))
has_mirror_mode = Has("Mirror Mode") | has_all_mirror_shards
