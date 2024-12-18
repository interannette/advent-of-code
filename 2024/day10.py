from dataclasses import dataclass
import logging
from typing import Iterable

logger = logging.getLogger()
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)


@dataclass(frozen=True)
class Coordinate:
    x: int
    y: int


class Day10Puzzle:

    topo: dict[int, dict[int, int]] = None
    trailheads: dict[Coordinate, set[Coordinate]] = None

    def __init__(self, input_lines: Iterable[str]):
        topo: dict[int, int] = dict()
        trailheads: dict[Coordinate, set[Coordinate]] = dict()
        i = 0
        for l in input_lines:
            j = 0
            row: dict[int, int] = dict()
            for c in l.strip():
                num_c = int(c)
                row[j] = num_c
                if num_c == 0:
                    trailheads[Coordinate(i, j)] = set()
                j += 1
            topo[i] = row
            i += 1

        self.trailheads = trailheads
        self.topo = topo

    def _neighbors(self, p: Coordinate) -> set[Coordinate]:
        neighbors: set[Coordinate] = set()
        if p.x > 0:
            neighbors.add(Coordinate(p.x - 1, p.y))
        if p.y > 0:
            neighbors.add(Coordinate(p.x, p.y - 1))
        if p.x < (len(self.topo) - 1):
            neighbors.add(Coordinate(p.x + 1, p.y))
        if p.y < (len(self.topo) - 1):  # assume square input
            neighbors.add(Coordinate(p.x, p.y + 1))
        return neighbors

    def find_peaks(self, trailhead: Coordinate) -> set[Coordinate]:
        next_steps: set[Coordinate] = {trailhead}
        for l in range(9):
            next_next_steps = set()
            for step in next_steps:
                last_value = self.topo[step.x][step.y]
                neighbors = self._neighbors(step)
                for n in neighbors:
                    if self.topo[n.x][n.y] == last_value + 1:
                        next_next_steps.add(n)
            next_steps = next_next_steps

        return next_steps

    def star1(self) -> int:
        count = 0
        for trailhead in self.trailheads.keys():
            peaks = self.find_peaks(trailhead)
            self.trailheads[trailhead] = peaks
            count += len(peaks)
        return count


test_input1 = """0123
1234
8765
9876""".splitlines()
test1 = Day10Puzzle(test_input1)
print(f"Test input 1 result {test1.star1()}")

test_input2 = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732""".splitlines()
test2 = Day10Puzzle(test_input2)
print(f"Test input 2 result {test2.star1()}")

real_input = open("inputs/day10.txt").readlines()
real_puzzle = Day10Puzzle(real_input)
print(f"Real input 1 result {real_puzzle.star1()}")
