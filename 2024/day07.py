import logging
from typing import Iterable

logger = logging.getLogger()
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.WARN)


class Star1Equation:
    test_value: int
    components: list[int]
    operations: list[callable]
    solvable: bool = None

    def __str__(self) -> str:
        return f"{self.test_value}: {self.components}, operation count {len(self.operations)}, solveable: {self.solvable}"

    @staticmethod
    def parse(line: str) -> "Star1Equation":
        v, c = line.split(":")
        return Star1Equation(int(v), [int(i.strip()) for i in c.split()])

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

    def next_iteration(self, operation: str) -> "Star1Equation":
        # test_value, [c1,c2,c3,...], [o1,o2,...]
        # test_value = c1 (o1) c2 (o2) c3...
        # test_value (~o1) c1 = c2 (o2) ...

        # next_test_value = test_value (~o1) c1
        # next_components = [c2, c3, ...]
        # next_operations = operation

        if operation == "plus":
            return Star1Equation(
                self.test_value - self.components[-1],
                self.components[:-1],
                [lambda x, y: x + y],
            )

        if operation == "times":
            return Star1Equation(
                self.test_value / self.components[-1],
                self.components[:-1],
                [lambda x, y: x * y],
            )

        raise ValueError("operation must be times or plus")

    @staticmethod
    def combine_iterations(
        first: "Star1Equation", sub_equation: "Star1Equation"
    ) -> "Star1Equation":
        logger.debug(f"combining {first} and {sub_equation}")
        return Star1Equation(
            first.test_value,
            first.components,
            sub_equation.operations,
            sub_equation.solvable,
        )

    def solve(self) -> "Star1Equation":
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
            return Star1Equation.combine_iterations(self, plus_sub_equation)
        # test times
        times_sub_equation = self.next_iteration("times")
        logger.debug(f"testing times sub: {times_sub_equation}")
        times_sub_equation = times_sub_equation.solve()
        if times_sub_equation.solvable:
            return Star1Equation.combine_iterations(self, times_sub_equation)

        self.solvable = False
        return self


class Day07Star1Puzzle:
    equations: list[Star1Equation]

    def __init__(self, input_lines: Iterable[str]):
        self.equations = [Star1Equation.parse(e) for e in input_lines]

    def star1(self) -> int:
        total = 0
        for e in self.equations:
            logger.debug(f"testing {e}")
            e = e.solve()
            if e.solvable:
                logger.info(f"{e} is solvable")
                total += e.test_value
        return total


class Star2Equation:
    test_value: int
    components: list[int]
    operations: list[callable]
    solvable: bool = None

    def __str__(self) -> str:
        return f"{self.test_value}: {self.components}, operation count {len(self.operations)}, solveable: {self.solvable}"

    @staticmethod
    def parse(line: str) -> "Star2Equation":
        v, c = line.split(":")
        return Star2Equation(int(v), [int(i.strip()) for i in c.split()])

    def __init__(
        self,
        test_value: int,
        components: list[int],
        operations: list[callable] = None,
        solvable: bool = None,
    ):
        self.test_value = test_value
        self.components = components
        self.operations = operations if operations else []
        self.solvable = solvable

    def next_iterations(self) -> list["Star2Equation"]:
        # test_value, [c1,c2,c3,...], [o1,o2,...]
        # test_value = c1 (o1) c2 (o2) c3...
        # test_value (~o1) c1 = c2 (o2) ...

        # next_test_value = test_value (~o1) c1
        # next_components = [c2, c3, ...]
        # next_operations = operation
        iterations = []
        iterations.append(
            Star2Equation(
                self.test_value - self.components[-1],
                self.components[:-1],
                [lambda x, y: x + y],
            )
        )
        if self.test_value % self.components[-1] == 0:
            iterations.append(
                Star2Equation(
                    int(self.test_value / self.components[-1]),
                    self.components[:-1],
                    [lambda x, y: x * y],
                )
            )
        iterations.append(
            Star2Equation(
                int(str(self.test_value)[: len(str(self.components[-1])) + 1]),
                self.components[:-1],
                [lambda x, y: int(str(x) + str(y))],
            )
        )
        return iterations

    @staticmethod
    def combine_iterations(
        first: "Star2Equation", sub_equation: "Star2Equation"
    ) -> "Star2Equation":
        logger.debug(f"combining {first} and {sub_equation}")
        return Star2Equation(
            first.test_value,
            first.components,
            sub_equation.operations,
            sub_equation.solvable,
        )

    def solve(self) -> "Star2Equation":
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
            elif (
                int(str(self.components[0]) + str(self.components[1]))
                == self.test_value
            ):
                self.operations.append(lambda x, y: int(str(x) + str(y)))
                self.solvable = True
                return self
            else:
                self.solvable = False
                return self

        # recursive: shorten and test:
        sub_equations = self.next_iterations()
        for sub_equation in sub_equations:
            logger.debug(f"testing sub equation {sub_equation}")
            sub_equation = sub_equation.solve()
            if sub_equation.solvable:
                logger.info(f"sub equation is solvable {sub_equation}")
                return Star2Equation.combine_iterations(self, sub_equation)

        self.solvable = False
        return self


class Day07Star2Puzzle:
    equations: list[Star2Equation]

    def __init__(self, input_lines: Iterable[str]):
        self.equations = [Star2Equation.parse(e) for e in input_lines]

    def star2(self) -> int:
        total = 0
        for e in self.equations:
            logger.debug(f"star method: testing {e}")
            e = e.solve()
            if e.solvable:
                logger.info(f"star method: {e} is solvable")
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


# 62005574426943 too low

equations = []
for e in input:
    equations.append((Star1Equation.parse(e), Star2Equation.parse(e)))

for e1, e2 in equations:
    s1 = e1.solve()
    s2 = e2.solve()
    if s1.solvable and not s2.solvable:
        logger.error(f"solvable under s1 rules but not s2, {e1}")
    elif not s2.solvable:
        logger.warning(f"not solvable under s2 rules {s2}")
