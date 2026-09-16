from dataclasses import dataclass
from typing import Any

from Options import OptionGroup, PerGameCommonOptions, Range, Toggle, Visibility, Choice, OptionSet, DefaultOnToggle


class DeathLink(Toggle):
    """
    Syncing deaths among other clients that have this option enabled.
    """
    display_name = "Death Link"
    visibility = Visibility.none


class GoldenTemple(Toggle):
    """
    Adding the Golden Temple into the item pool.
    """
    display_name = "Golden Temple"

class RareOrbs(Range):
    """
    How many of the Rare Orbs found in K-levels are needed to enter the Golden Temple.
    """
    display_name = "Rare Orb amount"

    range_start = 0
    range_end = 8
    # This value can not exceed 8

    default = 8

class TimeAttackMedals(OptionSet):
    """
    Creates a location for each selected medal.

    "Bronze", "Silver", "Gold", and "Shiny Gold" always include their respective
    medals.
    "Full" includes all medals.

    "RandomAll" randomly selects additional medals from those not already selected.
    "RandomOne" randomly selects one additional medal from those not already
    selected.

    "Bronzeless", "Silverless", "Goldless", and "Shiny Goldless" restrict the
    random selection pool by excluding those medals. These options have no effect
    unless "RandomAll" or "RandomOne" is selected.

    If Time Attack clear type is not in generation, this option will be disregarded.
    """

    display_name = "Time Attack Medals"
    valid_keys = {
        "Bronze", "Silver", "Gold", "Shiny Gold", "Full", "RandomAll", "RandomOne",
        "Bronzeless", "Silverless", "Goldless", "Shiny Goldless"
    }

class KongLetterCollectionCheckpoint(Toggle):
    """
    Locations for Kong Letters will be sent after a checkpoint instead of when they are picked up.
    """

    display_name = "Kong Letter collection upon checkpoint"
    visibility = Visibility.none


class RandomizeLevels(Toggle):
    """
    When enabled, randomizes the levels with each other.
    Excludes K levels and Bosses.
    """
    display_name = "Randomize Levels"
    visibility = Visibility.none

class SmogClear(DefaultOnToggle):
    """
    When enabled, requires to beat 7-1 to clear the smog covering the Factory world to move through it.
    If disabled, DK will be able to traverse the Factory world even with the smog present.
    """
    display_name = "Smog Clear"

class LiftOffLaunch(DefaultOnToggle):
    """
    When enabled, requires to beat 7-R to access Feather Fiend.
    If disabled, DK will be able to access Feather Fiend without the need to beat 7-R.
    """
    display_name = "Lift-off Launch"

class FactoryButtons(Range):
    """
    Amount of Factory Buttons that are required to access 7-R. (Default = 3
    Choosing 0 will disable this option and make 7-R always available.
    """
    display_name = "Factory Buttons"
    range_start = 0
    range_end = 15
    # This value can not exceed 15

    default = 3

class Rambi(Toggle):
    """
    When enabled, locks Rambi behind the Rambi’s Saddle item.
    """
    display_name = "Rambi"
    visibility = Visibility.none


class Minecart(Toggle):
    """
    When enabled, Minecart levels and sections require the item Minecart Pass to access.
    """
    display_name = "Minecart"
    visibility = Visibility.none


class RocketBarrel(Toggle):
    """
    When enabled, Rocket Barrel levels and sections require the item Rocket Barrel Fuel to access.
    """
    display_name = "Rocket Barrel"
    visibility = Visibility.none


class KongBarrel(Toggle):
    """
    When enabled, requires the item Kong Barrel to be unlocked.
    """
    display_name = "Kong Barrel"
    visibility = Visibility.none


class Roll(Toggle):
    """
    When enabled, shuffles your ability to roll into the item pool.
    """
    display_name = "Randomize Roll"
    visibility = Visibility.none


