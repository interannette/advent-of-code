from dataclasses import dataclass
import logging
from typing import Iterable, Optional

logger = logging.getLogger()
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.INFO)


@dataclass(frozen=True)
class Coordinate:
    x: int
    y: int
    direction: Optional[str] = None

    def __add__(self, other) -> "Coordinate":
        return Coordinate(self.x + other.x, self.y + other.y, self.direction)

    def __str__(self) -> str:
        return f"({self.x},{self.y}, {self.direction})"


ROTATION = {"^": ">", ">": "v", "v": "<", "<": "^"}
DIRECTION = {
    "^": Coordinate(1, 0),
    ">": Coordinate(0, 1),
    "v": Coordinate(-1, 0),
    "<": Coordinate(0, -1),
}


class Day06Star1Puzzle:
    obstacles: set[Coordinate]
    guard_coord: Coordinate
    size: int
    path: set[Coordinate]
    locations: set[Coordinate]
    loop: bool = False

    def __init__(self, input_lines: Iterable[str]):
        obstacles = set()
        i = len(input_lines) - 1
        for l in input_lines:
            j = 0
            for c in l:
                if c == "#":
                    obstacles.add(Coordinate(i, j))
                elif c in ROTATION.keys():
                    self.guard_coord = Coordinate(i, j, c)
                j += 1
            i -= 1
        self.size = len(input_lines)
        self.obstacles = obstacles
        self.path = set()

    def _is_out_of_map(self, c: Coordinate) -> bool:
        return c.x < 0 or c.y < 0 or c.x > self.size or c.y > self.size

    def advance_to_completion(self):
        while True:
            next_step = self.guard_coord + DIRECTION[self.guard_coord.direction]
            logger.debug(f"next step {next_step}")
            if self._is_out_of_map(next_step):
                logger.debug(f"next step {next_step} is out of bounds")
                self.path.add(self.guard_coord)
                return
            elif Coordinate(next_step.x, next_step.y) in self.obstacles:
                self.guard_coord = Coordinate(
                    self.guard_coord.x,
                    self.guard_coord.y,
                    ROTATION[self.guard_coord.direction],
                )
                logger.debug(f"guard rotated to {self.guard_coord}")
            elif next_step in self.path:
                self.loop = True
                return
            else:
                self.path.add(self.guard_coord)
                logger.debug(
                    f"moving guard to next step. adding {self.guard_coord} to path. path size {len(self.path)}"
                )
                self.guard_coord = next_step

    def star1(self) -> int:
        self.advance_to_completion()
        self.locations = {Coordinate(c.x, c.y) for c in self.path}
        return len(self.locations)


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

puzzle = Day06Star1Puzzle(input)
print(puzzle.star1())


loops = 0
for p in puzzle.locations:
    logger.debug(f"testing {p}")
    modified_puzzle = Day06Star1Puzzle(input)
    modified_puzzle.obstacles.add(p)

    modified_puzzle.advance_to_completion()

    if modified_puzzle.loop:
        logger.info(f"{p} results in a loop")
        loops += 1
    else:
        logger.debug(f"{p} does not loop")

print(loops)
