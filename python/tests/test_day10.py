from adoc23.day10 import solution1


def test_solution1_simple():
    all_input = """.....
.S-7.
.|.|.
.L-J.
....."""
    assert solution1(all_input) == 4


def test_solution1_simple2():
    all_input = """..F7.
.FJ|.
SJ.L7
|F--J
LJ..."""
    assert solution1(all_input) == 8


def test_solution1(shared_datadir):
    all_input = (shared_datadir / "day10.txt").read_text()
    assert solution1(all_input) == 6842
