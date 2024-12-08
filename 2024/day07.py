import logging
from typing import Iterable

logger = logging.getLogger()
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.WARN)


class Equation:
    test_value: int
    components: list[int]
    operations: list[callable]
    solvable: bool = None

    def __str__(self) -> str:
        return f"{self.test_value}: {self.components}, operation count {len(self.operations)}, solveable: {self.solvable}"

    @staticmethod
    def parse(line: str) -> "Equation":
        v, c = line.split(":")
        return Equation(int(v), [int(i.strip()) for i in c.split()])

    def __init__(
        self,
        test_value: int,
        components: list[int],
        operations: list[callable] = [],
        solvable: bool = None,
    ):
        self.test_value = test_value
        self.components = components
        self.operations = operations
        self.solvable = solvable

    def next_iteration(self, operation: str) -> "Equation":
        # test_value, [c1,c2,c3,...], [o1,o2,...]
        # test_value = c1 (o1) c2 (o2) c3...
        # test_value (~o1) c1 = c2 (o2) ...

        # next_test_value = test_value (~o1) c1
        # next_components = [c2, c3, ...]
        # next_operations = operation

        if operation == "plus":
            return Equation(
                self.test_value - self.components[-1],
                self.components[:-1],
                [lambda x, y: x + y],
            )

        if operation == "times":
            return Equation(
                self.test_value / self.components[-1],
                self.components[:-1],
                [lambda x, y: x * y],
            )

        raise ValueError("operation must be times or plus")

    @staticmethod
    def combine_iterations(first: "Equation", sub_equation: "Equation") -> "Equation":
        logger.debug(f"combining {first} and {sub_equation}")
        return Equation(
            first.test_value,
            first.components,
            sub_equation.operations,
            sub_equation.solvable,
        )

    def solve(self) -> "Equation":
        # base condition: single operation
        if len(self.components) == 2:
            logger.debug(f"base case solve {self}")
            if self.components[0] + self.components[1] == self.test_value:
                self.operations.append(lambda x, y: x + y)
                self.solvable = True
                return self
            elif self.components[0] * self.components[1] == self.test_value:
                self.operations.append(lambda x, y: x * y)
                self.solvable = True
                return self
            else:
                self.solvable = False
                return self

        # recursive: shorten and test:
        # test plus
        plus_sub_equation = self.next_iteration("plus")
        logger.debug(f"testing plus sub: {plus_sub_equation}")
        plus_sub_equation = plus_sub_equation.solve()
        logger.debug(f"result plus sub: {plus_sub_equation}")
        if plus_sub_equation.solvable:
            return Equation.combine_iterations(self, plus_sub_equation)
        # test times
        times_sub_equation = self.next_iteration("times")
        logger.debug(f"testing times sub: {times_sub_equation}")
        times_sub_equation = times_sub_equation.solve()
        if times_sub_equation.solvable:
            return Equation.combine_iterations(self, times_sub_equation)

        self.solvable = False
        return self


class Day07Puzzle:
    equations: list[Equation]

    def __init__(self, input_lines: Iterable[str]):
        self.equations = [Equation.parse(e) for e in input_lines]

    def star1(self) -> int:
        total = 0
        for e in self.equations:
            logger.debug(f"testing {e}")
            e = e.solve()
            if e.solvable:
                logger.info(f"{e} is solvable")
                total += e.test_value
        return total


test_input = False
if test_input:
    input = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20""".splitlines()
else:
    input = open("inputs/day07.txt").readlines()

puzzle = Day07Puzzle(input)
print(puzzle.star1())
