import re


def solution1(all_input: str) -> int:
    return sum(get_valid_game(line) for line in all_input.splitlines())


def get_valid_game(line: str) -> int:
    max_cubes = {"red": 12, "blue": 14, "green": 13}
    re_game = re.compile(r"^Game\s+(\d+)")
    re_set = re.compile(r"(\d+)\s+(red|blue|green)")
    game = int(re_game.match(line).group(1))
    for set_block in line.split(";"):
        for val, color in re_set.findall(set_block):
            if max_cubes[color] - int(val) < 0:
                return 0
    return game
