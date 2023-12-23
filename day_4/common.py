from typing import Set, Tuple


def numbers_str_to_set(numbers: str) -> Set[int]:
    return set(int(n) for n in numbers.split())


def parse_card(card: str) -> Tuple[Set[int], Set[int]]:
    winners_str, have_str = card.split(':')[1].split('|')
    return numbers_str_to_set(winners_str), numbers_str_to_set(have_str)
