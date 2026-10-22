import asyncio

import NetUtils
from CommonClient import logger

from .dkcr_game import DKCRGame
from .dkcr_context import DKCRContext

from .utils.check_pp import check_pp
from .utils.check_letters import check_letters
from .utils.check_level_data import check_level_data
from .utils.get_base_location_address import get_base_location_address
from .utils.get_last_level import get_last_level

from ..data.items import GameItems
from ..data.levels import GameLevels
from ..data.worlds import GameWorlds
from ..data.constants.addresses.custom import CustomAddresses


class DKCRClient:
    def __init__(self, ctx: DKCRContext, dkcr: DKCRGame) -> None:
        self.ctx = ctx
        self.dkcr = dkcr
        self.dolphin_connected = False
        self.sleep_time = 0.1

    async def run(self, exit_event: asyncio.Event) -> None:
        while not exit_event.is_set():
            await self.connect_client_to_dolphin()
            if self.dolphin_connected and self.ctx.slot is not None:
                await self.main_loop()
            elif self.dolphin_connected:
                self.dkcr.dolphin.write_bytes(0x817fc000, b'\x00\x00\x00\x00' * 40)
            await asyncio.sleep(self.sleep_time)
            self.sleep_time = 0.1

    async def connect_client_to_dolphin(self) -> None:
        if not self.dkcr.connect() or not self.dkcr.check_in_rom():
            logger.info(
                "Waiting for Donkey Kong Country Returns...\n"
                "(Retry in 5sec)"
            )
            self.dkcr.version = None
            self.dkcr.addresses = None
            self.dolphin_connected = False
            await self.ctx.disconnect()
            self.sleep_time += 5
            return
        elif not self.dolphin_connected:
            logger.info(f"Donkey Kong Country Returns {self.dkcr.version.value} successfully connected!")
            self.dolphin_connected = True
            self.dkcr.dolphin.write_bytes(0x817fc02a, b'\xff\xff') # Open all worlds

    async def main_loop(self) -> None:
        self.create_level_bitfield()
        locations_to_send: set[int] = set()
        last_level = await get_last_level(self.dkcr)
        base_location_address = get_base_location_address(last_level)
        if self.dkcr.is_in_level():
            await self.give_item()
            pp_field = self.dkcr.get_current_level_puzzle_piece_bitfield()
            letters = self.dkcr.get_all_letters()
            locations_to_send.update(await check_pp(base_location_address, pp_field))
            locations_to_send.update(await check_letters(base_location_address, letters))

        elif self.dkcr.is_in_world_map():
            await self.give_item()
            self.dkcr.reset_custom_pp()
            level_data = self.dkcr.get_current_level_data()
            locations_to_send.update(await check_level_data(base_location_address, level_data))
            locations_to_send.update(self.dkcr.get_keys())
            locations_to_send.update(self.dkcr.get_medals(base_location_address))
            if self.dkcr.get_mirror_mode() >= self.ctx.mirror_mode_shards_option != 0:
                self.dkcr.enable_mirror_mode()
            if self.ctx.mirror_mode_shards_option == 0:
                if self.dkcr.get_mirror_mode() >= 1:
                    self.dkcr.enable_mirror_mode()
            locations_to_send.update(self.dkcr.get_world_bundles(last_level[0], self.ctx.time_attack_resolved_option))
        elif self.dkcr.is_quit_from_game_over():
            pass
        elif self.dkcr.is_in_title():
            pass
        elif self.dkcr.is_in_super_guide():
            await self.give_item()
        elif self.dkcr.is_in_time_attack():
            await self.give_item()
        else:
            pass

        if self.dkcr.in_pre_rendered_cutscene():
            if self.dkcr.in_victory_cutscene():
                await self.ctx.send_msgs([{
                    "cmd": "StatusUpdate",
                    "status": NetUtils.ClientStatus.CLIENT_GOAL,
                }])

        await self.ctx.check_locations(locations_to_send)

    async def give_item(self):
        received_items = self.ctx.items_received
        current_index = self.ctx.last_received_item_index

        if current_index >= len(received_items):
            return

        items_to_process = received_items[current_index:]

        for item in items_to_process:
            item_name = self.ctx.item_names.lookup_in_game(item.item)
            dk_item = GameItems.from_display_name(item_name)

            match dk_item:
                case GameItems.PUZZLE_PIECE:
                    self.dkcr.add_pp()
                case (
                    GameItems.KONG_LETTER_JUNGLE |
                    GameItems.KONG_LETTER_BEACH |
                    GameItems.KONG_LETTER_RUINS |
                    GameItems.KONG_LETTER_CAVE |
                    GameItems.KONG_LETTER_FOREST |
                    GameItems.KONG_LETTER_CLIFF |
                    GameItems.KONG_LETTER_FACTORY |
                    GameItems.KONG_LETTER_VOLCANO
                ):
                    self.dkcr.add_kl(dk_item)
                case (
                    GameItems.JUNGLE_KEY |
                    GameItems.BEACH_KEY |
                    GameItems.RUINS_KEY |
                    GameItems.CAVE_KEY |
                    GameItems.FOREST_KEY |
                    GameItems.CLIFF_KEY |
                    GameItems.FACTORY_KEY |
                    GameItems.VOLCANO_KEY
                ):
                    self.dkcr.add_key(dk_item)
                case GameItems.RARE_ORB:
                    self.dkcr.add_orb()
                case GameItems.PROGRESSIVE_FACTORY_BUTTON:
                    self.dkcr.add_factory_button()
                case GameItems.PROGRESSIVE_BOSS_UNLOCK:
                    self.dkcr.add_boss_unlock()
                case GameItems.PROGRESSIVE_K_LEVEL_UNLOCK:
                    self.dkcr.add_k_level_unlock()
                case GameItems.MIRROR_SHARD:
                    self.dkcr.add_mirror_shard()
                case GameItems.MIRROR_MODE:
                    self.dkcr.set_mirror_mode()
                case GameItems.SQUAWKS:
                    self.dkcr.set_squawks()
                case GameItems.BALLOONX1:
                    self.dkcr.add_extra_lives(1)
                case GameItems.BALLOONX3:
                    self.dkcr.add_extra_lives(3)
                case GameItems.BALLOONX7:
                    self.dkcr.add_extra_lives(7)
                case GameItems.BANANA:
                    self.dkcr.add_bananas(1)
                case GameItems.BANANA_BUNCH:
                    self.dkcr.add_bananas(5)
                case GameItems.BIG_BANANA_BUNCH:
                    self.dkcr.add_bananas(20)
                case GameItems.BANANA_COIN:
                    self.dkcr.add_banana_coins(1)
                case GameItems.RECOVERY_HEART:
                    self.dkcr.add_recovery_heart()


            self.ctx.last_received_item_index += 1

    def create_level_bitfield(self):
        for level in GameLevels:
            match level:
                case GameLevels.JUNGLE_HIJINXS:
                    if True:
                        self.dkcr.dolphin.read_set_bit_in_bytes(CustomAddresses.LEVEL_CONNECTION, 10, level.level_map_index)
                case GameLevels.KING_OF_CLING:
                    if True:
                        self.dkcr.dolphin.read_set_bit_in_bytes(CustomAddresses.LEVEL_CONNECTION, 10, level.level_map_index)
                case GameLevels.TREE_TOP_BOP:
                    if True:
                        self.dkcr.dolphin.read_set_bit_in_bytes(CustomAddresses.LEVEL_CONNECTION, 10, level.level_map_index)
                case GameLevels.SUNSET_SHORE:
                    if self.dkcr.has_key(GameWorlds.JUNGLE):
                        self.dkcr.dolphin.read_set_bit_in_bytes(CustomAddresses.LEVEL_CONNECTION, 10, level.level_map_index)
                    if self.ctx.sunset_shore_key_option == 0:
                        if self.dkcr.read_keys(GameWorlds.JUNGLE):
                            self.dkcr.dolphin.read_set_bit_in_bytes(CustomAddresses.LEVEL_CONNECTION, 10, level.level_map_index)
                case GameLevels.CANOPY_CANNONS:
                    if True:
                        self.dkcr.dolphin.read_set_bit_in_bytes(CustomAddresses.LEVEL_CONNECTION, 10, level.level_map_index)
                case GameLevels.CRAZY_CART:
                    if True:
                        self.dkcr.dolphin.read_set_bit_in_bytes(CustomAddresses.LEVEL_CONNECTION, 10, level.level_map_index)
                case GameLevels.PLATFORM_PANIC:
                    if (
                        self.dkcr.get_kl(GameWorlds.JUNGLE) >= self.ctx.jungle_k_level_access_option
                        or self.dkcr.get_k_level_unlock() >= 1
                    ):
                        self.dkcr.dolphin.read_set_bit_in_bytes(CustomAddresses.LEVEL_CONNECTION, 10, level.level_map_index)
                case GameLevels.MUGLYS_MOUND:
                    if (
                        self.dkcr.get_pp() >= self.ctx.jungle_boss_access_option
                        or self.dkcr.get_boss_unlock() >= 1
                    ):
                        self.dkcr.dolphin.read_set_bit_in_bytes(CustomAddresses.LEVEL_CONNECTION, 10, level.level_map_index)
                case GameLevels.JUNGLE_SHOP:
                    if True:
                        self.dkcr.dolphin.read_set_bit_in_bytes(CustomAddresses.LEVEL_CONNECTION, 10, level.level_map_index)
                case GameLevels.POPPIN_PLANKS:
                    if True:
                        self.dkcr.dolphin.read_set_bit_in_bytes(CustomAddresses.LEVEL_CONNECTION, 10, level.level_map_index)
                case GameLevels.SLOPPY_SANDS:
                    if True:
                        self.dkcr.dolphin.read_set_bit_in_bytes(CustomAddresses.LEVEL_CONNECTION, 10, level.level_map_index)
                case GameLevels.PEACEFUL_PIER:
                    if True:
                        self.dkcr.dolphin.read_set_bit_in_bytes(CustomAddresses.LEVEL_CONNECTION, 10, level.level_map_index)
                case GameLevels.CANNON_CLUSTER:
                    if True:
                        self.dkcr.dolphin.read_set_bit_in_bytes(CustomAddresses.LEVEL_CONNECTION, 10, level.level_map_index)
                case GameLevels.STORMY_SHORE:
                    if True:
                        self.dkcr.dolphin.read_set_bit_in_bytes(CustomAddresses.LEVEL_CONNECTION, 10, level.level_map_index)
                case GameLevels.BLOWHOLE_BOUND:
                    if self.dkcr.has_key(GameWorlds.BEACH):
                        self.dkcr.dolphin.read_set_bit_in_bytes(CustomAddresses.LEVEL_CONNECTION, 10, level.level_map_index)
                    if self.ctx.blowhole_bound_key_option == 0:
                        if self.dkcr.read_keys(GameWorlds.BEACH):
                            self.dkcr.dolphin.read_set_bit_in_bytes(CustomAddresses.LEVEL_CONNECTION, 10, level.level_map_index)
                case GameLevels.TIDAL_TERROR:
                    if True:
                        self.dkcr.dolphin.read_set_bit_in_bytes(CustomAddresses.LEVEL_CONNECTION, 10, level.level_map_index)
                case GameLevels.TUMBLIN_TEMPLE:
                    if (self.dkcr.get_kl(GameWorlds.BEACH) >= self.ctx.beach_k_level_access_option
                        or self.dkcr.get_k_level_unlock() >= 2
                    ):
                        self.dkcr.dolphin.read_set_bit_in_bytes(CustomAddresses.LEVEL_CONNECTION, 10, level.level_map_index)
                case GameLevels.PINCHIN_PIRATES:
                    if (self.dkcr.get_pp() >= self.ctx.beach_boss_access_option
                        or self.dkcr.get_boss_unlock() >= 2
                    ):
                        self.dkcr.dolphin.read_set_bit_in_bytes(CustomAddresses.LEVEL_CONNECTION, 10, level.level_map_index)
                case GameLevels.BEACH_SHOP:
                    if True:
                        self.dkcr.dolphin.read_set_bit_in_bytes(CustomAddresses.LEVEL_CONNECTION, 10, level.level_map_index)
                case GameLevels.WONKY_WATERWAY:
                    if True:
                        self.dkcr.dolphin.read_set_bit_in_bytes(CustomAddresses.LEVEL_CONNECTION, 10, level.level_map_index)
                case GameLevels.BUTTON_BASH:
                    if True:
                        self.dkcr.dolphin.read_set_bit_in_bytes(CustomAddresses.LEVEL_CONNECTION, 10, level.level_map_index)
                case GameLevels.MAST_BLAST:
                    if True:
                        self.dkcr.dolphin.read_set_bit_in_bytes(CustomAddresses.LEVEL_CONNECTION, 10, level.level_map_index)
                case GameLevels.DAMP_DUNGEON:
                    if self.dkcr.has_key(GameWorlds.RUINS):
                        self.dkcr.dolphin.read_set_bit_in_bytes(CustomAddresses.LEVEL_CONNECTION, 10, level.level_map_index)
                    if self.ctx.damp_dungeon_key_option == 0:
                        if self.dkcr.read_keys(GameWorlds.RUINS):
                            self.dkcr.dolphin.read_set_bit_in_bytes(CustomAddresses.LEVEL_CONNECTION, 10, level.level_map_index)
                case GameLevels.ITTY_BITTY_BITERS:
                    if True:
                        self.dkcr.dolphin.read_set_bit_in_bytes(CustomAddresses.LEVEL_CONNECTION, 10, level.level_map_index)
                case GameLevels.TEMPLE_TOPPLE:
                    if True:
                        self.dkcr.dolphin.read_set_bit_in_bytes(CustomAddresses.LEVEL_CONNECTION, 10, level.level_map_index)
                case GameLevels.SHIFTY_SMASHERS:
                    if (self.dkcr.get_kl(GameWorlds.RUINS) >= self.ctx.ruins_k_level_access_option
                        or self.dkcr.get_k_level_unlock() >= 3
                    ):
                        self.dkcr.dolphin.read_set_bit_in_bytes(CustomAddresses.LEVEL_CONNECTION, 10, level.level_map_index)
                case GameLevels.RUINED_ROOST:
                    if (self.dkcr.get_pp() >= self.ctx.ruins_boss_access_option
                        or self.dkcr.get_boss_unlock() >= 3
                    ):
                        self.dkcr.dolphin.read_set_bit_in_bytes(CustomAddresses.LEVEL_CONNECTION, 10, level.level_map_index)
                case GameLevels.RUINS_SHOP:
                    if True:
                        self.dkcr.dolphin.read_set_bit_in_bytes(CustomAddresses.LEVEL_CONNECTION, 10, level.level_map_index)
                case GameLevels.RICKETY_RAILS:
                    if True:
                        self.dkcr.dolphin.read_set_bit_in_bytes(CustomAddresses.LEVEL_CONNECTION, 10, level.level_map_index)
                case GameLevels.GRIP_N_TRIP:
                    if True:
                        self.dkcr.dolphin.read_set_bit_in_bytes(CustomAddresses.LEVEL_CONNECTION, 10, level.level_map_index)
                case GameLevels.BOMBS_AWAY:
                    if True:
                        self.dkcr.dolphin.read_set_bit_in_bytes(CustomAddresses.LEVEL_CONNECTION, 10, level.level_map_index)
                case GameLevels.MOLE_PATROL:
                    if self.dkcr.has_key(GameWorlds.CAVE):
                        self.dkcr.dolphin.read_set_bit_in_bytes(CustomAddresses.LEVEL_CONNECTION, 10, level.level_map_index)
                    if self.ctx.mole_patrol_key_option == 0:
                        if self.dkcr.read_keys(GameWorlds.CAVE):
                            self.dkcr.dolphin.read_set_bit_in_bytes(CustomAddresses.LEVEL_CONNECTION, 10, level.level_map_index)
                case GameLevels.CROWDED_CAVERN:
                    if True:
                        self.dkcr.dolphin.read_set_bit_in_bytes(CustomAddresses.LEVEL_CONNECTION, 10, level.level_map_index)
                case GameLevels.JAGGED_JEWELS:
                    if (self.dkcr.get_kl(GameWorlds.CAVE) >= self.ctx.cave_k_level_access_option
                        or self.dkcr.get_k_level_unlock() >= 4
                    ):
                        self.dkcr.dolphin.read_set_bit_in_bytes(CustomAddresses.LEVEL_CONNECTION, 10, level.level_map_index)
                case GameLevels.THE_MOLE_TRAIN:
                    if (self.dkcr.get_pp() >= self.ctx.cave_boss_access_option
                        or self.dkcr.get_boss_unlock() >= 4
                    ):
                        self.dkcr.dolphin.read_set_bit_in_bytes(CustomAddresses.LEVEL_CONNECTION, 10, level.level_map_index)
                case GameLevels.CAVE_SHOP:
                    if True:
                        self.dkcr.dolphin.read_set_bit_in_bytes(CustomAddresses.LEVEL_CONNECTION, 10, level.level_map_index)
                case GameLevels.VINE_VALLEY:
                    if True:
                        self.dkcr.dolphin.read_set_bit_in_bytes(CustomAddresses.LEVEL_CONNECTION, 10, level.level_map_index)
                case GameLevels.CLINGY_SWINGY:
                    if True:
                        self.dkcr.dolphin.read_set_bit_in_bytes(CustomAddresses.LEVEL_CONNECTION, 10, level.level_map_index)
                case GameLevels.FLUTTER_FLYAWAY:
                    if True:
                        self.dkcr.dolphin.read_set_bit_in_bytes(CustomAddresses.LEVEL_CONNECTION, 10, level.level_map_index)
                case GameLevels.TIPPIN_TOTEMS:
                    if True:
                        self.dkcr.dolphin.read_set_bit_in_bytes(CustomAddresses.LEVEL_CONNECTION, 10, level.level_map_index)
                case GameLevels.LONGSHOT_LAUNCH:
                    if True:
                        self.dkcr.dolphin.read_set_bit_in_bytes(CustomAddresses.LEVEL_CONNECTION, 10, level.level_map_index)
                case GameLevels.SPRINGY_SPORES:
                    if self.dkcr.has_key(GameWorlds.FOREST):
                        self.dkcr.dolphin.read_set_bit_in_bytes(CustomAddresses.LEVEL_CONNECTION, 10, level.level_map_index)
                    if self.ctx.sunset_shore_key_option == 0:
                        if self.dkcr.read_keys(GameWorlds.FOREST):
                            self.dkcr.dolphin.read_set_bit_in_bytes(CustomAddresses.LEVEL_CONNECTION, 10, level.level_map_index)
                case GameLevels.WIGGLEVINE_WONDERS:
                    if self.dkcr.has_key(GameWorlds.FOREST):
                        self.dkcr.dolphin.read_set_bit_in_bytes(CustomAddresses.LEVEL_CONNECTION, 10, level.level_map_index)
                case GameLevels.MUNCHER_MARATHON:
                    if True:
                        self.dkcr.dolphin.read_set_bit_in_bytes(CustomAddresses.LEVEL_CONNECTION, 10, level.level_map_index)
                case GameLevels.BLAST_N_BOUNCE:
                    if (self.dkcr.get_kl(GameWorlds.FOREST) >= self.ctx.forest_k_level_access_option
                        or self.dkcr.get_k_level_unlock() >= 5
                    ):
                        self.dkcr.dolphin.read_set_bit_in_bytes(CustomAddresses.LEVEL_CONNECTION, 10, level.level_map_index)
                case GameLevels.MANGORUBY_RUN:
                    if (self.dkcr.get_pp() >= self.ctx.forest_boss_access_option
                        or self.dkcr.get_boss_unlock() >= 5
                    ):
                        self.dkcr.dolphin.read_set_bit_in_bytes(CustomAddresses.LEVEL_CONNECTION, 10, level.level_map_index)
                case GameLevels.FOREST_SHOP:
                    if True:
                        self.dkcr.dolphin.read_set_bit_in_bytes(CustomAddresses.LEVEL_CONNECTION, 10, level.level_map_index)
                case GameLevels.STICKY_SITUATION:
                    if True:
                        self.dkcr.dolphin.read_set_bit_in_bytes(CustomAddresses.LEVEL_CONNECTION, 10, level.level_map_index)
                case GameLevels.PREHISTORIC_PATH:
                    if True:
                        self.dkcr.dolphin.read_set_bit_in_bytes(CustomAddresses.LEVEL_CONNECTION, 10, level.level_map_index)
                case GameLevels.WEIGHTY_WAY:
                    if True:
                        self.dkcr.dolphin.read_set_bit_in_bytes(CustomAddresses.LEVEL_CONNECTION, 10, level.level_map_index)
                case GameLevels.BOULDER_ROLLER:
                    if True:
                        self.dkcr.dolphin.read_set_bit_in_bytes(CustomAddresses.LEVEL_CONNECTION, 10, level.level_map_index)
                case GameLevels.PRECARIOUS_PLATEAU:
                    if self.dkcr.has_key(GameWorlds.FOREST):
                        self.dkcr.dolphin.read_set_bit_in_bytes(CustomAddresses.LEVEL_CONNECTION, 10, level.level_map_index)
                    if self.ctx.precarious_plateau_key_option == 0:
                        if self.dkcr.read_keys(GameWorlds.CLIFF):
                            self.dkcr.dolphin.read_set_bit_in_bytes(CustomAddresses.LEVEL_CONNECTION, 10, level.level_map_index)
                case GameLevels.CRUMBLE_CANYON:
                    if True:
                        self.dkcr.dolphin.read_set_bit_in_bytes(CustomAddresses.LEVEL_CONNECTION, 10, level.level_map_index)
                case GameLevels.TIPPY_SHIPPY:
                    if True:
                        self.dkcr.dolphin.read_set_bit_in_bytes(CustomAddresses.LEVEL_CONNECTION, 10, level.level_map_index)
                case GameLevels.CLIFFTOP_CLIMB:
                    if True:
                        self.dkcr.dolphin.read_set_bit_in_bytes(CustomAddresses.LEVEL_CONNECTION, 10, level.level_map_index)
                case GameLevels.PERILOUS_PASSAGE:
                    if (self.dkcr.get_kl(GameWorlds.CLIFF) >= self.ctx.cliff_k_level_access_option
                        or self.dkcr.get_k_level_unlock() >= 6
                    ):
                        self.dkcr.dolphin.read_set_bit_in_bytes(CustomAddresses.LEVEL_CONNECTION, 10, level.level_map_index)
                case GameLevels.THUGLYS_HIGHRISE:
                    if (self.dkcr.get_pp() >= self.ctx.cliff_boss_access_option
                        or self.dkcr.get_boss_unlock() >= 6
                    ):
                        self.dkcr.dolphin.read_set_bit_in_bytes(CustomAddresses.LEVEL_CONNECTION, 10, level.level_map_index)
                case GameLevels.CLIFF_SHOP:
                    if True:
                        self.dkcr.dolphin.read_set_bit_in_bytes(CustomAddresses.LEVEL_CONNECTION, 10, level.level_map_index)
                case GameLevels.FOGGY_FUMES:
                    if True:
                        self.dkcr.dolphin.read_set_bit_in_bytes(CustomAddresses.LEVEL_CONNECTION, 10, level.level_map_index)
                case GameLevels.SLAMMIN_STEEL:
                    if self.ctx.smog_clear_option:
                        if self.dkcr.get_current_level_data(GameWorlds.CLIFF.world_index, GameLevels.FOGGY_FUMES.level_index).level_cleared:
                            self.dkcr.dolphin.read_set_bit_in_bytes(CustomAddresses.LEVEL_CONNECTION, 10, level.level_map_index)
                    else:
                        self.dkcr.dolphin.read_set_bit_in_bytes(CustomAddresses.LEVEL_CONNECTION, 10, level.level_map_index)
                case GameLevels.HANDY_HAZARDS:
                    if self.dkcr.has_key(GameWorlds.FACTORY):
                        self.dkcr.dolphin.read_set_bit_in_bytes(CustomAddresses.LEVEL_CONNECTION, 10, level.level_map_index)
                    if self.ctx.handy_hazards_key_option == 0:
                        if self.dkcr.read_keys(GameWorlds.FACTORY):
                            self.dkcr.dolphin.read_set_bit_in_bytes(CustomAddresses.LEVEL_CONNECTION, 10, level.level_map_index)
                case GameLevels.GEAR_GETAWAY:
                    if True:
                        self.dkcr.dolphin.read_set_bit_in_bytes(CustomAddresses.LEVEL_CONNECTION, 10, level.level_map_index)
                case GameLevels.COG_JOG:
                    if True:
                        self.dkcr.dolphin.read_set_bit_in_bytes(CustomAddresses.LEVEL_CONNECTION, 10, level.level_map_index)
                case GameLevels.SWITCHEROO:
                    if True:
                        self.dkcr.dolphin.read_set_bit_in_bytes(CustomAddresses.LEVEL_CONNECTION, 10, level.level_map_index)
                case GameLevels.MUSIC_MADNESS:
                    if True:
                        self.dkcr.dolphin.read_set_bit_in_bytes(CustomAddresses.LEVEL_CONNECTION, 10, level.level_map_index)
                case GameLevels.LIFT_OFF_LAUNCH:
                    if not self.ctx.factory_buttons_option:
                        self.dkcr.dolphin.read_set_bit_in_bytes(CustomAddresses.LEVEL_CONNECTION, 10, level.level_map_index)
                    else:
                        if self.dkcr.get_factory_button() >= self.ctx.factory_buttons_option:
                            self.dkcr.dolphin.read_set_bit_in_bytes(CustomAddresses.LEVEL_CONNECTION, 10, level.level_map_index)
                case GameLevels.TREACHEROUS_TRACK:
                    if (self.dkcr.get_kl(GameWorlds.FACTORY) >= self.ctx.factory_k_level_access_option
                        or self.dkcr.get_k_level_unlock() >= 7
                    ):
                        if self.dkcr.has_key(GameWorlds.FACTORY):
                            self.dkcr.dolphin.read_set_bit_in_bytes(CustomAddresses.LEVEL_CONNECTION, 10, level.level_map_index)
                case GameLevels.FEATHER_FIEND:
                    if (self.dkcr.get_pp() >= self.ctx.factory_boss_access_option
                        or self.dkcr.get_boss_unlock() >= 7
                    ):
                        if self.ctx.lift_off_launch_option:
                            if self.dkcr.get_current_level_data(GameWorlds.FACTORY.world_index, GameLevels.LIFT_OFF_LAUNCH.level_index).level_cleared:
                                self.dkcr.dolphin.read_set_bit_in_bytes(CustomAddresses.LEVEL_CONNECTION, 10, level.level_map_index)
                        else:
                            self.dkcr.dolphin.read_set_bit_in_bytes(CustomAddresses.LEVEL_CONNECTION, 10, level.level_map_index)
                case GameLevels.FACTORY_SHOP:
                    if True:
                        self.dkcr.dolphin.read_set_bit_in_bytes(CustomAddresses.LEVEL_CONNECTION, 10, level.level_map_index)
                case GameLevels.FURIOUS_FIRE:
                    if True:
                        self.dkcr.dolphin.read_set_bit_in_bytes(CustomAddresses.LEVEL_CONNECTION, 10, level.level_map_index)
                case GameLevels.HOT_ROCKET:
                    if True:
                        self.dkcr.dolphin.read_set_bit_in_bytes(CustomAddresses.LEVEL_CONNECTION, 10, level.level_map_index)
                case GameLevels.ROASTING_RAILS:
                    if True:
                        self.dkcr.dolphin.read_set_bit_in_bytes(CustomAddresses.LEVEL_CONNECTION, 10, level.level_map_index)
                case GameLevels.SMOKEY_PEAK:
                    if self.dkcr.has_key(GameWorlds.VOLCANO):
                        self.dkcr.dolphin.read_set_bit_in_bytes(CustomAddresses.LEVEL_CONNECTION, 10, level.level_map_index)
                    if self.ctx.smokey_peak_key_option == 0:
                        if self.dkcr.read_keys(GameWorlds.VOLCANO):
                            self.dkcr.dolphin.read_set_bit_in_bytes(CustomAddresses.LEVEL_CONNECTION, 10, level.level_map_index)
                case GameLevels.BOBBING_BASALT:
                    if True:
                        self.dkcr.dolphin.read_set_bit_in_bytes(CustomAddresses.LEVEL_CONNECTION, 10, level.level_map_index)
                case GameLevels.MOVING_MELTERS:
                    if True:
                        self.dkcr.dolphin.read_set_bit_in_bytes(CustomAddresses.LEVEL_CONNECTION, 10, level.level_map_index)
                case GameLevels.RED_RED_RISING:
                    if True:
                        self.dkcr.dolphin.read_set_bit_in_bytes(CustomAddresses.LEVEL_CONNECTION, 10, level.level_map_index)
                case GameLevels.FIVE_MONKEY_TRIAL:
                    if (self.dkcr.get_kl(GameWorlds.VOLCANO) >= self.ctx.volcano_k_level_access_option
                        or self.dkcr.get_k_level_unlock() >= 8
                    ):
                        self.dkcr.dolphin.read_set_bit_in_bytes(CustomAddresses.LEVEL_CONNECTION, 10, level.level_map_index)
                case GameLevels.TIKI_TONG_TERROR:
                    if (self.dkcr.get_pp() >= self.ctx.volcano_boss_access_option
                        or self.dkcr.get_boss_unlock() >= 8
                    ):
                        self.dkcr.dolphin.read_set_bit_in_bytes(CustomAddresses.LEVEL_CONNECTION, 10, level.level_map_index)
