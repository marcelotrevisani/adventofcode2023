import re


def solution1(all_input_str: str) -> int:
    re_int = re.compile(r"(\d)")
    all_numbers = [re_int.findall(num) for num in all_input_str.splitlines()]
    return sum(int(f"{num[0]}{num[-1]}") for num in all_numbers)


def solution2(all_input_str: str) -> int:
    mapping_int = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    re_int = re.compile(r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))")
    all_numbers = (re_int.findall(num) for num in all_input_str.splitlines())
    return sum(
        int(f"{mapping_int.get(num[0], num[0])}{mapping_int.get(num[-1], num[-1])}")
        for num in all_numbers
    )
