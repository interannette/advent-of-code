import re


def parse_ranges(input: str) -> list[tuple[int,int]]:
    range_strings = input.split(",")
    ranges = []
    for r in range_strings:
        (start,end) = r.split("-")
        ranges.append((int(start),int(end)))
    return ranges


STAR_1_PATTERN = re.compile("^(\\d+)\\1$")
STAR_2_PATTERN = re.compile("^(\\d+)\\1+$")

def find_invalid_numbers(start: int, end:int, star: int) -> list[int]:
    invalid_numbers = []
    for i in range(start, end+1):
        pattern = STAR_1_PATTERN if star == 1 else STAR_2_PATTERN
        matches = pattern.findall(str(i))
        if matches:
            invalid_numbers.append(i)
    return invalid_numbers

def compute_star(ranges: list[tuple[int,int]], star: int) -> int:
    total = 0
    for r in ranges:
        total += sum(find_invalid_numbers(r[0],r[1], star))
    return total

test_input = False
if test_input:
    input = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
else:
    input = open("inputs/day02.txt").readlines()[0]

print(compute_star(parse_ranges(input), 2))