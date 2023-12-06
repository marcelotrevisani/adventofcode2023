import re
from collections import namedtuple
from typing import List


def build_converters(all_inputs: List[str]) -> List[List]:
    re_num = re.compile(r"(\d+)")
    SourceDest = namedtuple("SourceDest", ["source", "dest"])
    result = []
    acc = []
    for line in all_inputs:
        if not line:
            continue
        line = line.strip()
        if line[0].isdigit() is False:
            if acc:
                result.append(acc)
            acc = []
            continue
        dist_start, source_start, step = re_num.findall(line)
        source_start = int(source_start)
        dist_start = int(dist_start)
        step = int(step)
        acc.append(
            SourceDest(
                source=range(source_start, source_start + step),
                dest=range(dist_start, dist_start + step),
            )
        )
    result.append(acc)
    return result


def convert_source_to_dest(seed: int, converter_section: List[range]) -> int:
    for converter in converter_section:
        if seed in converter.source:
            id_source = converter.source.index(seed)
            return converter.dest[id_source]
    return seed


def get_final_number(seed: int, all_converters: List[List]) -> int:
    for converter_section in all_converters:
        if converter_section:
            seed = convert_source_to_dest(seed, converter_section)
    return seed


def solution1(all_input: str) -> int:
    re_num = re.compile(r"(\d+)")
    all_lines = all_input.splitlines()
    all_converters = build_converters(all_lines[1:])
    all_seeds = [int(i.group(1)) for i in re_num.finditer(all_lines[0])]
    return min(get_final_number(seed, all_converters) for seed in all_seeds)
