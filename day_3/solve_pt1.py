from dataclasses import dataclass
from typing import List, Tuple, Set
from functools import lru_cache
from common import Solver, file_lines


@dataclass(init=True, frozen=True, eq=True)
class Point:
    x: int
    y: int

@dataclass(init=True, frozen=True, eq=True)
class PartNumber:
    number: int
    left_point: Point
    right_point: Point

    def eligible_symbols(self) -> Set[Point]:
        line_number = self.left_point.y  # will be same as right point
        leftist = Point(x=self.left_point.x - 1, y=line_number)
        rightist = Point(x=self.right_point.x + 1, y=line_number)
        prev_line = set(Point(x=i, y=line_number - 1) for i in range(leftist.x, rightist.x + 1))
        next_line = set(Point(x=i, y=line_number + 1) for i in range(leftist.x, rightist.x + 1))
        return {leftist, rightist} | prev_line | next_line

def build_part_number(number_repr: List[Tuple[str, Point]]) -> PartNumber:
    left_point = number_repr[0][1]
    right_point = number_repr[-1][1]
    number = int(''.join(c for c, _ in number_repr))
    return PartNumber(number=number, left_point=left_point, right_point=right_point)

@lru_cache(maxsize=2)
def parse_line(line: str, line_number: int) -> Tuple[Set, Set]:
    if not line:
        return set(), set()
    part_numbers, symbols = set(), set()
    current_number = []
    for idx, c in enumerate(line):
        if c.isdigit():
            current_number.append((c, Point(x=idx, y=line_number)))
            continue
        # Not a number, purge current_number if needed
        if len(current_number) > 0:
            part_numbers.add(build_part_number(current_number))
            current_number = []
        # See if we're a symbol and process accordingly
        if c != '.' and not c.isspace():
            symbols.add(Point(x=idx, y=line_number))
    else:
        # final purge
        if len(current_number) > 0:
            part_numbers.add(build_part_number(current_number))

    return part_numbers, symbols

def engine_parser(lines: List[str]) -> PartNumber:
    previous_symbols = set()
    for idx, line in enumerate(lines):
        parts, symbols = parse_line(line, idx)

        next_idx = idx + 1
        next_line = lines[next_idx] if next_idx < len(lines) else None
        _, next_symbols = parse_line(next_line, next_idx)

        all_symbols = previous_symbols | symbols | next_symbols

        for part in parts:
            if part.eligible_symbols() & all_symbols:
                yield part
        previous_symbols = symbols

class DayThreePartOneSolver(Solver):
    @staticmethod
    def solve(lines: List[str]) -> None:
        parts = set(engine_parser(lines))
        return sum(part.number for part in parts)


if __name__ == "__main__":
    file_path = './day_3/input.txt'
    ans = DayThreePartOneSolver.solve(file_lines(file_path))
    print(ans)
