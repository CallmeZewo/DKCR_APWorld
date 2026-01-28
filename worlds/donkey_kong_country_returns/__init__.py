from collections.abc import Mapping
from typing import Any

from worlds.AutoWorld import World

from worlds.donkey_kong_country_returns.DKCRNameConstants import Region as R

from worlds.LauncherComponents import components, Component, launch_subprocess, Type, SuffixIdentifier

from . import items, locations, regions, rules, web_world
from . import options as dkcr_options


def run_client() -> None:
    print("Running Donkey Kong Country Returns Client")
    from .DKCRClient import main

    launch_subprocess(main, name="DonkeyKongCountryReturnsClient")

components.append(
    Component(
        "Donkey Kong Country Returns Client",
        func=run_client,
        component_type=Type.CLIENT,
        file_identifier=SuffixIdentifier(".apdkcr"),
    )
)

class DKCRWorld(World):
    """
    Donkey Kong Country Returns is a Platform Collector
    Defeat the Tikis with your Pal Diddy Kong
    """

    game: str = "Donkey Kong Country Returns"
    patch_file_ending: str = ".apdkcr"

    web = web_world.DKCRWebWorld()

    options_dataclass = dkcr_options.DKCROptions
    options: dkcr_options.DKCROptions

    location_name_to_id = locations.LOCATION_NAME_TO_ID
    item_name_to_id = items.ITEM_NAME_TO_ID

    origin_region_name = R.JUNGLE

    def create_regions(self) -> None:
        regions.create_and_connect_regions(self)
        locations.create_all_locations(self)

    def set_rules(self) -> None:
        rules.set_all_rules(self)

    def create_items(self) -> None:
        items.create_all_items(self)

    def create_item(self, name: str) -> items.DKCRItem:
        return items.create_item_with_correct_classification(self, name)

    def get_filler_item_name(self) -> str:
        return items.get_random_filler_item_name(self)

    def fill_slot_data(self) -> Mapping[str, Any]:
        return self.options.as_dict(
            "golden_temple"
        )