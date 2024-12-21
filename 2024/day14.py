from dataclasses import dataclass
import logging
import math
import re
from typing import Iterable

logger = logging.getLogger()
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)


@dataclass(frozen=True)
class Coordinate:
    x: int
    y: int

    def __add__(self, other):
        return Coordinate(self.x + other.x, self.y + other.y)

    def __rmul__(self, other):
        return Coordinate(self.x * other, self.y * other)


@dataclass
class Robot:
    start: Coordinate
    velocity: Coordinate
    current: Coordinate

    robot_pattern = re.compile("p=(\d+),(\d+) v=(-?\d+),(-?\d+)")

    def __init__(self, s: str):
        matches = self.robot_pattern.findall(s)
        self.start = Coordinate(int(matches[0][0]), int(matches[0][1]))
        self.current = self.start
        self.velocity = Coordinate(int(matches[0][2]), int(matches[0][3]))

    def advance(self, bounds: Coordinate, rounds: int = 1):
        next = self.current + rounds * self.velocity
        self.current = Coordinate(next.x % bounds.x, next.y % bounds.y)


class Day14Puzzle:
    robots: list[Robot]
    bounds: Coordinate

    def __init__(self, input_lines: Iterable[str], bounds: Coordinate):
        self.bounds = bounds
        self.robots = []
        for l in input_lines:
            self.robots.append(Robot(l))

        logger.debug(f"Created puzzle with {len(self.robots)} robots")

    def star1(self) -> int:
        for r in self.robots:
            r.advance(self.bounds, 100)

        q1 = 0
        q2 = 0
        q3 = 0
        q4 = 0
        half_x = math.floor(self.bounds.x / 2)
        half_y = math.floor(self.bounds.y / 2)
        logger.debug(f"bounds for quadrants {half_x}, {half_y}")
        for r in self.robots:
            if r.current.x < half_x:
                if r.current.y < half_y:
                    logger.debug(f"putting {r.current} in q1")
                    q1 += 1
                elif r.current.y > half_y:
                    logger.debug(f"putting {r.current} in q3")
                    q3 += 1
                else:
                    logger.debug(f"skipping {r.current}")
            elif r.current.x > half_x:
                if r.current.y < half_y:
                    logger.debug(f"putting {r.current} in q2")
                    q2 += 1
                elif r.current.y > half_y:
                    logger.debug(f"putting {r.current} in q4")
                    q4 += 1
                else:
                    logger.debug(f"skipping {r.current}")
            else:
                logger.debug(f"skipping {r.current}")

        logger.info(f"q1:{q1}, q2:{q2}, q3:{q3}, q4:{q4}")
        return q1 * q2 * q3 * q4

    def _print_robots(self) -> str:
        positions = set([r.current for r in self.robots])
        result = ""
        for i in range(self.bounds.x):
            for j in range(self.bounds.y):
                if Coordinate(i, j) in positions:
                    result += "x"
                else:
                    result += "."
            result += "\n"
        return result

    def star2(self, min_rounds: int, max_rounds: int):
        for r in self.robots:
            r.advance(self.bounds, min_rounds)
        with open("outputs/day14.txt", "a") as file:
            for i in range(min_rounds, max_rounds):
                for r in self.robots:
                    r.advance(self.bounds)
                file.write(f"Seconds {i}\n")
                file.write(self._print_robots())


test_input = False
if test_input:
    input = """p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3
""".splitlines()
    bounds = Coordinate(11, 7)
else:
    input = open("inputs/day14.txt").readlines()
    bounds = Coordinate(101, 103)

puzzle = Day14Puzzle(input_lines=input, bounds=bounds)
puzzle.star2(7787, 7791)

# r = "p=2,4 v=2,-3"
# robot = Robot(r)
# print(f"start: {robot.current}")
# for i in range(5):
#     robot.advance(bounds=Coordinate(11, 7))
#     print(f"time {i+1}: {robot.current}")


# 12 + 101*x=64 + 103*y
# 101x=64-12+103y
# 101x=52+103y
# x=52/101+103/101*yield

loop1 = set([(12 + 101 * i) for i in range(100)])
loop2 = set([(64 + 103 * i) for i in range(100)])
print(loop1.intersection(loop2))
