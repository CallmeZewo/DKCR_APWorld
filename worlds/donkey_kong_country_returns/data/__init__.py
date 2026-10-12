from __future__ import annotations

from BaseClasses import ItemClassification
from enum import Enum
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .levels import GameLevels


class LevelTypeEnum(Enum):
    def __init__(self,
                 display_name: str,
                 level_index: int,
                 level_map_index: int,
                 data_offset: int,
                 pp_amount: int,
                 has_kong_letters: bool = True
                 ):
        self.display_name = display_name
        self.level_index = level_index
        self.level_map_index = level_map_index
        self.data_offset = data_offset
        self.pp_amount = pp_amount
        self.has_kong_letters = has_kong_letters
        self.connections = []

    @classmethod
    def from_display_name(cls, display_name: str) -> "LevelTypeEnum":
        for level in cls:
            if level.display_name == display_name:
                return level
        raise ValueError(
            f"{display_name!r} is not a valid {cls.__name__} diplay name"
        )

class WorldTypeEnum(Enum):
    def __init__(self,
                 display_name: str,
                 world_index: int,
                 key_address: int | None,
                 orb_address: int | None,
                 level_list: dict[GameLevels, GameLevels]):
        self.display_name = display_name
        self.world_index = world_index
        self.key_address = key_address
        self.orb_address = orb_address
        self.level_list: dict[GameLevels, GameLevels] = level_list
        self.connections = []

    @classmethod
    def from_display_name(cls, display_name: str) -> "WorldTypeEnum":
        for world in cls:
            if world.display_name == display_name:
                return world
        raise ValueError(
            f"{display_name!r} is not valid {cls.__name__} display name"
        )

    @classmethod
    def get_level_from_world_and_level_index(cls, world_index: int, level_index: int) -> "LevelTypeEnum":
        for world in cls:
            if world_index != world_index:
                continue
            for level in world.level_list:
                if level.level_index != level_index:
                    continue
                return level
        raise ValueError(
            f"level for world index: {world_index!r} and level index: {level_index!r} cant be found in {cls.__name__}"
        )

    @classmethod
    def get_level_offset_from_world_and_level_index(cls, world_index: int, level_index: int) -> int:
        for world in cls:
            if world.world_index != world_index:
                continue
            for level in world.level_list:
                if level.level_index != level_index:
                    continue
                return level.data_offset
        raise ValueError(
            f"level offset for world index: {world_index!r} and level index: {level_index!r} cant be found in {cls.__name__}"
        )


    def kong_letter_amount(self) -> int:
        amount: int = 0
        for level in self.level_list:
            amount += 1 if level.has_kong_letters else 0
        return amount

    def puzzle_piece_amount(self) -> int:
        amount: int = 0
        for level in self.level_list:
            amount += level.pp_amount
        return amount


class ItemTypeEnum(Enum):
    def __init__(self,
                 display_name: str,
                 code: int,
                 classification: ItemClassification,
                 amount: int = 1):
        self.display_name = display_name
        self.code = code
        self.classification = classification
        self.amount = amount

    @classmethod
    def from_display_name(cls, display_name: str) -> "ItemTypeEnum":
        for item in cls:
            if item.display_name == display_name:
                return item
        raise ValueError(
            f"{display_name!r} is not a valid {cls.__name__} display name"
        )

class Medals(Enum):
    Bronze = 0x0
    Silver = 0x1
    Gold = 0x2
    Shiny_Gold = 0x3
    Empty = 0xff

class LevelData:
    def __init__(self, bitflags: int, medal: int):
        self.level_available = bitflags & 0x80 == 0x80
        self.level_cleared = bitflags & 0x40 == 0x40
        self.flag_to_play_level_clear_animation = bitflags & 0x20 == 0x20
        self.all_puzzle_pieces_collected = bitflags & 0x10 == 0x10
        self.kong_collected = bitflags & 0x8 == 0x8
        self.cleared_with_super_guide = bitflags & 0x4 == 0x4
        self.mirror_mode_cleared = bitflags & 0x1 == 0x1

        self.medal = Medals(medal)