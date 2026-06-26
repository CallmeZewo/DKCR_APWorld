import asyncio
import time
import traceback
from typing import TYPE_CHECKING, Any, Optional

import dolphin_memory_engine as dme
from dataclasses import dataclass

import Utils
from CommonClient import ClientCommandProcessor, CommonContext, get_base_parser, gui_enabled, logger, server_loop
from NetUtils import ClientStatus

from .data.addresses import *
from .data.level_data import Levels
import utils

if TYPE_CHECKING:
    import kvui

CONNECTION_REFUSED_GAME_STATUS = \
    "Dolphin failed to connect. Please load a randomized ROM for 'Donkey Kong Country Returns'. Trying again in 5 seconds..."

CONNECTION_REFUSED_SAVED_STATUS = \
    "Dolphin failed to connect. Please load into the save file. Trying again in 5 seconds..."

CONNECTION_LOST_STATUS = \
    "Dolphin connection was lost. Please restart your emulator and make sure Donkey Kong Country Returns is running."

CONNECTION_CONNECTED_STATUS = "Dolphin connected successfully."
CONNECTION_INITIAL_STATUS = "Dolphin connection has not been initiated."

WorldNameToIndex: dict[str, int] = {
    "Beach": 0x00,
    "Cave": 0x01,
    "Cliff": 0x02,
    "Factory": 0x03,
    "Forest": 0x04,
    "Jungle": 0x05,
    "Ruins": 0x06,
    "Volcano": 0x07,
    "Golden Temple World": 0x08,
}

WorldIndexToName: dict[int, str] = {
    0x00: "Beach",
    0x01: "Cave",
    0x02: "Cliff",
    0x03: "Factory",
    0x04: "Forest",
    0x05: "Jungle",
    0x06: "Ruins",
    0x07: "Volcano",
    0x08: "Golden Temple World",
}

WorldIDToReal: dict[int, int] = {
    0x05: 1,
    0x00: 2,
    0x06: 3,
    0x01: 4,
    0x04: 5,
    0x02: 6,
    0x03: 7,
    0x07: 8,
    0x08: 9,
}


# CUSTOM_BASE = 0x93790000

# @dataclass
# class CustomRAM:
#     base: int = CUSTOM_BASE
#
#     MAGIC: int = 0
#     VERSION: int = 0
#     DEATH_LINK_FLAG: int = 0
#     SIZE: int = 0
#
#     def __post_init__(self):
#         offset = 0
#         self.MAGIC = self.base + offset; offset += 4
#         self.VERSION = self.base + offset; offset += 4
#         self.DEATH_LINK_FLAG = self.base + offset; offset += 4
#         self.SIZE = offset
#
# RAM = CustomRAM()

class DKCRCommandProcessor(ClientCommandProcessor):
    def __init__(self, ctx: CommonContext):
        super().__init__(ctx)

    def _cmd_dolphin(self) -> None:
        """
        Display the current Dolphin emulator connection status.
        """
        if isinstance(self.ctx, DKCRContext):
            logger.info(f"Dolphin Status: {self.ctx.dolphin_status}")

    #def _cmd_mirror(self) -> None:
    #    """
    #    Mirrors the Graphics of the Game
    #    """
    #    if isinstance(self.ctx, DKCRContext):
    #        dme.write_word(MIRROR_GRAPHICS_CODE[0], MIRROR_ON[0])
    #        dme.write_word(MIRROR_GRAPHICS_CODE[1], MIRROR_ON[1])

