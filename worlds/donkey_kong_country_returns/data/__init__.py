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
                 pointer: int,
                 pp_amount: int,
                 has_kong_letters: bool = True
                 ):
        self.display_name = display_name
        self.level_index = level_index
        self.pointer = pointer
        self.pp_amount = pp_amount
        self.has_kong_letters = has_kong_letters
        self.connections = []

    @classmethod
    def from_display_name(cls, display_name: str) -> "LevelTypeEnum":
        for level in cls:
            if level.display_name == display_name:
                return level
        raise ValueError(
            f"{display_name!r} is not valid {cls.__name__} diplay name"
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
            f"{display_name!r} is not valid {cls.__name__} diplay name"
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
            f"{display_name!r} is not valid {cls.__name__} diplay name"
        )