import logging
import math
from typing import Iterable

logger = logging.getLogger()
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)


class Day11Puzzle:
    stones: list[int] = None

    def __init__(self, input: str):
        stones = []
        for i in input.split(" "):
            stones.append(int(i))
        self.stones = stones

    @staticmethod  # see if the navie way works
    def advance(stones: list[int]) -> list[int]:
        """
        If the stone is engraved with the number 0,
            it is replaced by a stone engraved with the number 1.
        If the stone is engraved with a number that has an even number of digits,
            it is replaced by two stones. The left half of the digits are engraved on the new left stone, and the right half of the digits are engraved on the new right stone. (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
        If none of the other rules apply,
            the stone is replaced by a new stone; the old stone's number multiplied by 2024 is engraved on the new stone.
        """
        updated_stones = []
        for s in stones:
            if s == 0:
                updated_stones.append(1)
            elif ((math.floor(math.log10(s)) + 1) % 2) == 0:
                digit_count = int((math.floor(math.log10(s)) + 1) / 2)
                updated_stones.append(int(str(s)[0:digit_count]))
                updated_stones.append(int(str(s)[digit_count:]))
            else:
                updated_stones.append(s * 2024)
        return updated_stones

    def star1(self) -> int:
        for i in range(25):
            self.stones = Day11Puzzle.advance(self.stones)
        return len(self.stones)

    def star2(self) -> int:
        for i in range(75):
            if i % 10 == 0:
                print(f"round {i}")
            self.stones = Day11Puzzle.advance(self.stones)
        return len(self.stones)


# expect: 1 2024 1 0 9 9 2021976
# print(Day11Puzzle.advance([0, 1, 10, 99, 999]))

# stones = [125, 17]
# for i in range(6):
#     stones = Day11Puzzle.advance(stones)
#     print(stones)

# test_input = "125 17"
# test_puzzle = Day11Puzzle(test_input)
# print(f"test input result: {test_puzzle.star1()}")

real_input = open("inputs/day11.txt").readline()
real_puzzle = Day11Puzzle(real_input)
print(f"test input result: {real_puzzle.star2()}")
