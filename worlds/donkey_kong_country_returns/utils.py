import dataclasses
import dolphin_memory_engine as dme

from .data.addresses import *
from .data.levels import GameLevels
from .data.worlds import GameWorlds
from .data.constants import LocationOffset as Lo


class Color:
    GREEN = "\033[92m"
    RED = "\033[91m"
    YELLOW = "\033[93m"
    RESET = "\033[0m"

@dataclasses.dataclass()
class LevelMemData:
    flags: bytes
    record_time: float
    medal: int

def get_game_state():
    state = int.from_bytes(dme.read_bytes(MEM + GAME_STATE, 4), "big")
    return state


def get_level_data(level_offset: int, ):
    main = int.from_bytes(dme.read_bytes(LEVEL_DATA_POINTER, 4), "big")
    level_data = int.from_bytes(dme.read_bytes(main + level_offset, 4), "big")
    return LevelMemData(
        dme.read_byte(level_data + 0x3e),
        float.fromhex(dme.read_bytes(level_data + 0x38, 4)),
        dme.read_byte(level_data + 0x3d)
    )

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