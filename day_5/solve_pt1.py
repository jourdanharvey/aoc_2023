from typing import List, Optional, Tuple

from common import Solver, file_lines


class GardenerMap:
    def __init__(self, source_name, destination_name) -> None:
        self.source_name = source_name
        self.destination_name = destination_name
        self.map = {}

    def add(self, destination_start:int , source_start:int , range_length:int ) -> None:
        """
        Add a line from the input. e.g. 50 98 2

        Confusingly the input is kind of the wrong way around. The source maps to destination, even though the input
        is opposite order, so the above example means we get:
            x  -> y
            98    50
            99    51
        """
        destination_range = range(destination_start, destination_start + range_length)
        source_range = range(source_start, source_start + range_length)
        self.map.update({k:v for k, v in zip(source_range, destination_range)})

    def get_destination(self, source):
        """
        For the given source get the destination. A source maps to itself if there is not an explicit mapping
        """
        destination_number = self.map.get(source, source)
        return destination_number, self.destination_name

    @property
    def full_name(self):
        return f"f{self.source_name}-{self.destination_name}"


class Almanac():

    def __init__(self, seeds: List[int]) -> None:
        self.garden_maps = {}
        self.seeds = seeds

    def add_garden_map(self, garden_map: Optional[GardenerMap]) -> None:
        # For the first blank line garden would be None
        if not garden_map:
            return
        self.garden_maps[garden_map.source_name] = garden_map


    def min_location(self):
        return min(self.traverse_for_location())

    def traverse_for_location(self):
        for seed in self.seeds:
            yield self.location(seed)

    def location(self, seed):
        destination_number, destination_name = seed, 'seed'
        while destination_name in self.garden_maps:
            garden_map = self.garden_maps[destination_name]
            destination_number, destination_name = garden_map.get_destination(destination_number)
        return destination_number

    @classmethod
    def build(cls, lines: List[str]) -> "Almanac":
        almanac = None
        garden_map = None
        for line in lines:
            if not almanac:
                almanac = Almanac(seeds=cls.parse_seeds(line))
            elif not line or line.isspace():
                almanac.add_garden_map(garden_map)
                garden_map = None
            elif not cls.is_mapping(line):
                # if we don't have a mapping we start a new garden map
                garden_map = GardenerMap(*cls.parse_garden_map_names(line))
            else:
                # only remaining option is a mapping
                garden_map.add(*cls.parse_raw_mapping(line))
        if garden_map is not None:
            almanac.add_garden_map(garden_map)
        return almanac

    @staticmethod
    def parse_garden_map_names(line: str) -> Tuple[str, str]:
        """
        E.g. "seed-to-soil map:", returns seed-to-soil
        """
        words = line.split()[0].split('-')
        # e.g. seed, soil
        return words[0], words[-1]

    @staticmethod
    def is_mapping(line: str) -> bool:
        """
        The line is a mapping if the first char is a digit
        Don't let perfect be the enemy of good
        """
        return len(line) > 0 and line[0].isdigit()

    @staticmethod
    def parse_seeds(line: str) -> List[int]:
        """
        e.g. "seeds: 79 14 55 13" returns list of ints
        """
        return [int(s) for s in line.split(':')[1].split()]

    @staticmethod
    def parse_raw_mapping(line: str) -> List[int]:
        return [int(s) for s in line.split()]

class DayFivePartOneSolver(Solver):
    @staticmethod
    def solve(lines: List[str]) -> None:
        almanac = Almanac.build(lines)
        return almanac.min_location()

if __name__ == "__main__":
    file_path = './day_5/input.txt'
    ans = DayFivePartOneSolver.solve(file_lines(file_path))
    print(ans)