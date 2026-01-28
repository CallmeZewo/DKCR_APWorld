import asyncio
import time
import traceback
from typing import TYPE_CHECKING, Any, Optional

import dolphin_memory_engine as dme

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

# Custom DeathLink Flag
DEATH_LINK_FLAG = 0x81800010

# Player's slot name
SLOT_NAME_ADDRESS = 0x81810000

# Ingame Player Data #
DONKEY_KONG_CURRENT_HEALTH_ADDRESS = 0x8080dd8f
DIDDY_KONG_CURRENT_HEALTH_ADDRESS = 0x8080dd93

# IDK?????
OPEN_MENU_WHILE_IN_GAME_ADDRESS = 0x80617ecc

class DKCRCommandProcessor(ClientCommandProcessor):
    def __init__(self, ctx: CommonContext):
        super().__init__(ctx)

    def _cmd_dolphin(self) -> None:
        """
        Display the current Dolphin emulator connection status.
        """
        if isinstance(self.ctx, DKCRContext):
            logger.info(f"Dolphin Status: {self.ctx.dolphin_status}")

class DKCRContext(CommonContext):
    command_processor = DKCRCommandProcessor
    game: str = "Donkey Kong Country Returns"

    def __init__(self, server_address: Optional[str], password: Optional[str]) -> None:
        super().__init__(server_address, password)
        self.dolphin_sync_task: Optional[asyncio.Task[None]] = None
        self.dolphin_status: str = CONNECTION_INITIAL_STATUS
        self.awaiting_rom: bool = False
        self.has_send_death: bool = False

async def disconnect(self, allow_autoreconnect: bool = False) -> None:
    self.auth = None
    await super().disconnect(allow_autoreconnect)

async def server_auth(self, password_requested: bool = False) -> None:
    if password_requested and not self.password:
        await super().server_auth(password_requested)
    if not self.auth:
        if self.awaiting_rom:
            return
        self.awaiting_rom = True
        logger.info("Awaiting connection to Dolphin to get player information.")
        return
    await self.send_connection()

def on_package(self, cmd: str, args: dict[str, Any]) -> None:
    if cmd == "Connected":
        if "death_link" in args["slot_data"]:
            Utils.async_start(self.update_death_link(bool(args["slot_data"]["death_link"])))
    elif cmd == "Retrieved":
        requested_keys_dict = args["keys"]

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

def read_string(console_address: int, strlen: int) -> str:
    return dme.read_bytes(console_address, strlen).split(b"\0", 1)[0].decode()

def _give_death(ctx: DKCRContext) -> None:
    if (
        ctx.slot is not None
        and dme.is_hooked()
        and ctx.dolphin_status == CONNECTION_CONNECTED_STATUS
        and check_ingame()
    ):
        ctx.has_send_death = True
        write_byte(DEATH_LINK_FLAG, 1)

async def check_alive() -> bool:
    currentHealth = read_byte(DONKEY_KONG_CURRENT_HEALTH_ADDRESS)
    return currentHealth > 0 & check_ingame()

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

async def dolphin_sync_task(ctx: DKCRContext) -> None:
    logger.info("Starting Dolphin connector. Use /dolphin for status information.")
    sleep_time= 0.0
    while not ctx.exit_event_set():
        if sleep_time > 0.0:
            try:
                await asyncio.wait_for(ctx.watcher_event.wait(),sleep_time)
            except asyncio.TimeoutError:
                pass
            sleep_time = 0.0
        ctx.watcher_event.clear()

        try:
            if dme.is_hooked() and ctx.dolphin_status == CONNECTION_CONNECTED_STATUS:
                if not check_ingame():
                    # Reset the give item array while not in the game.
                    sleep_time = 0.1
                    continue
                if ctx.slot is not None:
                    if "DeathLink" in ctx.tags:
                        await check_death(ctx)
                else:
                    if not ctx.auth:
                        ctx.auth = read_string(SLOT_NAME_ADDRESS, strlen=0x40)
                    if ctx.awaiting_rom:
                        await ctx.server_auth()
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