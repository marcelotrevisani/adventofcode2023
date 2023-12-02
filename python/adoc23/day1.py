import re


def solution1(all_input_str: str) -> int:
    re_int = re.compile(r"(\d)")
    all_numbers = [re_int.findall(num) for num in all_input_str.splitlines()]
    return sum(int(f"{num[0]}{num[-1]}") for num in all_numbers)
