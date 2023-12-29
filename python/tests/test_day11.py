import pytest

from adoc23.day11 import solution1, solution2


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


@pytest.mark.parametrize("expansion, result", [(10, 1030), (100, 8410)])
def test_solution2_simple(expansion, result):
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
    assert solution2(all_input, expansion) == result


def test_solution2(shared_datadir):
    all_input = (shared_datadir / "day11.txt").read_text()
    assert solution2(all_input) == 752936133304
