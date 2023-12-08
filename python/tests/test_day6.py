from adoc23.day6 import solution1, solution2


def test_solution1_simple():
    all_input = """Time:      7  15   30
Distance:  9  40  200"""
    assert solution1(all_input) == 288


def test_solution1(shared_datadir):
    all_input = (shared_datadir / "day6.txt").read_text()
    assert solution1(all_input) == 0


def test_solution2():
    all_input = """Time:      7  15   30
    Distance:  9  40  200"""
    assert solution2(all_input) == 71503


def test_solution2(shared_datadir):
    all_input = (shared_datadir / "day6.txt").read_text()
    assert solution2(all_input) == 23632299
