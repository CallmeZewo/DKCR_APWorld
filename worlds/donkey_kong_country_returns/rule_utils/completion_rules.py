from __future__ import annotations
from typing import TYPE_CHECKING

from .boss_rules import can_enter_tiki_tong_terror
from .world_rules import can_enter_golden_temple

if TYPE_CHECKING:
    from worlds.donkey_kong_country_returns import DKCRWorld


def set_completion_condition(dkcr_world: DKCRWorld):
    if dkcr_world.options.goal.value == 0:
        dkcr_world.set_completion_rule(can_enter_tiki_tong_terror())
        return
    if dkcr_world.options.goal.value == 1:
        dkcr_world.set_completion_rule(can_enter_golden_temple())
        return