from adoc23.day8 import solution1


def test_solution1_simple():
    all_input = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)"""
    assert solution1(all_input) == 2


def test_solution1_simple2():
    all_input = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)"""
    assert solution1(all_input) == 6


def test_solution1(shared_datadir):
    all_input = (shared_datadir / "day8.txt").read_text()
    assert solution1(all_input) == 11911