class Grab(Toggle):
    """
    When enabled, shuffles your ability to grab into the item pool.
    """
    display_name = "Randomize Grab"
    visibility = Visibility.none


class Blow(Toggle):
    """
    When enabled, shuffles your ability to blow into the item pool.
    """
    display_name = "Randomize Blow"
    visibility = Visibility.none


class GroundPound(Toggle):
    """
    When enabled, shuffles your ability to Ground Pound into the item pool.
    """
    display_name = "Randomize Ground Pound"
    visibility = Visibility.none


class LevelClearType(OptionSet):
    """
    Creates a location for each selected level clear type.

    "Normal", "Time Attack" / "Time" and "Mirror Mode" / "Mirror" always include their respective
    clear types.
    "Full" includes all clear types.

    "RandomAll" randomly selects additional clear types from those not already selected.
    "RandomOne" randomly selects one additional clear type from those not already
    selected.

    "Normalless", "Time Attackless" / "Timeless" and "Mirror Modeless" / Mirrorless restrict the
    random selection pool by excluding those clear types. These options have no effect
    unless "RandomAll" or "RandomOne" is selected.
    """

    display_name = "Level Clear Type"
    valid_keys = {
        "Normal", "Time Attack", "Time", "Mirror Mode", "Mirror", "Full", "RandomAll", "RandomOne",
        "Normalless", "Time Attackless", "Timeless", "Mirror Modeless", "Mirrorless"
    }
    default = {"Normal"}

class KLevel(Toggle):
    """
    Creates Locations for the K Levels as well as for every Kong Letter.
    """
    display_name = "K Levels and Kong Letters"

class PuzzlePieces(Toggle):
    """
    Creates Locations for the Puzzle Pieces as well as setting Puzzle Pieces as a requirement to unlock the bosses.
    If this option is disabled, "Progressive Boss Unlock" Items will be put in pool instead.
    """
    display_name = "Puzzle Pieces and Boss Unlocks"

class WorldPuzzlePieceBundle(Toggle):
    """
    Creates locations for each world for getting every puzzle piece location in that world.
    """
    display_name = "World Puzzle Piece Bundle"
    visibility = Visibility.none

class WorldKongBundle(Toggle):
    """
    Creates locations for each world for getting every kong letter location in that world.
    The K Level option takes priority over this.
    """
    display_name = "World Kong Bundle"
    visibility = Visibility.none

class WorldCleared(Toggle):
    """
    Creates locations for each world for clearing every level in that world.
    The "Level Clear Type" option takes priority over this.
    """
    display_name = "World Cleared"
    visibility = Visibility.none

class WorldClearedMirror(Toggle):
    """
    Creates locations for each world for clearing every level in mirror mode in that world.
    The "Level Clear Type" option takes priority over this.
    """
    display_name = "World Cleared Mirror"
    visibility = Visibility.none

class WorldClearedTimeAttack(Toggle):
    """
    Creates locations for each world for clearing every level in time attack with the set medal in that world.
    The "Level Clear Type" option takes priority over this.
    """
    display_name = "World Cleared Time Attack"
    visibility = Visibility.none


class MirrorModeShards(Range):
    """
    Decides how many Mirror Shards are needed to unlock Mirror Mode.
    Setting this option to 0 will disable the Mirror Shards and Mirror Mode will get its own item.
    If Mirror Mode clear type is not in generation is option will be disregarded.
    """
    display_name = "Mirror Mode Shard amount"

    range_start = 0
    range_end = 15
    default = 8

class Squawks(Toggle):
    """
    Adds Squawks as an item which will enable Squawks as a permanent helper.
    Disabling this option makes Squawks available from the start.
    Squawks can be toggled in the Client as soon as he is available.
    """
    display_name = "Feathery Companion"

class SunsetShoreKey(DefaultOnToggle):
    """
    When enabled, adds the Jungle Shop Key for the level Sunset Shore as a location.
    """
    display_name = "Sunset Shore Key"


