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


@dataclass
class Region:
    plant: str
    coordinates: set[Coordinate]
    perimeter: int = -1

    def cost(self) -> int:
        return self.perimeter * len(self.coordinates)


class Day12Puzzle:

    size: int = None
    garden: dict[Coordinate, str] = None
    contained_coordinates: set[Coordinate] = set()

    def __init__(self, input_lines: Iterable[str]):
        garden: dict[Coordinate, str] = {}
        i = 0
        for l in input_lines:
            j = 0
            for c in l.strip():
                garden[Coordinate(i, j)] = c
                j += 1
            i += 1

        self.garden = garden
        self.size = i - 1

    def _neighbors(self, p: Coordinate) -> list[Coordinate]:
        neighbors: list[Coordinate] = []
        if p.x > 0:
            neighbors.append(Coordinate(p.x - 1, p.y))
        if p.y > 0:
            neighbors.append(Coordinate(p.x, p.y - 1))
        if p.x < (self.size):
            neighbors.append(Coordinate(p.x + 1, p.y))
        if p.y < (self.size):  # assume square input
            neighbors.append(Coordinate(p.x, p.y + 1))
        return neighbors

    def build_region_from_point(self, coordinate: Coordinate) -> Region:
        neighbors = list(self._neighbors(coordinate))
        visited_neighbors = {coordinate}
        plant = self.garden[coordinate]
        region = {coordinate}
        for n in neighbors:
            if self.garden[n] == plant:
                region.add(n)
                visited_neighbors.add(n)
                for m in self._neighbors(n):
                    if not m in visited_neighbors:
                        neighbors.append(m)

        return Region(plant, region)

    def star1(self) -> int:
        regions: list[Region] = []
        for i in range(self.size + 1):
            for j in range(self.size + 1):
                c = Coordinate(i, j)
                if not c in self.contained_coordinates:
                    logger.debug(f"finding region for {c}")
                    region = self.build_region_from_point(c)
                    regions.append(region)
                    self.contained_coordinates.update(region.coordinates)

        logger.debug(regions)
        return sum([r.cost() for r in regions])


test_input1 = """AAAA
BBCD
BBCC
EEEC""".splitlines()
test_puzzle1 = Day12Puzzle(test_input1)
print(test_puzzle1.star1())
# expect: 140

# test_input2 = """OOOOO
# OXOXO
# OOOOO
# OXOXO
# OOOOO""".splitlines()
# test_puzzle2 = Day12Puzzle(test_input2)
# print(test_puzzle2.star1())
# expect 772

# test_input3 = """RRRRIICCFF
# RRRRIICCCF
# VVRRRCCFFF
# VVRCCCJFFF
# VVVVCJJCFE
# VVIVCCJJEE
# VVIIICJJEE
# MIIIIIJJEE
# MIIISIJEEE
# MMMISSJEEE""".splitlines()
# test_puzzle3 = Day12Puzzle(test_input3)
# print(test_puzzle3.star1())
# expect 1930
