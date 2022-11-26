from typing import List
from utils.input_getter import get_input_for_day
from utils.intcode_computer import IntcodeComputer


def run_with_noun_and_verb(noun: int, verb: int, input: str) -> IntcodeComputer:
    values = [int(value) for value in input.split(",")]
    values[1] = noun
    values[2] = verb

    computer = IntcodeComputer(values)
    computer.execute()

    return computer.memory[0]


def first_star():
    input = get_input_for_day(2)[0].strip()
    return run_with_noun_and_verb(12, 2, input)


def second_star():
    input = get_input_for_day(2)[0].strip()
    for noun in range(100):
        for verb in range(100):
            if 19690720 == run_with_noun_and_verb(noun, verb, input):
                return (noun, verb, 100 * noun + verb)


print(second_star())
