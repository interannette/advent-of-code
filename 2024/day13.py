from dataclasses import dataclass
import logging
import re
from typing import Iterable

logger = logging.getLogger()
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)


@dataclass(frozen=True)
class Coordinate:
    x: int
    y: int


@dataclass
class Machine:
    a_rule: Coordinate
    b_rule: Coordinate
    prize_location: Coordinate

    def cost_to_win(self) -> int:
        # a_rule.x * m + b_rule.x * n = prize_location.x
        # a_rule.y * m + b_rule.y * n = prize_location.y
        # min: 3 * m + n
        m = (
            (self.prize_location.x / self.b_rule.x)
            - (self.prize_location.y / self.b_rule.y)
        ) / ((self.a_rule.x / self.b_rule.x) - (self.a_rule.y / self.b_rule.y))
        n = (
            (self.prize_location.y / self.a_rule.y)
            - (self.prize_location.x / self.a_rule.x)
        ) / ((self.b_rule.y / self.a_rule.y) - (self.b_rule.x / self.a_rule.x))

        m = int(round(m))
        n = int(round(n))

        if ((self.a_rule.x * m + self.b_rule.x * n) == self.prize_location.x) and (
            (self.a_rule.y * m + self.b_rule.y * n) == self.prize_location.y
        ):
            return 3 * m + n
        else:
            return 0


class Day13Star1Puzzle:
    machines: list[Machine]

    a_pattern = re.compile("Button A: X\+(\d+), Y\+(\d+)")
    b_pattern = re.compile("Button B: X\+(\d+), Y\+(\d+)")
    prize_pattern = re.compile("Prize: X=(\d+), Y=(\d+)")

    def __init__(self, input_lines: Iterable[str]):
        machines = []
        a: Coordinate = None
        b: Coordinate = None
        prize: Coordinate = None
        for l in input_lines:
            l = l.strip()
            if (
                l == ""
            ):  # I added a line to my input to get this to capture the last one
                if a and b and prize:
                    machines.append(Machine(a_rule=a, b_rule=b, prize_location=prize))
                    a = None
                    b = None
                    prize = None

            elif "A" in l:
                matches = self.a_pattern.findall(l)
                if matches:
                    a = Coordinate(int(matches[0][0]), int(matches[0][1]))
            elif "B" in l:
                matches = self.b_pattern.findall(l)
                if matches:
                    b = Coordinate(int(matches[0][0]), int(matches[0][1]))
            elif "P" in l:
                matches = self.prize_pattern.findall(l)
                if matches:
                    prize = Coordinate(int(matches[0][0]), int(matches[0][1]))

        logger.debug(f"Created with {len(machines)} machines")
        self.machines = machines

    def star1(self) -> int:
        return sum([m.cost_to_win() for m in self.machines])


class Day13Star2Puzzle:
    machines: list[Machine]

    a_pattern = re.compile("Button A: X\+(\d+), Y\+(\d+)")
    b_pattern = re.compile("Button B: X\+(\d+), Y\+(\d+)")
    prize_pattern = re.compile("Prize: X=(\d+), Y=(\d+)")

    def __init__(self, input_lines: Iterable[str]):
        machines = []
        a: Coordinate = None
        b: Coordinate = None
        prize: Coordinate = None
        for l in input_lines:
            l = l.strip()
            if (
                l == ""
            ):  # I added a line to my input to get this to capture the last one
                if a and b and prize:
                    machines.append(Machine(a_rule=a, b_rule=b, prize_location=prize))
                    a = None
                    b = None
                    prize = None

            elif "A" in l:
                matches = self.a_pattern.findall(l)
                if matches:
                    a = Coordinate(int(matches[0][0]), int(matches[0][1]))
            elif "B" in l:
                matches = self.b_pattern.findall(l)
                if matches:
                    b = Coordinate(int(matches[0][0]), int(matches[0][1]))
            elif "P" in l:
                matches = self.prize_pattern.findall(l)
                if matches:
                    prize = Coordinate(
                        int(matches[0][0]) + 10000000000000,
                        int(matches[0][1]) + 10000000000000,
                    )

        logger.debug(f"Created with {len(machines)} machines")
        self.machines = machines

    def star2(self) -> int:
        return sum([m.cost_to_win() for m in self.machines])


# input = """Button A: X+94, Y+34
# Button B: X+22, Y+67
# Prize: X=8400, Y=5400

# Button A: X+26, Y+66
# Button B: X+67, Y+21
# Prize: X=12748, Y=12176

# Button A: X+17, Y+86
# Button B: X+84, Y+37
# Prize: X=7870, Y=6450

# Button A: X+69, Y+23
# Button B: X+27, Y+71
# Prize: X=18641, Y=10279""".splitlines()

input = open("inputs/day13.txt").readlines()

puzzle = Day13Star2Puzzle(input)
print(puzzle.star2())
