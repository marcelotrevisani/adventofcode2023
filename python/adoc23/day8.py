import re
from collections import deque


def solution1(all_input: str) -> int:
    all_steps = deque(all_input.splitlines()[0].strip())
    all_nodes = re.findall(
        r"^(\w+)\s+=\s+\((\w+),\s+(\w+)\)$", all_input[1:], re.MULTILINE
    )
    refs_node = {ref_node: nodes for ref_node, *nodes in all_nodes}
    current_node = "AAA"
    count = 0
    while current_node != "ZZZ":
        count += 1
        pos = 0 if all_steps[0] == "L" else 1
        current_node = refs_node[current_node][pos]
        all_steps.rotate(-1)
    return count

