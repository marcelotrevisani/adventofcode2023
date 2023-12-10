import math
import re
from collections import deque
from copy import copy
from typing import List


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


def solution2_algorithm_endless(all_input: str) -> int:
    all_steps = deque(all_input.splitlines()[0].strip())
    all_nodes = re.findall(
        r"^(\w+)\s+=\s+\((\w+),\s+(\w+)\)$", all_input[1:], re.MULTILINE
    )
    refs_node = {ref_node.strip(): nodes for ref_node, *nodes in all_nodes}
    current_nodes = [
        node.strip() for node in refs_node.keys() if node.strip()[-1] == "A"
    ]
    count = 0
    while not check_end(current_nodes):
        count += 1
        pos = 0 if all_steps[0] == "L" else 1
        current_nodes = [refs_node[node][pos] for node in current_nodes]
        all_steps.rotate(-1)
    return count


def check_end(current_nodes: List[str]) -> bool:
    return all(node[-1] == "Z" for node in current_nodes)


def solution2(all_input: str) -> int:
    lr = deque(all_input.splitlines()[0].strip())
    all_nodes = re.findall(
        r"^(\w+)\s+=\s+\((\w+),\s+(\w+)\)$", all_input[1:], re.MULTILINE
    )
    refs_node = {ref_node.strip(): nodes for ref_node, *nodes in all_nodes}
    current_nodes = [
        node.strip() for node in refs_node.keys() if node.strip()[-1] == "A"
    ]
    initial_node = copy(current_nodes)
    all_pos = [0 for _ in range(len(current_nodes))]
    all_z = ["" for _ in range(len(current_nodes))]
    all_loops = []
    for pos, node_start in enumerate(initial_node):
        lr_copy = copy(lr)
        left_right = 0 if lr_copy[0] == "L" else 1
        lr_copy.rotate(-1)
        current_nodes[pos] = refs_node[current_nodes[pos]][left_right]
        count = 1
        while node_start != current_nodes[pos]:
            count += 1
            left_right = 0 if lr_copy[0] == "L" else 1
            lr_copy.rotate(-1)
            if current_nodes[pos][-1] == "Z":
                if all_z[pos] and current_nodes[pos] in all_z[pos]:
                    break
                all_z[pos] = current_nodes[pos]
                all_pos[pos] = count
            current_nodes[pos] = refs_node[current_nodes[pos]][left_right]
        all_loops.append(count)

    return math.lcm(*[i - j for i, j in zip(all_loops, all_pos)])
