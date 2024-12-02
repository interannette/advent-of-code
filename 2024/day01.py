from collections import Counter
from typing import Iterable


def parse_list(input_lines: Iterable[str]) -> tuple[list[int], list[int]]:
    list1 = []
    list2 = []
    for l in input_lines:
        [i1, i2] = l.split()
        list1.append(int(i1))
        list2.append(int(i2))
    return (list1, list2)


def star1(list1: list[int], list2:list[int]) -> int:

    list1.sort()
    list2.sort()

    combo = zip(list1, list2)

    diff = sum([abs(t1 - t2) for (t1,t2) in combo])

    return diff


def star2(list1: list[int], list2:list[int]) -> int:
    frequencies = Counter(list2)
    score = sum([s*frequencies[s] for s in list1])
    return score



test_input = False
if test_input:
    input = """3   4
    4   3
    2   5
    1   3
    3   9
    3   3""".splitlines()
else:
    input = open("inputs/day01.txt").readlines()

print(star2(*parse_list(input)))