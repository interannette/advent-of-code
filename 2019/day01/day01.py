import math
from typing import Callable, List


def readlines() -> List[int]:
    with open("/Users/annette/dev/advent-of-code/2019/day01/input.txt") as f:
        lines = f.readlines()
        return [int(line) for line in lines]


def calculate_fuel(mass: int) -> int:
    # Specifically, to find the fuel required for a module, take its mass,
    # divide by three, round down, and subtract 2.
    return math.floor(mass / 3) - 2


def calculate_fuel_including_fuel(mass: int) -> int:

    fuel = calculate_fuel(mass=mass)
    total = 0

    while fuel > 0:
        total += fuel
        fuel = calculate_fuel(fuel)

    return total


def sum_with_method(lines: List[int], calculation_method: Callable) -> int:
    sum = 0
    for line in lines:
        sum += calculation_method(line)
    return sum


def first_star():
    lines = readlines()
    return sum_with_method(lines, calculate_fuel)


def second_star():
    lines = readlines()
    return sum_with_method(lines, calculate_fuel_including_fuel)


print(second_star())
