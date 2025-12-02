import logging
from typing import Iterable

logger = logging.getLogger()
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)


class Day07Puzzle:
    def __init__(self, input_lines: Iterable[str]):
        pass

    def star1(self) -> int:
        return -1


test_input = True
if test_input:
    input = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20""".splitlines()
else:
    input = open("inputs/day07.txt").readlines()