class DKCRContext(CommonContext):
    command_processor = DKCRCommandProcessor
    game: str = "Donkey Kong Country Returns"

    def __init__(self, server_address: Optional[str], password: Optional[str]) -> None:
        super().__init__(server_address, password)
        self.items_handling: int = 3
        self.dolphin_sync_task: Optional[asyncio.Task[None]] = None
        self.dolphin_status: str = CONNECTION_INITIAL_STATUS
        self.has_send_death: bool = False
        self.last_letters: list[int] = []
        self.last_puzzle_field_dict = {}
        self.exited_level = True

    async def disconnect(self, allow_autoreconnect: bool = False) -> None:
        self.auth = None
        await super().disconnect(allow_autoreconnect)

    async def server_auth(self, password_requested: bool = False):
        if password_requested and not self.password:
            await super().server_auth(password_requested)
        await self.get_username()
        await self.send_connect()

    async def get_username(self):
        if not self.auth:
            self.auth = self.username
            if not self.auth:
                logger.info('Enter slot name:')
                self.auth = await self.console_input()

    def on_package(self, cmd: str, args: dict[str, Any]) -> None:
        if cmd == "Connected":
            slot_data = args.get("slot_data")
            if slot_data is None:
                return

            if slot_data.get("death_link") is not None:
                Utils.async_start(self.update_death_link(bool(args["slot_data"]["death_link"])))

        elif cmd == "Retrieved":
            requested_keys_dict = args.get("keys", {})

    # def on_deathlink(self, data: dict[str, Any]) -> None:
    #     super().on_deathlink(data)
    #     _give_death(self)

    def make_gui(self) -> type["kvui.GameManager"]:
        ui = super().make_gui()
        ui.base_title = "Archipelago Donkey Kong Country Returns"
        return ui

def read_string(console_address: int) -> str:
    return dme.read_bytes(console_address, 0x40).split(b"\0", 1)[0].decode()

def write_string64(console_address: int, value: str) -> None:
    max_len = 64
    if "\0" in value:
        raise ValueError("string contains null byte")
    data = value.encode()[:max_len-1] + b'\0'
    data += b'\0' * (max_len - len(data))
    dme.write_bytes(console_address, data)

# MAGIC_VALUE = 0x444b4352
# VERSION_VALUE = 1
#
# def init_custom_ram():
#     dme.write_word(RAM.MAGIC, MAGIC_VALUE)
#     dme.write_word(RAM.VERSION, VERSION_VALUE)

# def is_custom_ram_valid() -> bool:
#     try:
#         return (
#                 dme.read_word(RAM.MAGIC) == 0x444b4352 and
#                 dme.read_word(RAM.VERSION) == 1
#         )
#     except RuntimeError:
#         return False

# def _give_death(ctx: DKCRContext) -> None:
#     if (
#         ctx.slot is not None
#         and dme.is_hooked()
#         and ctx.dolphin_status == CONNECTION_CONNECTED_STATUS
#         and check_ingame()
#     ):
#         ctx.has_send_death = True
#         write_byte(RAM.DEATH_LINK_FLAG, 1)

async def check_alive() -> bool:
    currentHealth = dme.read_byte(DK_HEALTH)
    return currentHealth > 0 and check_ingame()

async def check_death(ctx: DKCRContext) -> None:
    if ctx.slot is not None and check_ingame():
        currentHealth = dme.read_byte(DK_HEALTH)
        if currentHealth <= 0:
            if not ctx.has_send_death and time.time() >= ctx.last_death_link + 3:
                ctx.has_send_death = True
                await ctx.send_death(ctx.player_names[ctx.slot] + " ran out of hearts.")
        else:
            ctx.has_send_death = False

def check_ingame() -> bool:
    return True

def check_inrom() -> bool:
    try:
        dme.read_bytes(MEM, 6)
    except RuntimeError:
        if dme.is_hooked():
            dme.un_hook()
        return False
    return True

# def get_level_data():
#     game_state = int.from_bytes(dme.read_bytes(MEM + GAME_STATE, 4), byteorder="big")
#     if game_state == 0x03 or game_state == 0x01:
#         level_data_address = int.from_bytes(dme.read_bytes(MEM + LEVEL_DATA_POINTER, 4), byteorder="big")
#         for Level in Levels.values():
#             ptr = Level.pointer
#             cur_level_address = level_data_address + ptr
#             flags = dme.read_byte(cur_level_address + 0x3e)
#             flags |= 0b10000000
#             dme.write_byte(cur_level_address, flags)

