from .dolphin import Dolphin
from ..data import LevelData, Medals
from ..data.constants.addresses.pal import PALAddresses
from ..data.constants.dkcr_version import DKCRVersion
from ..data.constants.addresses.ntscu_rev_1 import NTSCUAddresses
from ..data.constants.addresses.custom import CustomAddresses
from ..data.constants.game_states import State
from ..data.items import GameItems
from ..data.worlds import GameWorlds


class DKCRGame:
    def __init__(self, dolphin: Dolphin) -> None:
        self.dolphin = dolphin
        self.version: DKCRVersion | None = None
        self.addresses = None

    def connect(self) -> bool:
        if not self.dolphin.connect():
            return False

        if self.version is None:
            self.version = self.dolphin.get_version()

            if self.version == DKCRVersion.NTSC_U_REV_1:
                self.addresses = NTSCUAddresses
            elif self.version == DKCRVersion.PAL:
                self.addresses = PALAddresses
            else:
                return False

        return True

    def check_in_rom(self) -> bool:
        try:
            self.dolphin.read_bytes(self.addresses.GAME_ID, 6)
        except RuntimeError:
            if self.dolphin.connect():
                self.dolphin.disconnect()
            return False
        return True

    def get_game_state(self) -> State:
        return State(
            self.dolphin.read_word(
                self.addresses.GAME_STATE
            )
        )

    def is_in_level(self) -> bool:
        return self.get_game_state() == State.IN_LEVEL

    def is_in_world_map(self) -> bool:
        state = self.get_game_state()
        return state == State.WORLD_MAP or state == State.WORLD_MAP_AFTER_QUIT

    def is_quit_from_game_over(self) -> bool:
        return self.get_game_state() == State.QUIT_GAME_OVER

    def is_in_title(self) -> bool:
        return self.get_game_state() == State.TITLE

    def is_in_super_guide(self) -> bool:
        return self.get_game_state() == State.SUPER_GUIDE

    def is_in_time_attack(self) -> bool:
        return self.get_game_state() == State.TIME_ATTACK

    def in_pre_rendered_cutscene(self) -> bool:
        return self.dolphin.read_word(self.addresses.IN_PRE_RENDERED_CUTSCENE) == 1

    def cutscene_identifier(self):
        return self.dolphin.read_word(self.addresses.CUTSCENE_IDENTIFIER)

    def in_victory_cutscene(self) -> bool:
        identifier = self.cutscene_identifier()
        victory_solo = 0x31b100
        victory_duo = 0x31b900
        return identifier == victory_solo or identifier == victory_duo

    def get_current_level(self) -> int:
        return self.dolphin.read_word(
            self.addresses.LEVEL_NUMBER
        )

    def get_current_world(self) -> int:
        return self.dolphin.read_word(
            self.addresses.WORLD_OF_CURRENT_LEVEL
        )

    def get_current_level_data(self, world: int | None = None, level: int | None = None) -> "LevelData":
        if not world:
            world = self.get_current_world()
        if not level:
            level = self.get_current_level()

        offset = GameWorlds.get_level_offset_from_world_and_level_index(world, level)

        level_data = self.dolphin.read_word(
            self.addresses.LEVEL_DATA_POINTER
        )

        specific_level_data = self.dolphin.read_word(
            level_data + offset
        )

        return LevelData(
            self.dolphin.read_byte(specific_level_data + 0x3e),
            self.dolphin.read_byte(specific_level_data + 0x3d)
        )

    def get_current_level_puzzle_piece_bitfield(self):
        return self.dolphin.read_word(CustomAddresses.CURRENT_LEVEL_PP)

    def reset_custom_pp(self):
        self.dolphin.write_word(CustomAddresses.CURRENT_LEVEL_PP, 0x0)

    def add_bananas(self, amount: int):
        current_bananas = self.dolphin.read_word(self.addresses.BANANAS)
        new_amount = current_bananas + amount
        extra_lives_to_get = 0
        while new_amount >= 100:
            new_amount -= 100
            extra_lives_to_get += 1

        self.dolphin.write_word(self.addresses.BANANAS, new_amount)

        if extra_lives_to_get > 0:
            self.add_extra_lives(extra_lives_to_get)

    def add_banana_coins(self, amount: int):
        current_coins = self.dolphin.read_word(self.addresses.BANANA_COINS)
        new_amount = current_coins + amount
        if new_amount > 999:
            new_amount = 999

        self.dolphin.write_word(self.addresses.BANANA_COINS, new_amount)

    def add_extra_lives(self, amount: int):
        current_extra_lives = self.dolphin.read_word(self.addresses.LIVES)
        new_amount = current_extra_lives + amount
        if new_amount > 99:
            new_amount = 99

        self.dolphin.write_word(self.addresses.LIVES, new_amount)

    def add_recovery_heart(self):
        current_health_dk = self.dolphin.read_word(self.addresses.DK_HEALTH)
        current_health_dd = self.dolphin.read_word(self.addresses.DD_HEALTH)
        dk_has_heart_boost = self.dolphin.read_word(self.addresses.DK_HEART_BOOST_EQUIPPED)
        dd_has_heart_boost = self.dolphin.read_word(self.addresses.DIDDY_HEART_BOOST_EQUIPPED)
        if current_health_dk == 1:
            self.dolphin.write_word(self.addresses.DK_HEALTH, 2)
            return
        elif current_health_dk == 2 and dk_has_heart_boost == 1:
            self.dolphin.write_word(self.addresses.DK_HEALTH, 3)
            return
        if current_health_dd == 1:
            self.dolphin.write_word(self.addresses.DD_HEALTH, 2)
            return
        elif current_health_dd == 2 and dd_has_heart_boost == 1:
            self.dolphin.write_word(self.addresses.DD_HEALTH, 3)

    def get_k_letter(self) -> int:
        return self.dolphin.read_byte(self.addresses.K_LETTER)

    def get_o_letter(self) -> int:
        return self.dolphin.read_byte(self.addresses.O_LETTER)

    def get_n_letter(self) -> int:
        return self.dolphin.read_byte(self.addresses.N_LETTER)

    def get_g_letter(self) -> int:
        return self.dolphin.read_byte(self.addresses.G_LETTER)

    def get_all_letters(self) -> list[int]:
        return [self.get_k_letter(), self.get_o_letter(), self.get_n_letter(), self.get_g_letter()]

    def get_squawks_state(self) -> int:
        return self.dolphin.read_word(self.addresses.SQUAWKS_EQUIPPED)

    def get_dk_heart_boost_state(self) -> int:
        return self.dolphin.read_word(self.addresses.DK_HEART_BOOST_EQUIPPED)

    def get_dd_heart_boost_state(self) -> int:
        return self.dolphin.read_word(self.addresses.DIDDY_HEART_BOOST_EQUIPPED)

    def get_mirror_mode_state(self) -> int:
        return self.dolphin.read_word(self.addresses.MIRROR_MODE_ACTIVE)

    def add_pp(self):
        self.dolphin.read_add_write_bytes(CustomAddresses.PP_AMOUNT, 2, 1)

    def get_pp(self) -> int:
        return int.from_bytes(self.dolphin.read_bytes(CustomAddresses.PP_AMOUNT, 2))

    def add_kl(self, item: GameItems):
        match item:
            case GameItems.KONG_LETTER_JUNGLE:
                self.dolphin.read_add_write_byte(CustomAddresses.KL_JGL, 0x1)
            case GameItems.KONG_LETTER_BEACH:
                self.dolphin.read_add_write_byte(CustomAddresses.KL_BCH, 0x1)
            case GameItems.KONG_LETTER_RUINS:
                self.dolphin.read_add_write_byte(CustomAddresses.KL_RNS, 0x1)
            case GameItems.KONG_LETTER_CAVE:
                self.dolphin.read_add_write_byte(CustomAddresses.KL_CVE, 0x1)
            case GameItems.KONG_LETTER_FOREST:
                self.dolphin.read_add_write_byte(CustomAddresses.KL_FRS, 0x1)
            case GameItems.KONG_LETTER_CLIFF:
                self.dolphin.read_add_write_byte(CustomAddresses.KL_CLF, 0x1)
            case GameItems.KONG_LETTER_FACTORY:
                self.dolphin.read_add_write_byte(CustomAddresses.KL_FCT, 0x1)
            case GameItems.KONG_LETTER_VOLCANO:
                self.dolphin.read_add_write_byte(CustomAddresses.KL_VLC, 0x1)

    def get_kl(self, world: GameWorlds):
        match world:
            case GameWorlds.JUNGLE:
                return self.dolphin.read_byte(CustomAddresses.KL_JGL)
            case GameWorlds.BEACH:
                return self.dolphin.read_byte(CustomAddresses.KL_BCH)
            case GameWorlds.RUINS:
                return self.dolphin.read_byte(CustomAddresses.KL_RNS)
            case GameWorlds.CAVE:
                return self.dolphin.read_byte(CustomAddresses.KL_CVE)
            case GameWorlds.FOREST:
                return self.dolphin.read_byte(CustomAddresses.KL_FRS)
            case GameWorlds.CLIFF:
                return self.dolphin.read_byte(CustomAddresses.KL_CLF)
            case GameWorlds.FACTORY:
                return self.dolphin.read_byte(CustomAddresses.KL_FCT)
            case GameWorlds.VOLCANO:
                return self.dolphin.read_byte(CustomAddresses.KL_VLC)

    def read_keys(self, world: GameWorlds) -> bool:
        match world:
            case GameWorlds.JUNGLE:
                return self.dolphin.read_byte(self.addresses.JUNGLE_KEY) == 1
            case GameWorlds.BEACH:
                return self.dolphin.read_byte(self.addresses.BEACH_KEY) == 1
            case GameWorlds.RUINS:
                return self.dolphin.read_byte(self.addresses.RUINS_KEY) == 1
            case GameWorlds.CAVE:
                return self.dolphin.read_byte(self.addresses.CAVE_KEY) == 1
            case GameWorlds.FOREST:
                return self.dolphin.read_byte(self.addresses.FOREST_KEY) == 1
            case GameWorlds.CLIFF:
                return self.dolphin.read_byte(self.addresses.CLIFF_KEY) == 1
            case GameWorlds.FACTORY:
                return self.dolphin.read_byte(self.addresses.FACTORY_KEY) == 1
            case GameWorlds.VOLCANO:
                return self.dolphin.read_byte(self.addresses.VOLCANO_KEY) == 1
        return False

    def add_key(self, item: GameItems):
        match item:
            case GameItems.JUNGLE_KEY:
                self.dolphin.read_or_write_byte(CustomAddresses.KEYS, 0b1)
            case GameItems.BEACH_KEY:
                self.dolphin.read_or_write_byte(CustomAddresses.KEYS, 0b10)
            case GameItems.RUINS_KEY:
                self.dolphin.read_or_write_byte(CustomAddresses.KEYS, 0b100)
            case GameItems.CAVE_KEY:
                self.dolphin.read_or_write_byte(CustomAddresses.KEYS, 0b1000)
            case GameItems.FOREST_KEY:
                self.dolphin.read_or_write_byte(CustomAddresses.KEYS, 0b10000)
            case GameItems.CLIFF_KEY:
                self.dolphin.read_or_write_byte(CustomAddresses.KEYS, 0b100000)
            case GameItems.FACTORY_KEY:
                self.dolphin.read_or_write_byte(CustomAddresses.KEYS, 0b1000000)
            case GameItems.VOLCANO_KEY:
                self.dolphin.read_or_write_byte(CustomAddresses.KEYS, 0b10000000)

    def has_key(self, world: GameWorlds):
        match world:
            case GameWorlds.JUNGLE:
                return self.dolphin.read_byte(CustomAddresses.KEYS) & 0b1
            case GameWorlds.BEACH:
                return self.dolphin.read_byte(CustomAddresses.KEYS) & 0b10
            case GameWorlds.RUINS:
                return self.dolphin.read_byte(CustomAddresses.KEYS) & 0b100
            case GameWorlds.CAVE:
                return self.dolphin.read_byte(CustomAddresses.KEYS) & 0b1000
            case GameWorlds.FOREST:
                return self.dolphin.read_byte(CustomAddresses.KEYS) & 0b10000
            case GameWorlds.CLIFF:
                return self.dolphin.read_byte(CustomAddresses.KEYS) & 0b100000
            case GameWorlds.FACTORY:
                return self.dolphin.read_byte(CustomAddresses.KEYS) & 0b1000000
            case GameWorlds.VOLCANO:
                return self.dolphin.read_byte(CustomAddresses.KEYS) & 0b10000000

    def get_keys(self) -> set[int]:
        key_ids: set[int] = set()
        if self.read_keys(GameWorlds.JUNGLE):
            key_ids.add(0x10000 * GameWorlds.JUNGLE.world_index + 0x100 * 0xB + 0x41)
        if self.read_keys(GameWorlds.BEACH):
            key_ids.add(0x10000 * GameWorlds.BEACH.world_index + 0x100 * 0xB + 0x41)
        if self.read_keys(GameWorlds.RUINS):
            key_ids.add(0x10000 * GameWorlds.RUINS.world_index + 0x100 * 0xB + 0x41)
        if self.read_keys(GameWorlds.CAVE):
            key_ids.add(0x10000 * GameWorlds.CAVE.world_index + 0x100 * 0xB + 0x41)
        if self.read_keys(GameWorlds.FOREST):
            key_ids.add(0x10000 * GameWorlds.FOREST.world_index + 0x100 * 0xB + 0x41)
        if self.read_keys(GameWorlds.CLIFF):
            key_ids.add(0x10000 * GameWorlds.CLIFF.world_index + 0x100 * 0xB + 0x41)
        if self.read_keys(GameWorlds.FACTORY):
            key_ids.add(0x10000 * GameWorlds.FACTORY.world_index + 0x100 * 0xB + 0x41)
        if self.read_keys(GameWorlds.VOLCANO):
            key_ids.add(0x10000 * GameWorlds.VOLCANO.world_index + 0x100 * 0xB + 0x41)
        return key_ids

    def get_medals(self, base_address: int, world: int | None = None, level: int | None = None):
        level_data = self.get_current_level_data(world, level)

        if level_data.medal.check_count < 0: return set()

        locations_to_send = {
            base_address + offset
            for offset in range(0x23, 0x23 + level_data.medal.check_count)
        }

        return locations_to_send

    def add_orb(self):
        self.dolphin.read_add_write_byte(CustomAddresses.ORBS, 1)

    def add_factory_button(self):
        self.dolphin.read_add_write_byte(CustomAddresses.FACTORY_BUTTONS, 1)

    def get_factory_button(self):
        return self.dolphin.read_byte(CustomAddresses.FACTORY_BUTTONS)

    def add_boss_unlock(self):
        self.dolphin.read_add_write_byte(CustomAddresses.BOSS_UNLOCK, 1)

    def get_boss_unlock(self) -> int:
        return self.dolphin.read_byte(CustomAddresses.BOSS_UNLOCK)

    def add_k_level_unlock(self):
        self.dolphin.read_add_write_byte(CustomAddresses.K_LEVEL_UNLOCK, 1)

    def get_k_level_unlock(self) -> int:
        return self.dolphin.read_byte(CustomAddresses.K_LEVEL_UNLOCK)

    def add_mirror_shard(self):
        self.dolphin.read_add_write_byte(CustomAddresses.MIRROR_SHARDS, 1)

    def set_mirror_mode(self):
        self.dolphin.read_add_write_byte(CustomAddresses.MIRROR_SHARDS, 1)

    def get_mirror_mode(self):
        return self.dolphin.read_byte(CustomAddresses.MIRROR_SHARDS)

    def enable_mirror_mode(self):
        self.dolphin.write_word(self.addresses.MIRROR_MODE_UNLOCKED, 1)

    def set_squawks(self):
        self.dolphin.read_add_write_byte(CustomAddresses.SQUAWKS, 1)

    def get_world_bundles(self, world: int) -> set[int]:
        locations_to_send: set[int] = set()
        game_world: GameWorlds = GameWorlds.get_world_from_world_index(world)
        puzzle_piece_set_checker: list[bool] = []
        kong_letter_set_checker: list[bool] = []
        level_clear_checker: list[bool] = []
        level_clear_mirror_checker: list[bool] = []
        level_clear_time_attack_checker_bronze: list[bool] = []
        level_clear_time_attack_checker_silver: list[bool] = []
        level_clear_time_attack_checker_gold: list[bool] = []
        level_clear_time_attack_checker_shiny_gold: list[bool] = []
        for level in game_world.level_list:
            if level.level_index == 0xB: # Skip shop
                continue
            level_data = self.get_current_level_data(world, level.level_index)
            level_clear_checker.append(level_data.level_cleared)
            if level.level_index == 0xA: # Skip 7-R
                continue
            level_clear_mirror_checker.append(level_data.mirror_mode_cleared)
            level_clear_time_attack_checker_bronze.append(level_data.medal.value >= Medals.Bronze.value != Medals.Empty.value)
            level_clear_time_attack_checker_silver.append(level_data.medal.value >= Medals.Silver.value != Medals.Empty.value)
            level_clear_time_attack_checker_gold.append(level_data.medal.value >= Medals.Gold.value != Medals.Empty.value)
            level_clear_time_attack_checker_shiny_gold.append(level_data.medal.value >= Medals.Shiny_Gold.value != Medals.Empty.value)
            if level.level_index == 0x1: # Skip Levels without puzzle pieces and kong letters
                continue
            puzzle_piece_set_checker.append(level_data.all_puzzle_pieces_collected)
            if level.level_index == 0x0: # Skip Level without kong letters
                continue
            kong_letter_set_checker.append(level_data.kong_collected)

        base_address = 0x10000 * world + world + 0xF * 0x100

        if all(puzzle_piece_set_checker):
            locations_to_send.add(base_address + 0xB)
        if all(kong_letter_set_checker):
            locations_to_send.add(base_address + 0x1B)
        if all(level_clear_checker):
            locations_to_send.add(base_address + 0x21)
        if all(level_clear_mirror_checker):
            locations_to_send.add(base_address + 0x22)
        if all(level_clear_time_attack_checker_bronze):
            locations_to_send.add(base_address + 0x23)
        if all(level_clear_time_attack_checker_silver):
            locations_to_send.add(base_address + 0x24)
        if all(level_clear_time_attack_checker_gold):
            locations_to_send.add(base_address + 0x25)
        if all(level_clear_time_attack_checker_shiny_gold):
            locations_to_send.add(base_address + 0x26)

        return locations_to_send