class BlowholeBoundKey(DefaultOnToggle):
    """
    When enabled, adds the Beach Shop Key for the level Blowhole Bound as a location.
    """
    display_name = "Blowhole Bound Key"


class DampDungeonKey(DefaultOnToggle):
    """
    When enabled, adds the Ruins Shop Key for the level Damp Dungeon as a location.
    """
    display_name = "Damp Dungeon Key"


class MolePatrolKey(DefaultOnToggle):
    """
    When enabled, adds the Cave Shop Key for the level Mole Patrol as a location.
    """
    display_name = "Mole Patrol Key"


class SpringySporesKey(DefaultOnToggle):
    """
    When enabled, adds the Forest Shop Key for the level Springy Spores as a location.
    """
    display_name = "Springy Spores Key"


class PrecariousPlateauKey(DefaultOnToggle):
    """
    When enabled, adds the Cliff Shop Key for the level Precarious Plateau as a location.
    """
    display_name = "Precarious Plateau Key"


class HandyHazardsKey(DefaultOnToggle):
    """
    When enabled, adds the Factory Shop Key for the level Handy Hazards as a location.
    """
    display_name = "Handy Hazards Key"


class SmokeyPeakKey(DefaultOnToggle):
    """
    When enabled, adds the Volcano Shop Key for the level Smokey Peak as a location.
    """
    display_name = "Smokey Peak Key"


class JungleBossAccess(Range):
    """
    Sets the amount of total Puzzle Pieces needed to gain access to the Boss in the Jungle.
    The "Puzzle Piece" option takes priority over this option.
    """
    display_name = "Puzzle Piece requirement for Mugly's Mound"

    range_start = 0
    range_end = 40

    default = 20


class BeachBossAccess(Range):
    """
    Sets the amount of total Puzzle Pieces needed to gain access to the Boss in the Beach.
    The "Puzzle Piece" option takes priority over this option.
    """
    display_name = "Puzzle Piece requirement for Pinchin' Pirates"

    range_start = 0
    range_end = 80

    default = 45


class RuinsBossAccess(Range):
    """
    Sets the amount of total Puzzle Pieces needed to gain access to the Boss in the Ruins.
    The "Puzzle Piece" option takes priority over this option.
    """
    display_name = "Puzzle Piece requirement for Ruined Roost"

    range_start = 0
    range_end = 120

    default = 70


class CaveBossAccess(Range):
    """
    Sets the amount of total Puzzle Pieces needed to gain access to the Boss in the Cave.
    The "Puzzle Piece" option takes priority over this option.
    """
    display_name = "Puzzle Piece requirement for The Mole Train"

    range_start = 0
    range_end = 160

    default = 100


class ForestBossAccess(Range):
    """
    Sets the amount of total Puzzle Pieces needed to gain access to the Boss in the Forest.
    The "Puzzle Piece" option takes priority over this option.
    """
    display_name = "Puzzle Piece requirement for Mangoruby Run"

    range_start = 0
    range_end = 210

    default = 135


class CliffBossAccess(Range):
    """
    Sets the amount of total Puzzle Pieces needed to gain access to the Boss in the Cliff.
    The "Puzzle Piece" option takes priority over this option.
    """
    display_name = "Puzzle Piece requirement for Thugly's Highrise"

    range_start = 0
    range_end = 260

    default = 175


class FactoryBossAccess(Range):
    """
    Sets the amount of total Puzzle Pieces needed to gain access to the Boss in the Factory.
    The "Puzzle Piece" option takes priority over this option.
    """
    display_name = "Puzzle Piece requirement for Feather Fiend"

    range_start = 0
    range_end = 310

    default = 225


class VolcanoBossAccess(Range):
    """
    Sets the amount of total Puzzle Pieces needed to gain access to the Boss in the Volcano.
    The "Puzzle Piece" option takes priority over this option.
    """
    display_name = "Puzzle Piece requirement for Tiki Tong Terror"

    range_start = 0
    range_end = 340

    default = 290


