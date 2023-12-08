import math
import re
from decimal import Decimal


def calculate_num_possibilities(total_time: int, distance: int):
    delta = Decimal((total_time ** 2) - (4 * distance)).sqrt()
    root_left = max((-total_time + delta) / Decimal(-2), 0)
    if root_left.to_integral_value() == root_left:
        root_left += 1
    else:
        root_left = math.ceil(root_left)
    root_right = max((-total_time - delta) / Decimal(-2), 0)
    if root_right.to_integral_value() == root_right:
        root_right -= 1
    else:
        root_right = math.floor(root_right)
    return (root_right - root_left + 1)


def solution1(all_input: str) -> int:
    re_num = re.compile(r"(\d+)")
    struct_input = {}
    for line in all_input.splitlines():
        key, values = line.strip().split(":")
        struct_input[key] = [int(num) for num in re_num.findall(values)]
    num_runs = len(struct_input["Time"])
    result = 1
    for pos in range(num_runs):
        result *= calculate_num_possibilities(struct_input["Time"][pos], distance=struct_input["Distance"][pos])
    return result
