from dataclasses import dataclass
from enum import Enum, IntEnum
from typing import List
from utils.input_getter import get_input_for_day


class Outcome(IntEnum):
    LOSS = 0
    DRAW = 3
    WIN = 6


class Shape(Enum):
    ROCK = 1
    PAPER = 2
    SCISSOR = 3


WINNING_OUTCOMES = {  # value wins against key
    Shape.ROCK: Shape.PAPER,
    Shape.PAPER: Shape.SCISSOR,
    Shape.SCISSOR: Shape.ROCK,
}
LOSING_OUTCOMES = {  # value loses against key
    Shape.SCISSOR: Shape.PAPER,
    Shape.ROCK: Shape.SCISSOR,
    Shape.PAPER: Shape.ROCK,
}

FIRST_LABELS = {"A": Shape.ROCK, "B": Shape.PAPER, "C": Shape.SCISSOR}
FIRST_STAR_SECOND_LABELS = {"X": Shape.ROCK, "Y": Shape.PAPER, "Z": Shape.SCISSOR}
SECOND_STAR_LABELS = {"X": Outcome.LOSS, "Y": Outcome.DRAW, "Z": Outcome.WIN}


@dataclass
class FirstStarRound:
    first: Shape
    second: Shape

    @staticmethod
    def parse(input: str) -> "FirstStarRound":
        [f, s] = input.split(" ")

        try:
            first = FIRST_LABELS[f]
            second = FIRST_STAR_SECOND_LABELS[s]
        except:
            print(f"Failed to parse round from {input}")
            raise

        return FirstStarRound(first, second)

    def outcome(self) -> Outcome:
        if self.first == self.second:
            return Outcome.DRAW
        elif self.second == WINNING_OUTCOMES[self.first]:
            return Outcome.WIN
        else:
            return Outcome.LOSS

    def score(self) -> int:
        return self.outcome().value + self.second.value


@dataclass
class SecondStarRound:
    first: Shape
    outcome: Outcome

    @staticmethod
    def parse(input: str) -> "SecondStarRound":
        [f, o] = input.split(" ")

        first = FIRST_LABELS[f]
        outcome = SECOND_STAR_LABELS[o]
        return SecondStarRound(first, outcome)

    def compute_needed_move(self) -> Shape:

        if self.outcome == Outcome.DRAW:
            return self.first
        elif self.outcome == Outcome.WIN:
            return WINNING_OUTCOMES[self.first]
        else:
            return LOSING_OUTCOMES[self.first]

    def score(self) -> int:
        return self.outcome.value + self.compute_needed_move().value


def sum_first_star_rounds(input: List[str]) -> int:
    sum = 0
    rounds = [FirstStarRound.parse(i) for i in input if i]
    for round in rounds:
        sum += round.score()
    return sum


def sum_second_star_rounds(input: List[str]) -> int:
    sum = 0
    rounds = [SecondStarRound.parse(i) for i in input if i]
    for round in rounds:
        sum += round.score()
    return sum


def first_star():
    inputs = get_input_for_day()
    print(sum_first_star_rounds(inputs))


def second_star():
    inputs = get_input_for_day()
    print(sum_second_star_rounds(inputs))


if __name__ == "__main__":
    first_star()
    second_star()
