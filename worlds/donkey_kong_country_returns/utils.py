import dataclasses
import dolphin_memory_engine as dme
from .data.addresses import *

@dataclasses.dataclass()
class LevelMemData:
    flags: bytes
    record_time: float
    medal: int

def get_level_data(level_offset: int, ):
    main = int.from_bytes(dme.read_bytes(LEVEL_DATA_POINTER, 4), "big")
    level_data = int.from_bytes(dme.read_bytes(main + level_offset, 4), "big")
    return LevelMemData(
        dme.read_byte(level_data + 0x3e),
        float.fromhex(dme.read_bytes(level_data + 0x38, 4)),
        dme.read_byte(level_data + 0x3d)
    )