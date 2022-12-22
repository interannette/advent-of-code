from dataclasses import dataclass
import re
from typing import Dict, List, Optional, Set
from itertools import product, accumulate
from utils.input_getter import get_input_for_day


@dataclass
class Range:
    start: int
    end: int

    def __init__(
        self,
        center: Optional[int] = None,
        dist: Optional[int] = None,
        start: Optional[int] = None,
        end: Optional[int] = None,
    ) -> None:
        if not start:
            self.start = center - dist
            self.end = center + dist
        else:
            self.start = start
            self.end = end

    def is_in(self, val: int) -> bool:
        return self.start < val < self.end

    def included_points(self) -> Set[int]:
        return set(range(self.start, self.end + 1))


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

    def __init__(self, input: List[str]):
        self.sensors = []
        self.detected_beacons = []

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

    @staticmethod
    def safe_range_for_point_on_row(s: Position, dist: int, row: int) -> Range:

        y_dist = abs(s.y - row)
        x_dist = dist - y_dist

        return Range(center=s.x, dist=x_dist)

    def calculate_excluded_space(self, row: int) -> int:
        intervals_on_row = []
        for i in range(len(self.sensors)):
            s = self.sensors[i]
            b = self.detected_beacons[i]

            dist = Position.dist(s, b)
            if Range(s.y, dist).is_in(row):
                # find relevant part in row
                intervals_on_row.append(
                    SenorGrid.safe_range_for_point_on_row(s, dist, row)
                )

        excluded_points = set().union(*[i.included_points() for i in intervals_on_row])
        excluded_points.difference_update([s.x for s in self.sensors if s.y == row])
        excluded_points.difference_update(
            [s.x for s in self.detected_beacons if s.y == row]
        )
        return len(excluded_points)


def first_star():
    input = get_input_for_day()
    s = SenorGrid(input)
    print(s.calculate_excluded_space(2000000))


if __name__ == "__main__":
    first_star()
