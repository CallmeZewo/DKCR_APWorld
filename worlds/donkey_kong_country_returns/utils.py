from .data.levels import GameLevels
from .data.worlds import GameWorlds
from .data.constants import LocationOffset as Lo

def get_base_address(level: GameLevels = None, world: GameWorlds = None) -> None | int:
    if not world:
        return None
    if not level:
        return (
            world.world_index * Lo.WorldOffset
            + world.world_index + 0xF * Lo.LevelOffset
        )
    return (
        world.world_index * Lo.WorldOffset
        + level.level_index * Lo.LevelOffset
    )