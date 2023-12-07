from adoc23.day5 import solution1, solution2


def test_solution1_simple():
    all_input = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""
    assert solution1(all_input) == 35


def test_solution1(shared_datadir):
    all_input = (shared_datadir / "day5.txt").read_text()
    assert solution1(all_input) == 26273516


def test_solution2_simple():
    all_input = """seeds: 79 14 55 13

    seed-to-soil map:
    50 98 2
    52 50 48

    soil-to-fertilizer map:
    0 15 37
    37 52 2
    39 0 15

    fertilizer-to-water map:
    49 53 8
    0 11 42
    42 0 7
    57 7 4

    water-to-light map:
    88 18 7
    18 25 70

    light-to-temperature map:
    45 77 23
    81 45 19
    68 64 13

    temperature-to-humidity map:
    0 69 1
    1 0 69

    humidity-to-location map:
    60 56 37
    56 93 4"""
    assert solution2(all_input) == 35


def test_solution2(shared_datadir):
    all_input = (shared_datadir / "day5.txt").read_text()
    assert solution2(all_input) == 34039469
