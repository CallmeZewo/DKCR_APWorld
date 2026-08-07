import asyncio
import time
import traceback
from typing import Optional

import NetUtils
import Utils
import worlds.donkey_kong_country_returns.locations
from CommonClient import ClientCommandProcessor, CommonContext, get_base_parser, gui_enabled, logger, server_loop
from .items import ITEM_NAME_TO_ID
from .data.level_data import Levels
from .rules import *
from .utils import *
from .items import item_table
from .DKCRNameConstants import Dolphin as D

if TYPE_CHECKING:
    import kvui

class DKCRCommandProcessor(ClientCommandProcessor):
    def __init__(self, ctx: CommonContext):
        super().__init__(ctx)

    def _cmd_dolphin(self) -> None:
        """
        Display the current Dolphin emulator connection status.
        """
        if isinstance(self.ctx, DKCRContext):
            logger.info(f"Dolphin Status: {self.ctx.dolphin_status}")

    def _cmd_squawks(self) -> None:
        """
        Toggling Squawks once you unlocked him.
        """
        if isinstance(self.ctx, DKCRContext):
            self.ctx.toggle_squawks()

    def _cmd_kong_letter_amount(self, world: str = ""):
        """
        Check the amount of kong letters you have in the given world.
        [jungle, beach, ruins, cave, forest, cliff, factory, volcano]
        """
        if not isinstance(self.ctx, DKCRContext):
            return
        if world is "":
            self.output("please specify a world")
        amount = None
        match world:
            case "jungle":
                amount = self.ctx.kong_letter_amount_dict.get("jungle")
            case "beach":
                amount = self.ctx.kong_letter_amount_dict.get("beach")
            case "ruins":
                amount = self.ctx.kong_letter_amount_dict.get("ruins")
            case "cave":
                amount = self.ctx.kong_letter_amount_dict.get("cave")
            case "forest":
                amount = self.ctx.kong_letter_amount_dict.get("forest")
            case "cliff":
                amount = self.ctx.kong_letter_amount_dict.get("cliff")
            case "factory":
                amount = self.ctx.kong_letter_amount_dict.get("factory")
            case "volcano":
                amount = self.ctx.kong_letter_amount_dict.get("volcano")

        if amount is None:
            amount = 0

        logger.info(f"You have currently {amount} Kong Letter/s in {world}.")

    # def _cmd_mirror(self) -> None:
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
        self.items_handling: int = 0b111
        self.dolphin_sync_task: Optional[asyncio.Task[None]] = None
        self.dolphin_status: str = D.CONNECTION_INITIAL_STATUS
        self.has_send_death: bool = False
        self.exited_level = True
        self.has_squawks = False
        self.squawks_option = 0
        self.squawks_state = 1
        self.last_bitfield = (-1, -1)
        self.last_received_item_index = 0
        self.current_puzzle_piece_amount = 0
        self.current_mirror_shard_amount = 0
        self.mirror_mode_shards_option = 0
        self.factory_button_option = 0
        self.factory_smog_option = 0
        self.factory_lift_off_launch_option = 0
        self.valid_medals: dict[str, int] = {}
        self.keys_option: dict[str, int] = {}
        self.kong_letter_amount_dict: dict[str, int] = {
            "jungle": 0,
            "beach": 0,
            "ruins": 0,
            "cave": 0,
            "forest": 0,
            "cliff": 0,
            "factory": 0,
            "volcano": 0,
        }
        self.boss_access_req_dict: dict[str, int] = {
            "jungle": 0,
            "beach": 0,
            "ruins": 0,
            "cave": 0,
            "forest": 0,
            "cliff": 0,
            "factory": 0,
            "volcano": 0,
        }
        self.k_level_access_req_dict: dict[str, int] = {
            "jungle": 0,
            "beach": 0,
            "ruins": 0,
            "cave": 0,
            "forest": 0,
            "cliff": 0,
            "factory": 0,
            "volcano": 0,
        }




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
            self.clear_ram()
            self.squawks_option = slot_data.get("squawks")
            self.has_squawks = slot_data.get("has_squawks") if not None else False
            self.mirror_mode_shards_option = slot_data.get("mirror_mode_shards")
            self.factory_button_option = slot_data.get("factory_buttons")
            self.factory_smog_option = slot_data.get("smog_clear")
            self.factory_lift_off_launch_option = slot_data.get("lift_off_launch")
            self.kong_letter_amount_dict: dict[str, int] = {
                "jungle": slot_data.get("current_kong_letter_amount_jungle_gotten") if not None else 0,
                "beach": slot_data.get("current_kong_letter_amount_beach_gotten") if not None else 0,
                "ruins": slot_data.get("current_kong_letter_amount_ruins_gotten") if not None else 0,
                "cave": slot_data.get("current_kong_letter_amount_cave_gotten") if not None else 0,
                "forest": slot_data.get("current_kong_letter_amount_forest_gotten") if not None else 0,
                "cliff": slot_data.get("current_kong_letter_amount_cliff_gotten") if not None else 0,
                "factory": slot_data.get("current_kong_letter_amount_factory_gotten") if not None else 0,
                "volcano": slot_data.get("current_kong_letter_amount_volcano_gotten") if not None else 0,
            }
            self.boss_access_req_dict: dict[str, int] = {
                "jungle": slot_data["jungle_boss_access"],
                "beach": slot_data["beach_boss_access"],
                "ruins": slot_data["ruins_boss_access"],
                "cave": slot_data["cave_boss_access"],
                "forest": slot_data["forest_boss_access"],
                "cliff": slot_data["cliff_boss_access"],
                "factory": slot_data["factory_boss_access"],
                "volcano": slot_data["volcano_boss_access"],
            }
            self.k_level_access_req_dict: dict[str, int] = {
                "jungle": slot_data["jungle_k_level_access"],
                "beach": slot_data["beach_k_level_access"],
                "ruins": slot_data["ruins_k_level_access"],
                "cave": slot_data["cave_k_level_access"],
                "forest": slot_data["forest_k_level_access"],
                "cliff": slot_data["cliff_k_level_access"],
                "factory": slot_data["factory_k_level_access"],
                "volcano": slot_data["volcano_k_level_access"],
            }
            self.valid_medals = slot_data["time_attack_resolved"]
            self.keys_option = {
                "jungle": slot_data["sunset_shore_key"],
                "beach": slot_data["blowhole_bound_key"],
                "ruins": slot_data["damp_dungeon_key"],
                "cave": slot_data["mole_patrol_key"],
                "forest": slot_data["springy_spores_key"],
                "cliff": slot_data["precarious_plateau_key"],
                "factory": slot_data["handy_hazards_key"],
                "volcano": slot_data["smokey_peak_key"],
            }
            self.make_level_bitflag()
            if slot_data.get("death_link") is not None:
                Utils.async_start(self.update_death_link(bool(args["slot_data"]["death_link"])))

        elif cmd == "Retrieved":
            requested_keys_dict = args.get("keys", {})

        elif cmd == "ReceivedItems":
            index = args.get("index")
            items = args.get("items")
            print(index, items)

    # def on_deathlink(self, data: dict[str, Any]) -> None:
    #     super().on_deathlink(data)
    #     _give_death(self)

    def make_gui(self) -> type["kvui.GameManager"]:
        ui = super().make_gui()
        ui.base_title = "Archipelago Donkey Kong Country Returns"
        return ui

    async def give_dk_items(self):
        last_recv_item_idx = dme.read_word(CUSTOM_LAST_ITEM_INDEX_ADDR)
        if len(self.items_received) == last_recv_item_idx:
            return

        self.last_received_item_index = last_recv_item_idx
        recv_items = self.items_received[last_recv_item_idx:]
        for item in recv_items:
            last_recv_item_idx += 1
            item_name = self.item_names.lookup_in_game(item.item)
            dk_item = ITEM_NAME_TO_ID[item_name]

            if dk_item == item_table[I.PUZZLE_PIECE].code:
                await self.update_pp_data()
                await self.add_pp_amount_saved()

            if dk_item == item_table[I.Kong_Letter.KONG_LETTER_JUNGLE].code:
                await self.update_kong_letter_data("jungle")
                await self.add_kong_letter_amount_saved(JGL_KL_OFFSET)
            if dk_item == item_table[I.Kong_Letter.KONG_LETTER_BEACH].code:
                await self.update_kong_letter_data("beach")
                await self.add_kong_letter_amount_saved(BCH_KL_OFFSET)
            if dk_item == item_table[I.Kong_Letter.KONG_LETTER_RUINS].code:
                await self.update_kong_letter_data("ruins")
                await self.add_kong_letter_amount_saved(RNS_KL_OFFSET)
            if dk_item == item_table[I.Kong_Letter.KONG_LETTER_CAVE].code:
                await self.update_kong_letter_data("cave")
                await self.add_kong_letter_amount_saved(CVE_KL_OFFSET)
            if dk_item == item_table[I.Kong_Letter.KONG_LETTER_FOREST].code:
                await self.update_kong_letter_data("forest")
                await self.add_kong_letter_amount_saved(FRS_KL_OFFSET)
            if dk_item == item_table[I.Kong_Letter.KONG_LETTER_CLIFF].code:
                await self.update_kong_letter_data("cliff")
                await self.add_kong_letter_amount_saved(CLF_KL_OFFSET)
            if dk_item == item_table[I.Kong_Letter.KONG_LETTER_FACTORY].code:
                await self.update_kong_letter_data("factory")
                await self.add_kong_letter_amount_saved(FCT_KL_OFFSET)
            if dk_item == item_table[I.Kong_Letter.KONG_LETTER_VOLCANO].code:
                await self.update_kong_letter_data("volcano")
                await self.add_kong_letter_amount_saved(VLC_KL_OFFSET)

            if dk_item == item_table[I.Rare_Orb.GREEN_ORB_JUNGLE].code:
                await self.update_rare_orb_data("jungle")
                await self.add_rare_orb_collected_saved("jungle")
            if dk_item == item_table[I.Rare_Orb.BLUE_ORB_BEACH].code:
                await self.update_rare_orb_data("beach")
                await self.add_rare_orb_collected_saved("beach")
            if dk_item == item_table[I.Rare_Orb.WHITE_ORB_RUINS].code:
                await self.update_rare_orb_data("ruins")
                await self.add_rare_orb_collected_saved("ruins")
            if dk_item == item_table[I.Rare_Orb.MAGENTA_ORB_CAVE].code:
                await self.update_rare_orb_data("cave")
                await self.add_rare_orb_collected_saved("cave")
            if dk_item == item_table[I.Rare_Orb.ORANGE_ORB_CLIFF].code:
                await self.update_rare_orb_data("cliff")
                await self.add_rare_orb_collected_saved("cliff")
            if dk_item == item_table[I.Rare_Orb.YELLOW_ORB_FOREST].code:
                await self.update_rare_orb_data("forest")
                await self.add_rare_orb_collected_saved("forest")
            if dk_item == item_table[I.Rare_Orb.GRAY_ORB_FACTORY].code:
                await self.update_rare_orb_data("factory")
                await self.add_rare_orb_collected_saved("factory")
            if dk_item == item_table[I.Rare_Orb.RED_ORB_VOLCANO].code:
                await self.update_rare_orb_data("volcano")
                await self.add_rare_orb_collected_saved("volcano")

            if dk_item == item_table[I.Key.JUNGLE_KEY].code:
                await self.update_key_data("jungle")
                await self.add_key_collected_saved("jungle")
            if dk_item == item_table[I.Key.Beach_KEY].code:
                await self.update_key_data("beach")
                await self.add_key_collected_saved("beach")
            if dk_item == item_table[I.Key.Ruins_KEY].code:
                await self.update_key_data("ruins")
                await self.add_key_collected_saved("ruins")
            if dk_item == item_table[I.Key.CAVE_KEY].code:
                await self.update_key_data("cave")
                await self.add_key_collected_saved("cave")
            if dk_item == item_table[I.Key.FOREST_KEY].code:
                await self.update_key_data("forest")
                await self.add_key_collected_saved("forest")
            if dk_item == item_table[I.Key.CLIFF_KEY].code:
                await self.update_key_data("cliff")
                await self.add_key_collected_saved("cliff")
            if dk_item == item_table[I.Key.FACTORY_KEY].code:
                await self.update_key_data("factory")
                await self.add_key_collected_saved("factory")
            if dk_item == item_table[I.Key.VOLCANO_KEY].code:
                await self.update_key_data("volcano")
                await self.add_key_collected_saved("volcano")

            if dk_item == item_table[I.PROGRESSIVE_FACTORY_BUTTON].code:
                await self.add_factory_button()
            if dk_item == item_table[I.Unlockables.MIRROR_SHARD].code:
                await self.add_mirror_shard()
            if dk_item == item_table[I.Unlockables.MIRROR_MODE].code:
                await self.add_mirror_shard()
            if dk_item == item_table[I.Shop.SQUAWKS].code:
                await self.handle_squawks()

            elif dk_item == item_table[I.BANANA].code:
                await self.add_bananas(1)
            elif dk_item == item_table[I.BANANA_BUNCH].code:
                await self.add_bananas(10)
            elif dk_item == item_table[I.BIG_BANANA_BUNCH].code:
                await self.add_bananas(25)
            elif dk_item == item_table[I.BANANA_COIN].code:
                await  self.add_banana_coins(1)
            elif dk_item == item_table[I.BALLOONX1].code:
                await self.add_extra_lives(1)
            elif dk_item == item_table[I.BALLOONX3].code:
                await self.add_extra_lives(3)
            elif dk_item == item_table[I.BALLOONX7].code:
                await self.add_extra_lives(7)
            elif dk_item == item_table[I.RECOVERY_HEART].code:
                await self.add_recovery_heart()

        await self.update_recv_idx(last_recv_item_idx)
        self.make_level_bitflag()

    async def update_recv_idx(self, last_idx: int):
        self.last_received_item_index = last_idx
        dme.write_word(CUSTOM_LAST_ITEM_INDEX_ADDR, last_idx)


    async def update_pp_data(self):
        await self.send_msgs([{
            "cmd": "Set",
            "key": "current_puzzle_piece_amount_gotten",
            "default": 0,
            "want_reply": False,
            "operations": [{"operation": "add", "value": 1}]
        }])

    async def update_kong_letter_data(self, world: str):
        await self.send_msgs([{
            "cmd": "Set",
            "key": f"current_kong_letter_amount_{world}_gotten",
            "default": 0,
            "want_reply": False,
            "operations": [{"operation": "add", "value": 1}]
        }])

    async def update_rare_orb_data(self, world: str):
        await self.send_msgs([{
            "cmd": "Set",
            "key": f"rare_orb_{world}_gotten",
            "default": False,
            "want_reply": False,
            "operations": [{"operation": "replace", "value": True}]
        }])

    async def update_key_data(self, world: str):
        await self.send_msgs([{
            "cmd": "Set",
            "key": f"key_{world}_gotten",
            "default": False,
            "want_reply": False,
            "operations": [{"operation": "replace", "value": True}]
        }])

    async def update_key_local_flag(self, flag):
        await self.send_msgs([{
            "cmd": "Set",
            "key": f"key_local_flag",
            "default": False,
            "want_reply": False,
            "operations": [{"operation": "replace", "value": flag}]
        }])

    async def update_squawks(self, value):
        await self.send_msgs([{
            "cmd": "Set",
            "key": f"has_squawks",
            "default": False,
            "want_reply": False,
            "operations": [{"operation": "replace", "value": value}]
        }])

    async def add_bananas(self, amount: int):
        current_bananas = dme.read_word(BANANAS)
        new_amount = current_bananas + amount
        extra_lives_to_get = 0
        while new_amount >= 100:
            new_amount -= 100
            extra_lives_to_get += 1

        dme.write_word(BANANAS, new_amount)

        if extra_lives_to_get > 0:
            await self.add_extra_lives(extra_lives_to_get)

    async def add_banana_coins(self, amount: int):
        current_coins = dme.read_word(BANANA_COINS)
        new_amount = current_coins + amount
        if new_amount > 999:
            new_amount = 999

        dme.write_word(BANANA_COINS, new_amount)

    async def add_extra_lives(self, amount: int):
        current_extra_lives = dme.read_word(LIVES)
        new_amount = current_extra_lives + amount
        if new_amount > 99:
            new_amount = 99

        dme.write_word(LIVES, new_amount)

    async def add_recovery_heart(self):
        current_health_dk = dme.read_word(MEM + DK_HEALTH)
        current_health_dd = dme.read_word(MEM + DIDDY_HEALTH)
        if 0 < current_health_dk < 2:
            dme.write_word(MEM + DK_HEALTH, 2)
            return
        if 0 < current_health_dd < 2:
            dme.write_word(MEM + DIDDY_HEALTH, 2)
            return

    async def add_pp_amount_saved(self):
        pp = dme.read_word(CUSTOM_PP_AMOUNT_ADDR)
        dme.write_word(CUSTOM_PP_AMOUNT_ADDR, pp + 1)

    async def add_kong_letter_amount_saved(self, world_offset: int):
        kong_letter_save = dme.read_byte(CUSTOM_KL_AMOUNT_ADDR + world_offset) + 1
        match world_offset:
            case 0x0:
                if kong_letter_save >= self.k_level_access_req_dict["jungle"]:
                    try:
                        dme.write_byte(CUSTOM_KL_AMOUNT_ADDR + world_offset, 0xFF)
                    except:
                        pass
                    return
            case 0x1:
                if kong_letter_save >= self.k_level_access_req_dict["beach"]:
                    try:
                        dme.write_byte(CUSTOM_KL_AMOUNT_ADDR + world_offset, 0xFF)
                    except:
                        pass
                    return
            case 0x2:
                if kong_letter_save >= self.k_level_access_req_dict["ruins"]:
                    try:
                        dme.write_byte(CUSTOM_KL_AMOUNT_ADDR + world_offset, 0xFF)
                    except:
                        pass
                    return
            case 0x3:
                if kong_letter_save >= self.k_level_access_req_dict["cave"]:
                    try:
                        dme.write_byte(CUSTOM_KL_AMOUNT_ADDR + world_offset, 0xFF)
                    except:
                        pass
                    return
            case 0x4:
                if kong_letter_save >= self.k_level_access_req_dict["forest"]:
                    try:
                        dme.write_byte(CUSTOM_KL_AMOUNT_ADDR + world_offset, 0xFF)
                    except:
                        pass
                    return
            case 0x5:
                if kong_letter_save >= self.k_level_access_req_dict["cliff"]:
                    try:
                        dme.write_byte(CUSTOM_KL_AMOUNT_ADDR + world_offset, 0xFF)
                    except:
                        pass
                    return
            case 0x6:
                if kong_letter_save >= self.k_level_access_req_dict["factory"]:
                    try:
                        dme.write_byte(CUSTOM_KL_AMOUNT_ADDR + world_offset, 0xFF)
                    except:
                        pass
                    return
            case 0x7:
                if kong_letter_save >= self.k_level_access_req_dict["volcano"]:
                    try:
                        dme.write_byte(CUSTOM_KL_AMOUNT_ADDR + world_offset, 0xFF)
                    except:
                        pass
                    return
        dme.write_byte(CUSTOM_KL_AMOUNT_ADDR + world_offset, kong_letter_save)

    async def add_rare_orb_collected_saved(self, world: str):
        bit = CUSTOM_ORB_BITS.get(world)
        if bit is None:
            return

        current = dme.read_word(CUSTOM_ORB_BITFLAG_ADDR)

        if not (current & bit):
            dme.write_word(CUSTOM_ORB_BITFLAG_ADDR, current | bit)

    async def add_key_collected_saved(self, world: str):
        bit = CUSTOM_KEY_BITS.get(world)
        if bit is None:
            return

        current = dme.read_word(CUSTOM_KEY_BITFLAG_ADDR)

        if not (current & bit):
            dme.write_word(CUSTOM_KEY_BITFLAG_ADDR, current | bit)

    async def add_mirror_shard(self):
        new_shard_amount = dme.read_word(CUSTOM_MIRROR_SHARD_ADDR) + 1
        dme.write_word(CUSTOM_MIRROR_SHARD_ADDR, new_shard_amount)

    async def add_factory_button(self):
        new_button_amount = dme.read_word(CUSTOM_FACTORY_BUTTON_ADDR) + 1
        dme.write_word(CUSTOM_FACTORY_BUTTON_ADDR, new_button_amount)

    def toggle_squawks(self):
        if self.squawks_option == 0 or self.has_squawks:
            self.squawks_state = 1 if self.squawks_state == 0 else 0

    def check_squawks(self):
        dme.write_word(SQUAWKS, self.squawks_state)

    def make_level_bitflag(self):
        flag = 0

        for level, bit in level_bitflags.items():
            enabled = self.should_enable(level)

            if enabled:
                flag |= (1 << bit)

        flag_bytes = flag.to_bytes(10, "big")
        dme.write_bytes(CUSTOM_LEVEL_BITFLAG_ADDR, flag_bytes)

    def should_enable(self, level: str):
        match level:
            case L.PLATFORM_PANIC:
                if dme.read_byte(CUSTOM_KL_AMOUNT_ADDR + JGL_KL_OFFSET) == 0xFF:
                    return True
            case L.MUGLYS_MOUND:
                if dme.read_word(CUSTOM_PP_AMOUNT_ADDR) >= self.boss_access_req_dict["jungle"]:
                    return True
            case L.JUNGLE_HIJINXS:
                return True
            case L.KING_OF_CLING:
                return True
            case L.TREE_TOP_BOP:
                return True
            case L.SUNSET_SHORE:
                if dme.read_word(CUSTOM_KEY_BITFLAG_ADDR) & CUSTOM_KEY_BITS["jungle"] or self.keys_option["jungle"] == 0:
                    return True
            case L.CANOPY_CANNONS:
                return True
            case L.CRAZY_CART:
                return True
            case L.JUNGLE_SHOP:
                return True
            case L.TUMBLIN_TEMPLE:
                if dme.read_byte(CUSTOM_KL_AMOUNT_ADDR + BCH_KL_OFFSET) == 0xFF:
                    return True
            case L.PINCHIN_PIRATES:
                if dme.read_word(CUSTOM_PP_AMOUNT_ADDR) >= self.boss_access_req_dict["beach"]:
                    return True
            case L.POPPIN_PLANKS:
                return True
            case L.SLOPPY_SANDS:
                return True
            case L.PEACEFUL_PIER:
                return True
            case L.CANNON_CLUSTER:
                return True
            case L.STORMY_SHORE:
                return True
            case L.BLOWHOLE_BOUND:
                if dme.read_word(CUSTOM_KEY_BITFLAG_ADDR) & CUSTOM_KEY_BITS["beach"] or self.keys_option["beach"] == 0:
                    return True
            case L.TIDAL_TERROR:
                return True
            case L.BEACH_SHOP:
                return True
            case L.SHIFTY_SMASHERS:
                if dme.read_byte(CUSTOM_KL_AMOUNT_ADDR + RNS_KL_OFFSET) == 0xFF:
                    return True
            case L.RUINED_ROOST:
                if dme.read_word(CUSTOM_PP_AMOUNT_ADDR) >= self.boss_access_req_dict["ruins"]:
                    return True
            case L.WONKY_WATERWAY:
                return True
            case L.BUTTON_BASH:
                return True
            case L.MAST_BLAST:
                return True
            case L.DAMP_DUNGEON:
                if dme.read_word(CUSTOM_KEY_BITFLAG_ADDR) & CUSTOM_KEY_BITS["ruins"] or self.keys_option["ruins"] == 0:
                    return True
            case L.ITTY_BITTY_BITERS:
                return True
            case L.TEMPLE_TOPPLE:
                return True
            case L.RUINS_SHOP:
                return True
            case L.JAGGED_JEWELS:
                if dme.read_byte(CUSTOM_KL_AMOUNT_ADDR + CVE_KL_OFFSET) == 0xFF:
                    return True
            case L.THE_MOLE_TRAIN:
                if dme.read_word(CUSTOM_PP_AMOUNT_ADDR) >= self.boss_access_req_dict["cave"]:
                    return True
            case L.RICKETY_RAILS:
                return True
            case L.GRIP_N_TRIP:
                return True
            case L.BOMBS_AWAY:
                return True
            case L.MOLE_PATROL:
                if dme.read_word(CUSTOM_KEY_BITFLAG_ADDR) & CUSTOM_KEY_BITS["cave"] or self.keys_option["cave"] == 0:
                    return True
            case L.CROWDED_CAVERN:
                return True
            case L.CAVE_SHOP:
                return True
            case L.BLAST_N_BOUNCE:
                if dme.read_byte(CUSTOM_KL_AMOUNT_ADDR + FRS_KL_OFFSET) == 0xFF:
                    return True
            case L.MANGORUBY_RUN:
                if dme.read_word(CUSTOM_PP_AMOUNT_ADDR) >= self.boss_access_req_dict["forest"]:
                    return True
            case L.VINE_VALLEY:
                return True
            case L.CLINGY_SWINGY:
                return True
            case L.FLUTTER_FLYAWAY:
                return True
            case L.TIPPIN_TOTEMS:
                return True
            case L.LONGSHOT_LAUNCH:
                return True
            case L.SPRINGY_SPORES:
                if dme.read_word(CUSTOM_KEY_BITFLAG_ADDR) & CUSTOM_KEY_BITS["forest"] or self.keys_option["forest"] == 0:
                    return True
            case L.WIGGLEVINE_WONDERS:
                if dme.read_word(CUSTOM_KEY_BITFLAG_ADDR) & CUSTOM_KEY_BITS["forest"]:
                    return True
            case L.MUNCHER_MARATHON:
                return True
            case L.FOREST_SHOP:
                return True
            case L.PERILOUS_PASSAGE:
                if dme.read_byte(CUSTOM_KL_AMOUNT_ADDR + CLF_KL_OFFSET) == 0xFF:
                    return True
            case L.THUGLYS_HIGHRISE:
                if dme.read_word(CUSTOM_PP_AMOUNT_ADDR) >= self.boss_access_req_dict["cliff"]:
                    return True
            case L.STICKY_SITUATION:
                return True
            case L.PREHISTORIC_PATH:
                return True
            case L.WEIGHTY_WAY:
                return True
            case L.BOULDER_ROLLER:
                return True
            case L.PRECARIOUS_PLATEAU:
                if dme.read_word(CUSTOM_KEY_BITFLAG_ADDR) & CUSTOM_KEY_BITS["cliff"] or self.keys_option["cliff"] == 0:
                    return True
            case L.CRUMBLE_CANYON:
                return True
            case L.TIPPY_SHIPPY:
                return True
            case L.CLIFFTOP_CLIMB:
                return True
            case L.CLIFF_SHOP:
                return True
            case L.TREACHEROUS_TRACK:
                if dme.read_byte(CUSTOM_KL_AMOUNT_ADDR + FCT_KL_OFFSET) == 0xFF:
                    return True
            case L.FEATHER_FIEND:
                if dme.read_word(CUSTOM_PP_AMOUNT_ADDR) >= self.boss_access_req_dict["factory"]:
                    if self.factory_lift_off_launch_option == 0:
                        return True
                    elif self.factory_lift_off_launch_option == 1 and self.check_level_cleared(LIFT_OFF_LAUNCH_POINTER):
                        return True
            case L.FOGGY_FUMES:
                return True
            case L.SLAMMIN_STEEL:
                if self.factory_smog_option == 0:
                    return True
                elif self.factory_smog_option == 1 and self.check_level_cleared(FOGGY_FUMES_POINTER):
                    return True
            case L.HANDY_HAZARDS:
                if dme.read_word(CUSTOM_KEY_BITFLAG_ADDR) & CUSTOM_KEY_BITS["factory"] or self.keys_option["factory"] == 0:
                    return True
            case L.GEAR_GETAWAY:
                return True
            case L.COG_JOG:
                return True
            case L.SWITCHEROO:
                return True
            case L.MUSIC_MADNESS:
                return True
            case L.LIFT_OFF_LAUNCH:
                if dme.read_word(CUSTOM_FACTORY_BUTTON_ADDR) >= self.factory_button_option:
                    return True
            case L.FACTORY_SHOP:
                return True
            case L.FIVE_MONKEY_TRIAL:
                if dme.read_byte(CUSTOM_KL_AMOUNT_ADDR + VLC_KL_OFFSET) == 0xFF:
                    return True
            case L.TIKI_TONG_TERROR:
                if dme.read_word(CUSTOM_PP_AMOUNT_ADDR) >= self.boss_access_req_dict["volcano"]:
                    return True
            case L.FURIOUS_FIRE:
                return True
            case L.HOT_ROCKET:
                return True
            case L.ROASTING_RAILS:
                return True
            case L.SMOKEY_PEAK:
                if dme.read_word(CUSTOM_KEY_BITFLAG_ADDR) & CUSTOM_KEY_BITS["volcano"] or self.keys_option["volcano"] == 0:
                    return True
            case L.BOBBING_BASALT:
                return True
            case L.MOVING_MELTERS:
                return True
            case L.RED_RED_RISING:
                return True
            case L.VOLCANO_SHOP:
                return True
            case L.GOLDEN_TEMPLE:
                return False
        return False

    async def check_puzzle_piece(self, levelID: int, worldID: int):
        bitfield = None
        for _ in range(10):
            try:
                ptr1 = dme.read_word(0x80820144)
                ptr2 = dme.read_word(ptr1 + 0x34)
                bitfield = dme.read_word(ptr2)
                break
            except Exception:
                await asyncio.sleep(0.01)
        if bitfield is None:
            return []

        if bitfield == getattr(self, "last_bitfield", None):
            return []

        self.last_bitfield = bitfield

        found_pieces = []
        bits = bitfield

        while bits:
            lsb = bits & -bits
            piece_id = lsb.bit_length()

            found_pieces.append(0x10000 * worldID + 0x100 * levelID + piece_id)

            bits ^= lsb

        return found_pieces

    async def check_letters(self, levelID: int, worldID: int):
        if levelID == K_LEVEL_INDEX or levelID == BOSS_LEVEL_INDEX:
            return []
        letter_ids = [KONG_LETTER_K, KONG_LETTER_O, KONG_LETTER_N, KONG_LETTER_G]
        current_letters = [
            dme.read_byte(K_LETTER + MEM),
            dme.read_byte(O_LETTER + MEM),
            dme.read_byte(N_LETTER + MEM),
            dme.read_byte(G_LETTER + MEM),
        ]

        found_letters = []

        for current, letter_id in zip(current_letters, letter_ids):
            if current == 1:
                found_letters.append(0x10000 * worldID + 0x100 * levelID + letter_id)

        return found_letters

    async def check_level_clear(self):
        returning = []

        main_level_data_ptr = int.from_bytes(dme.read_bytes(LEVEL_DATA_POINTER + MEM, 4), byteorder="big")
        current_level = int.from_bytes(dme.read_bytes(CURRENT_LEVEL, 4), byteorder="big")
        current_world = int.from_bytes(dme.read_bytes(WORLD_OF_CURRENT_LEVEL, 4), byteorder="big")

        for name, data in Levels.items():
            if data.index != current_level:
                continue
            if data.world_index != current_world:
                continue
            level_data = int.from_bytes(dme.read_bytes(data.pointer + main_level_data_ptr, 4), byteorder="big")
            flags = dme.read_byte(level_data + LEVEL_DATA_FLAGS_OFFSET)

            world = data.world_index
            level = data.index
            id_base = 0x10000 * world + 0x100 * level

            if flags & 0x40:
                returning.append(id_base + CLEARED)
                if level == K_LEVEL_INDEX:
                    returning.append(id_base + RARE_ORB)

            if flags & 0x10:
                returning.append(id_base + PUZZLE_PIECE_SET)

            if flags & 0x08:
                returning.append(id_base + KONG_LETTER_SET)

            if flags & 0x01:
                returning.append(id_base + CLEARED_MIRROR)

        return returning

    async def check_time_attack(self):
        found_medals = []

        medal_order = [
            ("Bronze", CLEARED_TIME_ATTACK_BRONZE),
            ("Silver", CLEARED_TIME_ATTACK_SILVER),
            ("Gold", CLEARED_TIME_ATTACK_GOLD),
            ("Shiny Gold", CLEARED_TIME_ATTACK_SHINY_GOLD),
        ]

        main_level_data_ptr = int.from_bytes(dme.read_bytes(LEVEL_DATA_POINTER + MEM, 4), byteorder="big")
        current_level = int.from_bytes(dme.read_bytes(CURRENT_LEVEL, 4), byteorder="big")
        current_world = int.from_bytes(dme.read_bytes(WORLD_OF_CURRENT_LEVEL, 4), byteorder="big")

        for _, data in Levels.items():
            if data.index != current_level:
                continue
            if data.world_index != current_world:
                continue
            level_data = int.from_bytes(dme.read_bytes(data.pointer + main_level_data_ptr, 4), byteorder="big")
            medal = dme.read_byte(level_data + MEDAL_OFFSET)
            if medal != 0xFF:
                world = data.world_index
                level = data.index
                id_base = 0x10000 * world + 0x100 * level

                for rank, (_, location_id) in enumerate(medal_order):
                    if rank <= medal and self.valid_medals[medal_order[rank][0]]:
                        found_medals.append(id_base + location_id)

        return found_medals

    async def check_key(self):
        jungle_key = dme.read_byte(WORLD_MAP_KEY_JUNGLE)
        beach_key = dme.read_byte(WORLD_MAP_KEY_BEACH)
        ruins_key = dme.read_byte(WORLD_MAP_KEY_RUINS)
        cave_key = dme.read_byte(WORLD_MAP_KEY_CAVE)
        forest_key = dme.read_byte(WORLD_MAP_KEY_FOREST)
        cliff_key = dme.read_byte(WORLD_MAP_KEY_CLIFF)
        factory_key = dme.read_byte(WORLD_MAP_KEY_FACTORY)
        volcano_key = dme.read_byte(WORLD_MAP_KEY_VOLCANO)

        found_keys = []

        if jungle_key == 0x1:
            found_keys.append(JUNGLE_WORLD_INDEX * 0x10000 + SHOP_LEVEL_INDEX * 0x100 + SHOP_KEY)
        if beach_key == 0x1:
            found_keys.append(BEACH_WORLD_INDEX * 0x10000 + SHOP_LEVEL_INDEX * 0x100 + SHOP_KEY)
        if ruins_key == 0x1:
            found_keys.append(RUINS_WORLD_INDEX * 0x10000 + SHOP_LEVEL_INDEX * 0x100 + SHOP_KEY)
        if cave_key == 0x1:
            found_keys.append(CAVE_WORLD_INDEX * 0x10000 + SHOP_LEVEL_INDEX * 0x100 + SHOP_KEY)
        if forest_key == 0x1:
            found_keys.append(FOREST_WORLD_INDEX * 0x10000 + SHOP_LEVEL_INDEX * 0x100 + SHOP_KEY)
        if cliff_key == 0x1:
            found_keys.append(CLIFF_WORLD_INDEX * 0x10000 + SHOP_LEVEL_INDEX * 0x100 + SHOP_KEY)
        if factory_key == 0x1:
            found_keys.append(FACTORY_WORLD_INDEX * 0x10000 + SHOP_LEVEL_INDEX * 0x100 + SHOP_KEY)
        if volcano_key == 0x1:
            found_keys.append(VOLCANO_WORLD_INDEX * 0x10000 + SHOP_LEVEL_INDEX * 0x100 + SHOP_KEY)

        return found_keys

    async def check_mirror_mode(self):
        if self.mirror_mode_shards_option == 0:
            self.mirror_mode_shards_option += 1
        if dme.read_word(CUSTOM_MIRROR_SHARD_ADDR) >= self.mirror_mode_shards_option:
            dme.write_word(MEM + MIRROR_UNLOCKED, 1)

    async def handle_squawks(self):
        await self.update_squawks(True)
        self.has_squawks = True
        self.toggle_squawks()

    def check_level_cleared(self, level_ptr):
        main_level_data_ptr = int.from_bytes(dme.read_bytes(LEVEL_DATA_POINTER + MEM, 4), byteorder="big")
        level_data = int.from_bytes(dme.read_bytes(level_ptr + main_level_data_ptr, 4), byteorder="big")
        flags = dme.read_byte(level_data + LEVEL_DATA_FLAGS_OFFSET)
        if flags & 0x40:
            return True
        if flags & 0x01:
            return True
        return False

    def clear_ram(self):
        dme.write_word(CUSTOM_LAST_ITEM_INDEX_ADDR, 0)
        dme.write_word(CUSTOM_PP_AMOUNT_ADDR, 0)
        dme.write_word(CUSTOM_ORB_BITFLAG_ADDR, 0)
        dme.write_word(CUSTOM_KL_AMOUNT_ADDR, 0)
        dme.write_word(CUSTOM_KL_AMOUNT_ADDR + 0x4, 0)
        dme.write_word(CUSTOM_LEVEL_BITFLAG_ADDR, 0)
        dme.write_word(CUSTOM_LEVEL_BITFLAG_ADDR + 0x4, 0)
        dme.write_word(CUSTOM_LEVEL_BITFLAG_ADDR + 0x8, 0)
        dme.write_word(CUSTOM_KEY_BITFLAG_ADDR, 0)
        dme.write_word(CUSTOM_MIRROR_SHARD_ADDR, 0)
        dme.write_word(CUSTOM_FACTORY_BUTTON_ADDR, 0)


