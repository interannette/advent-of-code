from dataclasses import dataclass
from typing import List
from utils.input_getter import get_input_for_day


@dataclass
class Range:
    start: int
    end: int

    @staticmethod
    def parse(input: str) -> "Range":
        start, end = input.split("-")
        return Range(int(start), int(end))

    def overlaps(self, other: "Range") -> bool:
        # if one is totally before the other, there is no overlap
        # otherwise, there is overlap
        no_overlap = (self.end < other.start) or (other.end < self.start)
        return not no_overlap

    def contains(self, other: "Range") -> bool:
        return self.start <= other.start and other.end <= self.end


def sum_contains(inputs: List[str]) -> int:
    sum = 0
    for input in inputs:
        first_str, second_str = input.split(",")
        first = Range.parse(first_str)
        second = Range.parse(second_str)

        if first.contains(second) or second.contains(first):
            sum += 1

    return sum


def sum_overlaps(inputs: List[str]) -> int:
    sum = 0
    for input in inputs:
        first_str, second_str = input.split(",")
        first = Range.parse(first_str)
        second = Range.parse(second_str)

        if first.overlaps(second):
            sum += 1

    return sum


def first_star():
    input = get_input_for_day()
    print(sum_contains(input))


def second_star():
    input = get_input_for_day()
    print(sum_overlaps(input))


if __name__ == "__main__":
    second_star()
