from __future__ import annotations
from typing import TYPE_CHECKING

from ..data.constants import ItemName as In

if TYPE_CHECKING:
    from ..world import DKCRWorld

filler_weights: dict[str, int] = {
    In.BALLOONX1.value: 5,
    In.BALLOONX3.value: 3,
    In.BALLOONX7.value: 1,
    In.BANANA.value: 25,
    In.BANANA_BUNCH.value: 20,
    In.BIG_BANANA_BUNCH.value: 10,
    In.BANANA_COIN.value: 15,
    In.RECOVERY_HEART.value: 20,
}

def generate_filler(filler_amount: int, dkcr_world: DKCRWorld):
    fillers = dkcr_world.random.choices(
        population=list(filler_weights.keys()),
        weights=list(filler_weights.values()),
        k=filler_amount
    )

    for filler in fillers:
        dkcr_world.multiworld.itempool.append(dkcr_world.create_item(filler))

def get_random_filler_item_name(dkcr_world: DKCRWorld):
    return dkcr_world.random.choices(
        population=list(filler_weights.keys()),
        weights=list(filler_weights.values()),
        k=1
    )