from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..world import DKCRWorld


def resolve_medals(dkcr_world: DKCRWorld) -> set[str]:
    available_medals = {"Bronze", "Silver", "Gold", "Shiny Gold"}
    values = dkcr_world.options.time_attack_medal.value
    is_ut = getattr(dkcr_world.multiworld, "generation_is_fake", False)
    if is_ut:
        return dkcr_world.ut_medals
    if dkcr_world.selected_medals:
        return dkcr_world.selected_medals
    if "Full" in values:
        return available_medals

    for medal in available_medals:
        if medal in values:
            dkcr_world.selected_medals.add(medal)
    if "RandomAll" in values or "RandomOne" in values:
        available_medals -= dkcr_world.selected_medals

        exclusions = {
            "Bronzeless": "Bronze",
            "Silverless": "Silver",
            "Goldless": "Gold",
            "Shiny Goldless": "Shiny Gold",
        }

        for option, medal in exclusions.items():
            if option in values:
                available_medals.discard(medal)

        if "RandomAll" in values:
            for medal in available_medals:
                if dkcr_world.random.choice([True, False]):
                    dkcr_world.selected_medals.add(medal)

        elif "RandomOne" in values and available_medals:
            dkcr_world.selected_medals.add(dkcr_world.random.choice(list(available_medals)))

    return dkcr_world.selected_medals

def resolve_level_clear_types(dkcr_world: DKCRWorld) -> set[str]:
    available_clear_types = {"Normal", "Time Attack", "Mirror Mode"}
    values = dkcr_world.options.level_clear_type.value
    is_ut = getattr(dkcr_world.multiworld, "generation_is_fake", False)
    if is_ut:
        return dkcr_world.ut_level_clear_types
    if dkcr_world.selected_clear_types:
        return dkcr_world.selected_clear_types
    if "Full" in values:
        return available_clear_types

    for clear_type in available_clear_types:
        if clear_type in values:
            dkcr_world.selected_clear_types.add(clear_type)
        elif "Time" in values:
            dkcr_world.selected_clear_types.add("Time Attack")
        elif "Mirror" in values:
            dkcr_world.selected_clear_types.add("Mirror Mode")
    if "RandomAll" in values or "RandomOne" in values:
        available_clear_types -= dkcr_world.selected_clear_types

        exclusions = {
            "Normalless": "Normal",
            "Time Attackless": "Time Attack",
            "Timeless": "Time Attack",
            "Mirror Modeless": "Mirror Mode",
            "Mirrorless": "Mirror Mode",
        }

        for option, clear_type in exclusions.items():
            if option in values:
                available_clear_types.discard(clear_type)

        if "RandomAll" in values:
            for clear_type in available_clear_types:
                if dkcr_world.random.choice([True, False]):
                    dkcr_world.selected_clear_types.add(clear_type)

        elif "RandomOne" in values and available_clear_types:
            dkcr_world.selected_clear_types.add(dkcr_world.random.choice(list(available_clear_types)))

    if not dkcr_world.selected_medals and "Time Attack" in dkcr_world.selected_clear_types:
        dkcr_world.selected_clear_types.remove("Time Attack")

    return dkcr_world.selected_clear_types