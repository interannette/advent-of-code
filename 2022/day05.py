from dataclasses import dataclass
import re
import string
from typing import Dict, List, Type, TypeVar
from utils.input_getter import get_input_for_day


@dataclass
class Move:
    amount: int
    start: int
    end: int

    @staticmethod
    def parse(input: str) -> "Move":
        m = re.search("^move (\d*) from (\d*) to (\d*)$", input)
        if m:
            return Move(int(m.group(1)), int(m.group(2)), int(m.group(3)))
        else:
            return None


@dataclass
class Dock:
    stacks: Dict[int, List[str]]

    @staticmethod
    def parse(inputs: List[str]) -> "Dock":
        if len(inputs[0]) == 11:
            num_stacks = 3
        else:
            num_stacks = int((len(inputs[0]) + 1) / 4)

        stacks = {i: [] for i in range(1, num_stacks + 1)}

        if num_stacks == 3:
            regex = "(   |\[\w\]) (   |\[\w\]) (   |\[\w\])"
        else:
            regex = "(   |\[\w\]) (   |\[\w\]) (   |\[\w\]) (   |\[\w\]) (   |\[\w\]) (   |\[\w\]) (   |\[\w\]) (   |\[\w\]) (   |\[\w\])"

        for input in inputs:
            m = re.search(regex, input)
            if not m:
                raise Exception(f"unable to parse line {input}")

            for i in range(1, num_stacks + 1):
                if m.group(i).strip():
                    stacks[i].append(m.group(i))

        return Dock(stacks=stacks)

    def apply_move(self, move: Move) -> None:
        for i in range(move.amount):
            c = self.stacks[move.start].pop(0)
            self.stacks[move.end].insert(0, c)


TDock = TypeVar("TDock", bound=Dock)


class CrateMover9001(Dock):
    @staticmethod
    def parse(inputs: List[str]) -> "CrateMover9001":
        return CrateMover9001(Dock.parse(inputs).stacks)

    def apply_move(self, move: Move) -> None:
        crates = self.stacks[move.start][0 : move.amount]
        self.stacks[move.end] = crates + self.stacks[move.end]
        self.stacks[move.start] = self.stacks[move.start][move.amount :]


def run_steps(inputs: List[str], model: TDock) -> TDock:

    dock_lines = [line for line in inputs if "[" in line]
    move_lines = [line for line in inputs if "move" in line]

    dock = model.parse(dock_lines)

    for move_line in move_lines:
        move = Move.parse(move_line)
        dock.apply_move(move=move)

    return dock


def build_end_str(dock: Dock) -> str:
    top = [value[0][1:-1] for value in dock.stacks.values()]
    return "".join(top)


def first_star():
    input = get_input_for_day()
    dock = run_steps(input, Dock)
    print(build_end_str(dock))


def second_star():
    input = get_input_for_day()
    dock = run_steps(input, CrateMover9001)
    print(build_end_str(dock))


if __name__ == "__main__":
    second_star()
