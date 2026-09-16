from collections.abc import Mapping
from typing import Any

from Utils import visualize_regions
from worlds.AutoWorld import World
from worlds.LauncherComponents import components, Component, launch_subprocess, Type, SuffixIdentifier, icon_paths
from . import web_world
from .option_utils import options as dkcr_options
from .data.constants import Generic as G
from .item_utils import generate_item_name_to_id, create_item_with_correct_classification, generate_all_items, get_random_filler_item_name
from .item_utils.dkcr_item import DKCRItem
from .location_utils import generate_all_locations
from .option_utils.validate_options import validate_options
from .rule_utils import resolve_medals, resolve_level_clear_types, set_completion_condition
from .region_utils import setup_regions


def run_client() -> None:
    print("Running Donkey Kong Country Returns Client")
    from .DKCRClient import main

    launch_subprocess(main, name="DonkeyKongCountryReturnsClient")


components.append(
    Component(
        "[DKCR USA 1.1] Donkey Kong Country Returns Client",
        func=run_client,
        component_type=Type.CLIENT,
        icon="DKCRIcon"
    )
)
icon_paths["DKCRIcon"] = "ap:worlds.donkey_kong_country_returns/assets/DKCRClientIcon.png"


class DKCRWorld(World):
    """
    Donkey Kong Country Returns is a 2.5D Platform Collector.
    Take back the banans that the Tiki's stole from you with the help of your pal Diddy Kong.
    Travel across your island fighting off one Tiki after another.
    What will you find at the end?
    """

    game: str = G.GAME_NAME.value
    patch_file_ending: str = ".apdkcr"

    web = web_world.DKCRWebWorld()

    options_dataclass = dkcr_options.DKCROptions
    options: dkcr_options.DKCROptions

    location_name_to_id = generate_all_locations()
    item_name_to_id = generate_item_name_to_id()
    ut_can_gen_without_yaml = True
    origin_region_name = "Jungle"

    def __init__(self, multiworld, player):
        super().__init__(multiworld, player)
        self.selected_medals = set()
        self.selected_clear_types = set()


    @staticmethod
    def interpret_slot_data(slot_data: dict[str, Any]) -> dict[str, Any]:
        return slot_data

    def generate_early(self) -> None:
        dkcr_options.handle_ut_yamless(self, None)
        self.selected_medals: set = resolve_medals(self)
        self.selected_clear_types: set = resolve_level_clear_types(self)
        validate_options(self)

    def create_regions(self) -> None:
        setup_regions(self)

    def create_items(self) -> None:
        generate_all_items(self)

    def set_rules(self) -> None:
        set_completion_condition(self)

    def create_item(self, name: str) -> DKCRItem:
        return create_item_with_correct_classification(self, name)

    def get_filler_item_name(self) -> str:
        return get_random_filler_item_name(self)

    def fill_slot_data(self) -> Mapping[str, Any]:
        slot_data = self.options.get_slot_data_dict()
        medals = {
            "Bronze": 0,
            "Silver": 0,
            "Gold": 0,
            "Shiny Gold": 0
        }
        clear_types = {
            "Normal": 0,
            "Time Attack": 0,
            "Mirror Mode": 0,
        }
        for medal in self.selected_medals:
            medals[medal] = 1
        slot_data["time_attack_resolved"] = medals
        for clear_type in self.selected_clear_types:
            clear_types[clear_type] = 1
        slot_data["level_clear_type_resolved"] = clear_types

        visualize_regions(self.multiworld.get_region(self.origin_region_name, self.player), f"Player{self.player}.puml",
                          show_entrance_names=True,
                          regions_to_highlight=self.multiworld.get_all_state(self.player).reachable_regions[
                              self.player])

        return slot_data

