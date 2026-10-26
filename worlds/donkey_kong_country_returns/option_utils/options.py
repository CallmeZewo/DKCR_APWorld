from dataclasses import dataclass
from typing import Any

from Options import OptionGroup, PerGameCommonOptions, Range, Toggle, Visibility, Choice, OptionSet, DefaultOnToggle


class Goal(Choice):
    """
    Required end goal to beat the game.
    Tiki Tong Terror: defeat the end boss in 8-B
    Golden Temple: clear the golden temple
    All K Level: clear every K Level
    """
    option_tiki_tong_terror = 0
    option_golden_temple = 1
    # option_all_k_level = 2
    # option_all_bosses = 3
    # option_all_level = 4
    # option_all_kong_letter = 5
    # option_all_puzzle_pieces = 6
    # planned
    default = 0

class DeathLink(Toggle):
    """
    Syncing deaths among other clients that have this option enabled.
    """
    display_name = "Death Link"
    visibility = Visibility.none


class GoldenTemple(Toggle):
    """
    Golden Temple is randomized.
    """
    display_name = "Include Golden Temple"
    visibility = Visibility.none

class RareOrbs(Range):
    """
    How many of the Rare Orbs usually found in K-levels are needed to enter the Golden Temple.
    """
    display_name = "Required Rare Orb amount for Golden Temple"

    range_start = 0
    range_end = 8
    # This value can not exceed 8

    default = 6

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
    default = {"Bronze"}

class KongLetterCollectionCheckpoint(Toggle):
    """
    Locations for Kong Letters will be sent after a checkpoint instead of when they are picked up.
    """

    display_name = "Kong Letter collection upon checkpoint"
    visibility = Visibility.none


class RandomizeLevels(Toggle):
    """
    When enabled, randomizes levels with levels of the same type.
    """
    display_name = "Randomize Levels"
    visibility = Visibility.none

class SmogClear(DefaultOnToggle):
    """
    When enabled, requires to beat 7-1 to clear the smog covering the Factory world to move through it.
    If disabled, DK will be able to traverse the Factory world even with the smog present.
    """
    display_name = "Smog Clear required for Factory access"

class LiftOffLaunch(DefaultOnToggle):
    """
    When enabled, requires to beat 7-R to access Feather Fiend.
    If disabled, DK will be able to access Feather Fiend without the need to beat 7-R.
    """
    display_name = "Lift-off Launch required for Feather Fiend access"

class FactoryButtons(Range):
    """
    Amount of Factory Buttons that are required to access 7-R.
    Choosing 0 will disable this option and make 7-R always available.
    """
    display_name = "Factory Button requirement for Lift-off Launch"
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

    display_name = "Level Clear Types"
    valid_keys = {
        "Normal", "Time Attack", "Time", "Mirror Mode", "Mirror", "Full", "RandomAll", "RandomOne",
        "Normalless", "Time Attackless", "Timeless", "Mirror Modeless", "Mirrorless"
    }
    default = {"Normal"}

class KLevel(Toggle):
    """
    K Level are part of the generation.
    K Level are locked behind kong letter items of their world.
    No Kong Letter items will be added into generation if this option is disabled.
    """
    display_name = "Include K Levels"

class KLevelRequirement(Range):
    """
    Amount of K Level clears that are required when goal is set to "All K Level"
    """

    range_start = 1
    range_end = 8
    default = 6

    display_name = "K Level Requirement for K Level goal"
    visibility = Visibility.none

class KongLetter(Toggle):
    """
    Kong Letter collectibles are added as locations.
    """
    display_name = "Include Kong Letters"

class PuzzlePieces(Toggle):
    """
    Puzzle Piece collectibles are added as locations.
    """
    display_name = "Include Puzzle Pieces"

class PuzzlePieceAmount(Range):
    """
    Amount of puzzle pieces in generation.
    """
    display_name = "Total Puzzle Piece amount in generation"
    range_start = 0
    range_end = 350
    default = 300

class PuzzlePiecesUnlockBosses(Toggle):
    """
    If enabled, bosses are unlocked with puzzle piece items.
    If disabled, bosses are unlocked with "Progressive Boss Unlock" items.
    No Puzzle Piece items will be added into generation if this option is disabled.
    """
    display_name = "Puzzle Pieces unlock bosses"

class KongLetterUnlockKLevel(Toggle):
    """
    If enabled, K Level are unlocked with kong letter items.
    If disabled, K Level are unlocked with "Progressive K Level Unlock" items.
    No Kong Letter items will be added into generation if this option is disabled.
    """
    display_name = "Kong Letter unlock K Level"

