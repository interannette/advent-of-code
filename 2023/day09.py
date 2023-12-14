from dataclasses import dataclass
from typing import List

sample = True


if sample:
    INPUT = \
        '''0 3 6 9 12 15
        1 3 6 10 15 21
        10 13 16 21 30 45'''.splitlines()
else:
    INPUT = open("inputs/day09.txt").readlines()
INPUT = [s.strip() for s in INPUT]


@dataclass
class History:
    values: List[int]

    @staticmethod
    def parse(line: str) -> "History":
        return History(values=[int(l) for l in line.split(' ')])

    def extrapolate_next_value(self) -> int:

        diffs = [self.values]

        done = False
        while not done:
            current_diffs = []
            for i in range(len(diffs[-1]) - 1):
                current_diffs.append(diffs[-1][i + 1] - diffs[-1][i])
            diffs.append(current_diffs)
            done = all([i == 0 for i in current_diffs])

        for i in range(len(diffs)-1, 0, -1):
            current_end = diffs[i][-1]
            previous_end = diffs[i-1][-1]
            needed_value = current_end + previous_end
            diffs[i-1].append(needed_value)

        return diffs[0][-1]

    def extrapolate_first_value(self) -> int:

        diffs = [self.values]

        done = False
        while not done:
            current_diffs = []
            for i in range(len(diffs[-1]) - 1):
                current_diffs.append(diffs[-1][i + 1] - diffs[-1][i])
            diffs.append(current_diffs)
            done = all([i == 0 for i in current_diffs])

        for i in range(len(diffs)-1, 0, -1):
            current_first = diffs[i][0]
            previous_first = diffs[i-1][0]
            needed_value = previous_first - current_first
            diffs[i-1].insert(0, needed_value)

        return diffs[0][0]


def solve_part1():
    total = 0
    for i in INPUT:
        history = History.parse(i)
        total = total + history.extrapolate_next_value()
    return total


def solve_part2():
    total = 0
    for i in INPUT:
        history = History.parse(i)
        total = total + history.extrapolate_first_value()
    return total


print(solve_part2())
