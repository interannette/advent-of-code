from collections import Counter
import re
from typing import Iterable


def parse_star1_input(input_lines: Iterable[str]) -> any:
    pattern = "mul\((\d{1,3}),(\d{1,3})\)"
    compiled_pattern = re.compile(pattern)
    pairs = compiled_pattern.findall(input_lines[0])
    num_pairs = [(int(s), int(t)) for (s,t) in pairs]
    return num_pairs

def star1(pairs: list[tuple[int]]) -> int:
    return sum([s*t for (s,t) in pairs])


def parse_star2_input(input_lines: Iterable[str]) -> any:
    pattern = "mul\((\d{1,3}),(\d{1,3})\)|(don't\(\))|(do\(\))"
    compiled_pattern = re.compile(pattern)
    matches = compiled_pattern.findall(input_lines[0])
    return matches

def star2(matches) -> int:
    on = True
    total = 0
    for (s, t, dont, do) in matches:
        if s and t:
            if on:
                total += int(s) * int(t)
        elif dont:
            on = False
        elif do:
            on = True

    return total



test_input = False
if test_input:
    #input = """xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))""".splitlines()
    input = """xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))""".splitlines()
else:
    input = open("inputs/day03.txt").readlines()

print(star1(parse_star1_input(input)))
print(star2(parse_star2_input(input)))