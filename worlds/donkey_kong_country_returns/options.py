from dataclasses import dataclass

from Options import Choice, OptionGroup, PerGameCommonOptions, Range, Toggle, DefaultOnToggle

class GoldenTemple(Toggle):
    """
    Adding the Golden Temple into the itempool
    """
    display_name = "Golden Temple"

class Rambi(Toggle):
    """
    When enabled, locks Rambi behind the Rambi’s Saddle item.
    """
    display_name = "Rambi"

class Minecart(Toggle):
    """
    When enabled, Mine Cart levels and sections require the item Mine Cart Key to access.
    """
    display_name = "Mine Cart"

class RocketBarrel(Toggle):
    """
    When enabled, Rocket Barrel levels and sections require the item Rocket Barrel Fuel to access.
    """
    display_name = "Rocket Barrel"

class DiddyKong(Toggle):
    """
    When enabled, requires the item Diddy Kong's Jetpack for the use of Diddy Kong.
    """
    display_name = "Diddy Kong"

class SunsetShoreKey(Toggle):
    """
    When enabled, adds the Jungle Shop Key for the level Sunset Shore as a location.
    """
    display_name = "Sunset Shore Key"

class BlowholeBoundKey(Toggle):
    """
    When enabled, adds the Beach Shop Key for the level Blowhole Bound as a location.
    """
    display_name = "Blowhole Bound Key"

class DampDungeonKey(Toggle):
    """
    When enabled, adds the Ruins Shop Key for the level Damp Dungeon as a location.
    """
    display_name = "Damp Dungeon Key"

class MolePatrolKey(Toggle):
    """
    When enabled, adds the Cave Shop Key for the level Mole Patrol as a location.
    """
    display_name = "Mole Patrol Key"

class SpringySporesKey(Toggle):
    """
    When enabled, adds the Forest Shop Key for the level Springy Spores as a location.
    """
    display_name = "Springy Spores Key"

class PrecariousPlateauKey(Toggle):
    """
    When enabled, adds the Cliff Shop Key for the level Precarious Plateau as a location.
    """
    display_name = "Precarious Plateau Key"

class HandyHazardsKey(Toggle):
    """
    When enabled, adds the Factory Shop Key for the level Handy Hazards as a location.
    """
    display_name = "Handy Hazards Key"

class SmokeyPeakKey(Toggle):
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
    range_end = 326
    # This Value can not exceed 326

    default = 260

class VolcanoBossAccess(Range):
    """
    Sets the amount of total Puzzle Pieces needed to gain access to the Boss in the Volcano.
    """
    display_name = "Puzzle Piece requirement for Tiki Tong Terror"

    range_start = 0
    range_end = 368
    # This Value can not exceed 368

    default = 320

@dataclass
class DKCROptions(PerGameCommonOptions):
    golden_temple: GoldenTemple
    rambi: Rambi
    mine_cart: Minecart
    rocket_barrel: RocketBarrel
    diddy_kong: DiddyKong
    sunset_shore_key: SunsetShoreKey
    blowhole_bound_key: BlowholeBoundKey
    damp_dungeon_key: DampDungeonKey
    mole_patrol_key: MolePatrolKey
    springy_spores: SpringySporesKey
    precarious_plateau_key: PrecariousPlateauKey
    handy_hazards: HandyHazardsKey
    smokey_peak: SmokeyPeakKey
    jungle_boss_access: JungleBossAccess
    beach_boss_access: BeachBossAccess
    ruins_boss_access: RuinsBossAccess
    cave_boss_access: CaveBossAccess
    forest_boss_access: ForestBossAccess
    cliff_boss_access: CliffBossAccess
    factory_boss_access: FactoryBossAccess
    volcano_boss_access: VolcanoBossAccess

option_groups = [
    OptionGroup(
        "Gameplay Options",
        [GoldenTemple, Rambi, Minecart, RocketBarrel, DiddyKong]
    ),
    OptionGroup(
        "Key Options",
        [SunsetShoreKey, BlowholeBoundKey, DampDungeonKey, MolePatrolKey, SpringySporesKey, PrecariousPlateauKey,
         HandyHazardsKey, SmokeyPeakKey]
    ),
    OptionGroup(
        "Boss Access Options",
        [JungleBossAccess, BeachBossAccess, RuinsBossAccess, CaveBossAccess, ForestBossAccess, CliffBossAccess,
         FactoryBossAccess, VolcanoBossAccess]
    )
]

option_presets = {
    "Full": {
        "golden_temple": True,
        "rambi": True,
        "mine_cart": True,
        "rocket_barrel": True,
        "diddy_kong": True,
        "sunset_shore_key": True,
        "blowhole_bound_key": True,
        "damp_dungeon_key": True,
        "mole_patrol_key": True,
        "springy_spores": True,
        "precarious_plateau_key": True,
        "handy_hazards": True,
        "smokey_peak": True,
        "jungle_boss_access": True,
        "beach_boss_access": True,
        "ruins_boss_access": True,
        "cave_boss_access": True,
        "forest_boss_access": True,
        "cliff_boss_access": True,
        "factory_boss_access": True,
        "volcano_boss_access": True,
    },
    "Empty": {
        "golden_temple": False,
        "rambi": False,
        "mine_cart": False,
        "rocket_barrel": False,
        "diddy_kong": False,
        "sunset_shore_key": False,
        "blowhole_bound_key": False,
        "damp_dungeon_key": False,
        "mole_patrol_key": False,
        "springy_spores": False,
        "precarious_plateau_key": False,
        "handy_hazards": False,
        "smokey_peak": False,
        "jungle_boss_access": False,
        "beach_boss_access": False,
        "ruins_boss_access": False,
        "cave_boss_access": False,
        "forest_boss_access": False,
        "cliff_boss_access": False,
        "factory_boss_access": False,
        "volcano_boss_access": False,
    }
}