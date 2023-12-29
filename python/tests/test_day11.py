from adoc23.day11 import solution1


def test_solution1_simple():
    all_input = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""
    assert solution1(all_input) == 374


def test_solution1(shared_datadir):
    all_input = (shared_datadir / "day11.txt").read_text()
    assert solution1(all_input) == 9639160
