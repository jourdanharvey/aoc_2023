from abc import ABC, abstractmethod
from contextlib import contextmanager
from typing import Any, List, Iterator, Tuple, TypeVar

def file_lines(file_path: str) -> List[str]:
    return list([l.strip() for l in file_lines_genertor(file_path)])


def file_lines_genertor(file_path: str) -> str:
    with open(file_path, 'r') as file:
        for line in file:
            yield line


class Solver(ABC):
    @abstractmethod
    def solve(self, lines):
        ...

@contextmanager
def ignored(*exceptions):
    try:
        yield
    except exceptions:
        pass

T = TypeVar("T")

def two_dimensional_generator(rows: List[List[T]]) -> Tuple[int, int, T]:
    for x, row in enumerate(rows):
        for y, cell in enumerate(row):
            yield x, y, cell
