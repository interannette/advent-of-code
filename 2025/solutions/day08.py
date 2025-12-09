import math
from collections.abc import Iterable
from dataclasses import dataclass


@dataclass(frozen=True)
class Coordinate:
    x: int
    y: int
    z: int

    @staticmethod
    def parse(l: str) -> "Coordinate":
        x, y, z = l.split(",")
        return Coordinate(int(x), int(y), int(z))

    @staticmethod
    def dist(l: "Coordinate", r: "Coordinate") -> float:
        return math.sqrt((l.x - r.x) ** 2 + (l.y - r.y) ** 2 + (l.z - r.z) ** 2)


@dataclass(frozen=True)
class Pair:
    coordinates: frozenset[Coordinate]
    d: float

    @staticmethod
    def compute(c1: Coordinate, c2: Coordinate) -> "Pair":
        return Pair(frozenset({c1, c2}), Coordinate.dist(c1, c2))

    def x_product(self) -> int:
        l = [c for c in self.coordinates]
        return l[0].x * l[1].x


class Day08Puzzle:
    junction_boxes = list[Coordinate]

    def __init__(self, input_lines: Iterable[str]):
        self.junction_boxes = [Coordinate.parse(l) for l in input_lines]
        return

    def compute_distances(self) -> list[Pair]:
        distances = set()
        for j in range(len(self.junction_boxes)):
            for i in range(j + 1, len(self.junction_boxes)):
                distances.add(Pair.compute(self.junction_boxes[j], self.junction_boxes[i]))

        sorted_distances = sorted(distances, key=lambda p: p.d)
        return sorted_distances

    def add_next_junction(self, sorted_distances: list[Pair], circuits: set[frozenset[Coordinate]], index: int) -> \
            tuple[set[
                frozenset[Coordinate]], Pair]:
        pair = sorted_distances[index]

        # find if the new pair belongs to any existing circuits
        overlapping_circuits = set()
        for c in circuits:
            intersection = c.intersection(pair.coordinates)
            if intersection:
                overlapping_circuits.add(c)

        # add new pair to circuits, merging with existing circuits as needed
        if len(overlapping_circuits) == 0:
            circuits.add(pair.coordinates)
        elif len(overlapping_circuits) == 1:
            existing_circuit = overlapping_circuits.pop()
            circuits.remove(existing_circuit)
            new_circuit = existing_circuit | pair.coordinates
            circuits.add(frozenset(new_circuit))
        elif len(overlapping_circuits) == 2:
            existing_circuit1 = overlapping_circuits.pop()
            existing_circuit2 = overlapping_circuits.pop()
            circuits.remove(existing_circuit1)
            circuits.remove(existing_circuit2)
            joined_circuit = existing_circuit1 | existing_circuit2 | pair.coordinates
            circuits.add(frozenset(joined_circuit))
        else:
            raise Exception("more than 2 overlapping circuits")

        return circuits, pair

    def build_circuits(self, sorted_distances: list[Pair], num_pairs: int):
        circuits = set()

        for i in range(num_pairs):
            circuits, _ = self.add_next_junction(sorted_distances, circuits, i)

        return circuits

    def build_full_circuit(self, sorted_distances: list[Pair]) -> Pair:
        circuits = set()
        circuits, last_pair = self.add_next_junction(sorted_distances, circuits, 0)
        i = 1
        while max([len(c) for c in circuits]) < len(self.junction_boxes):
            circuits, last_pair = self.add_next_junction(sorted_distances, circuits, i)
            i += 1
        return last_pair

    def star1(self, num_pairs: int) -> int:
        sorted_distances = self.compute_distances()
        circuits = self.build_circuits(sorted_distances, num_pairs)
        sorted_circuits = sorted(circuits, key=lambda c: len(c), reverse=True)
        return len(sorted_circuits[0]) * len(sorted_circuits[1]) * len(sorted_circuits[2])

    def star2(self) -> int:
        sorted_distances = self.compute_distances()
        last_pair = self.build_full_circuit(sorted_distances)
        return last_pair.x_product()


use_test_input = False
if use_test_input:
    input = """162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689""".splitlines()
else:
    input = open("solutions/inputs/day08.txt").readlines()

puzzle = Day08Puzzle(input)
# print(f"Test input: {use_test_input}. Star 1 result {puzzle.star1(10 if use_test_input else 1000)}")
# 98696
print(f"Test input: {use_test_input}. Star 2 result {puzzle.star2()}")
# 2245203960
