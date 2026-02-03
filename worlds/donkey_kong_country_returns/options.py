from dataclasses import dataclass, fields
from typing import Any
from Options import Choice, OptionGroup, PerGameCommonOptions, Range, Toggle, DefaultOnToggle, Visibility

class DeathLink(Toggle):
    """
    Syncing deaths among other clients that have this option enabled.
    """
    display_name = "Death Link"
    visibility = Visibility.none

class GoldenTemple(Toggle):
    """
    Adding the Golden Temple into the item pool
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

class RandomizeLevels(Toggle):
    """
    When enabled, randomizes the levels with each other.
    Excludes K levels and Bosses.
    """
    display_name = "Randomize Levels"
    visibility = Visibility.none

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
    visibility = Visibility.none

class MirrorModeShards(Range):
    """
    Decides how many Mirror Shards are needed to unlock Mirror Mode.
    """
    display_name = "Mirror Mode Shard amount"
    visibility = Visibility.none

    range_start = 0
    range_end = 25
    default = 8

class SunsetShoreKey(Toggle):
    """
    When enabled, adds the Jungle Shop Key for the level Sunset Shore as a location.
    """
    display_name = "Sunset Shore Key"
    visibility = Visibility.none

class BlowholeBoundKey(Toggle):
    """
    When enabled, adds the Beach Shop Key for the level Blowhole Bound as a location.
    """
    display_name = "Blowhole Bound Key"
    visibility = Visibility.none

class DampDungeonKey(Toggle):
    """
    When enabled, adds the Ruins Shop Key for the level Damp Dungeon as a location.
    """
    display_name = "Damp Dungeon Key"
    visibility = Visibility.none

class MolePatrolKey(Toggle):
    """
    When enabled, adds the Cave Shop Key for the level Mole Patrol as a location.
    """
    display_name = "Mole Patrol Key"
    visibility = Visibility.none

class SpringySporesKey(Toggle):
    """
    When enabled, adds the Forest Shop Key for the level Springy Spores as a location.
    """
    display_name = "Springy Spores Key"
    visibility = Visibility.none

class PrecariousPlateauKey(Toggle):
    """
    When enabled, adds the Cliff Shop Key for the level Precarious Plateau as a location.
    """
    display_name = "Precarious Plateau Key"
    visibility = Visibility.none

class HandyHazardsKey(Toggle):
    """
    When enabled, adds the Factory Shop Key for the level Handy Hazards as a location.
    """
    display_name = "Handy Hazards Key"
    visibility = Visibility.none

class SmokeyPeakKey(Toggle):
    """
    When enabled, adds the Volcano Shop Key for the level Smokey Peak as a location.
    """
    display_name = "Smokey Peak Key"
    visibility = Visibility.none

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
    range_end = 366
    # This Value can not exceed 366

    default = 320

@dataclass
class DKCROptions(PerGameCommonOptions):
    death_link: DeathLink
    golden_temple: GoldenTemple
    rare_orbs: RareOrbs
    randomize_levels: RandomizeLevels
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

    def get_slot_data_dict(self) -> dict[str, Any]:
        return self.as_dict(
            "death_link",
            "golden_temple",
            "rare_orbs",
            "randomize_levels",
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
        )

option_groups = [
    OptionGroup(
        "Gameplay options",
        [DeathLink, GoldenTemple, RareOrbs, RandomizeLevels]
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
        "Moveset options",
        [Roll, Grab, Blow, GroundPound]
    ),
    OptionGroup(
        "Misc options",
        [Rambi, Minecart, RocketBarrel, KongBarrel]
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