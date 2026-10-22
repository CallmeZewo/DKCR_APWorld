from __future__ import annotations
from typing import TYPE_CHECKING

from ..data.constants import LevelName as Ln
from ..item_utils.dkcr_item import DKCRItem
from .dkcr_location import DKCRLocation

if TYPE_CHECKING:
    from ..world import DKCRWorld

def create_events(dkcr_world: DKCRWorld):
    dkcr_world.get_region(Ln.MUGLYS_MOUND).add_event(
        location_name=f"{Ln.MUGLYS_MOUND} event",
        item_name="Jungle boss beaten",
        location_type=DKCRLocation,
        item_type=DKCRItem
    )
    dkcr_world.get_region(Ln.PINCHIN_PIRATES).add_event(
        location_name=f"{Ln.PINCHIN_PIRATES} event",
        item_name="Beach boss beaten",
        location_type=DKCRLocation,
        item_type=DKCRItem
    )
    dkcr_world.get_region(Ln.RUINED_ROOST).add_event(
        location_name=f"{Ln.RUINED_ROOST} event",
        item_name="Ruins boss beaten",
        location_type=DKCRLocation,
        item_type=DKCRItem
    )
    dkcr_world.get_region(Ln.THE_MOLE_TRAIN).add_event(
        location_name=f"{Ln.THE_MOLE_TRAIN} event",
        item_name="Cave boss beaten",
        location_type=DKCRLocation,
        item_type=DKCRItem
    )
    dkcr_world.get_region(Ln.MANGORUBY_RUN).add_event(
        location_name=f"{Ln.MANGORUBY_RUN} event",
        item_name="Forest boss beaten",
        location_type=DKCRLocation,
        item_type=DKCRItem
    )
    dkcr_world.get_region(Ln.THUGLYS_HIGHRISE).add_event(
        location_name=f"{Ln.THUGLYS_HIGHRISE} event",
        item_name="Cliff boss beaten",
        location_type=DKCRLocation,
        item_type=DKCRItem
    )
    dkcr_world.get_region(Ln.FEATHER_FIEND).add_event(
        location_name=f"{Ln.FEATHER_FIEND} event",
        item_name="Factory boss beaten",
        location_type=DKCRLocation,
        item_type=DKCRItem
    )
    dkcr_world.get_region(Ln.TIKI_TONG_TERROR).add_event(
        location_name=f"{Ln.TIKI_TONG_TERROR} event",
        item_name="Volcano boss beaten",
        location_type=DKCRLocation,
        item_type=DKCRItem
    )