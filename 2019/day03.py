from dataclasses import dataclass
import math
from typing import Dict, List, Optional, Set

from utils.input_getter import get_input_for_day


@dataclass(frozen=True)
class Coordinate:
    x: int
    y: int

    @staticmethod
    def manhattan_distanct(c1: "Coordinate", c2: "Coordinate") -> int:
        return abs(c1.x - c2.x) + abs(c1.y - c2.y)

    @staticmethod
    def build_line(
        start: "Coordinate", x_units: int, y_units: int
    ) -> List["Coordinate"]:
        # one or the other of x & y must be 0.
        line = []

        if x_units > 0:
            for i in range(1, x_units + 1):
                line.append(Coordinate(start.x + i, start.y))
        elif x_units < 0:
            for i in range(-1, x_units - 1, -1):
                line.append(Coordinate(start.x + i, start.y))

        if y_units > 0:
            for i in range(1, y_units + 1):
                line.append(Coordinate(start.x, start.y + i))
        elif y_units < 0:
            for i in range(-1, y_units - 1, -1):
                line.append(Coordinate(start.x, start.y + i))

        return line


def build_path(directions: List[str]) -> Dict[Coordinate, int]:

    previous_coord = Coordinate(0, 0)
    previous_dist = 0
    positions = {previous_coord: previous_dist}

    for current in directions:
        direction = current[0]
        length = int(current[1:])
        new_segment = None
        if direction == "U":
            new_segment = Coordinate.build_line(previous_coord, 0, length)
            previous_coord = Coordinate(previous_coord.x, previous_coord.y + length)
        elif direction == "D":
            new_segment = Coordinate.build_line(previous_coord, 0, -1 * length)
            previous_coord = Coordinate(previous_coord.x, previous_coord.y - length)
        elif direction == "R":
            new_segment = Coordinate.build_line(previous_coord, length, 0)
            previous_coord = Coordinate(previous_coord.x + length, previous_coord.y)
        elif direction == "L":
            new_segment = Coordinate.build_line(previous_coord, -1 * length, 0)
            previous_coord = Coordinate(previous_coord.x - length, previous_coord.y)

        for c in new_segment:
            previous_dist += 1
            positions.setdefault(c, previous_dist)

    return positions


def parse_path(path_str: str) -> Dict[Coordinate, int]:
    return build_path(path_str.strip().split(","))


def solve_intersection(
    first_line: str, second_line: str, step_distance: Optional[bool]
):
    first_path = parse_path(first_line)
    second_path = parse_path(second_line)

    paths_intersection = set(first_path.keys()).intersection(set(second_path.keys()))

    origin = Coordinate(0, 0)
    paths_intersection.remove(origin)

    def distance_function(p):
        if step_distance:
            return first_path[p] + second_path[p]
        else:
            return Coordinate.manhattan_distanct(origin, p)

    closest_intersection = min(paths_intersection, key=distance_function)

    return distance_function(closest_intersection)


def first_star():
    lines = get_input_for_day(3)
    return solve_intersection(lines[0], lines[1], False)


def second_star():
    lines = get_input_for_day(3)
    return solve_intersection(lines[0], lines[1], True)


if __name__ == "__main__":
    print(second_star())
