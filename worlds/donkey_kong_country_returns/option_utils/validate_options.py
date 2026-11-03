from __future__ import annotations
from typing import TYPE_CHECKING

from Options import OptionError

if TYPE_CHECKING:
    from worlds.donkey_kong_country_returns import DKCRWorld

def validate_options(dkcr_world: DKCRWorld):
    options = dkcr_world.options

    if not dkcr_world.selected_clear_types:
        raise OptionError(f"There should be at least one level clear type selected in your yaml.")

    if options.level_clear_type.value in ["Time", "Time Attack"]:
        if "Bronze" or "Silver" or "Gold" or "Shiny Gold" not in dkcr_world.selected_medals:
            raise OptionError(f"The level clear type 'Time Attack' does not work without the 'Time Attack Medal' option.")

    if options.puzzle_pieces.value == 0 and options.kong_letter.value == 0 and options.puzzle_piece_amount > 50 and options.puzzle_pieces_unlock_bosses.value == 1:
        raise OptionError(f"Its not recommended to put more than 50 as the value of 'Puzzle Piece Amount' if both the Puzzle Piece and Kong Letter Locations are turned off while using Puzzle Pieces as the unlock method for Bosses.")

    if options.puzzle_pieces.value == 0 and options.kong_letter.value == 0 and options.kong_letter_unlock_k_level.value == 1:
        if (options.jungle_kong_letter_amount.value +
            options.beach_kong_letter_amount.value +
            options.ruins_kong_letter_amount.value +
            options.cave_kong_letter_amount.value +
            options.forest_kong_letter_amount.value +
            options.cliff_kong_letter_amount.value +
            options.factory_kong_letter_amount.value +
            options.volcano_kong_letter_amount.value > 50
        ):
            raise OptionError(f"Its not recommended to put more than 50 as the combined value of 'Kong Letter Amount [K Level]' if both the Puzzle Piece and Kong Letter Locations are turned off while using Kong Letter as the unlock method for K Level.")
