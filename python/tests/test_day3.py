from adoc23.day3 import solution1


def test_solution1_simple():
    all_input = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""
    assert solution1(all_input) == 4361


def test_solution1(shared_datadir):
    all_input = (shared_datadir / "day3-input.txt").read_text()
    assert solution1(all_input) == 0