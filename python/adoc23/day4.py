import re


def solution1(all_input: str) -> int:
    return sum(get_points_by_card(line) for line in all_input.splitlines())


def get_points_by_card(line: str) -> int:
    stripped_line = line.split(":", 1)[1]
    winning_numbers, my_card = stripped_line.split("|", 1)
    re_numbers = re.compile(r"(\d+)")
    winning_numbers = set(re_numbers.findall(winning_numbers))
    my_card = set(re_numbers.findall(my_card))
    num_winning_numbers = len(winning_numbers.intersection(my_card))
    if num_winning_numbers == 0:
        return 0
    return 2 ** (num_winning_numbers - 1)
