from adoc23.day1 import solution1


def test_solution1_simple():
    all_input_str = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""
    assert solution1(all_input_str) == 142


def test_solution1(shared_datadir):
    all_input = (shared_datadir / "day1.txt").read_text()
    assert solution1(all_input) == 54927
