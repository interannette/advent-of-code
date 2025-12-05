from collections.abc import Iterable
from dataclasses import dataclass

PAPER = "@"
EMPTY = "."


@dataclass(frozen=True)
class Coordinate:
    x: int
    y: int


class Day04Puzzle:

    floor: dict[Coordinate, str] = None
    size: int = 0

    def __init__(self, input_lines: Iterable[str]):
        floor: dict[Coordinate, str] = dict()
        i = 0
        for line in input_lines:
            j = 0
            for c in line.strip():
                floor[Coordinate(i, j)] = c
                j += 1
            i += 1

        self.floor = floor
        self.size = i

    def _neighbors(self, p: Coordinate) -> set[Coordinate]:
        neighbors: set[Coordinate] = set()
        if p.x > 0:
            neighbors.add(Coordinate(p.x - 1, p.y))
            if p.y > 0:
                neighbors.add(Coordinate(p.x - 1, p.y - 1))
            if p.y < (self.size - 1):
                neighbors.add(Coordinate(p.x - 1, p.y + 1))
        if p.x < (self.size - 1):
            neighbors.add(Coordinate(p.x + 1, p.y))
            if p.y > 0:
                neighbors.add(Coordinate(p.x + 1, p.y - 1))
            if p.y < (self.size - 1):
                neighbors.add(Coordinate(p.x + 1, p.y + 1))
        if p.y > 0:
            neighbors.add(Coordinate(p.x, p.y - 1))
        if p.y < (self.size - 1):  # assume square input
            neighbors.add(Coordinate(p.x, p.y + 1))
        return neighbors

    def star1(self) -> int:
        count = 0
        for pos in self.floor.keys():
            if self.floor[pos] == PAPER:
                neighbors = self._neighbors(pos)
                neighbors = {n for n in neighbors if self.floor[n] == PAPER}
                if len(neighbors) < 4:
                    count += 1
        return count

    def star2(self) -> int:
        num_removed = 0
        while True:
            removed_this_round = self.remove_one_round()
            if removed_this_round == 0:
                return num_removed
            num_removed += removed_this_round

    def remove_one_round(self) -> int:
        to_remove: set[Coordinate] = set()
        for pos in self.floor.keys():
            if self.floor[pos] == PAPER:
                neighbors = self._neighbors(pos)
                neighbors = {n for n in neighbors if self.floor[n] == PAPER}
                if len(neighbors) < 4:
                    to_remove.add(pos)

        for p in to_remove:
            self.floor[p] = EMPTY
        return len(to_remove)


use_test_input = True
if use_test_input:
    input = """..@@.@@@@.
    @@@.@.@.@@
    @@@@@.@.@@
    @.@@@@..@.
    @@.@@@@.@@
    .@@@@@@@.@
    .@.@.@.@@@
    @.@@@.@@@@
    .@@@@@@@@.
    @.@.@@@.@.""".splitlines()
else:
    input = open("solutions/inputs/day04.txt").readlines()

puzzle = Day04Puzzle(input)
# print(f"Test input 2 result {test2.star1()}")
print(f"Test input result: rolls: {puzzle.star2()}")
