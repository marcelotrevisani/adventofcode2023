from adoc23.day8 import solution1, solution2


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


def test_solution2_simple():
    all_input = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)"""
    assert solution2(all_input) == 6


def test_solution2(shared_datadir):
    all_input = (shared_datadir / "day8.txt").read_text()
    assert solution2(all_input) == 10151663816849
