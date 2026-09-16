from ..data.levels import GameLevels
from ..data.worlds import GameWorlds

def get_region_type(display_name: str):
    try:
        return GameLevels.from_display_name(display_name)
    except ValueError:
        try:
            return GameWorlds.from_display_name(display_name)
        except ValueError:
            raise ValueError(f"{display_name!r} is not a valid level or world")