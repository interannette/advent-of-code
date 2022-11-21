from collections import Counter
from typing import List
from utils.input_getter import get_input_for_day


def digits_list(number: int) -> List[int]:
    """
    index 0 = left most digit
    index 5 = right most digit
    assumes 6 digit number
    """
    digits = []
    for i in range(6):
        digits.append(number // 10 ** (5 - i) % 10)
    return digits


def meets_first_requirements(p: int) -> bool:
    """
    It is a six-digit number.
    The value is within the range given in your puzzle input.
    Two adjacent digits are the same (like 22 in 122345).
    Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
    """
    digits = digits_list(p)
    found_adjacent = False
    for i in range(len(digits) - 1):
        diff = digits[i + 1] - digits[i]
        if diff < 0:
            return False
        elif diff == 0:
            found_adjacent = True

    return found_adjacent


def meets_second_requirements(p: int) -> bool:
    """
    It is a six-digit number.
    The value is within the range given in your puzzle input.
    Two adjacent digits are the same (like 22 in 122345).
    the two adjacent matching digits are not part of a larger group of matching digits.
    Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
    """
    digits = digits_list(p)

    for i in range(len(digits) - 1):
        if digits[i + 1] < digits[i]:
            return False

    c = Counter(digits)
    for (d, n) in c.most_common():
        if n == 2:
            return True

    return False


def first_star() -> int:
    input = get_input_for_day(4)
    [start, end] = [int(i) for i in input[0].split("-")]
    match = 0
    for i in range(start, end + 1):
        if meets_first_requirements(i):
            match += 1
    return match


def second_star() -> int:
    input = get_input_for_day(4)
    [start, end] = [int(i) for i in input[0].split("-")]
    match = 0
    for i in range(start, end + 1):
        if meets_second_requirements(i):
            match += 1
    return match


if __name__ == "__main__":
    print(second_star())
