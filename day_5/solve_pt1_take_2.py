from collections import namedtuple
from typing import List, Optional, Tuple

from common import Solver, file_lines

def parse_garden_map_names(line: str) -> Tuple[str, str]:
    """
    E.g. "seed-to-soil map:", returns seed-to-soil
    """
    words = line.split()[0].split('-')
    # e.g. seed, soil
    return words[0], words[-1]

def is_mapping(line: str) -> bool:
    """
    The line is a mapping if the first char is a digit
    Don't let perfect be the enemy of good
    """
    return len(line) > 0 and line[0].isdigit()

def parse_seeds(line: str) -> List[int]:
    """
    e.g. "seeds: 79 14 55 13" returns list of ints
    """
    return [int(s) for s in line.split(':')[1].split()]

def parse_raw_mapping(line: str) -> List[int]:
    return [int(s) for s in line.split()]

def is_blank(line: str) -> bool:
    return not line or line.isspace()

Mapping = namedtuple('Mapping', ('source', 'dest', 'range_len'))

class Almanac:
    def __init__(self):
        self.mappings = []

    def add_mapping_from_line(self, line: str) -> None:
        dest, source, range_len = parse_raw_mapping(line)
        self.mappings.append(Mapping(source, dest, range_len))

    def reset(self) -> None:
        self.__init__()

    def process_destinations(self, destinations: List[int]) -> List[int]:
        return [self.navigate(d) for d in destinations]

    def navigate(self, source: int) -> int:
        for map_source, map_dest, range_len in self.mappings:
            # inclusive, exclusive
            min_inc, max_exc = map_source, map_source + range_len
            if min_inc <= source < max_exc:
                return source - map_source + map_dest
        return source

class DayFivePartOneTakeTwoSolver(Solver):
    @staticmethod
    def solve(lines: List[str]) -> int:
        destinations = parse_seeds(lines[0])
        almanac = Almanac()
        for line in lines[2:]:
            if is_blank(line):
                destinations = almanac.process_destinations(destinations)
                almanac.reset()
                continue
            if is_mapping(line):
                almanac.add_mapping_from_line(line)
        destinations = almanac.process_destinations(destinations)
        return min(destinations)

if __name__ == "__main__":
    file_path = './day_5/input.txt'
    ans = DayFivePartOneTakeTwoSolver.solve(file_lines(file_path))
    print(ans)