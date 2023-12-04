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


def get_num_winning_numbers(line: str) -> int:
    stripped_line = line.split(":", 1)[1]
    winning_numbers, my_card = stripped_line.split("|", 1)
    re_numbers = re.compile(r"(\d+)")
    winning_numbers = set(re_numbers.findall(winning_numbers))
    my_card = set(re_numbers.findall(my_card))
    return len(winning_numbers.intersection(my_card))


def solution2(all_input: str) -> int:
    list_lines = all_input.strip().splitlines()
    all_winning_numbers = [get_num_winning_numbers(line) for line in list_lines]
    num_cards = [1] * len(list_lines)
    for pos, num_win in enumerate(all_winning_numbers):
        if num_win == 0:
            continue
        for i in range(pos + 1, pos + num_win + 1):
            if i >= len(list_lines):
                num_cards[-1] += 1
            else:
                num_cards[i] += num_cards[pos]
    return sum(num_cards)
