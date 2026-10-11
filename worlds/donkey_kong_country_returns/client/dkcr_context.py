from win32event import CancelWaitableTimer

from CommonClient import CommonContext, logger

from .dkcr_command_processor import DKCRCommandProcessor
from .dkcr_game_manager import create_game_manager

class DKCRContext(CommonContext):
    game = "Donkey Kong Country Returns"
    command_processor = DKCRCommandProcessor
    items_handling = 0b111

    def __init__(
        self,
        server_address: str | None = None,
        password: str | None = None,
    ) -> None:
        super().__init__(server_address, password)

        self.last_received_item_index: int = 0

    def make_gui(self) -> "type[kvui.GameManager]":
        return create_game_manager(super().make_gui())

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

    async def on_package(self, cmd: str, args: dict) -> None:
        if cmd == "Connected":
            slot_data = args.get("slot_data")
            if slot_data is None:
                return

    async def send_msg(self, cmd: str, key: str, default, operation: list[dict], want_reply: bool = False):
        await self.send_msgs([{
            "cmd": cmd,
            "key": key,
            "default": default,
            "want_reply": want_reply,
            "operations": operation
        }])