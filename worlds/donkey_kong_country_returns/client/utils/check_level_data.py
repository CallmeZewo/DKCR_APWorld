from ...data import LevelData


async def check_level_data(base_location_address: int, level_data: LevelData):
    locations_to_send: set[int] = set()

    if level_data.level_cleared:
        locations_to_send.add(base_location_address + 0x21)
    if level_data.mirror_mode_cleared:
        locations_to_send.add(base_location_address + 0x22)
    if level_data.kong_collected:
        locations_to_send.add(base_location_address + 0x1A)
    if level_data.all_puzzle_pieces_collected:
        locations_to_send.add(base_location_address + 0xA)

    return locations_to_send