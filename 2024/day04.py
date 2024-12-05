from typing import Iterable
import logging

logger = logging.getLogger()
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.WARN)


class Day04Puzzle:
    letters: list[list[str]]
    size: int

    def __init__(self, input_lines: Iterable[str]):
        self.letters = [list(l.strip()) for l in input_lines]
        self.size = len(self.letters)

    @staticmethod
    def _count_instances_for_string(letters: str) -> int:
        # return count forward and backward
        count = 0
        for i in range(len(letters) - 3):
            if letters[i : i + 4] == "XMAS":
                count += 1
            elif letters[i : i + 4] == "SAMX":
                count += 1
        if count > 0:
            logger.debug(f"found {count} in line {letters}")
        return count

    @staticmethod
    def _count_instances_for_lines(lines: list[list[str]]) -> int:

        logger.debug("counting lines")
        for l in lines:
            logger.debug(l)
        return sum([Day04Puzzle._count_instances_for_string("".join(l)) for l in lines])

    def count_horizontal(self) -> int:
        count = Day04Puzzle._count_instances_for_lines(self.letters)
        logger.info(f"horizontal count {count}")
        return count

    def count_vertical(self) -> int:
        columns = [[l[i] for l in self.letters] for i in range(len(self.letters[0]))]
        count = Day04Puzzle._count_instances_for_lines(columns)
        logger.info(f"vertical count {count}")
        return count

    def _build_lines(
        self, starting_points: list[tuple[str, str]], increment: tuple[int, int]
    ) -> list[list[str]]:

        lines = []
        for s, t in starting_points:
            logger.debug(
                f"computing line for starting point ({s},{t}) and increment {increment}"
            )
            line = []
            for step in range(self.size):
                x = s + step * increment[0]
                y = t + step * increment[1]
                if x < 0 or x >= self.size or y < 0 or y >= self.size:
                    break
                else:
                    line.append(self.letters[x][y])

            lines.append(line)

        return lines

    def count_down_right_diagonal(self) -> int:
        # \
        # (0,0),(1,1),...
        # (0,1),(1,2),(2,3),...
        # ...
        # (0,n),

        # (1,0),(2,1),(3,2),...
        # (2,0),(3,1),(4,2),...

        starting_points = [(0, i) for i in range(self.size)] + [
            (i + 1, 0) for i in range(self.size - 1)
        ]
        increment = (1, 1)

        lines = self._build_lines(starting_points, increment)
        count = Day04Puzzle._count_instances_for_lines(lines)
        logger.info(f"down right count {count}")
        return count

    def count_up_right_diagonal(self) -> int:
        # /
        # (n,0), (n-1, 1), (n-2, 2), ...(0,n)
        # (n-1, 0), (n-2,1), (n-3, 2), ...()
        # (0,0),

        # (n, 1), (n-1, 2), (n-2, 3),...
        # (n, 2), ..
        # (n, 3), ...
        starting_points = [(i, 0) for i in range(self.size)] + [
            (self.size - 1, i + 1) for i in range(self.size - 1)
        ]
        logger.debug(f"starting points {starting_points}")
        increment = (-1, 1)

        lines = self._build_lines(starting_points, increment)

        count = Day04Puzzle._count_instances_for_lines(lines)
        logger.info(f"up right count {count}")
        return count

    def star1(self) -> int:
        # This word search allows words to be horizontal, vertical, diagonal,
        # written backwards, or even overlapping other words.
        # It's a little unusual, though, as you don't merely need to find one instance of XMAS
        # - you need to find all of them
        count = self.count_horizontal()
        count += self.count_vertical()
        count += self.count_down_right_diagonal()
        count += self.count_up_right_diagonal()
        return count


def parse_star2_input(input_lines: Iterable[str]) -> any:
    return None


def star2(parsed_input: any) -> int:
    return -1


test_input = False
if test_input:
    input = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX""".splitlines()

else:
    input = open("inputs/day04.txt").readlines()

puzzle = Day04Puzzle(input_lines=input)
print(puzzle.star1())
# print(star1(parse_star1_input(input)))
# print(star2(parse_star2_input(input)))
