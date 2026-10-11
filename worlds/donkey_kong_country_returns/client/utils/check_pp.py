async def check_pp(base_location_address: int, pp_field: int) -> set[int]:
    locations_to_send: set[int] = set()

    if pp_field & 0x1:
        locations_to_send.add(base_location_address + 0x1)
    if pp_field & 0x2:
        locations_to_send.add(base_location_address + 0x2)
    if pp_field & 0x4:
        locations_to_send.add(base_location_address + 0x3)
    if pp_field & 0x8:
        locations_to_send.add(base_location_address + 0x4)
    if pp_field & 0x10:
        locations_to_send.add(base_location_address + 0x5)
    if pp_field & 0x20:
        locations_to_send.add(base_location_address + 0x6)
    if pp_field & 0x40:
        locations_to_send.add(base_location_address + 0x7)
    if pp_field & 0x80:
        locations_to_send.add(base_location_address + 0x8)
    if pp_field & 0x100:
        locations_to_send.add(base_location_address + 0x9)

    return locations_to_send
