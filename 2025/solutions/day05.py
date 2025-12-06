from collections.abc import Iterable


class Day05Puzzle:
    fresh_ranges: list[tuple[int, int]] = None
    available_ingredients: list[int] = None

    def __init__(self, input_lines: Iterable[str]):
        self.available_ingredients = []
        self.fresh_ranges = []
        for line in input_lines:
            line = line.strip()
            if "-" in line:
                start, end = line.split("-")
                self.fresh_ranges.append((int(start), int(end)))
            elif line.isdigit():
                self.available_ingredients.append(int(line))

        self.fresh_ranges.sort()

        return

    def is_fresh(self, ingredient: int) -> bool:
        for start, end in self.fresh_ranges:
            if start <= ingredient <= end:
                return True
        return False

    def star1(self) -> int:
        return sum(
            1 for ingredient in self.available_ingredients if self.is_fresh(ingredient)
        )

    def consolidate_ranges(self) -> list[tuple[int,int]]:
        consolidated_ranges = []
        for (s1,e1) in self.fresh_ranges:
            if len(consolidated_ranges) == 0:
                consolidated_ranges.append((s1,e1))
                continue

            (s0, e0) = consolidated_ranges[-1]
            if s0 == s1:
                # since we ordered lex, we know e1 >= e0
                consolidated_ranges[-1] = (s1,e1)
            elif s0 < s1 <= e0:
                if e1 > e0:
                    consolidated_ranges[-1]=(s0,e1)
            elif e0 < s1:
                consolidated_ranges.append((s1,e1))
        return consolidated_ranges

    def star2(self) -> int:
        consolidated_ranges = self.consolidate_ranges()
        return sum([(end-start+1) for (start,end) in consolidated_ranges])


use_test_input = False
if use_test_input:
    input = """3-5
10-14
16-20
12-18

1
5
8
11
17
32""".splitlines()
else:
    input = open("solutions/inputs/day05.txt").readlines()

puzzle = Day05Puzzle(input)
#print(f"Test input: {use_test_input}. Star 1 result {puzzle.star1()}")
print(f"Test input: {use_test_input}. Star 2 result {puzzle.star2()}")
# 332693433746707 = too low
# 344423158480189