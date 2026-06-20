import asyncio
import time
import traceback
from typing import TYPE_CHECKING, Any, Optional

import dolphin_memory_engine as dme
from dataclasses import dataclass

from dolphin_memory_engine import read_word

import Utils
from CommonClient import ClientCommandProcessor, CommonContext, get_base_parser, gui_enabled, logger, server_loop
from NetUtils import ClientStatus

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

CUSTOM_BASE = 0x93790000

@dataclass
class CustomRAM:
    base: int = CUSTOM_BASE

    MAGIC: int = 0
    VERSION: int = 0
    DEATH_LINK_FLAG: int = 0
    SIZE: int = 0

    def __post_init__(self):
        offset = 0
        self.MAGIC = self.base + offset; offset += 4
        self.VERSION = self.base + offset; offset += 4
        self.DEATH_LINK_FLAG = self.base + offset; offset += 4
        self.SIZE = offset

RAM = CustomRAM()

# Ingame Player Data #
DONKEY_KONG_CURRENT_HEALTH_ADDRESS = 0x8080dd8f
DIDDY_KONG_CURRENT_HEALTH_ADDRESS = 0x8080dd93

K_LETTER_ADDRESS = 0x8080dda7
O_LETTER_ADDRESS = 0x8080ddab
N_LETTER_ADDRESS = 0x8080ddaf
G_LETTER_ADDRESS = 0x8080ddb3

# World / Level Data

# Bosses = 1
# K Level = 0
# 7-R = 10

# Mirror Trap
#MIRROR_GRAPHICS_CODE = (0x800c2b4c, 0x800c2b50)
#MIRROR_ON = (0x60000000, 0x38600001)
#MIRROR_OFF = (0x4182000c, 0x38600000)

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
        self.CURRENT_LEVEL_ID = None
        self.CURRENT_WORLD_ID = None
        self.CURRENT_LEVELS_PUZZLE_PIECE_BITFIELD = None
        self.PUZZLE_PIECE_DICT: dict[tuple[int, int], tuple[int, bool]] = {}
        self.KONG_LETTER_DICT: dict[tuple[int, int], tuple[list[int], bool]] = {}

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

    def on_deathlink(self, data: dict[str, Any]) -> None:
        super().on_deathlink(data)
        _give_death(self)

    def make_gui(self) -> type["kvui.GameManager"]:
        ui = super().make_gui()
        ui.base_title = "Archipelago Donkey Kong Country Returns"
        return ui

def read_byte(console_address: int) -> int:
    return int.from_bytes(dme.read_byte(console_address), byteorder="big")

def write_byte(console_address: int, value: int) -> None:
    dme.write_byte(console_address, value.to_bytes(byteorder="big"))

def read_string(console_address: int) -> str:
    return dme.read_bytes(console_address, 0x40).split(b"\0", 1)[0].decode()

def write_string64(console_address: int, value: str) -> None:
    max_len = 64
    if "\0" in value:
        raise ValueError("string contains null byte")
    data = value.encode()[:max_len-1] + b'\0'
    data += b'\0' * (max_len - len(data))
    dme.write_bytes(console_address, data)

MAGIC_VALUE = 0x444b4352
VERSION_VALUE = 1

def init_custom_ram():
    dme.write_word(RAM.MAGIC, MAGIC_VALUE)
    dme.write_word(RAM.VERSION, VERSION_VALUE)

def is_custom_ram_valid() -> bool:
    try:
        return (
                dme.read_word(RAM.MAGIC) == 0x444b4352 and
                dme.read_word(RAM.VERSION) == 1
        )
    except RuntimeError:
        return False

def _give_death(ctx: DKCRContext) -> None:
    if (
        ctx.slot is not None
        and dme.is_hooked()
        and ctx.dolphin_status == CONNECTION_CONNECTED_STATUS
        and check_ingame()
    ):
        ctx.has_send_death = True
        write_byte(RAM.DEATH_LINK_FLAG, 1)

async def check_alive() -> bool:
    currentHealth = read_byte(DONKEY_KONG_CURRENT_HEALTH_ADDRESS)
    return currentHealth > 0 and check_ingame()

async def check_death(ctx: DKCRContext) -> None:
    if ctx.slot is not None and check_ingame():
        currentHealth = read_byte(DONKEY_KONG_CURRENT_HEALTH_ADDRESS)
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
        dme.read_bytes(0x80000000, 6)
    except RuntimeError:
        if dme.is_hooked():
            dme.un_hook()
        return False
    return True

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
                    if dme.read_bytes(0x80000000, 6) != b"SF8E01":
                        logger.info(CONNECTION_REFUSED_GAME_STATUS)
                        ctx.dolphin_status = CONNECTION_REFUSED_GAME_STATUS
                        dme.un_hook()
                        sleep_time = 5
                    else:
                        init_custom_ram()
                        if is_custom_ram_valid():
                            logger.info("Custom RAM successfully initialized")
                        else:
                            logger.info("Custom RAM failed to initialize, reconnecting to dolphin to try again...")
                            dme.un_hook()
                            continue
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