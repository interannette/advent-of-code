from collections import Counter
from utils.input_getter import get_input_for_day


def find_marker(input: str) -> int:
    return find_unique(input, 4)


def find_message(input: str) -> int:
    return find_unique(input, 14)


def find_unique(input: str, amount: int) -> int:
    for i in range(amount, len(input)):
        c = Counter(input[i - amount : i])
        if len(c) == amount:
            return i


def first_star():
    input = get_input_for_day()
    print(find_marker(input[0]))


def second_star():
    input = get_input_for_day()
    print(find_message(input[0]))


if __name__ == "__main__":
    second_star()
