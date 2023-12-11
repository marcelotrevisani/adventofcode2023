from adoc23.day9 import solution1, solution2


def test_solution1_simple():
    all_input = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""
    assert solution1(all_input) == 114


def test_solution1(shared_datadir):
    all_input = (shared_datadir / "day9.txt").read_text()
    assert solution1(all_input) == 1974232246


def test_solution2_simple():
    all_input = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""
    assert solution2(all_input) == 2


def test_solution2(shared_datadir):
    all_input = (shared_datadir / "day9.txt").read_text()
    assert solution2(all_input) == 928