class JungleKLevelAccess(Range):
    """
    Sets the amount of total Kong Letters, from the respective, World needed to gain access to the K Level in the Jungle.
    """
    display_name = "Kong Letter requirement for Platform Panic"

    range_start = 0
    range_end = 24
    # This Value can not exceed 24

    default = 12


class BeachKLevelAccess(Range):
    """
    Sets the amount of total Kong Letters, from the respective, World needed to gain access to the K Level in the Beach.
    """
    display_name = "Kong Letter requirement for Tumblin' Temple"

    range_start = 0
    range_end = 28
    # This Value can not exceed 28

    default = 14


class RuinsKLevelAccess(Range):
    """
    Sets the amount of total Kong Letters, from the respective, World needed to gain access to the K Level in the Ruins.
    """
    display_name = "Kong Letter requirement for Shifty Smashers"

    range_start = 0
    range_end = 24
    # This Value can not exceed 24

    default = 12


class CaveKLevelAccess(Range):
    """
    Sets the amount of total Kong Letters, from the respective, World needed to gain access to the K Level in the Cave.
    """
    display_name = "Kong Letter requirement for Jagged Jewels"

    range_start = 0
    range_end = 20
    # This Value can not exceed 20

    default = 10


class ForestKLevelAccess(Range):
    """
    Sets the amount of total Kong Letters, from the respective, World needed to gain access to the K Level in the Forest.
    """
    display_name = "Kong Letter requirement for Blast & Bounce"

    range_start = 0
    range_end = 32
    # This Value can not exceed 32

    default = 16


class CliffKLevelAccess(Range):
    """
    Sets the amount of total Kong Letters, from the respective, World needed to gain access to the K Level in the Cliff.
    """
    display_name = "Kong Letter requirement for Perilous Passage"

    range_start = 0
    range_end = 32
    # This Value can not exceed 32

    default = 16


class FactoryKLevelAccess(Range):
    """
    Sets the amount of total Kong Letters, from the respective, World needed to gain access to the K Level in the Factory.
    """
    display_name = "Kong Letter requirement for Treacherous Track"

    range_start = 0
    range_end = 28
    # This Value can not exceed 28

    default = 14


class VolcanoKLevelAccess(Range):
    """
    Sets the amount of total Kong Letters, from the respective, World needed to gain access to the K Level in the Volcano.
    """
    display_name = "Kong Letter requirement for Five Monkey Trial"

    range_start = 0
    range_end = 28
    # This Value can not exceed 28

    default = 14


