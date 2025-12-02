from dataclasses import dataclass
import logging
import math
from typing import Iterable

logger = logging.getLogger()
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)


@dataclass(frozen=True)
class Coordinate:
    x: int
    y: int

    def __add__(self, other) -> "Coordinate":
        return Coordinate(self.x + other.x, self.y + other.y)

    def __str__(self) -> str:
        return f"({self.x},{self.y})"


class Day08Puzzle:
    antenna_coordinates_by_type: dict[str, set[Coordinate]]
    antenna_coordinates: set[Coordinate]
    antinodes: set[Coordinate]
    size: int

    def __init__(self, input_lines: Iterable[str]):
        antenna_coordinates_by_type = dict()
        antenna_coordinates = set()
        i = 0
        for l in input_lines:
            j = 0
            for c in l:
                if c != ".":
                    this_coordinate = Coordinate(j, i)
                    coordinates = antenna_coordinates_by_type.get(c)
                    if not coordinates:
                        coordinates = set()
                    coordinates.add(this_coordinate)
                    antenna_coordinates_by_type[c] = coordinates
                    antenna_coordinates.add(this_coordinate)
                j += 1
            i += 1
        self.size = len(input_lines)
        self.antenna_coordinates_by_type = antenna_coordinates_by_type
        self.antenna_coordinates = antenna_coordinates
        self.antinodes = set()

    def find_antinodes(
        self, antenna1: Coordinate, antenna2: Coordinate
    ) -> set[Coordinate]:

        logger.debug(f"finding line for {antenna1} & {antenna2}")
        antinodes = set()

        def y_coordinate_on_line(x: int) -> int:
            y = (antenna2.y - antenna1.y) / (antenna2.x - antenna1.x) * (
                x - antenna1.x
            ) + antenna1.y
            return int(y)

        def dist_antenna1(c: Coordinate) -> float:
            return abs(c.x - antenna1.x) + abs(c.y - antenna1.y)

        def dist_antenna2(c: Coordinate) -> float:
            return abs(c.x - antenna2.x) + abs(c.y - antenna2.y)

        for x in range(self.size):
            c = Coordinate(x, y_coordinate_on_line(x))
            logger.debug(f"found {c} on line")
            if c.y and c.y >= 0 and c.y < self.size:
                logger.debug(f"testing distances for {c}")
                d1 = dist_antenna1(c)
                d2 = dist_antenna2(c)
                logger.debug(f"distances: {d1} and {d2}")
                if (d1 * 2 == d2) or (d1 == d2 * 2):
                    logger.info(f"found antinode {c}")
                    antinodes.add(c)
                    if len(antinodes) == 2:
                        return antinodes

        return antinodes

    def star1(self) -> int:
        for antennas in self.antenna_coordinates_by_type.values():
            for a in antennas:
                for b in antennas:
                    if a != b:
                        antinodes_for_pair = self.find_antinodes(a, b)
                        if antinodes_for_pair:
                            logger.info(
                                f"found antinodes {antinodes_for_pair} for {a} and {b}"
                            )
                            self.antinodes.update(antinodes_for_pair)
        return len(self.antinodes)


# Example 1
# antenna: (4, 3), (5,5)
# antinodes: (3, 1), (6,7)
# print("EXAMPLE 1")
# input = """..........
# ..........
# ..........
# ....a.....
# ..........
# .....a....
# ..........
# ..........
# ..........
# ..........""".splitlines()
# puzzle = Day08Puzzle(input)
# print(puzzle.star1())
# print(puzzle.antinodes)


# antinodes (3,1),(0,2),(2,6),(6,7)
# antenna (4,3),(8,4),(5,5)
# print("EXAMPLE 2")
# input = """..........
# ..........
# ..........
# ....a.....
# ........a.
# .....a....
# ..........
# ..........
# ..........
# ..........""".splitlines()
# puzzle = Day08Puzzle(input)
# print(puzzle.star1())
# print(puzzle.antinodes)


# antinodes (3,1),(0,2),(2,6), (6,7)
# antenna (4,3),(8,4),(5,5)
# print("EXAMPLE 3")
# input = """..........
# ..........
# ..........
# ....a.....
# ........a.
# .....a....
# ..........
# ......A...
# ..........
# ..........""".splitlines()
# puzzle = Day08Puzzle(input)
# print(puzzle.star1())
# print(puzzle.antinodes)


# antenna:
# 0: (8,1),(5,2),(7,3),(4,5)
# A: (7,5), (8,8), (9,9)
# antinodes: (6,0), (11,0),(3,1),(4,2),(10,2),
# (2,3),(9,4),(1,5),(3,6),(0,7),
# (7,7),(10,10),(10,11), (7,5)
"""
0:  ......#....#
1:  ...#....0...
2:  ....#0....#.
3:  ..#....0....
4:  ....0....#..
5:  .#....A.....
6:  ...#........
7:  #......#....
8:  ........A...
9:  .........A..
10: ..........#.
11: ..........#.
"""


test_input = True
if test_input:
    input = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............""".splitlines()
else:
    input = open("inputs/day08.txt").readlines()


puzzle = Day08Puzzle(input)
print(puzzle.star1())
print(puzzle.antinodes)