def read_string(console_address: int) -> str:
    return dme.read_bytes(console_address, 0x40).split(b"\0", 1)[0].decode()


def write_string64(console_address: int, value: str) -> None:
    max_len = 64
    if "\0" in value:
        raise ValueError("string contains null byte")
    data = value.encode()[:max_len - 1] + b'\0'
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


def check_in_rom() -> bool:
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


async def dolphin_sync_task(ctx: DKCRContext) -> None:
    logger.info("Starting Dolphin connector. Use /dolphin for status information.")
    sleep_time = 0.0
    while not ctx.exit_event.is_set():
        if sleep_time > 0.0:
            try:
                await asyncio.wait_for(ctx.watcher_event.wait(), sleep_time)
            except asyncio.TimeoutError:
                pass
            sleep_time = 0.0
        ctx.watcher_event.clear()
        try:
            if dme.is_hooked() and ctx.dolphin_status == D.CONNECTION_CONNECTED_STATUS:
                if not check_in_rom():
                    # Reset the give item array while not in the game.
                    sleep_time = 0.1
                    continue
                if ctx.slot is not None:
                    # Loop
                    await ctx.give_dk_items()
                    game_state = get_game_state()
                    if (game_state == STATE_WORLD_MAP or game_state == STATE_WORLD_MAP_AFTER_QUIT) and ctx.exited_level:
                        ctx.exited_level = False
                        for loc_id in await ctx.check_level_clear():
                            await ctx.check_locations([loc_id])
                        for loc_id in await ctx.check_time_attack():
                            await ctx.check_locations([loc_id])
                    if game_state == STATE_WORLD_MAP or game_state == STATE_WORLD_MAP_AFTER_QUIT:
                        for loc_id in await ctx.check_key():
                            await ctx.check_locations([loc_id])
                        await ctx.check_mirror_mode()
                    if game_state == STATE_TIME_ATTACK:
                        ctx.exited_level = True
                    if game_state == STATE_IN_LEVEL:
                        ctx.exited_level = True
                        ctx.check_squawks()
                        current_level_index = int.from_bytes(dme.read_bytes(MEM + CURRENT_LEVEL, 4), byteorder="big")
                        current_world_index = int.from_bytes(dme.read_bytes(MEM + WORLD_OF_CURRENT_LEVEL, 4),
                                                             byteorder="big")
                        for name, data in Levels.items():
                            if data.world_index == current_world_index and data.index == current_level_index:
                                for loc_id in await ctx.check_letters(data.index, current_world_index):
                                    await ctx.check_locations([loc_id])
                                for loc_id in await ctx.check_puzzle_piece(data.index, data.world_index):
                                    await ctx.check_locations([loc_id])
                        if dme.read_word(MEM + CUTSCENE_IDENTIFIER) == VICTORY_CUTSCENE_DK or dme.read_word(MEM + CUTSCENE_IDENTIFIER) == VICTORY_CUTSCENE_DK_AND_DD:
                            await ctx.send_msgs([{
                                "cmd": "StatusUpdate",
                                "status": NetUtils.ClientStatus.CLIENT_GOAL,
                            }])
                    # if FromOption(GoldenTemple) == 0:
                    #     if dme.read_word(MEM + CUTSCENE_IDENTIFIER) == VICTORY_CUTSCENE_DK or dme.read_word(MEM + CUTSCENE_IDENTIFIER) == VICTORY_CUTSCENE_DK_AND_DD:
                    #         await ctx.send_msgs([{
                    #             "cmd": "StatusUpdate",
                    #             "status": NetUtils.ClientStatus.CLIENT_GOAL,
                    #         }])
                    # else:
                    #     if dme.read_word(MEM + MIRROR_UNLOCKED) == 1:
                    #         await ctx.send_msgs([{
                    #             "cmd": "StatusUpdate",
                    #             "status": NetUtils.ClientStatus.CLIENT_GOAL,
                    #         }])
                    if "DeathLink" in ctx.tags:
                        await check_death(ctx)
                sleep_time = 0.1
            else:
                if ctx.dolphin_status == D.CONNECTION_CONNECTED_STATUS:
                    logger.info("Connection to Dolphin lost, reconnecting...")
                    ctx.dolphin_status = D.CONNECTION_LOST_STATUS
                logger.info("Attempting to connect to Dolphin...")
                dme.hook()
                if dme.is_hooked():
                    if dme.read_bytes(MEM + GAME_ID, 6) != b"SF8E01" and dme.read_byte(MEM + REV_NUMBER) != 0x01:
                        logger.info(D.CONNECTION_REFUSED_GAME_STATUS)
                        ctx.dolphin_status = D.CONNECTION_REFUSED_GAME_STATUS
                        dme.un_hook()
                        sleep_time = 5
                    else:
                        logger.info(D.CONNECTION_CONNECTED_STATUS)
                        ctx.dolphin_status = D.CONNECTION_CONNECTED_STATUS
                        ctx.locations_checked = set()
                else:
                    logger.info("Connection to Dolphin failed, attempting again in 5 seconds...")
                    ctx.dolphin_status = D.CONNECTION_LOST_STATUS
                    await ctx.disconnect()
                    sleep_time = 5
                    continue
        except Exception:
            dme.un_hook()
            logger.info("Connection to Dolphin failed, attempting again in 5 seconds...")
            logger.error(traceback.format_exc())
            ctx.dolphin_status = D.CONNECTION_LOST_STATUS
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
