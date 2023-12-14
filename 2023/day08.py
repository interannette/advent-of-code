import re
from dataclasses import dataclass
from typing import NamedTuple, List, Dict

data = 4

if data == 1:
    INPUT = \
        '''RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)'''.splitlines()
elif data == 2:
    INPUT = \
        '''LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)'''.splitlines()
elif data == 3:
    INPUT = \
        '''LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)'''.splitlines()
else:
    INPUT = open("inputs/day08.txt").readlines()
INPUT = [s.strip() for s in INPUT]


class Maps(NamedTuple):
    steps: List[str]
    lefts: Dict[str, str]
    rights: Dict[str, str]


def parse_maps() -> Maps:
    steps = []
    lefts = {}
    rights = {}

    # ZZZ = (ZZZ, ZZZ)
    pattern = re.compile('(\\w{3}) = \\((\\w{3}), (\\w{3})\\)')
    for i in INPUT:
        if not steps:
            steps = list(i)
        else:
            m = pattern.match(i)
            if m:
                k = m.group(1)
                l = m.group(2)
                r = m.group(3)
                lefts[k] = l
                rights[k] = r

    return Maps(steps=steps, lefts=lefts, rights=rights)


def solve_part1() -> int:
    maps = parse_maps()

    current_node = 'AAA'
    i = 0
    while current_node != 'ZZZ':
        instruction = maps.steps[i % len(maps.steps)]
        i = i+1
        if instruction == 'L':
            current_node = maps.lefts[current_node]
        else:
            current_node = maps.rights[current_node]
    return i


@dataclass
class Cycle:
    complete: bool
    steps: List[str]
    repeat: int
    current_index: int

    @staticmethod
    def create_cycle(n: str, repeat: int) -> "Cycle":
        return Cycle(complete=False, steps=[n], repeat=repeat, current_index=0)

    def add_step(self, step: str) -> bool:
        if self.complete:
            self.current_index = (self.current_index + 1) % len(self.steps)
            return True
        self.steps.append(step)
        if len(self.steps) % self.repeat == 0 and self.steps[0] == step:
            self.complete = True
            print(f"completed cycle {self}")
            return True

    def current_step(self) -> str:
        if not self.complete:
            return self.steps[-1]
        else:
            return self.steps[self.current_index]


def all_z(cycles: List[Cycle]) -> bool:
    return all([c.current_step()[-1:] == 'Z' for c in cycles])


def done(cycles: List[Cycle]) -> bool:
    return all_z(cycles) or all([c.complete for c in cycles])


def solve_part2_brute_force() -> int:
    maps = parse_maps()
    current_nodes = [n for n in maps.lefts.keys() if n[-1:] == "A"]
    i = 0
    while not all([c[-1:] == 'Z' for c in current_nodes]):
        instruction = maps.steps[i % len(maps.steps)]
        i = i+1
        if instruction == 'L':
            current_nodes = [maps.lefts[c] for c in current_nodes]
        else:
            current_nodes = [maps.rights[c] for c in current_nodes]
    return i


def solve_part2() -> int:
    maps = parse_maps()
    repeat = len(maps.steps)
    cycles = [Cycle.create_cycle(n, repeat) for n in maps.lefts.keys() if n[-1:] == "A"]
    cycles = [cycles[0]]

    for c in cycles:
        j = 0
        while not c.complete:
            instruction = maps.steps[j % len(maps.steps)]
            j = j + 1
            if instruction == 'L':
                c.add_step(maps.lefts[c.current_step()])
            else:
                c.add_step(maps.rights[c.current_step()])

        print(f"cycle {c.steps[0]} complete {j}")

    return 0
    #
    # print(f"A nodes {len(cycles)}. repeats {repeat}")
    # i = 0
    # while not done(cycles):
    #     if i % len(maps.steps) == 0:
    #         print("repeat complete")
    #     instruction = maps.steps[i % len(maps.steps)]
    #     i = i+1
    #     if instruction == 'L':
    #         for c in cycles:
    #             c.add_step(maps.lefts[c.current_step()])
    #     else:
    #         for c in cycles:
    #             c.add_step(maps.rights[c.current_step()])
    #
    # if all_z(cycles):
    #     return i
    # else:
    #     return -1
    # we have cycles, do some math


print(solve_part2())

