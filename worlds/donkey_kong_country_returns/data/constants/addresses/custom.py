 # 0x817FC000 to 0x817FC3BB (956 bytes)

class CustomAddresses:
    BASE = 0x817FC000

    # AP Connection 0x0
    SLOT_NAME = BASE + 0x0

    LAST_ITEM_INDEX = BASE + 0x10
    PP_AMOUNT = BASE + 0x12
    KL = BASE + 0x14
    KL_JGL = KL + 0x0
    KL_BCH = KL + 0x1
    KL_RNS = KL + 0x2
    KL_CVE = KL + 0x3
    KL_FRS = KL + 0x4
    KL_CLF = KL + 0x5
    KL_FCT = KL + 0x6
    KL_VLC = KL + 0x7

    MIRROR_SHARDS = BASE + 0x1c
    FACTORY_BUTTONS = BASE + 0x1d
    ORBS = BASE + 0x1e
    KEYS = BASE + 0x1f

    LEVEL_CONNECTION = BASE + 0x20
    WORLD_CONNECTION = BASE + 0x2a

    CURRENT_LEVEL_PP = BASE + 0x2c
    BOSS_UNLOCK = BASE + 0x30
    K_LEVEL_UNLOCK = BASE + 0x31
    SQUAWKS = BASE + 32