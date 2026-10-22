from enum import IntEnum

class State(IntEnum):
    IN_LEVEL = 0x0
    WORLD_MAP = 0x1
    QUIT_GAME_OVER = 0x2
    WORLD_MAP_AFTER_QUIT = 0x3
    TITLE = 0x4
    SUPER_GUIDE = 0x5
    TIME_ATTACK = 0x6