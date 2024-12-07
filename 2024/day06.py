from dataclasses import dataclass
import logging
from typing import Iterable

logger = logging.getLogger()
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.WARN)


@dataclass(frozen=True)
class Coordinate:
    x: int
    y: int

    def __add__(self, other) -> "Coordinate":
        return Coordinate(self.x + other.x, self.y + other.y)

    def __str__(self) -> str:
        return f"({self.x},{self.y})"


ROTATION = {"^": ">", ">": "v", "v": "<", "<": "^"}
DIRECTION = {
    "^": Coordinate(1, 0),
    ">": Coordinate(0, 1),
    "v": Coordinate(-1, 0),
    "<": Coordinate(0, -1),
}


class Day06Puzzle:
    obstacles: set[Coordinate]
    guard_coord: Coordinate
    guard: str
    size: int
    path: set[Coordinate]

    def __init__(self, input_lines: Iterable[str]):
        obstacles = set()
        i = len(input_lines) - 1
        for l in input_lines:
            j = 0
            for c in l:
                if c == "#":
                    obstacles.add(Coordinate(i, j))
                elif c in ROTATION.keys():
                    self.guard_coord = Coordinate(i, j)
                    self.guard = c
                j += 1
            i -= 1
        self.size = len(input_lines)
        self.obstacles = obstacles
        self.path = set()

    def _is_out_of_map(self, c: Coordinate) -> bool:
        return c.x < 0 or c.y < 0 or c.x > self.size or c.y > self.size

    def _advance_to_exit(self):
        while True:
            next_step = self.guard_coord + DIRECTION[self.guard]
            logger.debug(f"next step {next_step}")
            if self._is_out_of_map(next_step):
                logger.info(f"next step {next_step} is out of bounds")
                self.path.add(self.guard_coord)
                return
            elif next_step in self.obstacles:
                self.guard = ROTATION[self.guard]
                logger.info(f"guard rotated to {self.guard}")
            else:
                self.path.add(self.guard_coord)
                logger.info(
                    f"moving guard to next step. adding {self.guard_coord} to path. path size {len(self.path)}"
                )
                self.guard_coord = next_step

    def star1(self) -> int:
        self._advance_to_exit()
        return len(self.path)

    def star2(parsed_input: any) -> int:
        return -1


test_input = False
if test_input:
    input = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...""".splitlines()
else:
    input = open("inputs/day06.txt").readlines()

puzzle = Day06Puzzle(input)
print(puzzle.star1())
