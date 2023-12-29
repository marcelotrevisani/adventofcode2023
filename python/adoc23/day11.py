import itertools


def solution1(all_input: str) -> int:
    all_input = [list(line) for line in all_input.splitlines()]
    blank_col, blank_line = get_expanded_positions(all_input)
    expand_universe(all_input, blank_col, blank_line)
    all_points = get_all_points(all_input)
    result = 0
    for point1, point2 in itertools.combinations(all_points, 2):
        result += abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
    return result


def expand_universe(all_input, blank_col, blank_line):
    for line in all_input:
        for shift, col_pos in enumerate(sorted(blank_col)):
            line.insert(col_pos + shift, ".")
    for shift, line_pos in enumerate(sorted(blank_line)):
        all_input.insert(line_pos + shift, ["."] * len(all_input[0]))


def get_expanded_positions(all_input):
    blank_line = []
    blank_col = [True] * len(all_input[0])
    for pos_line, line in enumerate(all_input):
        if len(set(line)) == 1:
            blank_line.append(pos_line)
        for pos_col, col in enumerate(line):
            blank_col[pos_col] &= col == "."
    blank_col = [pos for pos, col in enumerate(blank_col) if col]
    return blank_col, blank_line


def get_all_points(all_input: list[list[str]]) -> list[tuple[int, int]]:
    all_points = []
    for line_pos, line in enumerate(all_input):
        for col_pos, col in enumerate(line):
            if col != ".":
                all_points.append((line_pos, col_pos))
    return all_points


def get_all_points_without_changing_universe(
    all_input: list[list[str]], expansion: int
) -> list[tuple[int, int]]:
    blank_col, blank_line = get_expanded_positions(all_input)
    blank_col.sort()
    blank_line.sort()
    result = []
    for line_pos, line in enumerate(all_input):
        for col_pos, col in enumerate(line):
            if col == ".":
                continue
            num_line_shift = sum(line_pos > val for val in blank_line)
            shift_line = num_line_shift * expansion
            num_col_shift = sum(col_pos > val for val in blank_col)
            shift_col = num_col_shift * expansion
            if shift_line > 0:
                shift_line -= num_line_shift
            if shift_col > 0:
                shift_col -= num_col_shift
            result.append((line_pos + shift_line, col_pos + shift_col))
    return result


def solution2(all_input: str, expansion: int = 1_000_000) -> int:
    all_input = [list(line) for line in all_input.splitlines()]
    all_points = get_all_points_without_changing_universe(all_input, expansion)
    result = 0
    for point1, point2 in itertools.combinations(all_points, 2):
        result += abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
    return result
