from BaseClasses import Tutorial
from worlds.AutoWorld import WebWorld

from .options import option_groups, option_presets

class DKCRWebWorld(WebWorld):
    game = "Donkey Kong Country Returns"

    theme = "jungle"

    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up Donkey Kong Country Returns for MultiWorld.",
        "English",
        "en_Donkey Kong Country Returns.md",
        "setup/en",
        ["CallmeZero"],
    )

    tutorials = [setup_en]

    option_groups = option_groups
    option_presets = option_presets