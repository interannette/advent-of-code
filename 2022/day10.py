from dataclasses import dataclass
from enum import Enum
from typing import List
from utils.input_getter import get_input_for_day


class Operation(Enum):
    NOOP = 0
    ADDX = 1


@dataclass
class Instruction:
    value: int
    operation: Operation

    def __init__(self, input: str):
        parts = input.split(" ")
        if len(parts) == 2:
            self.operation = Operation.ADDX
            self.value = int(parts[1])
        else:
            self.operation = Operation.NOOP
            self.value = 0


class ClockCircuit:
    register_history: List[int]  # value at index i is the value at the end of round i
    current_value: int
    curent_cycle: int
    ops: List[Instruction]

    def __init__(self, inputs: List[str]):
        self.curent_cycle = 0
        self.current_value = 1
        self.register_history = [1]
        self.ops = [Instruction(i) for i in inputs]

    def run_cycles(self) -> None:
        while len(self.ops) > 0:
            op = self.ops.pop(0)

            self.curent_cycle += 1
            self.register_history.append(self.current_value)

            if op.operation == Operation.ADDX:
                self.curent_cycle += 1
                self.current_value += op.value
                self.register_history.append(self.current_value)

    def signal_strength(self) -> int:
        # For now, consider the signal strength (the cycle number multiplied by the value of the X register)
        # during the 20th cycle and every 40 cycles after that
        # (that is, during the 20th, 60th, 100th, 140th, 180th, and 220th cycles).
        if self.curent_cycle < 20:
            return 0

        signal_stregth = 0
        c = 20
        while c <= self.curent_cycle:
            signal_stregth += c * self.register_history[c - 1]
            c += 40

        return signal_stregth

    def print_pixels(self) -> List[str]:
        pixels = []  # list bool

        for cycle in range(1, len(self.register_history)):
            pixel_pos = (cycle - 1) % 40
            value = self.register_history[cycle - 1]
            pixels.append(value - 1 <= pixel_pos <= value + 1)

        display = []
        line = ""
        for i in range(len(pixels)):
            if i != 0 and i % 40 == 0:
                display.append(line)
                line = ""
            line += "#" if pixels[i] else "."
        display.append(line)

        return display


if __name__ == "__main__":
    input = get_input_for_day()
    c = ClockCircuit(input)
    c.run_cycles()
    print(c.signal_strength())

    for l in c.print_pixels():
        print(l)
