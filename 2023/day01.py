import re

INPUT = open("inputs/day01.txt").readlines()

# region: part 1
# INPUT = \
#     '''1abc2
#     pqr3stu8vwx
#     a1b2c3d4e5f
#     treb7uchet'''.splitlines()

digits_re = re.compile('\\d')


def parse_number(s: str) -> int:
    digits = digits_re.findall(s)
    return int(digits[0] + digits[-1])


def solve_1() -> int:
    return sum([parse_number(s) for s in INPUT])
# endregion: part 1


# region: part 2

# INPUT = \
#     '''two1nine
#     eightwothree
#     abcone2threexyz
#     xtwone3four
#     4nineeightseven2
#     zoneight234
#     7pqrstsixteen'''.splitlines()

digit_strings = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}
digits_flexible_re = re.compile(f"(?=(\\d|{'|'.join(digit_strings.keys())}))")


def parse_number_flexible(s: str) -> int:
    maybe_digits = digits_flexible_re.findall(s)
    first = maybe_digits[0] if len(maybe_digits[0]) == 1 else digit_strings[maybe_digits[0]]
    last = maybe_digits[-1] if len(maybe_digits[-1]) == 1 else digit_strings[maybe_digits[-1]]
    return int(first + last)


def solve_2() -> int:
    return sum([parse_number_flexible(s) for s in INPUT])
# endregion: part 2




