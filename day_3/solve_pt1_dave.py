from dataclasses import dataclass
from typing import List, Tuple, Set
from functools import lru_cache
from common import Solver, file_lines


class DayThreePartOneDaveSolver(Solver):
    @staticmethod
    def solve(lines: List[str]) -> None:
        if len(lines) == 0:
            return 0
        scanning = 'SCANNING'
        unseen_building = 'UNSEEN_BUILDING'
        seen_building = 'SEEN_BUILDING'

        state = scanning
        n = len(lines)
        m = len(lines[0])
        curr_number = 0
        total = 0

        def can_reach_symbol(row, col):
            for i in (-1, 0, 1):
                for j in (-1, 0, 1):
                    try:
                        c = lines[row+i][col+j]
                        if not (c.isdigit() or c == '.' or c.isspace()):
                            return True
                    except IndexError:
                        pass
            return False

        for i in range(n):
            for j in range(m):
                c = lines[i][j]
                if c.isdigit():
                    curr_number =  curr_number * 10 + int(c)
                    if can_reach_symbol(i,j) or state == seen_building:
                        state =  seen_building
                    else:
                        state = unseen_building
                else:
                    if state == seen_building:
                        total += curr_number
                    curr_number = 0
                    state = scanning
            if state == seen_building:
                total += curr_number
                curr_number = 0
                state = scanning

        return total


if __name__ == "__main__":
    file_path = './day_3/input.txt'
    ans = DayThreePartOneDaveSolver.solve(file_lines(file_path))
    print(ans)
