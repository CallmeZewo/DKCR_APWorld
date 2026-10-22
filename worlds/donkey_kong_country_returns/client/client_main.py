import asyncio

import colorama
import Utils
from CommonClient import server_loop, get_base_parser
from Utils import gui_enabled
from .dkcr_client import DKCRClient
from .dkcr_game import DKCRGame
from .dolphin import Dolphin
from .dkcr_context import DKCRContext


async def run_client(connect: str | None = None, password: str | None = None) -> None:
    ctx = DKCRContext(connect, password)
    dolphin = Dolphin()
    dkcr = DKCRGame(dolphin)
    client = DKCRClient(ctx, dkcr)

    ctx.server_task = asyncio.create_task(server_loop(ctx), name="ServerLoop")

    if gui_enabled:
        ctx.run_gui()

    ctx.run_cli()

    client_task = asyncio.create_task(
        client.run(ctx.exit_event),
        name="DKCRClient"
    )

    try:
        await ctx.exit_event.wait()
    finally:
        ctx.server_address = None

        await ctx.shutdown()

        if client_task:
            await client_task


def main(connect: str | None = None, password: str | None = None) -> None:
    Utils.init_logging("Donkey Kong Country Returns Client")
    colorama.init()
    asyncio.run(run_client(connect, password))


if __name__ == "__main__":
    parser = get_base_parser()
    args = parser.parse_args()
    main(args.connect, args.password)