class WorldPuzzlePieceBundle(Toggle):
    """
    Creates locations for each world for getting every puzzle piece location in that world.
    """
    display_name = "Add World Puzzle Piece Bundle locations"

class WorldKongBundle(Toggle):
    """
    Creates locations for each world for getting every kong letter location in that world.
    """
    display_name = "Add World Kong Bundle locations"

class WorldCleared(Toggle):
    """
    Creates locations for each world for clearing every level in that world.
    """
    display_name = "Add World Cleared locations"

class WorldClearedMirror(Toggle):
    """
    Creates locations for each world for clearing every level in mirror mode in that world.
    """
    display_name = "Add World Cleared Mirror locations"

class WorldClearedTimeAttack(Toggle):
    """
    Creates locations for each world for clearing every level in time attack with the set medal in that world.
    """
    display_name = "Add World Cleared Time Attack locations"


class MirrorModeShards(Range):
    """
    Decides how many Mirror Shards are needed to unlock Mirror Mode.
    Setting this option to 0 will disable the Mirror Shards and Mirror Mode will get its own item.
    """
    display_name = "Mirror Mode Shard amount for Mirror Mode unlock"

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
    display_name = "Include Sunset Shore Key"


class BlowholeBoundKey(DefaultOnToggle):
    """
    Randomizes the Beach Shop Key for the level Blowhole Bound.
    """
    display_name = "Include Blowhole Bound Key"


class DampDungeonKey(DefaultOnToggle):
    """
    Randomizes the Ruins Shop Key for the level Damp Dungeon.
    """
    display_name = "Include Damp Dungeon Key"


class MolePatrolKey(DefaultOnToggle):
    """
    Randomizes the Cave Shop Key for the level Mole Patrol.
    """
    display_name = "Include Mole Patrol Key"


class SpringySporesKey(DefaultOnToggle):
    """
    Randomizes the Forest Shop Key for the level Springy Spores.
    """
    display_name = "Include Springy Spores Key"


class PrecariousPlateauKey(DefaultOnToggle):
    """
    Randomizes the Cliff Shop Key for the level Precarious Plateau.
    """
    display_name = "Include Precarious Plateau Key"


class HandyHazardsKey(DefaultOnToggle):
    """
    Randomizes the Factory Shop Key for the level Handy Hazards.
    """
    display_name = "Include Handy Hazards Key"


class SmokeyPeakKey(DefaultOnToggle):
    """
    Randomizes the Volcano Shop Key for the level Smokey Peak.
    """
    display_name = "Include Smokey Peak Key"


class JungleBossAccess(Range):
    """
    Sets the percentage of total Puzzle Pieces needed to gain access to the Boss in the Jungle.
    """
    display_name = "Puzzle Piece % requirement for Mugly's Mound"

    range_start = 0
    range_end = 100

    default = 5


class BeachBossAccess(Range):
    """
    Sets the percentage of total Puzzle Pieces needed to gain access to the Boss in the Beach.
    """
    display_name = "Puzzle Piece % requirement for Pinchin' Pirates"

    range_start = 0
    range_end = 100

    default = 10


class RuinsBossAccess(Range):
    """
    Sets the percentage of total Puzzle Pieces needed to gain access to the Boss in the Ruins.
    """
    display_name = "Puzzle Piece % requirement for Ruined Roost"

    range_start = 0
    range_end = 100

    default = 20


class CaveBossAccess(Range):
    """
    Sets the percentage of total Puzzle Pieces needed to gain access to the Boss in the Cave.
    """
    display_name = "Puzzle Piece % requirement for The Mole Train"

    range_start = 0
    range_end = 100

    default = 35


class ForestBossAccess(Range):
    """
    Sets the percentage of total Puzzle Pieces needed to gain access to the Boss in the Forest.
    """
    display_name = "Puzzle Piece % requirement for Mangoruby Run"

    range_start = 0
    range_end = 100

    default = 50


class CliffBossAccess(Range):
    """
    Sets the percentage of total Puzzle Pieces needed to gain access to the Boss in the Cliff.
    """
    display_name = "Puzzle Piece % requirement for Thugly's Highrise"

    range_start = 0
    range_end = 100

    default = 65


class FactoryBossAccess(Range):
    """
    Sets the percentage of total Puzzle Pieces needed to gain access to the Boss in the Factory.
    """
    display_name = "Puzzle Piece % requirement for Feather Fiend"

    range_start = 0
    range_end = 100

    default = 80


