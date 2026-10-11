async def check_letters(base_location_address: int, letters: list[int]):
    locations_to_send: set[int] = set()

    if letters[0] == 0x1:
        locations_to_send.add(base_location_address + 0x11)
    if letters[1] == 0x1:
        locations_to_send.add(base_location_address + 0x12)
    if letters[2] == 0x1:
        locations_to_send.add(base_location_address + 0x13)
    if letters[3] == 0x1:
        locations_to_send.add(base_location_address + 0x14)

    return locations_to_send