import re


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
