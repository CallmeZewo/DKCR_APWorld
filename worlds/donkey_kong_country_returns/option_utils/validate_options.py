from __future__ import annotations
from typing import TYPE_CHECKING

from Options import OptionError

if TYPE_CHECKING:
    from worlds.donkey_kong_country_returns import DKCRWorld

def validate_options(dkcr_world: DKCRWorld):
    options = dkcr_world.options

    if not dkcr_world.selected_clear_types:
        raise OptionError(f"There should be at least one level clear type selected in your yaml.")

    if options.level_clear_type.value in ["Time", "Time Attack"]:
        if not dkcr_world.selected_medals:
            raise OptionError(f"If the level clear type 'Time Attack' does not work without the 'Time Attack Medal' option.")



