from worlds.donkey_kong_country_returns.data.level_data import Levels
from worlds.donkey_kong_country_returns.data.indexes import *
from worlds.donkey_kong_country_returns.utils import Color


# -------------------------
# STRUCTURE INTEGRITY
# -------------------------

def test_unique_world_index_pair():
    seen = set()

    for level_name, level_data in Levels.items():
        key = (level_data.world_index, level_data.index)

        assert key not in seen, (
            f"Duplicate level index: {level_name}"
        )
        seen.add(key)


def test_unique_pointers():
    seen = {}

    for level_name, level_data in Levels.items():
        if level_data.pointer in seen:
            raise AssertionError(
                f"{level_name} and {seen[level_data.pointer]} "
                f"share pointer {hex(level_data.pointer)}"
            )

        seen[level_data.pointer] = level_name


# -------------------------
# CONNECTION VALIDATION
# -------------------------

def test_connection_source_match_level():
    for level_name, level_data in Levels.items():
        for connection in level_data.connections:
            assert connection.from_level_index == level_data.index, (
                f"{level_name}: "
                f"{connection.from_level_index=} "
                f"does not match {level_data.index=}"
            )


def test_all_connection_targets_exist():
    valid_indices = {
        (level_data.world_index, level_data.index)
        for level_data in Levels.values()
    }

    for level_name, level_data in Levels.items():
        for connection in level_data.connections:
            assert (
                       level_data.world_index,
                       connection.to_level_index,
                   ) in valid_indices, (
                f"{level_name} points to missing level "
                f"{connection.to_level_index}"
            )


# -------------------------
# SPECIAL LEVEL RULES
# -------------------------

def test_shop_indices():
    for level_name, level_data in Levels.items():
        if "SHOP" in level_name:
            assert level_data.index == SHOP_LEVEL_INDEX, (
                f"{level_name} does not use SHOP_LEVEL_INDEX"
            )


def test_k_levels_have_one_connection():
    for level_name, level_data in Levels.items():
        if level_data.index == K_LEVEL_INDEX and level_data.world_index != GOLDEN_TEMPLE_WORLD_INDEX:
            assert len(level_data.connections) == 1, (
                f"{level_name} has {len(level_data.connections)} connections"
            )


def test_shops_have_no_puzzle_pieces():
    for level_name, level_data in Levels.items():
        if level_data.index == SHOP_LEVEL_INDEX:
            assert level_data.puzzle_piece_amount == PP_0, (
                f"{level_name} has {level_data.puzzle_piece_amount} puzzle pieces"
            )


def test_bosses_have_no_puzzle_pieces():
    for level_name, level_data in Levels.items():
        if level_data.index == BOSS_LEVEL_INDEX:
            assert level_data.puzzle_piece_amount == PP_0, (
                f"{level_name} has {level_data.puzzle_piece_amount} puzzle pieces"
            )


def test_k_levels_have_five_pieces():
    for level_name, level_data in Levels.items():
        if level_data.index == K_LEVEL_INDEX and level_data.world_index != GOLDEN_TEMPLE_WORLD_INDEX:
            assert level_data.puzzle_piece_amount == PP_5, (
                f"{level_name} has {level_data.puzzle_piece_amount} puzzle pieces"
            )


# -------------------------
# GLOBAL CONSISTENCY
# -------------------------

def test_total_puzzle_piece_count():
    total = sum(level_data.puzzle_piece_amount for level_data in Levels.values())

    assert total == 371, (
        f"Expected 366 puzzle pieces, but got {total}"
    )


# -------------------------
# RUNNER
# -------------------------

def run_all_tests():
    tests = [
        fn for name, fn in globals().items()
        if name.startswith("test_") and callable(fn)
    ]

    tests.sort(key=lambda f: f.__name__)

    passed = 0
    failed = 0

    for test in tests:
        try:
            test()
            print(f"{Color.GREEN}PASS{Color.RESET} {test.__name__}")
            passed += 1
        except AssertionError as e:
            print(f"{Color.YELLOW}FAIL{Color.RESET} {test.__name__}: {e}")
            failed += 1
        except Exception as e:
            print(f"{Color.RED}ERROR{Color.RESET} {test.__name__}: {e}")
            failed += 1

    print("\n---")
    print(f"{Color.GREEN}PASS{Color.RESET}: {passed}")
    print(f"{Color.RED}FAIL{Color.RESET}: {failed}")

    return failed == 0


if __name__ == "__main__":
    run_all_tests()
