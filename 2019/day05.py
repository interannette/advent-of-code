from utils.input_getter import get_input_for_day
from utils.intcode_computer import IntcodeComputer


def first_star() -> None:
    input = get_input_for_day(5)[0].strip()
    computer = IntcodeComputer(values=[int(value) for value in input.split(",")])
    computer.execute()


if __name__ == "__main__":
    first_star()
