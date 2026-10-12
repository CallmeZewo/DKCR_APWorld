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

        self.rare_orbs_option: int = 0
        self.smog_clear_option: int = 0
        self.lift_off_launch_option: int = 0
        self.factory_buttons_option: int = 0
        self.level_clear_type_option: dict[str, int] = {}
        self.k_level_option: int = 0
        self.puzzle_pieces_option: int = 0
        self.world_puzzle_piece_bundle_option: int = 0
        self.world_kong_letter_bundle_option: int = 0
        self.world_cleared_option: int = 0
        self.world_cleared_mirror_option: int = 0
        self.world_cleared_time_attack_option: int = 0
        self.mirror_mode_shards_option: int = 0
        self.squawks_option: int = 0
        self.sunset_shore_key_option: int = 0
        self.blowhole_bound_key_option: int = 0
        self.damp_dungeon_key_option: int = 0
        self.mole_patrol_key_option: int = 0
        self.springy_spores_key_option: int = 0
        self.precarious_plateau_key_option: int = 0
        self.handy_hazards_key_option: int = 0
        self.smokey_peak_key_option: int = 0
        self.jungle_boss_access_option: int = 0
        self.beach_boss_access_option: int = 0
        self.ruins_boss_access_option: int = 0
        self.cave_boss_access_option: int = 0
        self.forest_boss_access_option: int = 0
        self.cliff_boss_access_option: int = 0
        self.factory_boss_access_option: int = 0
        self.volcano_boss_access_option: int = 0
        self.jungle_k_level_access_option: int = 0
        self.beach_k_level_access_option: int = 0
        self.ruins_k_level_access_option: int = 0
        self.cave_k_level_access_option: int = 0
        self.forest_k_level_access_option: int = 0
        self.cliff_k_level_access_option: int = 0
        self.factory_k_level_access_option: int = 0
        self.volcano_k_level_access_option: int = 0
        self.time_attack_resolved_option: dict[str, int] = {}

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

    def on_package(self, cmd: str, args: dict) -> None:
        if cmd == "Connected":
            slot_data = args.get("slot_data")
            if slot_data is None:
                return
            self.rare_orbs_option = slot_data.get("rare_orbs")
            self.smog_clear_option = slot_data.get("smog_clear")
            self.lift_off_launch_option = slot_data.get("lift_off_launch")
            self.factory_buttons_option = slot_data.get("factory_buttons")
            self.level_clear_type_option: dict[str, int] = slot_data.get("level_clear_type")
            self.k_level_option = slot_data.get("k_level")
            self.puzzle_pieces_option = slot_data.get("puzzle_pieces")
            self.world_puzzle_piece_bundle_option = slot_data.get("world_puzzle_piece_bundle")
            self.world_kong_letter_bundle_option = slot_data.get("world_kong_letter_bundle")
            self.world_cleared_option = slot_data.get("world_cleared")
            self.world_cleared_mirror_option = slot_data.get("world_cleared_mirror")
            self.world_cleared_time_attack_option = slot_data.get("world_cleared_time_attack")
            self.mirror_mode_shards_option = slot_data.get("mirror_mode_shards")
            self.squawks_option = slot_data.get("squawks")
            self.sunset_shore_key_option = slot_data.get("sunset_shore_key")
            self.blowhole_bound_key_option = slot_data.get("blowhole_bound_key")
            self.damp_dungeon_key_option = slot_data.get("damp_dungeon_key")
            self.mole_patrol_key_option = slot_data.get("mole_patrol_key")
            self.springy_spores_key_option = slot_data.get("springy_spores_key")
            self.precarious_plateau_key_option = slot_data.get("precarious_plateau_key")
            self.handy_hazards_key_option = slot_data.get("handy_hazards_key")
            self.smokey_peak_key_option = slot_data.get("smokey_peak_key")
            self.jungle_boss_access_option = slot_data.get("jungle_boss_access")
            self.beach_boss_access_option = slot_data.get("beach_boss_access")
            self.ruins_boss_access_option = slot_data.get("ruins_boss_access")
            self.cave_boss_access_option = slot_data.get("cave_boss_access")
            self.forest_boss_access_option = slot_data.get("forest_boss_access")
            self.cliff_boss_access_option = slot_data.get("cliff_boss_access")
            self.factory_boss_access_option = slot_data.get("factory_boss_access")
            self.volcano_boss_access_option = slot_data.get("volcano_boss_access")
            self.jungle_k_level_access_option = slot_data.get("jungle_k_level_access")
            self.beach_k_level_access_option = slot_data.get("beach_k_level_access")
            self.ruins_k_level_access_option = slot_data.get("ruins_k_level_access")
            self.cave_k_level_access_option = slot_data.get("cave_k_level_access")
            self.forest_k_level_access_option = slot_data.get("forest_k_level_access")
            self.cliff_k_level_access_option = slot_data.get("cliff_k_level_access")
            self.factory_k_level_access_option = slot_data.get("factory_k_level_access")
            self.volcano_k_level_access_option = slot_data.get("volcano_k_level_access")
            self.time_attack_resolved_option: dict[str, int] = slot_data.get("time_attack_resolved")


    async def send_msg(self, cmd: str, key: str, default, operation: list[dict], want_reply: bool = False):
        await self.send_msgs([{
            "cmd": cmd,
            "key": key,
            "default": default,
            "want_reply": want_reply,
            "operations": operation
        }])