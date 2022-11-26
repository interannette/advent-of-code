from dataclasses import dataclass
from enum import IntEnum
import math
from typing import List, Optional, Tuple


class Opcode(IntEnum):
    ADD = 1
    MULTIPLY = 2
    INPUT = 3
    OUTPUT = 4
    JUMP_IF_TRUE = 5
    JUMP_IF_FALSE = 6
    LESS_THEN = 7
    EQUALS = 8
    HALT = 99


class ParameterMode(IntEnum):
    POSITION = 0
    IMMEDIATE = 1


@dataclass
class Parameter:
    mode: ParameterMode = 0
    value: Optional[int] = 0


@dataclass
class Instruction:
    opcode: Opcode
    first: Optional[ParameterMode]
    second: Optional[ParameterMode]
    result: Optional[ParameterMode]

    @staticmethod
    def parse(i: int) -> Tuple[Opcode, ParameterMode, ParameterMode, ParameterMode]:
        first_two_digits = i % 100
        hundreds_digit = i // 10**2 % 10
        thousands_digit = i // 10**3 % 10
        ten_thousands_digit = i // 10**4 % 10
        return (
            first_two_digits,
            hundreds_digit,
            thousands_digit,
            ten_thousands_digit,
        )


class IntcodeComputer:
    memory: List[int]
    instruction_pointer: int

    def __init__(self, values: List[int]):
        self.memory = values
        self.instruction_pointer = 0

    @staticmethod
    def build_instruction(values: List[int]) -> Instruction:
        (op, mode1, mode2, mode_result) = Instruction.parse(values[0])

        return Instruction(
            op,
            Parameter(mode1, values[1]) if len(values) > 1 else None,
            Parameter(mode2, values[2]) if len(values) > 2 else None,
            Parameter(mode_result, values[3]) if len(values) > 3 else None,
        )

    def current_instruction(self) -> Instruction:

        pos = (
            self.memory[self.instruction_pointer],
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

        return IntcodeComputer.build_instruction(pos)

    def _get_first_value(self) -> int:
        instruction = self.current_instruction()
        first_value = (
            instruction.first.value
            if instruction.first.mode == ParameterMode.IMMEDIATE
            else self.memory[instruction.first.value]
        )
        return first_value

    def _get_second_value(self) -> int:
        instruction = self.current_instruction()
        second_value = (
            instruction.second.value
            if instruction.second.mode == ParameterMode.IMMEDIATE
            else self.memory[instruction.second.value]
        )
        return second_value

    def execute_current_instruction(self) -> Instruction:
        instruction = self.current_instruction()
        advance = None

        if instruction.opcode == Opcode.HALT:
            print(f"Halting!")
            return

        if instruction.opcode in {Opcode.ADD, Opcode.MULTIPLY}:
            operation = sum if instruction.opcode == Opcode.ADD else math.prod
            # We assume result will always be position mode
            self.memory[instruction.result.value] = operation(
                [self._get_first_value(), self._get_second_value()]
            )
            advance = 4
        elif instruction.opcode == Opcode.INPUT:
            value = input("Input a value...")
            self.memory[instruction.first.value] = int(value)
            advance = 2

        elif instruction.opcode == Opcode.OUTPUT:
            print(f"Output {self._get_first_value()}")
            advance = 2

        elif instruction.opcode == Opcode.JUMP_IF_TRUE:
            # if the first parameter is non-zero,
            # it sets the instruction pointer to the value from the second parameter.
            # Otherwise, it does nothing.
            if self._get_first_value() != 0:
                self.instruction_pointer = self._get_second_value()
            else:
                advance = 3
        elif instruction.opcode == Opcode.JUMP_IF_FALSE:
            # if the first parameter is zero,
            # it sets the instruction pointer to the value from the second parameter.
            # Otherwise, it does nothing.
            if self._get_first_value() == 0:
                self.instruction_pointer = self._get_second_value()
            else:
                advance = 3
        elif instruction.opcode == Opcode.LESS_THEN:
            # if the first parameter is less than the second parameter,
            # it stores 1 in the position given by the third parameter.
            # Otherwise, it stores 0.
            value = 1 if self._get_first_value() < self._get_second_value() else 0
            self.memory[instruction.result.value] = value
            advance = 4
        elif instruction.opcode == Opcode.EQUALS:
            # if the first parameter is equal to the second parameter,
            # it stores 1 in the position given by the third parameter.
            # Otherwise, it stores 0
            value = 1 if self._get_first_value() == self._get_second_value() else 0
            self.memory[instruction.result.value] = value
            advance = 4
        else:
            raise Exception(f"Unknown Opcode {instruction.opcode}")

        if advance:
            self.instruction_pointer += advance
        return self.current_instruction()

    def execute(self) -> None:
        while self.current_instruction().opcode != Opcode.HALT:
            self.execute_current_instruction()
