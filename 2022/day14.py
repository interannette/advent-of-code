from collections import defaultdict
from typing import Dict, List, Tuple
from utils.input_getter import get_input_for_day


class Cave:
    rocks: Dict[int, Dict[int, bool]]
    sand: Dict[int, Dict[int, bool]]
    max_y: int

    def __init__(self, input: List[str]):
        self.rocks = defaultdict(lambda: defaultdict(lambda: False))
        self.sand = defaultdict(lambda: defaultdict(lambda: False))
        for l in input:
            points = l.split(" -> ")

            previous = None
            for current in points:
                current = [int(i) for i in current.split(",")]
                if previous:
                    if previous[0] == current[0]:
                        step = 1 if previous[1] < current[1] else -1
                        for i in range(previous[1], current[1] + step, step):
                            self.rocks[previous[0]][i] = True
                    elif previous[1] == current[1]:
                        step = 1 if previous[0] < current[0] else -1
                        for i in range(previous[0], current[0] + step, step):
                            self.rocks[i][previous[1]] = True
                    else:
                        raise Exception("Not a straight line")

                previous = current

        y_values = []
        for v in self.rocks.values():
            y_values.extend(v.keys())
        self.max_y = max(y_values)

    def _is_open(self, x: int, y: int) -> bool:
        is_sand = self.sand[x] and self.sand[x][y]
        is_rock = self.rocks[x] and self.rocks[x][y]
        return not is_sand and not is_rock

    def _advance_sand(self, pos: Tuple[int, int]) -> Tuple[int, int]:
        """A unit of sand always falls down one step if possible.
        If the tile immediately below is blocked (by rock or sand),
        the unit of sand attempts to instead move diagonally one step down and to the left.
        If that tile is blocked, the unit of sand attempts to instead move diagonally one step down and to the right."""

        x = pos[0]
        y = pos[1]

        if self._is_open(x, y + 1):
            return (x, y + 1)
        elif self._is_open(x - 1, y + 1):
            return (x - 1, y + 1)
        elif self._is_open(x + 1, y + 1):
            return (x + 1, y + 1)
        else:
            return pos

    def add_sand(self, with_floor: bool = False) -> bool:
        pos = (500, 0)

        if not with_floor:
            while pos[1] <= self.max_y:
                previous = pos
                pos = self._advance_sand(pos)
                if pos == previous:
                    break

            if pos[1] > self.max_y:
                return False
            else:
                self.sand[pos[0]][pos[1]] = True
                return True
        else:
            floor_value = self.max_y + 2
            while pos[1] < floor_value - 1:
                previous = pos
                pos = self._advance_sand(pos)
                if pos == previous:
                    break

            self.sand[pos[0]][pos[1]] = True
            return pos != (500, 0)

    def fill_sand(self, with_floor: bool = False) -> None:
        result = self.add_sand(with_floor)
        while result:
            result = self.add_sand(with_floor)

    def count_sand(self) -> int:
        total_sand = 0
        for row in self.sand.values():
            total_sand += sum(row.values())
        return total_sand


def first_star():
    input = get_input_for_day()
    c = Cave(input)
    c.fill_sand()
    print(c.count_sand())


def second_star():
    input = get_input_for_day()
    c = Cave(input)
    c.fill_sand(with_floor=True)
    print(c.count_sand())


if __name__ == "__main__":
    second_star()
