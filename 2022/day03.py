from math import floor
from typing import List
from utils.input_getter import get_input_for_day


def find_overlap(r: str) -> str:
    first = set(r[0 : floor(len(r) / 2)])
    second = set(r[floor(len(r) / 2) :])

    return first.intersection(second).pop()


def find_badge(e1: str, e2: str, e3: str) -> str:
    return set(e1).intersection(e2).intersection(e3).pop()


def priority(c: str) -> int:
    ascii_val = ord(c)
    if c == c.lower():
        return ascii_val - 96
    else:
        return ascii_val - 38


def compute_priorities(inputs: List[str]) -> int:
    sum = 0
    for input in inputs:
        sum += priority(find_overlap(input))
    return sum


def compute_badge_priorities(inputs: List[str]) -> int:
    sum = 0
    for i in range(0, len(inputs) - 2, 3):
        sum += priority(find_badge(*inputs[i : i + 3]))
    return sum


def first_star():
    inputs = get_input_for_day()
    print(compute_priorities(inputs))


def second_star():
    inputs = get_input_for_day()
    print(compute_badge_priorities(inputs))


if __name__ == "__main__":
    second_star()
