from typing import List


def solution1(all_input: str) -> int:
    matrix = [list(line) for line in all_input.splitlines()]
    result = 0
    for row_pos, line in enumerate(matrix):
        acc = ""
        flag = False
        for col_pos, character in enumerate(line):
            if not character.isdigit():
                if flag:
                    result += int(acc)
                acc = ""
                flag = False
                continue
            acc += character
            flag = flag or is_part_number(row_pos, col_pos, matrix)
        if flag:
            result += int(acc)
    return result


def is_part_number(row_pos: int, col_pos: int, matrix: List[List]) -> bool:
    special_char = set("[@_!#$%^&*()<>?/\|}{~:]+-=")
    row_start = max(row_pos - 1, 0)
    row_end = min(row_pos + 1, len(matrix) - 1)
    col_start = max(col_pos - 1, 0)
    col_end = min(col_pos + 1, len(matrix[0]) - 1)
    for row in range(row_start, row_end + 1):
        for col in range(col_start, col_end + 1):
            if matrix[row][col] in special_char:
                return True
    return False
