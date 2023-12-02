from adoc23.day1 import solution1, solution2


def test_solution1_simple():
    all_input_str = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""
    assert solution1(all_input_str) == 142


def test_solution1(shared_datadir):
    all_input = (shared_datadir / "day1-solution1.txt").read_text()
    assert solution1(all_input) == 54927


def test_solution2_simple():
    all_input_str = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""
    assert solution2(all_input_str) == 281


def test_solution2(shared_datadir):
    all_input = (shared_datadir / "day1-solution2.txt").read_text()
    assert solution2(all_input) == 54581
