from typing import Iterable


def parse_star1_input(input_lines: Iterable[str]) -> any:
    return None


def star1(parsed_input: any) -> int:
    return -1


def parse_star2_input(input_lines: Iterable[str]) -> any:
    return None


def star2(parsed_input: any) -> int:
    return -1


test_input = True
if test_input:
    input = """""".splitlines()
else:
    input = open("inputs/day04.txt").readlines()

print(star1(parse_star1_input(input)))
print(star2(parse_star2_input(input)))
