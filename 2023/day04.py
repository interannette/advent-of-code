import re
from collections.abc import Set
from dataclasses import dataclass
from typing import List

sample = False

if sample:
    INPUT = \
        '''Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11'''.splitlines()
else:
    INPUT = open("inputs/day04.txt").readlines()
INPUT = [s.strip() for s in INPUT]


@dataclass
class Card:
    id: int
    winners: Set[int]
    numbers: Set[int]

    def overlap(self) -> int:
        return len(self.winners.intersection(self.numbers))


def parse_cards() -> List[Card]:

    cards = []
    pattern = re.compile('^Card\\s+(\\d+):([\\s\\d]+)\\|([\\s\\d]+)$')

    for line in INPUT:
        m = pattern.match(line)
        if not m:
            raise ValueError("invalid line: " + line)

        winner_string = m.group(2)
        numbers_string = m.group(3)

        winners = {int(s) for s in winner_string.strip().split()}
        numbers = {int(s) for s in numbers_string.strip().split()}

        cards.append(Card(int(m.group(1)), winners, numbers))

    return cards


def solve_part1():
    total = 0

    cards = parse_cards()

    for card in cards:
        count = card.overlap()

        print(f"got {count} for card {card.id}")

        if count >= 1:
            total = total + 2**(count - 1)

    print(total)


def solve_part2():
    cards = parse_cards()

    for card in cards:
        count = card.overlap()
        if count >= 1:
            for i in range(count):
                cards.append(cards[card.id+i])

    print(len(cards))


solve_part2()


