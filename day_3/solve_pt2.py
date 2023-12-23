from collections import deque
from typing import List, Optional, Set, Tuple

from common import Solver, file_lines, ignored, two_dimensional_generator


from day_3.common import is_symbol, surrounding_points

GEAR = "*"


def isdigit(c):
    return c is not None and c.isdigit()

def scan_for_number(x: int, y: int, lines: List[str]) -> Tuple[Optional[int], Set[Tuple[int, int]]]:
    sentinal = None, set()
    number_deque = deque()
    visited = set()

    if not (0 <= y < len(lines) and 0 <= x < len(lines[y])):
        return sentinal

    line = lines[y]
    c = line[x]
    if not isdigit(c):
        return sentinal
    idx = x
    while 0 <= idx < len(line) and isdigit(line[idx]):
        number_deque.append(line[idx])
        visited.add((idx, y))
        idx += 1
    idx = x - 1
    while 0 <= idx < len(line) and isdigit(line[idx]):
        number_deque.appendleft(line[idx])
        visited.add((idx, y))
        idx -= 1
    number = int("".join(number_deque)) if len(number_deque) > 0 else None
    return number, visited


def get_surrounding_numbers(gear_x: int, gear_y: int, lines: List[str]) -> List[int]:
    numbers = []
    visited = set()
    for x, y in surrounding_points(gear_x, gear_y):
        if (x, y) in visited:
            continue
        new_number, new_visits = scan_for_number(x, y, lines)
        if new_number is not None:
            numbers.append(new_number)
        visited |= new_visits
    return numbers

def gear_ratio(x, y, lines) -> int:
    numbers = get_surrounding_numbers(x, y, lines)
    if len(numbers) == 2:
        return numbers[0] * numbers[1]
    return 0

def gear_ratios(lines: List[str]) -> int:
    for x, y, c in two_dimensional_generator(lines):
        if c == GEAR:
            yield gear_ratio(x, y, lines)


class DayThreePartTwoSolver(Solver):
    @staticmethod
    def solve(lines: List[str]) -> None:
        return sum(gear_ratios(lines))


if __name__ == "__main__":
    file_path = './day_3/input.txt'
    ans = DayThreePartTwoSolver.solve(file_lines(file_path))
    print(ans)