class VolcanoBossAccess(Range):
    """
    Sets the percentage of total Puzzle Pieces needed to gain access to the Boss in the Volcano.
    """
    display_name = "Puzzle Piece % requirement for Tiki Tong Terror"

    range_start = 0
    range_end = 100

    default = 95

class JungleKongLetterAmount(Range):
    """
    Amount of jungle kong letters in generation.
    """
    display_name = "Total jungle kong letter amount in generation"
    range_start = 0
    range_end = 50
    default = 30

class BeachKongLetterAmount(Range):
    """
    Amount of beach kong letters in generation.
    """
    display_name = "Total beach kong letter amount in generation"
    range_start = 0
    range_end = 50
    default = 30

class RuinsKongLetterAmount(Range):
    """
    Amount of ruins kong letters in generation.
    """
    display_name = "Total ruins kong letter amount in generation"
    range_start = 0
    range_end = 50
    default = 30

class CaveKongLetterAmount(Range):
    """
    Amount of cave kong letters in generation.
    """
    display_name = "Total cave kong letter amount in generation"
    range_start = 0
    range_end = 50
    default = 30

class ForestKongLetterAmount(Range):
    """
    Amount of forest kong letters in generation.
    """
    display_name = "Total forest kong letter amount in generation"
    range_start = 0
    range_end = 50
    default = 30

class CliffKongLetterAmount(Range):
    """
    Amount of cliff kong letters in generation.
    """
    display_name = "Total cliff kong letter amount in generation"
    range_start = 0
    range_end = 50
    default = 30

class FactoryKongLetterAmount(Range):
    """
    Amount of factory kong letters in generation.
    """
    display_name = "Total factory kong letter amount in generation"
    range_start = 0
    range_end = 50
    default = 30

class VolcanoKongLetterAmount(Range):
    """
    Amount of volcano kong letters in generation.
    """
    display_name = "Total volcano kong letter amount in generation"
    range_start = 0
    range_end = 50
    default = 30

class JungleKLevelAccess(Range):
    """
    Sets the percentage of total Jungle Kong Letters needed to gain access to the K Level in the Jungle.
    """
    display_name = "Kong Letter % requirement for Platform Panic access"

    range_start = 0
    range_end = 100

    default = 50


class BeachKLevelAccess(Range):
    """
    Sets the percentage of total Beach Kong Letters needed to gain access to the K Level in the Beach.
    """
    display_name = "Kong Letter % requirement for Tumblin' Temple access"

    range_start = 0
    range_end = 100

    default = 50


class RuinsKLevelAccess(Range):
    """
    Sets the percentage of total Ruins Kong Letters needed to gain access to the K Level in the Ruins.
    """
    display_name = "Kong Letter % requirement for Shifty Smashers access"

    range_start = 0
    range_end = 100

    default = 50


class CaveKLevelAccess(Range):
    """
    Sets the percentage of total Cave Kong Letters needed to gain access to the K Level in the Cave.
    """
    display_name = "Kong Letter % requirement for Jagged Jewels access"

    range_start = 0
    range_end = 100

    default = 50


class ForestKLevelAccess(Range):
    """
    Sets the percentage of total Forest Kong Letters needed to gain access to the K Level in the Forest.
    """
    display_name = "Kong Letter % requirement for Blast & Bounce access"

    range_start = 0
    range_end = 100

    default = 50


class CliffKLevelAccess(Range):
    """
    Sets the percentage of total Cliff Kong Letters needed to gain access to the K Level in the Cliff.
    """
    display_name = "Kong Letter % requirement for Perilous Passage access"

    range_start = 0
    range_end = 100

    default = 50


class FactoryKLevelAccess(Range):
    """
    Sets the percentage of total Factory Kong Letters needed to gain access to the K Level in the Factory.
    """
    display_name = "Kong Letter % requirement for Treacherous Track access"

    range_start = 0
    range_end = 100

    default = 50


class VolcanoKLevelAccess(Range):
    """
    Sets the percentage of total Volcano Kong Letters needed to gain access to the K Level in the Volcano.
    """
    display_name = "Kong Letter % requirement for Five Monkey Trial access"

    range_start = 0
    range_end = 100

    default = 50