def check_puzzle_piece(ctx: DKCRContext, levelID: int, worldID: int):
    bit = dme.read_word(dme.read_word(dme.read_word(0x80820144) + 0x34))

    if levelID not in ctx.last_puzzle_field_dict:
        ctx.last_puzzle_field_dict[levelID] = bit
        return 0

    last = ctx.last_puzzle_field_dict.get(levelID, 0)

    new_bits = bit & ~last

    ctx.last_puzzle_field_dict[levelID] = bit

    if new_bits == 0:
        return 0

    changed_bit = new_bits & -new_bits

    pos = 1
    temp = changed_bit

    while temp > 1:
        temp >>= 1
        pos += 1

    if levelID == 0x00:
        levelID = 13

    return 10000 * WorldIDToReal[worldID] + 100 * (levelID - 1) + pos

def check_letters(ctx: DKCRContext, levelID: int, worldID: int):
    if levelID == 0x00 or levelID == 0x01:
        return 0
    LETTER_IDS = [20, 21, 22, 23]
    CurrentLetters = [
        dme.read_byte(K_LETTER + MEM),
        dme.read_byte(O_LETTER + MEM),
        dme.read_byte(N_LETTER + MEM),
        dme.read_byte(G_LETTER + MEM),
    ]

    if ctx.last_letters == CurrentLetters:
        return 0

    if not ctx.last_letters:
        ctx.last_letters = CurrentLetters
        return 0

    changed = 0
    for i in range(len(LETTER_IDS)):
        if ctx.last_letters[i] == 0 and CurrentLetters[i] == 1:
            changed = LETTER_IDS[i]

    ctx.last_letters = CurrentLetters

    return 10000 * WorldIDToReal[worldID] + 100 * (levelID - 1) + changed

def check_level_clear(ctx: DKCRContext):
    returning = []
    main_level_data_ptr = int.from_bytes(dme.read_bytes(LEVEL_DATA_POINTER + MEM, 4), byteorder="big")
    for name, data in Levels.items():
        if data.index != int.from_bytes(dme.read_bytes(CURRENT_LEVEL, 4), "big"):
            if data.world_name != int.from_bytes(dme.read_bytes(WORLD_OF_CURRENT_LEVEL, 4), "big"):
                continue
        level_data = int.from_bytes(dme.read_bytes(data.pointer + main_level_data_ptr, 4), byteorder="big")
        flags = dme.read_byte(level_data + 0x3e)
        print(flags)
        if flags & 0x40:
            world = WorldIDToReal[WorldNameToIndex[data.world_name]]
            level = data.index
            if level == 0x01:
                level = 12
            if level == 0x00:
                level = 13
            returning.append(10000 * world + (level - 1) * 100 + 30)

        if flags & 0x10:
            world = WorldIDToReal[WorldNameToIndex[data.world_name]]
            level = data.index
            if level == 0x00:
                level = 13
            returning.append(10000 * world + (level - 1) * 100 + 10)

        if flags & 0x08:
            world = WorldIDToReal[WorldNameToIndex[data.world_name]]
            level = data.index
            returning.append(10000 * world + (level - 1) * 100 + 24)
    if not returning:
        return 0
    return returning



