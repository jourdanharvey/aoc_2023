from typing import List

from common import Solver, file_lines
from day_4.common import parse_card

def score_game(game: str) -> int:
    winners, have = parse_card(game)
    n_overlap = len(winners & have)
    return 2**(n_overlap-1) if n_overlap > 0 else 0

class DayFourPartOneSolver(Solver):
    @staticmethod
    def solve(lines: List[str]) -> None:
        return sum((score_game(line) for line in lines))

if __name__ == "__main__":
    file_path = './day_4/input.txt'
    ans = DayFourPartOneSolver.solve(file_lines(file_path))
    print(ans)