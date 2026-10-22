def get_base_location_address(level: tuple[int, int]) -> int:
    return level[0] * 0x10000 + level[1] * 0x100