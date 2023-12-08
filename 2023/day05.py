from collections import namedtuple
from dataclasses import dataclass
from enum import Enum
from typing import List, Dict, Tuple, OrderedDict

sample = False
if sample:
    INPUT = \
    '''seeds: 79 14 55 13
    
    seed-to-soil map:
    50 98 2
    52 50 48
    
    soil-to-fertilizer map:
    0 15 37
    37 52 2
    39 0 15
    
    fertilizer-to-water map:
    49 53 8
    0 11 42
    42 0 7
    57 7 4
    
    water-to-light map:
    88 18 7
    18 25 70
    
    light-to-temperature map:
    45 77 23
    81 45 19
    68 64 13
    
    temperature-to-humidity map:
    0 69 1
    1 0 69
    
    humidity-to-location map:
    60 56 37
    56 93 4'''.splitlines()
else:
    INPUT = open("inputs/day05.txt").readlines()
INPUT = [s.strip() for s in INPUT]


class Category(Enum):
    SEED = 1
    SOIL = 2
    FERTILIZER = 3
    WATER = 4
    LIGHT = 5
    TEMPERATURE = 6
    HUMIDITY = 7
    LOCATION = 8


Value = namedtuple('Value', ['category', 'number'])
InputRule = namedtuple('InputRule', ['source_start', 'destination_start', 'range_length'])


@dataclass
class Almanac:
    initial_seeds: List[int]
    rules: Dict[Category, Tuple[Category, OrderedDict[int, int]]]

    def get_next_value(self, v: Value) -> Value:
        cutoffs = self.rules[v.category][1]

        # (0,0), (10, 1000), (12, 200), (20, 0)
        # 0-9 -> deta = 0
        # 10-11 -> delta = 1000
        # 12-19 -> delta = 200
        # >=20 -> 0
        # biggest source less than value
        delta = 0
        for k, d in cutoffs.items():
            if k <= v.number:
                delta = d
            else:
                break

        next_value = Value(self.rules[v.category][0], v.number + delta)
        #print(f"mapped value {v} to next value {next_value}")
        return next_value

    def run_seed(self, s: int) -> int:
        previous_value = Value(Category.SEED, s)
        next_value = self.get_next_value(previous_value)
        while next_value.category != Category.LOCATION:
            previous_value = next_value
            next_value = self.get_next_value(previous_value)
        if next_value.category == Category.LOCATION:
            return next_value.number
        else:
            raise Exception(f"End value not location. {next_value}")

    def locations(self) -> List[int]:
        locations = []
        for s in self.initial_seeds:
            locations.append(self.run_seed(s))

        return locations

    def locations_part2(self) -> List[int]:
        locations = []
        for i in range(0, len(self.initial_seeds)-1, 2):
            for j in range(self.initial_seeds[i+1]):
                locations.append(self.run_seed(self.initial_seeds[i]+j))
        return locations


def convert_rules(pending_rules: List[InputRule]) -> OrderedDict[int, int]:
    pending_rules.sort(key=lambda t: t[0])
    converted_rules = OrderedDict[int, int]()
    if len(pending_rules) > 1 and pending_rules[0].source_start != 0:
        converted_rules[0] = 0

    for input_rule in pending_rules:
        converted_rules[input_rule.source_start] = input_rule.destination_start - input_rule.source_start
        converted_rules[input_rule.source_start + input_rule.range_length] = 0 # start next segment as 0, will overwrite if needed
    return converted_rules


def parse_almanac() -> Almanac:
    seeds = []
    rules = {}
    #     rules: Dict[Category, Tuple[Category, List[ConvertedRule]]]
    current_source = None
    current_destination = None
    pending_rules = []

    for line in INPUT:
        if 'seeds:' in line:
            seeds = [int(s) for s in line.replace('seeds: ', '').split()]
        elif 'map' in line:
            # humidity-to-location map:
            parts = line.replace(' map:', '').split('-')
            current_source = Category[parts[0].upper()]
            current_destination = Category[parts[2].upper()]
        elif line == '':
            rules[current_source] = (current_destination, convert_rules(pending_rules))

            # clear out
            current_source = None
            current_destination = None
            pending_rules = []
        else:
            parts = [int(s) for s in line.split()]
            pending_rules.append(InputRule(destination_start=parts[0], source_start=parts[1], range_length=parts[2]))

    # add last set of pending rules
    rules[current_source] = (current_destination, convert_rules(pending_rules))

    return Almanac(initial_seeds=seeds, rules=rules)


def solve_part1():
    almanac = parse_almanac()
    print(f"initial seeds: {len(almanac.initial_seeds)}")
    locations = almanac.locations()
    print(f"locations {len(locations)}")
    return min(locations)


def solve_part2():
    almanac = parse_almanac()
    print(f"initial seeds: {len(almanac.initial_seeds)}")
    locations = almanac.locations_part2()
    print(f"locations {len(locations)}")
    return min(locations)


# 63627802 - too low
# 546703948 - too high
print(solve_part2())

