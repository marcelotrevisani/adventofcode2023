import pytest

from adoc23.day10 import solution1, solution2


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


@pytest.mark.parametrize(
    "str_input, exp_value",
    [
        #         (
        #         """...........
        # .S-------7.
        # .|F-----7|.
        # .||.....||.
        # .||.....||.
        # .|L-7.F-J|.
        # .|..|.|..|.
        # .L--J.L--J.
        # ...........""",
        #         4
        #     ),
        #     (""".F----7F7F7F7F-7....
        # .|F--7||||||||FJ....
        # .||.FJ||||||||L7....
        # FJL7L7LJLJ||LJ.L-7..
        # L--J.L7...LJS7F-7L7.
        # ....F-J..F7FJ|L7L7L7
        # ....L7.F7||L7|.L7L7|
        # .....|FJLJ|FJ|F7|.LJ
        # ....FJL-7.||.||||...
        # ....L---J.LJ.LJLJ...""", 8),
        (
            """FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L""",
            10,
        )
    ],
)
def test_solution2_simple(str_input, exp_value):
    assert solution2(str_input) == exp_value


def test_solution2(shared_datadir):
    all_input = (shared_datadir / "day10.txt").read_text()
    assert solution2(all_input) == 393
