from itertools import product
from typing import Any, List
from common import Solver, file_lines, ignored, two_dimensional_generator

DOT = '.'

CARDINAL_POINTS = set(product([-1,0,1], repeat=2)) - {(0,0)}

def possible_symbol_locations(x, y):
    for poss_x, poss_y in CARDINAL_POINTS:
        yield poss_x + x, poss_y + y

def is_symbol(c: str):
    return c != DOT and not c.isdigit()

def find_symbol(char_x: int, char_y: int, lines: List[str]) -> bool:
    for x, y in possible_symbol_locations(char_x, char_y):
        with ignored(IndexError):
            c = lines[x][y]
            if is_symbol(c):
                return True
    else:
        return False

def find_parts(lines: List[str]) -> int:
    number, touches = '', False
    for x, y, c in two_dimensional_generator(lines):
        if c.isdigit():
            number += c
            touches = touches or find_symbol(x, y, lines)
        else:
            yield int(touches and number)
            number, touches = '', False
    else:
        yield int(touches and number)


class DayThreePartOneTakeTwoSolver(Solver):
    @staticmethod
    def solve(lines: List[str]) -> None:
        return sum(find_parts(lines))


if __name__ == "__main__":
    file_path = './day_3/input.txt'
    ans = DayThreePartOneTakeTwoSolver.solve(file_lines(file_path))
    print(ans)
