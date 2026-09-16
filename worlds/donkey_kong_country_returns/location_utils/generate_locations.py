from rule_builder.field_resolvers import FromOption
from ..data.constants import (
    PPIndex as Pi,
    KongLetterIndex as Kli,
    ClearTypeIndex as Cti,
    LocationName as Ln,
    SpecialIndex as Si,
    LevelIndex as Li,
    KONG_LETTER_MAPPING as KLM,
    CLEAR_LOCATION_MAPPING as CLM
)
from ..data.levels import GameLevels
from ..data.worlds import GameWorlds
from ..utils import get_base_address


def generate_all_locations() -> dict[str, int]:
    location_name_to_id: dict[str, int] = {}
    for world in GameWorlds:
        if world.world_index != GameWorlds.GOLDEN_TEMPLE_WORLD.world_index:
            location_name_to_id.update(generate_world_location(world))
        for level in world.level_list.values():
            location_name_to_id.update(generate_level_location(world, level))
    return location_name_to_id


def generate_world_location(world: GameWorlds) -> dict[str, int]:
    base_address = get_base_address(world=world)
    world_location_gen: dict[str, int] = {
        f"{world.display_name} {Ln.PUZZLE_BUNDLE.value}":
            base_address + Pi.PUZZLE_PIECE_BUNDLE,

        f"{world.display_name} {Ln.KONG_BUNDLE.value}":
            base_address + Kli.KONG_LETTER_BUNDLE,

        f"{world.display_name} {Ln.CLEARED.value}":
            base_address + Cti.CLEARED,

        f"{world.display_name} {Ln.CLEARED_MIRROR.value}":
            base_address + Cti.CLEARED_MIRROR,

        f"{world.display_name} {Ln.CLEARED_TIME_ATTACK_BRONZE.value}":
            base_address + Cti.CLEARED_TIME_ATTACK_BRONZE,

        f"{world.display_name} {Ln.CLEARED_TIME_ATTACK_SILVER.value}":
            base_address + Cti.CLEARED_TIME_ATTACK_SILVER,

        f"{world.display_name} {Ln.CLEARED_TIME_ATTACK_GOLD.value}":
            base_address + Cti.CLEARED_TIME_ATTACK_GOLD,

        f"{world.display_name} {Ln.CLEARED_TIME_ATTACK_SHINY_GOLD.value}":
            base_address + Cti.CLEARED_TIME_ATTACK_SHINY_GOLD
    }
    return world_location_gen


def generate_level_location(world: GameWorlds, level: GameLevels) -> dict[str, int]:
    level_location_gen: dict[str, int] = {}
    base_address = get_base_address(level=level, world=world)
    for i in range(1, level.pp_amount + 1):
        level_location_gen[
            f"{level.display_name} {Ln.PUZZLE_PIECE.value} ({i})"
        ] = base_address + Pi.PUZZLE_PIECE_BASE + i

    if level.has_kong_letters:
        for letter, offset in KLM:
            level_location_gen[
                f"{level.display_name} {letter.value}"
            ] = base_address + offset

    if level.level_index == Li.SHOP_LEVEL_INDEX:
        level_location_gen[
            f"{level.display_name} {Ln.KEY}"
        ] = base_address + Si.SHOP_KEY
        return level_location_gen

    if level.level_index == Li.LIFT_OFF_LAUNCH_LEVEL_INDEX:
        level_location_gen[
            f"{level.display_name} {Ln.CLEARED}"
        ] = base_address + Cti.CLEARED
        return level_location_gen

    if level.display_name != GameLevels.GOLDEN_TEMPLE.display_name and level.level_index == Li.K_LEVEL_INDEX:
        level_location_gen[
            f"{level.display_name} {Ln.RARE_ORB}"
        ] = base_address + Si.RARE_ORB

    if level.display_name == GameLevels.GOLDEN_TEMPLE.display_name:
        level_location_gen[
            f"{level.display_name} {Ln.MIRROR_MODE_UNLOCK}"
        ] = base_address + Si.MIRROR_MODE_UNLOCK

    for loc_name, offset in CLM:
        level_location_gen[
            f"{level.display_name} {loc_name}"
        ] = base_address + offset

    return level_location_gen
