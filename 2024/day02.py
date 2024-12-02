from collections import Counter
from typing import Iterable


def parse_input(input_lines: Iterable[str]) -> list[list[int]]:
    reports = []
    for l in input_lines:
        r = []
        for i in l.split():
            r.append(int(i))
        reports.append(r)
    return reports


def test_report(report: list[int]) -> bool:
    # The levels are either all increasing or all decreasing.
    # Any two adjacent levels differ by at least one and at most three.

    increasing = True if report[-1] > report[0] else False

    for i in range(len(report)-1):
        diff = report[i+1] - report[i]

        if increasing and diff <= 0:
            return False
        if not increasing and diff >= 0:
            return False
            
        if abs(diff) > 3:
            return False
        
    return True

def test_report_with_tolerance(report: list[int]) -> bool:
    # The levels are either all increasing or all decreasing.
    # Any two adjacent levels differ by at least one and at most three.
    # tolerate a single bad level

    if test_report(report):
        return True
            
    for i in range(len(report)):
        if test_report(report[:i]+report[i+1:]):
            return True
        
    return False

def star1(reports: list[list[int]]) -> int:
    return sum([1 if test_report(r) else 0 for r in reports])


def star2(reports: list[list[int]]) -> int:
    return sum([1 if test_report_with_tolerance(r) else 0 for r in reports])


test_input = False
if test_input:
    input = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9""".splitlines()
else:
    input = open("inputs/day02.txt").readlines()

print(star2(parse_input(input)))
