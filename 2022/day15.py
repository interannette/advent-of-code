from dataclasses import dataclass
import re
from typing import Dict, List, Set
from itertools import product
from utils.input_getter import get_input_for_day


@dataclass(frozen=True)
class Position:
    x: int
    y: int

    @staticmethod
    def dist(s, t) -> int:
        return abs(s.x - t.x) + abs(s.y - t.y)


class SenorGrid:

    sensors: List[Position]
    detected_beacons = List[Position]
    excluded_space = Set[Position]

    def __init__(self, input: List[str]):
        self.sensors = []
        self.detected_beacons = []
        self.excluded_space = set()
        for l in input:
            m = re.search(
                "^Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)$",
                l,
            )
            if m:
                self.sensors.append(Position(int(m.group(1)), int(m.group(2))))
                self.detected_beacons.append(Position(int(m.group(3)), int(m.group(4))))
            else:
                raise Exception("unable to parse line")

    @staticmethod
    def safe_range_for_point(s: Position, dist: int) -> Set[Position]:
        # Boundary:
        # (s.x + dist, s.y) <> (s.x-dist, s.y)
        # (s.x , s.y-dist) <> (s.x, s.y+dist)
        p = [
            Position(x, y)
            for (x, y) in product(
                range(s.x - dist, s.x + dist + 1), range(s.y - dist, s.y + dist + 1)
            )
            if Position.dist(s, Position(x, y)) <= dist
        ]

        return set(p)

    def calculate_excluded_space(self) -> None:
        for i in range(len(self.sensors)):
            s = self.sensors[i]
            b = self.detected_beacons[i]

            dist = abs(s.x - b.x) + abs(s.y - b.y)
            self.excluded_space.update(SenorGrid.safe_range_for_point(s, dist))

        self.excluded_space.difference_update(self.sensors)
        self.excluded_space.difference_update(self.detected_beacons)


def first_star():
    input = get_input_for_day()
    s = SenorGrid(input)
    s.calculate_excluded_space()
    row = [p.x for p in s.excluded_space if p.y == 2000000]
    print(len(row))


if __name__ == "__main__":
    first_star()