@dataclass
class DKCROptions(PerGameCommonOptions):
    death_link: DeathLink
    golden_temple: GoldenTemple
    rare_orbs: RareOrbs
    time_attack_medal: TimeAttackMedals
    kong_letter_collection_checkpoint: KongLetterCollectionCheckpoint
    randomize_levels: RandomizeLevels
    smog_clear: SmogClear
    lift_off_launch: LiftOffLaunch
    factory_buttons: FactoryButtons
    rambi: Rambi
    minecart: Minecart
    rocket_barrel: RocketBarrel
    kong_barrel: KongBarrel
    roll: Roll
    grab: Grab
    blow: Blow
    ground_pound: GroundPound
    level_clear_type: LevelClearType
    k_level: KLevel
    puzzle_pieces: PuzzlePieces
    world_puzzle_piece_bundle: WorldPuzzlePieceBundle
    world_kong_bundle: WorldKongBundle
    world_cleared: WorldCleared
    world_cleared_mirror: WorldClearedMirror
    world_cleared_time_attack: WorldClearedTimeAttack
    mirror_mode_shards: MirrorModeShards
    squawks: Squawks
    sunset_shore_key: SunsetShoreKey
    blowhole_bound_key: BlowholeBoundKey
    damp_dungeon_key: DampDungeonKey
    mole_patrol_key: MolePatrolKey
    springy_spores_key: SpringySporesKey
    precarious_plateau_key: PrecariousPlateauKey
    handy_hazards_key: HandyHazardsKey
    smokey_peak_key: SmokeyPeakKey
    jungle_boss_access: JungleBossAccess
    beach_boss_access: BeachBossAccess
    ruins_boss_access: RuinsBossAccess
    cave_boss_access: CaveBossAccess
    forest_boss_access: ForestBossAccess
    cliff_boss_access: CliffBossAccess
    factory_boss_access: FactoryBossAccess
    volcano_boss_access: VolcanoBossAccess
    jungle_k_level_access: JungleKLevelAccess
    beach_k_level_access: BeachKLevelAccess
    ruins_k_level_access: RuinsKLevelAccess
    cave_k_level_access: CaveKLevelAccess
    forest_k_level_access: ForestKLevelAccess
    cliff_k_level_access: CliffKLevelAccess
    factory_k_level_access: FactoryKLevelAccess
    volcano_k_level_access: VolcanoKLevelAccess

    def get_slot_data_dict(self) -> dict[str, Any]:
        return self.as_dict(
            "death_link",
            "golden_temple",
            "rare_orbs",
            "time_attack_medal",
            "kong_letter_collection_checkpoint",
            "randomize_levels",
            "smog_clear",
            "lift_off_launch",
            "factory_buttons",
            "rambi",
            "minecart",
            "rocket_barrel",
            "kong_barrel",
            "roll",
            "grab",
            "blow",
            "ground_pound",
            "level_clear_type",
            "k_level",
            "puzzle_pieces",
            "world_puzzle_piece_bundle",
            "world_kong_bundle",
            "world_cleared",
            "world_cleared_mirror",
            "world_cleared_time_attack",
            "mirror_mode_shards",
            "squawks",
            "sunset_shore_key",
            "blowhole_bound_key",
            "damp_dungeon_key",
            "mole_patrol_key",
            "springy_spores_key",
            "precarious_plateau_key",
            "handy_hazards_key",
            "smokey_peak_key",
            "jungle_boss_access",
            "beach_boss_access",
            "ruins_boss_access",
            "cave_boss_access",
            "forest_boss_access",
            "cliff_boss_access",
            "factory_boss_access",
            "volcano_boss_access",
            "jungle_k_level_access",
            "beach_k_level_access",
            "ruins_k_level_access",
            "cave_k_level_access",
            "forest_k_level_access",
            "cliff_k_level_access",
            "factory_k_level_access",
            "volcano_k_level_access",
        )


option_groups = [
    OptionGroup(
        "Gameplay options",
        [DeathLink, GoldenTemple, RareOrbs, RandomizeLevels, KongLetterCollectionCheckpoint, TimeAttackMedals, LevelClearType]
    ),
    OptionGroup(
        "Key options",
        [SunsetShoreKey, BlowholeBoundKey, DampDungeonKey, MolePatrolKey, SpringySporesKey, PrecariousPlateauKey,
         HandyHazardsKey, SmokeyPeakKey]
    ),
    OptionGroup(
        "World options",
        [WorldPuzzlePieceBundle, WorldKongBundle, WorldCleared, WorldClearedMirror, WorldClearedTimeAttack]
    ),
    OptionGroup(
        "Boss access options",
        [PuzzlePieces ,JungleBossAccess, BeachBossAccess, RuinsBossAccess, CaveBossAccess, ForestBossAccess, CliffBossAccess,
         FactoryBossAccess, VolcanoBossAccess]
    ),
    OptionGroup(
        "K Level access options",
        [KLevel, JungleKLevelAccess, BeachKLevelAccess, RuinsKLevelAccess, CaveKLevelAccess, ForestKLevelAccess, CliffKLevelAccess,
         FactoryKLevelAccess, VolcanoKLevelAccess]
    ),
    OptionGroup(
        "Moveset options",
        [Roll, Grab, Blow, GroundPound]
    ),
    OptionGroup(
        "Misc options",
        [SmogClear, LiftOffLaunch, FactoryButtons, Rambi, Minecart, RocketBarrel, KongBarrel, Squawks]
    ),
    OptionGroup(
        "Mirror mode options",
        [MirrorModeShards]
    )
]


