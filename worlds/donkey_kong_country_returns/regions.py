from __future__ import annotations

from multiprocessing.forkserver import connect_to_new_process
from typing import TYPE_CHECKING, Mapping

from BaseClasses import Region
from rule_builder.rules import Rule
from .data.level_data import Levels
from .data.indexes import *
from .data.world_data import Worlds
from .DKCRNameConstants import Level

if TYPE_CHECKING:
    from . import DKCRWorld

def create_and_connect_regions(world: DKCRWorld) -> None:
    create_all_regions(world)

def create_all_regions(world: DKCRWorld) -> None:
    regions = world.multiworld.regions

    regions.append(create_regions_helper("Menu", world))

    for world_name, world_data in Worlds.items():
        regions.append(create_regions_helper(world_name, world))

        for level_name, level_data in Levels.items():
            if level_data.world_index == world_data.world_index:
                regions.append(create_regions_helper(level_name, world))
                if level_data.index == FIRST_LEVEL_INDEX or level_name == Level.GOLDEN_TEMPLE:
                    connect_regions(world, world_name, level_name, f"{world_name} to {level_name}")
                    connect_regions(world, level_name, world_name, f"{level_name} to {world_name}")

        for level_name_from, level_data_from in Levels.items():
            if level_data_from.world_index != world_data.world_index:
                continue

            for connection_from in level_data_from.connections:
                if connection_from is None:
                    continue
                if connection_from.rule is None:
                    for level_name_to, level_data_to in Levels.items():
                        if level_data_to.world_index == level_data_from.world_index:
                            if connection_from.to_level_index == level_data_to.index:
                                connect_regions(world, level_name_from, level_name_to, f"{level_name_from} to {level_name_to}")
                                break
                else:
                    for level_name_to_rule, level_data_to_rule in Levels.items():
                        if level_data_to_rule.world_index == level_data_from.world_index:
                            if connection_from.to_level_index == level_data_to_rule.index:
                                connect_regions_with_rule(world, level_name_from, level_name_to_rule, f"{level_name_from} to {level_name_to_rule}", connection_from.rule)

        connect_regions(world, "Menu", world_name, f"Menu to {world_name}")
        connect_regions(world, world_name,"Menu" , f"{world_name} to Menu")

def create_regions_helper(name: str, world: DKCRWorld) -> Region:
    return Region(name, world.player, world.multiworld)

def connect_regions(world, from_name: str, to_name: str, entrance_name: str):
    from_region = world.get_region(from_name)
    to_region = world.get_region(to_name)
    entrance = from_region.connect(to_region, entrance_name)
    return entrance
def connect_regions_with_rule(world, from_name: str, to_name: str, entrance_name: str, rule: Rule):
    from_region = world.get_region(from_name)
    to_region = world.get_region(to_name)
    entrance = from_region.connect(to_region, entrance_name, rule)
    return entrance