from typing import List
from collections import defaultdict
from dataclasses import dataclass


@dataclass(init=True, eq=True, repr=True)
class GameSet:
    red: int = 0
    blue: int = 0
    green: int = 0

    def power(self) -> int:
        return (self.red or 1) * (self.blue or 1) * (self.green or 1)

    def merge(self, other: "GameSet") -> None:
        self.red = max(self.red, other.red)
        self.blue = max(self.blue, other.blue)
        self.green = max(self.green, other.green)

    def __le__(self, other: "GameSet") -> bool:
        return all([
            self.red <= other.red,
            self.blue <= other.blue,
            self.green <= other.green,
        ])

@dataclass
class Game:
    id: int
    game_sets: List[GameSet]


def get_id(text: str) -> int:
    return int(text.split(':')[0].split(' ')[1])

def cube_generator(cubes_text: str):
    for cube in cubes_text.split(','):
        count, key = cube.strip().split(' ')
        yield key, int(count)

def get_counts(text: str) -> dict:
    counts = defaultdict(int)
    for key, count in cube_generator(text):
        counts[key] += count
    return counts

def get_game_sets(text):
    for set_text in text.split(';'):
        yield GameSet(**get_counts(set_text))

def build_game(line: str) -> Game:
    id_text, sets_text = line.split(':')
    _, id = id_text.split(' ')
    return Game(id=id, game_sets=list(get_game_sets(sets_text)))

def game_parser(file_str: str) -> int:
    with open(file_str, 'r') as file:
        for line in file:
            game = build_game(line)
            max_game_set = GameSet()
            for game_set in game.game_sets:
                max_game_set.merge(game_set)
            yield max_game_set.power()

print(sum(game_parser('./input.txt')))