async def dolphin_sync_task(ctx: DKCRContext) -> None:
    logger.info("Starting Dolphin connector. Use /dolphin for status information.")
    sleep_time = 0.0
    while not ctx.exit_event.is_set():
        if sleep_time > 0.0:
            try:
                await asyncio.wait_for(ctx.watcher_event.wait(),sleep_time)
            except asyncio.TimeoutError:
                pass
            sleep_time = 0.0
        ctx.watcher_event.clear()
        try:
            if dme.is_hooked() and ctx.dolphin_status == CONNECTION_CONNECTED_STATUS:
                if not check_inrom():
                    # Reset the give item array while not in the game.
                    sleep_time = 0.1
                    continue
                if ctx.slot is not None:
                    # Loop
                    game_state = utils.get_game_state()
                    if (game_state == 0x1 or game_state == 0x3) and ctx.exited_level:
                        ctx.exited_level = False
                        loc_id = check_level_clear(ctx)
                        if loc_id != 0:
                            await ctx.check_locations(loc_id)
                    if game_state == 0x0:
                        ctx.exited_level = True
                        current_level_index = int.from_bytes(dme.read_bytes(MEM + CURRENT_LEVEL, 4), byteorder="big")
                        current_world_index = int.from_bytes(dme.read_bytes(MEM + WORLD_OF_CURRENT_LEVEL, 4), byteorder="big")
                        for name, data in Levels.items():
                            if data.world_name == WorldIndexToName[current_world_index] and data.index == current_level_index:
                                loc_id = check_letters(ctx, data.index, current_world_index)
                                if loc_id > 0:
                                    await ctx.check_locations([loc_id])
                                loc_id = check_puzzle_piece(ctx, data.index, current_world_index)
                                if loc_id > 0:
                                    await ctx.check_locations([loc_id])
                    if "DeathLink" in ctx.tags:
                        await check_death(ctx)
                sleep_time = 0.1
            else:
                if ctx.dolphin_status == CONNECTION_CONNECTED_STATUS:
                    logger.info("Connection to Dolphin lost, reconnecting...")
                    ctx.dolphin_status = CONNECTION_LOST_STATUS
                logger.info("Attempting to connect to Dolphin...")
                dme.hook()
                if dme.is_hooked():
                    if dme.read_bytes(MEM + GAME_ID, 6) != b"SF8E01" and dme.read_byte(MEM + REV_NUMBER) != 0x01:
                        logger.info(CONNECTION_REFUSED_GAME_STATUS)
                        ctx.dolphin_status = CONNECTION_REFUSED_GAME_STATUS
                        dme.un_hook()
                        sleep_time = 5
                    else:
                        logger.info(CONNECTION_CONNECTED_STATUS)
                        ctx.dolphin_status = CONNECTION_CONNECTED_STATUS
                        ctx.locations_checked = set()
                else:
                    logger.info("Connection to Dolphin failed, attempting again in 5 seconds...")
                    ctx.dolphin_status = CONNECTION_LOST_STATUS
                    await ctx.disconnect()
                    sleep_time = 5
                    continue
        except Exception:
            dme.un_hook()
            logger.info("Connection to Dolphin failed, attempting again in 5 seconds...")
            logger.error(traceback.format_exc())
            ctx.dolphin_status = CONNECTION_LOST_STATUS
            await ctx.disconnect()
            sleep_time = 5
            continue

def main(connect: Optional[str] = None, password: Optional[str] = None) -> None:
    Utils.init_logging("Donkey Kong Country Returns Client")

    async def _main(connect: Optional[str], password: Optional[str]) -> None:
        ctx = DKCRContext(connect, password)
        ctx.server_task = asyncio.create_task(server_loop(ctx), name="ServerLoop")
        if gui_enabled:
            ctx.run_gui()
        ctx.run_cli()
        await asyncio.sleep(1)

        ctx.dolphin_sync_task = asyncio.create_task(dolphin_sync_task(ctx), name="DolphinSync")

        await ctx.exit_event.wait()
        # Wake the sync task, if it is currently sleeping, so it can start shutting down when it sees that the
        # exit_event is set.
        ctx.watcher_event.set()
        ctx.server_address = None

        await ctx.shutdown()

        if ctx.dolphin_sync_task:
            await ctx.dolphin_sync_task

    import colorama

    colorama.init()
    asyncio.run(_main(connect, password))

if __name__ == "__main__":
    parser = get_base_parser()
    args = parser.parse_args()
    main(args.connect, args.password)