import dataclasses
import multiprocessing
import re
from collections import namedtuple
from typing import List
import itertools

SourceDest = namedtuple("SourceDest", ["source", "dest"])


def build_converters(all_inputs: List[str]) -> List[List]:
    re_num = re.compile(r"(\d+)")
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


def process_seed_chunk(seed_chunk, all_converters):
    return min(get_final_number(seed, all_converters) for seed in seed_chunk)


def solution2(all_input: str) -> int:
    all_lines = all_input.splitlines()
    all_seeds = []
    for seed in re.finditer(r"(\d+)\s+(\d+)", all_lines[0]):
        start, step = seed.groups()
        start = int(start)
        end = start + int(step)
        all_seeds.append(range(start, end))
    all_converters = build_converters(all_lines[1:])
    num_processes = multiprocessing.cpu_count()
    result = None
    for batch in all_seeds:
        if len(batch) <= num_processes:
            seed_chunks = [batch]
        else:
            step = len(batch) // num_processes
            start = batch.start
            seed_chunks = [
                range(start + (step * i), start + (step * (i + 1)))
                for i in range(num_processes)
            ]
            seed_chunks[-1] = range(seed_chunks[-1].start, batch.stop)

        with multiprocessing.Pool(processes=num_processes) as pool:
            results = min(
                pool.starmap(
                    process_seed_chunk,
                    [(chunk, all_converters) for chunk in seed_chunks],
                )
            )

        if result is None:
            result = results
        else:
            result = min(result, results)
    return result
