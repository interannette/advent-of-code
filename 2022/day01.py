from typing import List
from utils.input_getter import get_input_for_day
from dataclasses import dataclass


@dataclass
class Elf:
    pos: int
    calories: int

    def add(self, more):
        self.calories += more


def build_elves(inputs: List[str]) -> List[Elf]:
    elves = [Elf(1, 0)]

    for input in inputs:
        if input == "":
            elves.append(Elf(elves[-1].pos + 1, 0))
        else:
            elves[-1].add(int(input))
    return elves


def find_max_elf(inputs: List[str]) -> Elf:
    elves = build_elves(inputs)
    max_elf = max(elves, key=lambda x: x.calories)
    return max_elf


def find_top_three_elves(inputs: List[str]) -> List[Elf]:
    elves = build_elves(inputs)
    elves.sort(key=lambda x: x.calories, reverse=True)
    return elves[0:3]


def first_star():
    inputs = get_input_for_day(1)
    print(find_max_elf(inputs))


def second_star():
    inputs = get_input_for_day(1)
    top_three = find_top_three_elves(inputs)
    print(f"Top three: {top_three}. Total {sum([e.calories for e in top_three])}")


if __name__ == "__main__":
    second_star()
