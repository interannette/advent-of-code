from functools import cmp_to_key
import math
from typing import List, Tuple, Union
from utils.input_getter import get_input_for_day
import logging


def are_equal(
    first: Union[int, List[Union[int, List]]],
    second: Union[int, List[Union[int, List]]],
) -> bool:
    first_is_int = isinstance(first, int)
    second_is_int = isinstance(second, int)

    if first_is_int == second_is_int:
        return first == second
    elif first_is_int and not second_is_int:
        return are_equal([first], second)
    elif not first_is_int and second_is_int:
        return are_equal(first, [second])
    else:
        return True


def is_correct_order(
    first: Union[int, List[Union[int, List]]],
    second: Union[int, List[Union[int, List]]],
) -> bool:

    first_is_int = isinstance(first, int)
    second_is_int = isinstance(second, int)

    if first_is_int and second_is_int:
        correct = first < second
        if correct:
            logging.debug(f"Returning correct: {first} < {second}")
        else:
            logging.debug(f"Returning incorrect: {first} >= {second}")
        return correct
    elif first_is_int and not second_is_int:
        return is_correct_order([first], second)
    elif not first_is_int and second_is_int:
        return is_correct_order(first, [second])

    for i in range(min(len(first), len(second))):
        if are_equal(first[i], second[i]):
            continue

        return is_correct_order(first[i], second[i])

    correct = len(first) < len(second)
    if correct:
        logging.debug(f"Returning correct: {first} is shorter than {second}")
    else:
        logging.debug(f"Returning incorrect: {first} is longer than {second}")
    return correct


def comparison(
    first: Union[int, List[Union[int, List]]],
    second: Union[int, List[Union[int, List]]],
) -> int:
    if is_correct_order(first, second):
        return -1
    else:
        return 1


def convert_to_list(s: str) -> Union[int, List[Union[int, List]]]:
    return eval(s)


def compute_sum_packets(inputs: List[Tuple[str, str]]) -> int:
    sum = 0
    i = 0

    for i in range(len(inputs)):
        (f, s) = inputs[i]
        logging.debug(f"Pair {i+1}:")
        if is_correct_order(convert_to_list(f), convert_to_list(s)):
            logging.debug(f"{f} is less than")
            logging.debug(f"{s}")
            logging.debug("")
            sum += i + 1
        else:
            logging.debug(f"{f} is NOT less than")
            logging.debug(f"{s}")

        logging.debug("")
    return sum


def build_pairs(inputs: List[str]) -> List[Tuple[str, str]]:
    pairs = []
    for i in range(math.ceil(len(inputs) / 3)):
        f, s = inputs[3 * i : 3 * i + 2]
        pairs.append((f, s))

    return pairs


def first_star():
    inputs = get_input_for_day()
    pairs = build_pairs(inputs=inputs)
    print(compute_sum_packets(pairs))


DIVIDER_PACKETS = [[[6]], [[2]]]


def order_packets(inputs: List[str]):
    packets = [eval(i) for i in inputs if i != ""]
    packets.extend(DIVIDER_PACKETS)

    sorted_packets = sorted(packets, key=cmp_to_key(comparison))

    logging.debug(f"Sorted {len(sorted_packets)} packets")
    for p in sorted_packets:
        logging.debug(p)

    return sorted_packets


def find_decoder_key(inputs: List[str]) -> int:
    sorted_packets = order_packets(inputs)
    i = sorted_packets.index(DIVIDER_PACKETS[0]) + 1
    j = sorted_packets.index(DIVIDER_PACKETS[1]) + 1
    return i * j


def second_star():
    inputs = get_input_for_day()
    print(find_decoder_key(inputs))

    # 21384 too high


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    second_star()
