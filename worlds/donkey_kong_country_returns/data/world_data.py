import dataclasses

from .indexes import *
from .addresses import *
from ..DKCRNameConstants import World as W
from .world_connection import WorldConnection
from ..rules import *


@dataclasses.dataclass(slots=True)
class WorldData:
    world_index: int
    key_address: int | None
    orb_address: int | None
    connection: list[WorldConnection]

    def puzzle_piece_amount(self, levels) -> int:
        sum = 0
        for l in levels.values():
            sum += l.puzzle_piece_amount if l.world_index == self.world_index else 0
        return sum

    def kong_letter_amount(self, levels) -> int:
        sum = 0
        for l in levels.values():
            sum += l.kong_letter_amount if l.world_index == self.world_index else 0
        return sum

Worlds: dict[str, WorldData] = {
    W.JUNGLE: WorldData(
        world_index=JUNGLE_WORLD_INDEX,
        key_address=WORLD_MAP_KEY_JUNGLE,
        orb_address=RARE_ORB_JUNGLE,
        connection=[
            WorldConnection(
                from_world_index=JUNGLE_WORLD_INDEX,
                to_world_index=BEACH_WORLD_INDEX,
                rule=beaten_boss_jungle
            )
        ]
    ),

    W.BEACH: WorldData(
        world_index=BEACH_WORLD_INDEX,
        key_address=WORLD_MAP_KEY_BEACH,
        orb_address=RARE_ORB_BEACH,
        connection=[
            WorldConnection(
                from_world_index=BEACH_WORLD_INDEX,
                to_world_index=JUNGLE_WORLD_INDEX
            ),
            WorldConnection(
                from_world_index=BEACH_WORLD_INDEX,
                to_world_index=RUINS_WORLD_INDEX,
                rule=beaten_boss_beach
            )
        ]
    ),

    W.RUINS: WorldData(
        world_index=RUINS_WORLD_INDEX,
        key_address=WORLD_MAP_KEY_RUINS,
        orb_address=RARE_ORB_RUINS,
        connection=[
            WorldConnection(
                from_world_index=RUINS_WORLD_INDEX,
                to_world_index=BEACH_WORLD_INDEX
            ),
            WorldConnection(
                from_world_index=RUINS_WORLD_INDEX,
                to_world_index=CAVE_WORLD_INDEX,
                rule=beaten_boss_ruins
            )
        ]
    ),

    W.CAVE: WorldData(
        world_index=CAVE_WORLD_INDEX,
        key_address=WORLD_MAP_KEY_CAVE,
        orb_address=RARE_ORB_CAVE,
        connection=[
            WorldConnection(
                from_world_index=CAVE_WORLD_INDEX,
                to_world_index=RUINS_WORLD_INDEX
            ),
            WorldConnection(
                from_world_index=CAVE_WORLD_INDEX,
                to_world_index=FOREST_WORLD_INDEX,
                rule=beaten_boss_cave
            )
        ]
    ),

    W.FOREST: WorldData(
        world_index=FOREST_WORLD_INDEX,
        key_address=WORLD_MAP_KEY_FOREST,
        orb_address=RARE_ORB_FOREST,
        connection=[
            WorldConnection(
                from_world_index=FOREST_WORLD_INDEX,
                to_world_index=CAVE_WORLD_INDEX
            ),
            WorldConnection(
                from_world_index=FOREST_WORLD_INDEX,
                to_world_index=CLIFF_WORLD_INDEX,
                rule=beaten_boss_forest
            )
        ]
    ),

    W.CLIFF: WorldData(
        world_index=CLIFF_WORLD_INDEX,
        key_address=WORLD_MAP_KEY_CLIFF,
        orb_address=RARE_ORB_CLIFF,
        connection=[
            WorldConnection(
                from_world_index=CLIFF_WORLD_INDEX,
                to_world_index=FOREST_WORLD_INDEX
            ),
            WorldConnection(
                from_world_index=CLIFF_WORLD_INDEX,
                to_world_index=FACTORY_WORLD_INDEX,
                rule=beaten_boss_cliff
            )
        ]
    ),

    W.FACTORY: WorldData(
        world_index=FACTORY_WORLD_INDEX,
        key_address=WORLD_MAP_KEY_FACTORY,
        orb_address=RARE_ORB_FACTORY,
        connection=[
            WorldConnection(
                from_world_index=FACTORY_WORLD_INDEX,
                to_world_index=CLIFF_WORLD_INDEX
            ),
            WorldConnection(
                from_world_index=FACTORY_WORLD_INDEX,
                to_world_index=VOLCANO_WORLD_INDEX,
                rule=beaten_boss_factory
            )
        ]
    ),

    W.VOLCANO: WorldData(
        world_index=VOLCANO_WORLD_INDEX,
        key_address=WORLD_MAP_KEY_VOLCANO,
        orb_address=RARE_ORB_VOLCANO,
        connection=[
            WorldConnection(
                from_world_index=VOLCANO_WORLD_INDEX,
                to_world_index=FACTORY_WORLD_INDEX
            ),
            WorldConnection(
                from_world_index=VOLCANO_WORLD_INDEX,
                to_world_index=GOLDEN_TEMPLE_WORLD_INDEX,
                rule=beaten_boss_volcano
            )
        ]
    ),

    W.GOLDEN_TEMPLE: WorldData(
        world_index=GOLDEN_TEMPLE_WORLD_INDEX,
        key_address=None,
        orb_address=None,
        connection=[
            WorldConnection(
                from_world_index=GOLDEN_TEMPLE_WORLD_INDEX,
                to_world_index=VOLCANO_WORLD_INDEX
            ),
            WorldConnection(
                from_world_index=GOLDEN_TEMPLE_WORLD_INDEX,
                to_world_index=JUNGLE_WORLD_INDEX,
                rule=beaten_boss_volcano
            )
        ]
    ),
}