@dataclass
class DKCROptions(PerGameCommonOptions):
    goal: Goal
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
    kong_letter: KongLetter
    puzzle_pieces: PuzzlePieces
    puzzle_piece_amount: PuzzlePieceAmount
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
    jungle_kong_letter_amount: JungleKongLetterAmount
    beach_kong_letter_amount: BeachKongLetterAmount
    ruins_kong_letter_amount: RuinsKongLetterAmount
    cave_kong_letter_amount: CaveKongLetterAmount
    forest_kong_letter_amount: ForestKongLetterAmount
    cliff_kong_letter_amount: CliffKongLetterAmount
    factory_kong_letter_amount: FactoryKongLetterAmount
    volcano_kong_letter_amount: VolcanoKongLetterAmount
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
            "goal",
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
            "kong_letter",
            "puzzle_pieces",
            "puzzle_piece_amount",
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
            "jungle_kong_letter_amount",
            "beach_kong_letter_amount",
            "ruins_kong_letter_amount",
            "cave_kong_letter_amount",
            "forest_kong_letter_amount",
            "cliff_kong_letter_amount",
            "factory_kong_letter_amount",
            "volcano_kong_letter_amount",
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
        [Goal, DeathLink, GoldenTemple, RareOrbs, RandomizeLevels, KongLetterCollectionCheckpoint, TimeAttackMedals, LevelClearType]
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
        [PuzzlePieceAmount, PuzzlePieces ,JungleBossAccess, BeachBossAccess, RuinsBossAccess, CaveBossAccess, ForestBossAccess, CliffBossAccess,
         FactoryBossAccess, VolcanoBossAccess]
    ),
    OptionGroup(
        "K Level access options",
        [KongLetter, KLevel, JungleKongLetterAmount, BeachKongLetterAmount, RuinsKongLetterAmount, CaveKongLetterAmount,
         ForestKongLetterAmount, CliffKongLetterAmount, FactoryKongLetterAmount, VolcanoKongLetterAmount,
         JungleKLevelAccess, BeachKLevelAccess, RuinsKLevelAccess, CaveKLevelAccess, ForestKLevelAccess, CliffKLevelAccess,
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

    dkcr_world.options.goal.value = slot_data["goal"]
    dkcr_world.ut_medals = set(slot_data["time_attack_resolved"])
    dkcr_world.options.smog_clear.value = slot_data["smog_clear"]
    dkcr_world.options.lift_off_launch.value = slot_data["lift_off_launch"]
    dkcr_world.options.factory_buttons.value = slot_data["factory_buttons"]
    dkcr_world.ut_level_clear_types = set(slot_data["level_clear_type_resolved"])
    dkcr_world.options.k_level.value = slot_data["k_level"]
    dkcr_world.options.kong_letter.value = slot_data["kong_letter"]
    dkcr_world.options.puzzle_pieces.value = slot_data["puzzle_pieces"]
    dkcr_world.options.puzzle_piece_amount.value = slot_data["puzzle_piece_amount"]
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
    dkcr_world.options.jungle_kong_letter_amount.value = slot_data["jungle_kong_letter_amount"]
    dkcr_world.options.beach_kong_letter_amount.value = slot_data["beach_kong_letter_amount"]
    dkcr_world.options.ruins_kong_letter_amount.value = slot_data["ruins_kong_letter_amount"]
    dkcr_world.options.cave_kong_letter_amount.value = slot_data["cave_kong_letter_amount"]
    dkcr_world.options.forest_kong_letter_amount.value = slot_data["forest_kong_letter_amount"]
    dkcr_world.options.cliff_kong_letter_amount.value = slot_data["cliff_kong_letter_amount"]
    dkcr_world.options.factory_kong_letter_amount.value = slot_data["factory_kong_letter_amount"]
    dkcr_world.options.volcano_kong_letter_amount.value = slot_data["volcano_kong_letter_amount"]
    dkcr_world.options.jungle_k_level_access.value = slot_data["jungle_k_level_access"]
    dkcr_world.options.beach_k_level_access.value = slot_data["beach_k_level_access"]
    dkcr_world.options.ruins_k_level_access.value = slot_data["ruins_k_level_access"]
    dkcr_world.options.cave_k_level_access.value = slot_data["cave_k_level_access"]
    dkcr_world.options.forest_k_level_access.value = slot_data["forest_k_level_access"]
    dkcr_world.options.cliff_k_level_access.value = slot_data["cliff_k_level_access"]
    dkcr_world.options.factory_k_level_access.value = slot_data["factory_k_level_access"]
    dkcr_world.options.volcano_k_level_access.value = slot_data["volcano_k_level_access"]

    return slot_data