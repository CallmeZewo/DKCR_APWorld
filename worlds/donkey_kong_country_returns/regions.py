from __future__ import annotations

from typing import TYPE_CHECKING, Mapping

from BaseClasses import Region
from rule_builder.rules import Rule
from .data.level_data import Levels
from .data.world_data import Worlds
from .DKCRNameConstants import Level as LV

if TYPE_CHECKING:
    from . import DKCRWorld

def create_and_connect_regions(world: DKCRWorld) -> None:
    create_all_regions(world)

def create_all_regions(world: DKCRWorld) -> None:
    regions = world.multiworld.regions

    regions.append(create_regions_helper("Menu", world))

    for world_name in Worlds:
        regions.append(create_regions_helper(world_name, world))

        for level_name, level_data in Levels.items():
            if level_data.world_name == world_name:
                regions.append(create_regions_helper(level_name, world))
                if level_data.index == 0x2 or level_name == LV.GOLDEN_TEMPLE:
                    connect_regions(world, world_name, level_name, f"{world_name} to {level_name}")

        for level_name_from, level_data_from in Levels.items():
            if level_data_from.world_name != world_name:
                continue

            for connection in level_data_from.connections:
                if connection is None:
                    continue

                # rule connection form: [target_index, rule]
                if isinstance(connection, list):
                    target_index = connection[0]
                    rule = connection[1] if len(connection) > 1 else None

                    for level_name_to_rule, level_data_to_rule in Levels.items():
                        if level_data_to_rule.index == target_index and level_data_to_rule.world_name == world_name:
                            connect_regions_with_rule(
                                world,
                                level_name_from,
                                level_name_to_rule,
                                f"{level_name_from} to {level_name_to_rule}",
                                rule,
                            )
                            break
                    continue

                # normal connection
                for level_name_to, level_data_to in Levels.items():
                    if level_data_to.index == connection and level_data_to.world_name == world_name:
                        connect_regions(
                            world,
                            level_name_from,
                            level_name_to,
                            f"{level_name_from} to {level_name_to}",
                        )
                        break

        connect_regions(world, "Menu", world_name, f"Menu to {world_name}")




def create_regions_helper(name: str, world: DKCRWorld) -> Region:
    return Region(name, world.player, world.multiworld)

def connect_regions(world, from_name: str, to_name: str, entrance_name: str):
    from_region = world.get_region(from_name)
    to_region = world.get_region(to_name)
    entrance = from_region.connect(to_region, entrance_name)
    print(entrance_name)
    return entrance
def connect_regions_with_rule(world, from_name: str, to_name: str, entrance_name: str, rule: Mapping[str, int]):
    from_region = world.get_region(from_name)
    to_region = world.get_region(to_name)
    entrance = from_region.connect(to_region, entrance_name)
    entrance.access_rule = lambda state: state.has_any_count(rule, world.player)
    return entrance