
from collections import namedtuple, deque

from typing import List

from common import Solver, file_lines
from day_4.common import parse_card

def score_card(card: str) -> int:
    winners, have = parse_card(card)
    return len(winners & have)

GameState = namedtuple('GameState', ('copies', 'score'))

class DayFourPartTwoSolver(Solver):
    @staticmethod
    def solve(lines: List[str]) -> None:
        state = deque(GameState(copies=1, score=score_card(card)) for card in lines)
        score = len(state)
        while len(state) > 1:
            current_copies, current_score = state.popleft()
            score += current_copies * current_score
            for i in range(current_score):
                item = state[i]
                state[i] = GameState(copies=item.copies + current_copies, score=item.score)

        return score

if __name__ == "__main__":
    file_path = './day_4/input.txt'
    ans = DayFourPartTwoSolver.solve(file_lines(file_path))
    print(ans)
