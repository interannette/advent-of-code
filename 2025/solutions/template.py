from collections.abc import Iterable


class DayNPuzzle:

    def __init__(self, input_lines: Iterable[str]):
        return

    def star1(self) -> int:
        return 0

    def star2(self) -> int:
        return 0


use_test_input = True
if use_test_input:
    input = """""".splitlines()
else:
    input = open("solutions/inputs/dayN.txt").readlines()

puzzle = DayNPuzzle(input)
print(f"Test input: {use_test_input}. Star 1 result {puzzle.star1()}")
print(f"Test input: {use_test_input}. Star 2 result {puzzle.star2()}")
