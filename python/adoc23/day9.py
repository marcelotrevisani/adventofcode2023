import re
from typing import List


def find_next_number(all_num: List[int]) -> int:
    current_line = all_num
    result = 0
    while any(num != 0 for num in current_line):
        result += current_line[-1]
        new_line = [val - current_line[pos] for pos, val in enumerate(current_line[1:])]
        current_line = new_line
    return result


def solution1(all_input: str) -> int:
    re_num = re.compile(r"([-]*\d+)")
    result = 0
    for line in all_input.splitlines():
        all_num = [int(num) for num in re_num.findall(line)]
        result += find_next_number(all_num)
    return result


def solution2(all_input: str) -> int:
    re_num = re.compile(r"([-]*\d+)")
    result = 0
    for line in all_input.splitlines():
        all_num = [int(num) for num in reversed(re_num.findall(line))]
        result += find_next_number(all_num)
    return result
