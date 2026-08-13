from collections.abc import Mapping
from typing import Any

from worlds.AutoWorld import World

from worlds.donkey_kong_country_returns.DKCRNameConstants import Generic as G

from worlds.LauncherComponents import components, Component, launch_subprocess, Type, SuffixIdentifier, icon_paths

from . import items, locations, regions, rules, web_world
from . import options as dkcr_options

from Utils import visualize_regions

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
        icon="DKCRIcon"
    )
)
icon_paths["DKCRIcon"] = "ap:worlds.donkey_kong_country_returns/assets/DKCRClientIcon.png"

class DKCRWorld(World):
    """
    Donkey Kong Country Returns is a Platform Collector
    Defeat the Tikis with your Pal Diddy Kong
    """

    game: str = G.GAME_NAME
    patch_file_ending: str = ".apdkcr"

    web = web_world.DKCRWebWorld()

    options_dataclass = dkcr_options.DKCROptions
    options: dkcr_options.DKCROptions

    location_name_to_id = locations.LOCATION_NAME_TO_ID
    item_name_to_id = items.ITEM_NAME_TO_ID
    ut_can_gen_without_yaml = True
    origin_region_name = "Menu"
    def __init__(self):
        super().__init__(self.multiworld, self.player)
        self.selected_medals = set()

    @staticmethod
    def interpret_slot_data(slot_data: dict[str, Any]) -> dict[str, Any]:
        return slot_data

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
        slot_data = self.options.get_slot_data_dict()
        medals = {
            "Bronze": 0,
            "Silver": 0,
            "Gold": 0,
            "Shiny Gold": 0
        }
        for medal in self.selected_medals:
            medals[medal] = 1
        slot_data["time_attack_resolved"] = medals
        # visualize_regions(self.multiworld.get_region("Menu", self.player), f"Player{self.player}.puml", show_entrance_names=True, regions_to_highlight=self.multiworld.get_all_state(self.player).reachable_regions[self.player])
        return slot_data

    def generate_early(self) -> None:
        self.selected_medals = self.resolve_option_set_medals()
        dkcr_options.handle_ut_yamless(self, None)

    def resolve_option_set_medals(self) -> set[str]:
        available_medals = {"Bronze", "Silver", "Gold", "Shiny Gold"}
        values = self.options.time_attack_medal
        is_ut = getattr(self.multiworld, "generation_is_fake", False)
        if is_ut:
            return self.ut_medals
        if self.selected_medals:
            return self.selected_medals
        if "Full" in values:
            return available_medals

        for medal in available_medals:
            if medal in values:
                self.selected_medals.add(medal)
        if "RandomAll" in values or "RandomOne" in values:
            available_medals -= self.selected_medals

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
                    if self.random.choice([True, False]):
                        self.selected_medals.add(medal)

            elif "RandomOne" in values and available_medals:
                self.selected_medals.add(self.random.choice(list(available_medals)))

        return self.selected_medals
