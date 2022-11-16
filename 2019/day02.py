from dataclasses import dataclass
from enum import IntEnum
import math
from typing import List, Optional
from utils.input_getter import get_input_for_day


class Opcode(IntEnum):
    ADD = 1
    MULTIPLY = 2
    HALT = 99


@dataclass
class Instruction:
    opcode: Opcode
    first_arg_pos: Optional[int]
    second_arg_pos: Optional[int]
    result_pos: Optional[int]


class IntcodeComputer:
    memory: List[int]
    instruction_pointer: int

    def __init__(self, values: List[int]):
        self.memory = values
        self.instruction_pointer = 0

    def current_instruction(self) -> Instruction:

        pos = (
            self.memory[self.instruction_pointer + 1]
            if self.instruction_pointer + 1 < len(self.memory)
            else None,
            self.memory[self.instruction_pointer + 2]
            if self.instruction_pointer + 2 < len(self.memory)
            else None,
            self.memory[self.instruction_pointer + 3]
            if self.instruction_pointer + 3 < len(self.memory)
            else None,
        )

        return Instruction(self.memory[self.instruction_pointer], *pos)

    def advance(self) -> Instruction:
        self.instruction_pointer += 4
        return self.current_instruction()

    def execute_current_instruction(self) -> Instruction:
        instruction = self.current_instruction()
        operation = None
        if instruction.opcode == Opcode.HALT:
            return
        elif instruction.opcode == Opcode.ADD:
            operation = sum
        elif instruction.opcode == Opcode.MULTIPLY:
            operation = math.prod

        self.memory[instruction.result_pos] = operation(
            [
                self.memory[instruction.first_arg_pos],
                self.memory[instruction.second_arg_pos],
            ]
        )
        return self.advance()

    def execute(self) -> None:
        while self.current_instruction().opcode != Opcode.HALT:
            self.execute_current_instruction()


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
