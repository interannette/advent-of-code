import math
from operator import mul, add
from typing import Callable, List, Optional, Tuple
import re

from utils.input_getter import get_input_for_day


class Monkey:
    items: List[int]
    operation: Callable[[int], int]
    test: Callable[[int], int]
    test_modulo: int
    total_inspected: int
    relief_multiplier: Optional[int]

    def __init__(self, inputs: List[str], multiplier: Optional[int] = 3) -> None:

        if len(inputs) != 5:
            raise Exception(f"incorrect input {len(inputs)} lines")

        self.total_inspected = 0
        self.relief_multiplier = multiplier

        # Start list
        s = re.search("^\s*Starting items: ([\d, ]*)$", inputs[0])
        str_items = s.group(1)
        self.items = [int(i) for i in str_items.split(", ")]

        # Operation function:
        operation_match = re.search(
            "^\s*Operation: new = (.*) ([+\\*]) (.*)", inputs[1]
        )

        def operation_function(w: int) -> int:
            op = None
            if operation_match.group(2) == "+":
                op = add
            elif operation_match.group(2) == "*":
                op = mul

            if operation_match.group(1) == "old" and operation_match.group(3) == "old":
                return op(w, w)
            elif operation_match.group(1) == "old":
                return op(w, int(operation_match.group(3)))
            else:
                return op(int(operation_match.group(1)), w)

        self.operation = operation_function

        # Test function
        divisor_test_match = re.search("^\s*Test: divisible by (\d*)$", inputs[2])
        divisor = int(divisor_test_match.group(1))
        self.test_modulo = divisor
        true_test_match = re.search("\s*If true: throw to monkey (\d*)$", inputs[3])
        true_monkey = int(true_test_match.group(1))
        false_test_match = re.search("\s*If false: throw to monkey (\d*)$", inputs[4])
        false_monkey = int(false_test_match.group(1))

        def test_function(w: int) -> int:
            if w % divisor == 0:
                return true_monkey
            else:
                return false_monkey

        self.test = test_function

    def take_turn(self) -> List[Tuple[int, int]]:
        throws = []
        for item in self.items:
            self.total_inspected += 1
            worry_level = self.operation(item)
            if self.relief_multiplier:
                worry_level = math.floor(worry_level / self.relief_multiplier)
            to_monkey = self.test(worry_level)

            throws.append((to_monkey, worry_level))
        self.items = []
        return throws

    def add_item(self, item: int) -> None:
        self.items.append(item)


class MonkeyBusiness:
    monkeys: List[Monkey]
    round: int
    big_business_monkeys: bool

    def __init__(
        self,
        inputs: List[str],
        big_business_monkeys: bool = False,
        relief_multiplier: int = 3,
    ) -> None:
        self.round = 0
        self.monkeys = []

        modulos = []
        i = 0
        while i < len(inputs):
            # i = "Monkey..."
            # i + 1 - i + 6 = inputs
            # i + 7 = blank
            monkey = Monkey(inputs[i + 1 : i + 6], multiplier=relief_multiplier)
            self.monkeys.append(monkey)
            modulos.append(monkey.test_modulo)
            i += 7

        self.common_divisor = math.lcm(*modulos)
        self.big_business_monkeys = big_business_monkeys

    def execute_round(self) -> None:
        self.round += 1

        for monkey in self.monkeys:
            thrown = monkey.take_turn()
            for (to_monkey, worry_level) in thrown:
                item = (
                    worry_level % self.common_divisor
                    if self.big_business_monkeys
                    else worry_level
                )
                self.monkeys[to_monkey].add_item(item)

    def compute_level(self) -> int:
        counts = [monkey.total_inspected for monkey in self.monkeys]
        counts.sort(reverse=True)
        return counts[0] * counts[1]


def first_star():
    input = get_input_for_day()
    monkey_business = MonkeyBusiness(input)
    for i in range(20):
        monkey_business.execute_round()
    print(monkey_business.compute_level())


def second_star():
    input = get_input_for_day()
    monkey_business = MonkeyBusiness(
        input, relief_multiplier=1, big_business_monkeys=True
    )
    for i in range(10000):
        monkey_business.execute_round()
    print(monkey_business.compute_level())


if __name__ == "__main__":
    second_star()
