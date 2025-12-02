import logging
from math import floor
from typing import Iterable

logger = logging.getLogger()
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)


class Day05Puzzle:
    # b must come before a
    before_after_rules: dict[int, set[int]]
    # a cannot come after b
    after_before_rules: dict[int, set[int]]
    updates: list[list[int]]

    def __init__(self, input_lines: Iterable[str]):
        before_after_rules = dict()
        after_before_rules = dict()
        updates = []

        for l in input_lines:
            if "|" in l:
                (x, y) = l.split("|")
                x = int(x)
                y = int(y)
                s = before_after_rules.get(x)
                if not s:
                    s = set()
                s.add(y)
                before_after_rules[x] = s

                # y:set(x)
                t = after_before_rules.get(y)
                if not t:
                    t = set()
                t.add(x)
                after_before_rules[y] = t

            elif "," in l:
                updates.append([int(x) for x in l.split(",")])

        self.before_after_rules = before_after_rules
        self.after_before_rules = after_before_rules
        self.updates = updates

    def _validate_update(self, update: list[int]) -> int:
        after = set(update)
        for i in range(len(update)):
            rules = self.after_before_rules.get(update[i])
            # if anything before i is contained in the rules, it's not valid
            # if update[i] is before anything in rules, return false
            # if rules is in after, return false
            if rules:
                if not after.isdisjoint(rules):
                    logger.info(
                        f"update is invalid {update} for {update[i]}:{rules} - {after}"
                    )
                    return 0
            after.remove(update[i])
        logger.info(f"found valid update: {update}")
        return update[floor(len(update) / 2)]

    # continue along update until you find a broken rule
    # once you find a broken rule, swap the offending rule
    # take the updated update and check again
    # if you make it to the end you are valid

    def _fix_invalid_update(self, update: list[int]) -> int:
        return 0

    def star1(self) -> int:
        return sum([self._validate_update(update) for update in self.updates])

    def star2(self) -> int:
        return sum([self._fix_invalid_update(update) for update in self.updates])


test_input = False
if test_input:
    input = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47""".splitlines()
else:
    input = open("inputs/day05.txt").readlines()

puzzle = Day05Puzzle(input)
print(puzzle.star1())
