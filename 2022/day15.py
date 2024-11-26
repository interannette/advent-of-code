from dataclasses import dataclass
import re
from typing import Dict, List, Optional, Set
from itertools import product, accumulate
from utils.input_getter import get_input_for_day
import logging


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
        if dist:
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
    def safe_range_for_point_on_row(
        s: Position, dist: int, row: int, limit: Optional[int] = None
    ) -> Range:

        y_dist = abs(s.y - row)
        x_dist = dist - y_dist

        r = Range(center=s.x, dist=x_dist)

        if limit:
            return Range(start=max(0, r.start), end=min(limit, r.end))
        else:
            return r

    def calculate_excluded_space(
        self, row: int, limit: Optional[int] = None, exclude: Optional[bool] = True
    ) -> Set[int]:
        intervals_on_row = []
        for i in range(len(self.sensors)):
            s = self.sensors[i]
            b = self.detected_beacons[i]

            dist = Position.dist(s, b)
            if Range(center=s.y, dist=dist).is_in(row):
                # find relevant part in row
                intervals_on_row.append(
                    SenorGrid.safe_range_for_point_on_row(s, dist, row, limit)
                )

        if exclude:
            excluded_points = set().union(
                *[i.included_points() for i in intervals_on_row]
            )
            excluded_points.difference_update([s.x for s in self.sensors if s.y == row])
            excluded_points.difference_update(
                [s.x for s in self.detected_beacons if s.y == row]
            )
            return excluded_points
        else:
            intervals_on_row.sort(key=lambda x: x.start)
            current = Range(
                start=intervals_on_row[0].start, end=intervals_on_row[0].end
            )
            missing = set()
            for interval in intervals_on_row:
                if interval.start <= current.end + 1:
                    current.end = interval.end
                else:
                    missing.update(range(current.end + 1, interval.start + 1))
                    current = Range(start=interval.start, end=interval.end)

            return missing

    def calculate_tuning_frequence(self, limit: int) -> int:

        for i in range(limit + 1):
            logging.debug(f"Checking row: {i}")
            row = self.calculate_excluded_space(i, limit, False)
            if len(row) > 0:
                return row.pop() * 4000000 + i

        return -1


def first_star():
    input = get_input_for_day()
    s = SenorGrid(input)
    print(len(s.calculate_excluded_space(2000000)))


def second_star():
    input = get_input_for_day()
    s = SenorGrid(input)
    print(s.calculate_tuning_frequence(4000000))


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    second_star()
