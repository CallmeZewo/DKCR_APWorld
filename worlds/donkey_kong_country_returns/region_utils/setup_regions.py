from __future__ import annotations

from typing import TYPE_CHECKING, Mapping

from . import generate_all_regions, connect_all_regions, fill_all_regions
from ..location_utils.event_locations import create_events
from ..location_utils.create_location_rules import create_location_rules

if TYPE_CHECKING:
    from . import DKCRWorld

def setup_regions(dkcr_world: DKCRWorld) -> None:
    generate_all_regions(dkcr_world)
    create_events(dkcr_world)
    connect_all_regions(dkcr_world)
    fill_all_regions(dkcr_world)
    create_location_rules(dkcr_world)
