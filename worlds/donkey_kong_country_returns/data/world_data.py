import dataclasses

from .level_data import LEVELS_BY_WORLD
from ..DKCRNameConstants import World as W


@dataclasses.dataclass(slots=True)
class WorldData:
    world_index: int
    key_address: int | None
    orb_address: int | None
    puzzle_piece_amount: int
    kong_letter_amount: int


WORLD_RAW = {
    W.JUNGLE: (0x05, 0x80de13, 0x80ddd0),
    W.BEACH: (0x00, 0x80ddff, 0x80ddd4),
    W.RUINS: (0x06, 0x80de17, 0x80ddd8),
    W.CAVE: (0x01, 0x80de03, 0x80dddc),
    W.FOREST: (0x04, 0x80de0f, 0x80dde0),
    W.CLIFF: (0x02, 0x80de07, 0x80dde4),
    W.FACTORY: (0x03, 0x80de0b, 0x80dde8),
    W.VOLCANO: (0x07, 0x80de1b, 0x80ddec),
    W.GOLDEN_TEMPLE: (0x08, None, None),
}


def get_total_puzzle_pieces(name: str) -> int:
    return sum(
        l.puzzle_piece_amount or 0
        for l in LEVELS_BY_WORLD[name]
    )


def get_total_kong_letters(name: str) -> int:
    return sum(
        l.kong_letter_amount or 0
        for l in LEVELS_BY_WORLD[name]
    )


Worlds: dict[str, WorldData] = {
    name: WorldData(
        world_index=index,
        key_address=key,
        orb_address=orb,
        puzzle_piece_amount=get_total_puzzle_pieces(name),
        kong_letter_amount=get_total_kong_letters(name),
    )
    for name, (index, key, orb) in WORLD_RAW.items()
}
