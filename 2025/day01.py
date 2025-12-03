from dataclasses import dataclass


@dataclass
class Instruction:
    direction: str
    amount: int

    def apply(self, start: int) -> int:
        if self.direction == "L":
            return (start - self.amount) % 100
        elif self.direction == "R":
            return (start + self.amount) % 100
        else:
            raise ValueError(f"Unknown direction: {self.direction}")

    def apply_and_count(self, start: int) -> (int, int):
        end = self.apply(start)
        count = 0
        if end == 0:
            if start == 0:
                count = self.amount // 100
            else:
                count = self.amount // 100 + 1
        else:
            if self.direction == "L":
                count = self.amount // 100
                if end > start and start != 0:
                    count += 1
            elif self.direction == "R":
                count = self.amount // 100
                if end < start and start != 0:
                    count += 1
        return end, count


def parse_instruction(instruction_str: str) -> Instruction:
    direction = instruction_str[0]
    amount = int(instruction_str[1:])
    if amount == 0:
        raise ValueError("Amount cannot be zero")
    return Instruction(direction, amount)


test_input = False
if test_input:
    input = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82""".splitlines()
else:
    input = open("inputs/day01.txt").readlines()


instructions = [parse_instruction(line) for line in input]


def star1():
    position = 50
    times_at_zero = 0
    for instr in instructions:
        position = instr.apply(position)
        if position == 0:
            times_at_zero += 1

    print(f"Times at zero: {times_at_zero}")


def star2():
    current_position = 50
    times_passing_zero = 0
    for instr in instructions:
        current_position, rotations = instr.apply_and_count(current_position)
        times_passing_zero += rotations

    print(f"Times passing zero: {times_passing_zero}")


star2()