def handle_ut_yamless(dkcr_world, slot_data: dict[str, Any] | None) -> dict[str, Any] | None:
    if (
            not slot_data
            and hasattr(dkcr_world.multiworld, "re_gen_passthrough")
            and isinstance(dkcr_world.multiworld.re_gen_passthrough, dict)
            and dkcr_world.game in dkcr_world.multiworld.re_gen_passthrough
    ):
        slot_data = dkcr_world.multiworld.re_gen_passthrough[dkcr_world.game]

    if not slot_data:
        return None

    dkcr_world.ut_medals = set(slot_data["time_attack_resolved"])
    dkcr_world.options.smog_clear.value = slot_data["smog_clear"]
    dkcr_world.options.lift_off_launch.value = slot_data["lift_off_launch"]
    dkcr_world.options.factory_buttons.value = slot_data["factory_buttons"]
    dkcr_world.ut_level_clear_types = set(slot_data["level_clear_type_resolved"])
    dkcr_world.options.mirror_mode.value = slot_data["mirror_mode"]
    dkcr_world.options.mirror_mode_shards.value = slot_data["mirror_mode_shards"]
    dkcr_world.options.squawks.value = slot_data["squawks"]
    dkcr_world.options.sunset_shore_key.value = slot_data["sunset_shore_key"]
    dkcr_world.options.blowhole_bound_key.value = slot_data["blowhole_bound_key"]
    dkcr_world.options.damp_dungeon_key.value = slot_data["damp_dungeon_key"]
    dkcr_world.options.mole_patrol_key.value = slot_data["mole_patrol_key"]
    dkcr_world.options.springy_spores_key.value = slot_data["springy_spores_key"]
    dkcr_world.options.precarious_plateau_key.value = slot_data["precarious_plateau_key"]
    dkcr_world.options.handy_hazards_key.value = slot_data["handy_hazards_key"]
    dkcr_world.options.smokey_peak_key.value = slot_data["smokey_peak_key"]
    dkcr_world.options.jungle_boss_access.value = slot_data["jungle_boss_access"]
    dkcr_world.options.beach_boss_access.value = slot_data["beach_boss_access"]
    dkcr_world.options.ruins_boss_access.value = slot_data["ruins_boss_access"]
    dkcr_world.options.cave_boss_access.value = slot_data["cave_boss_access"]
    dkcr_world.options.forest_boss_access.value = slot_data["forest_boss_access"]
    dkcr_world.options.cliff_boss_access.value = slot_data["cliff_boss_access"]
    dkcr_world.options.factory_boss_access.value = slot_data["factory_boss_access"]
    dkcr_world.options.volcano_boss_access.value = slot_data["volcano_boss_access"]
    dkcr_world.options.jungle_k_level_access.value = slot_data["jungle_k_level_access"]
    dkcr_world.options.beach_k_level_access.value = slot_data["beach_k_level_access"]
    dkcr_world.options.ruins_k_level_access.value = slot_data["ruins_k_level_access"]
    dkcr_world.options.cave_k_level_access.value = slot_data["cave_k_level_access"]
    dkcr_world.options.forest_k_level_access.value = slot_data["forest_k_level_access"]
    dkcr_world.options.cliff_k_level_access.value = slot_data["cliff_k_level_access"]
    dkcr_world.options.factory_k_level_access.value = slot_data["factory_k_level_access"]
    dkcr_world.options.volcano_k_level_access.value = slot_data["volcano_k_level_access"]

    return slot_data