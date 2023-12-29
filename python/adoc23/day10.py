import bisect
import re
from collections import defaultdict
from operator import itemgetter


def solution1(all_input: str) -> int:
    all_input = list(all_input.splitlines())
    starting_point = (0, 0)
    size = (len(all_input), len(all_input[0]))
    for pos, line in enumerate(all_input):
        if "S" in line:
            starting_point = (pos, line.find("S"))
            break
    map_mov = {
        "|": [(1, 0), (-1, 0)],
        "-": [(0, -1), (0, 1)],
        "L": [(0, 1), (-1, 0)],
        "J": [(0, -1), (-1, 0)],
        "7": [(1, 0), (0, -1)],
        "F": [(1, 0), (0, 1)],
        ".": [(0, 0), (0, 0)],
    }
    count = 1
    next_point = [
        (starting_point[0] + 1, starting_point[1]),
        (starting_point[0] - 1, starting_point[1]),
        (starting_point[0], starting_point[1] + 1),
        (starting_point[0], starting_point[1] - 1),
    ]
    next_point = [
        (i, j) for i, j in next_point if i >= 0 and j >= 0 and all_input[i][j] != "."
    ]
    current = next_point[0]
    previous_point = starting_point
    while current != starting_point:
        mv = map_mov[all_input[current[0]][current[1]]]
        next_point = (current[0] + mv[0][0], current[1] + mv[0][1])
        if next_point == previous_point:
            next_point = (current[0] + mv[1][0], current[1] + mv[1][1])
        previous_point = current
        current = next_point
        count += 1
    return count // 2


def solution2(all_input: str) -> int:
    all_input = list(all_input.splitlines())
    starting_point = (0, 0)
    for pos, line in enumerate(all_input):
        if "S" in line:
            starting_point = (pos, line.find("S"))
            break
    next_point = [
        (starting_point[0] + 1, starting_point[1]),
        (starting_point[0] - 1, starting_point[1]),
        (starting_point[0], starting_point[1] + 1),
        (starting_point[0], starting_point[1] - 1),
    ]
    next_point = [
        (i, j) for i, j in next_point if i >= 0 and j >= 0 and all_input[i][j] != "."
    ]
    trace, all_points = get_trace(all_input, next_point, starting_point)
    count = 0
    for line_pos, line in enumerate(all_input[1:-1], start=1):
        for col_pos, col in enumerate(line[1:-1], start=1):
            if (line_pos, col_pos) in all_points:
                continue
            if abs(sum(trace[line_pos][:col_pos])) == 1:
                count += 1
    return count


def get_trace(all_input, next_point, starting_point):
    map_mov = {
        "|": [(1, 0), (-1, 0)],
        "-": [(0, -1), (0, 1)],
        "L": [(0, 1), (-1, 0)],
        "J": [(0, -1), (-1, 0)],
        "7": [(1, 0), (0, -1)],
        "F": [(1, 0), (0, 1)],
        ".": [(0, 0), (0, 0)],
    }
    num_lines, num_cols = (len(all_input), len(all_input[0]))
    start_val = get_start_val_symbol(map_mov, next_point, starting_point)
    all_points = set()
    all_input[starting_point[0]] = all_input[starting_point[0]].replace("S", start_val)
    current = starting_point
    next_point = next_point[0]
    previous_point = None
    trace = [[0] * num_cols for _ in range(num_lines)]
    while next_point != starting_point:
        all_points.add(current)
        mv = map_mov[all_input[current[0]][current[1]]]
        next_point = (current[0] + mv[0][0], current[1] + mv[0][1])
        if next_point == previous_point:
            next_point = (current[0] + mv[1][0], current[1] + mv[1][1])
        if previous_point:
            trace[current[0]][current[1]] = (next_point[0] - previous_point[0]) / 2
        previous_point = current
        current = next_point
    if start_val != "-":
        trace[starting_point[0]][starting_point[1]] = (-1) * sum(
            trace[starting_point[0]]
        )
    return trace, all_points


def get_start_val_symbol(map_mov, next_point, starting_point):
    start_val = ""
    for val, pos in map_mov.items():
        pos1, pos2 = pos
        if (
            pos1[0] + starting_point[0],
            pos1[1] + starting_point[1],
        ) in next_point and (
            pos2[0] + starting_point[0],
            pos2[1] + starting_point[1],
        ) in next_point:
            start_val = val
            break
    return start_val
