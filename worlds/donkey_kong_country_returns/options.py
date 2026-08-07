from dataclasses import dataclass
from typing import Any, TYPE_CHECKING

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
    visibility = Visibility.none

class RareOrbs(Range):
    """
    How many of the Rare Orbs found in K-levels are needed to enter the Golden Temple.
    """
    display_name = "Rare Orb amount"

    range_start = 0
    range_end = 8
    # This value can not exceed 8

    default = 8
    visibility = Visibility.none

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


class MirrorMode(Toggle):
    """
    Completing a level in Mirror Mode is considered a check.
    """
    display_name = "Mirror Mode"


class MirrorModeShards(Range):
    """
    Decides how many Mirror Shards are needed to unlock Mirror Mode.
    Setting this option to 0 will disable the Mirror Shards and Mirror Mode will get its own item.
    """
    display_name = "Mirror Mode Shard amount"

    range_start = 0
    range_end = 25
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
    """
    display_name = "Puzzle Piece requirement for Mugly's Mound"

    range_start = 0
    range_end = 41
    # This Value can not exceed 41

    default = 20


class BeachBossAccess(Range):
    """
    Sets the amount of total Puzzle Pieces needed to gain access to the Boss in the Beach.
    """
    display_name = "Puzzle Piece requirement for Pinchin' Pirates"

    range_start = 0
    range_end = 85
    # This Value can not exceed 85

    default = 50


class RuinsBossAccess(Range):
    """
    Sets the amount of total Puzzle Pieces needed to gain access to the Boss in the Ruins.
    """
    display_name = "Puzzle Piece requirement for Ruined Roost"

    range_start = 0
    range_end = 132
    # This Value can not exceed 132

    default = 80


class CaveBossAccess(Range):
    """
    Sets the amount of total Puzzle Pieces needed to gain access to the Boss in the Cave.
    """
    display_name = "Puzzle Piece requirement for The Mole Train"

    range_start = 0
    range_end = 162
    # This Value can not exceed 162

    default = 110


class ForestBossAccess(Range):
    """
    Sets the amount of total Puzzle Pieces needed to gain access to the Boss in the Forest.
    """
    display_name = "Puzzle Piece requirement for Mangoruby Run"

    range_start = 0
    range_end = 219
    # This Value can not exceed 219

    default = 150


class CliffBossAccess(Range):
    """
    Sets the amount of total Puzzle Pieces needed to gain access to the Boss in the Cliff.
    """
    display_name = "Puzzle Piece requirement for Thugly's Highrise"

    range_start = 0
    range_end = 274
    # This Value can not exceed 274

    default = 200


class FactoryBossAccess(Range):
    """
    Sets the amount of total Puzzle Pieces needed to gain access to the Boss in the Factory.
    """
    display_name = "Puzzle Piece requirement for Feather Fiend"

    range_start = 0
    range_end = 324
    # This Value can not exceed 324

    default = 260


class VolcanoBossAccess(Range):
    """
    Sets the amount of total Puzzle Pieces needed to gain access to the Boss in the Volcano.
    """
    display_name = "Puzzle Piece requirement for Tiki Tong Terror"

    range_start = 0
    range_end = 371
    # This Value can not exceed 371

    default = 320


class JungleKLevelAccess(Range):
    """
    Sets the amount of total Kong Letters, from the respective, World needed to gain access to the K Level in the Jungle.
    """
    display_name = "Puzzle Piece requirement for Platform Panic"

    range_start = 0
    range_end = 24
    # This Value can not exceed 24

    default = 24


class BeachKLevelAccess(Range):
    """
    Sets the amount of total Kong Letters, from the respective, World needed to gain access to the K Level in the Beach.
    """
    display_name = "Puzzle Piece requirement for Tumblin' Temple"

    range_start = 0
    range_end = 28
    # This Value can not exceed 28

    default = 28


class RuinsKLevelAccess(Range):
    """
    Sets the amount of total Kong Letters, from the respective, World needed to gain access to the K Level in the Ruins.
    """
    display_name = "Puzzle Piece requirement for Shifty Smashers"

    range_start = 0
    range_end = 24
    # This Value can not exceed 24

    default = 24


class CaveKLevelAccess(Range):
    """
    Sets the amount of total Kong Letters, from the respective, World needed to gain access to the K Level in the Cave.
    """
    display_name = "Puzzle Piece requirement for Jagged Jewels"

    range_start = 0
    range_end = 20
    # This Value can not exceed 20

    default = 20


class ForestKLevelAccess(Range):
    """
    Sets the amount of total Kong Letters, from the respective, World needed to gain access to the K Level in the Forest.
    """
    display_name = "Puzzle Piece requirement for Blast & Bounce"

    range_start = 0
    range_end = 32
    # This Value can not exceed 32

    default = 32


class CliffKLevelAccess(Range):
    """
    Sets the amount of total Kong Letters, from the respective, World needed to gain access to the K Level in the Cliff.
    """
    display_name = "Puzzle Piece requirement for Perilous Passage"

    range_start = 0
    range_end = 32
    # This Value can not exceed 32

    default = 32


class FactoryKLevelAccess(Range):
    """
    Sets the amount of total Kong Letters, from the respective, World needed to gain access to the K Level in the Factory.
    """
    display_name = "Puzzle Piece requirement for Treacherous Track"

    range_start = 0
    range_end = 28
    # This Value can not exceed 28

    default = 28


class VolcanoKLevelAccess(Range):
    """
    Sets the amount of total Kong Letters, from the respective, World needed to gain access to the K Level in the Volcano.
    """
    display_name = "Puzzle Piece requirement for Five Monkey Trial"

    range_start = 0
    range_end = 28
    # This Value can not exceed 28

    default = 28


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
    mirror_mode: MirrorMode
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
            "mirror_mode",
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
        [DeathLink, GoldenTemple, RareOrbs, RandomizeLevels, KongLetterCollectionCheckpoint, TimeAttackMedals]
    ),
    OptionGroup(
        "Key options",
        [SunsetShoreKey, BlowholeBoundKey, DampDungeonKey, MolePatrolKey, SpringySporesKey, PrecariousPlateauKey,
         HandyHazardsKey, SmokeyPeakKey]
    ),
    OptionGroup(
        "Boss access options",
        [JungleBossAccess, BeachBossAccess, RuinsBossAccess, CaveBossAccess, ForestBossAccess, CliffBossAccess,
         FactoryBossAccess, VolcanoBossAccess]
    ),
    OptionGroup(
        "K Level access options",
        [JungleKLevelAccess, BeachKLevelAccess, RuinsKLevelAccess, CaveKLevelAccess, ForestKLevelAccess, CliffKLevelAccess,
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
        [MirrorMode, MirrorModeShards]
    )
]

option_presets = {
    "Full": {
        "rare_orbs": 8,
        "golden_temple": True,
        "rambi": True,
        "minecart": True,
        "rocket_barrel": True,
        "kong_barrel": True,
        "run": True,
        "roll": True,
        "grab": True,
        "blow": True,
        "ground_pound": True,
        "mirror_mode": True,
        "mirror_mode_shards": 8,
        "sunset_shore_key": True,
        "blowhole_bound_key": True,
        "damp_dungeon_key": True,
        "mole_patrol_key": True,
        "springy_spores_key": True,
        "precarious_plateau_key": True,
        "handy_hazards_key": True,
        "smokey_peak_key": True,
        "jungle_boss_access": 20,
        "beach_boss_access": 50,
        "ruins_boss_access": 80,
        "cave_boss_access": 110,
        "forest_boss_access": 150,
        "cliff_boss_access": 200,
        "factory_boss_access": 260,
        "volcano_boss_access": 320,
    },
    "Empty": {
        "rare_orbs": 0,
        "golden_temple": False,
        "rambi": False,
        "minecart": False,
        "rocket_barrel": False,
        "kong_barrel": False,
        "run": False,
        "roll": False,
        "grab": False,
        "blow": False,
        "ground_pound": False,
        "mirror_mode": False,
        "mirror_mode_shards": 0,
        "sunset_shore_key": False,
        "blowhole_bound_key": False,
        "damp_dungeon_key": False,
        "mole_patrol_key": False,
        "springy_spores_key": False,
        "precarious_plateau_key": False,
        "handy_hazards_key": False,
        "smokey_peak_key": False,
        "jungle_boss_access": 20,
        "beach_boss_access": 50,
        "ruins_boss_access": 80,
        "cave_boss_access": 110,
        "forest_boss_access": 150,
        "cliff_boss_access": 200,
        "factory_boss_access": 260,
        "volcano_boss_access": 320,
    }
}


def handle_ut_yamless(world, slot_data: dict[str, Any] | None) -> dict[str, Any] | None:
    if (
            not slot_data
            and hasattr(world.multiworld, "re_gen_passthrough")
            and isinstance(world.multiworld.re_gen_passthrough, dict)
            and world.game in world.multiworld.re_gen_passthrough
    ):
        slot_data = world.multiworld.re_gen_passthrough[world.game]

    if not slot_data:
        return None

    world.ut_medals = set(slot_data["time_attack_resolved"])
    world.options.smog_clear.value = slot_data["smog_clear"]
    world.options.lift_off_launch.value = slot_data["lift_off_launch"]
    world.options.factory_buttons.value = slot_data["factory_buttons"]
    world.options.mirror_mode.value = slot_data["mirror_mode"]
    world.options.mirror_mode_shards.value = slot_data["mirror_mode_shards"]
    world.options.squawks.value = slot_data["squawks"]
    world.options.sunset_shore_key.value = slot_data["sunset_shore_key"]
    world.options.blowhole_bound_key.value = slot_data["blowhole_bound_key"]
    world.options.damp_dungeon_key.value = slot_data["damp_dungeon_key"]
    world.options.mole_patrol_key.value = slot_data["mole_patrol_key"]
    world.options.springy_spores_key.value = slot_data["springy_spores_key"]
    world.options.precarious_plateau_key.value = slot_data["precarious_plateau_key"]
    world.options.handy_hazards_key.value = slot_data["handy_hazards_key"]
    world.options.smokey_peak_key.value = slot_data["smokey_peak_key"]
    world.options.jungle_boss_access.value = slot_data["jungle_boss_access"]
    world.options.beach_boss_access.value = slot_data["beach_boss_access"]
    world.options.ruins_boss_access.value = slot_data["ruins_boss_access"]
    world.options.cave_boss_access.value = slot_data["cave_boss_access"]
    world.options.forest_boss_access.value = slot_data["forest_boss_access"]
    world.options.cliff_boss_access.value = slot_data["cliff_boss_access"]
    world.options.factory_boss_access.value = slot_data["factory_boss_access"]
    world.options.volcano_boss_access.value = slot_data["volcano_boss_access"]
    world.options.jungle_k_level_access.value = slot_data["jungle_k_level_access"]
    world.options.beach_k_level_access.value = slot_data["beach_k_level_access"]
    world.options.ruins_k_level_access.value = slot_data["ruins_k_level_access"]
    world.options.cave_k_level_access.value = slot_data["cave_k_level_access"]
    world.options.forest_k_level_access.value = slot_data["forest_k_level_access"]
    world.options.cliff_k_level_access.value = slot_data["cliff_k_level_access"]
    world.options.factory_k_level_access.value = slot_data["factory_k_level_access"]
    world.options.volcano_k_level_access.value = slot_data["volcano_k_level_access"]

    return slot_data