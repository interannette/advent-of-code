from enum import Enum, IntEnum
from typing import List, NamedTuple

sample = False

if sample:
    INPUT = \
        '''32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483'''.splitlines()
else:
    INPUT = open("inputs/day07.txt").readlines()
INPUT = [s.strip() for s in INPUT]


class Type(Enum):
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIR = 3
    THREE_OF_A_KIND = 4
    FULL_HOUSE = 5
    FOUR_OF_A_KIND = 6
    FIVE_OF_A_KIND = 7


class Card(IntEnum):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    T = 10
    J = 11
    Q = 12
    K = 13
    A = 14


class Part2Card(IntEnum):
    J = 0
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    T = 10
    Q = 11
    K = 12
    A = 13


class Line(NamedTuple):
    hand: List[Card]
    bid: int


class Part2Line(NamedTuple):
    hand: List[Part2Card]
    bid: int


def find_type(hand: List[Card]) -> Type:
    frequency = {}
    for i in hand:
        frequency[i] = frequency.get(i, 0) + 1

    counts = [v for v in frequency.values()]
    max_counts = max(counts)

    if max_counts == 5:
        return Type.FIVE_OF_A_KIND
    if max_counts == 4:
        return Type.FOUR_OF_A_KIND
    if max_counts == 3:
        if 2 in counts:
            return Type.FULL_HOUSE
        else:
            return Type.THREE_OF_A_KIND
    if max_counts == 2:
        if len(counts) == 3:
            return Type.TWO_PAIR
        else:
            return Type.ONE_PAIR
    return Type.HIGH_CARD


def part2_find_type(hand: List[Part2Card]) -> Type:
    frequency = {}
    for i in hand:
        frequency[i] = frequency.get(i, 0) + 1

    counts = [v for k, v in frequency.items() if k != Part2Card.J]
    wilds = frequency.get(Part2Card.J, 0)
    max_counts = max(counts) if counts else 0

    if wilds == 5 or wilds == 4:
        return Type.FIVE_OF_A_KIND
    if wilds == 3:
        if max_counts == 2:
            return Type.FIVE_OF_A_KIND
        else:
            return Type.FOUR_OF_A_KIND
    if wilds == 2:
        if max_counts == 3:
            return Type.FIVE_OF_A_KIND
        if max_counts == 2:
            return Type.FOUR_OF_A_KIND
        return Type.THREE_OF_A_KIND
    if wilds == 1:
        if max_counts == 4:
            return Type.FIVE_OF_A_KIND
        if max_counts == 3:
            return Type.FOUR_OF_A_KIND
        if max_counts == 2:
            # two pairs
            if len(counts) == 2:
                return Type.FULL_HOUSE
            else:
                return Type.THREE_OF_A_KIND
        return Type.ONE_PAIR
    if wilds == 0:
        if max_counts == 5:
            return Type.FIVE_OF_A_KIND
        if max_counts == 4:
            return Type.FOUR_OF_A_KIND
        if max_counts == 3:
            if 2 in counts:
                return Type.FULL_HOUSE
            else:
                return Type.THREE_OF_A_KIND
        if max_counts == 2:
            if len(counts) == 3:
                return Type.TWO_PAIR
            else:
                return Type.ONE_PAIR
        return Type.HIGH_CARD


def parse_hand(s: str) -> List[Card]:
    cards = []
    for c in s:
        if c.isdigit():
            cards.append(Card(int(c)))
        else:
            cards.append(Card[c])

    return cards


def part2_parse_hand(s: str) -> List[Part2Card]:
    cards = []
    for c in s:
        if c.isdigit():
            cards.append(Part2Card(int(c)))
        else:
            cards.append(Part2Card[c])

    return cards


def solve_part1() -> int:
    lines_by_type = {t: [] for t in Type}
    for i in INPUT:
        parts = i.split()
        line = Line(hand=parse_hand(parts[0]), bid=int(parts[1]))
        lines_by_type.get(find_type(line.hand)).append(line)

    total = 0
    current_rank = 0
    for t in Type:
        lines = lines_by_type[t]
        lines.sort()
        for line in lines:
            current_rank = current_rank + 1
            total = total + current_rank * line.bid

    return total


def solve_part2() -> int:
    lines_by_type = {t: [] for t in Type}
    for i in INPUT:
        parts = i.split()
        line = Line(hand=part2_parse_hand(parts[0]), bid=int(parts[1]))
        type = part2_find_type(line.hand)
        lines_by_type.get(type).append(line)

    total = 0
    current_rank = 0
    for t in Type:
        lines = lines_by_type[t]
        lines.sort()
        for line in lines:
            current_rank = current_rank + 1
            total = total + current_rank * line.bid

    return total


# 249194813, too low
print(solve_part2())
