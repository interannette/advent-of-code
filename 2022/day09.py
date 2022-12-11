from copy import copy
from dataclasses import dataclass
from enum import Enum
import math
from typing import List, TypeVar
from utils.input_getter import get_input_for_day


class Direction(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

    @staticmethod
    def parse(d: str) -> "Direction":
        if d == "U":
            return Direction.UP
        elif d == "D":
            return Direction.DOWN
        elif d == "L":
            return Direction.LEFT
        elif d == "R":
            return Direction.RIGHT


class Move:
    direction: Direction
    amount: int

    def __init__(self, input: str):
        d, a = input.split(" ")
        self.direction = Direction.parse(d)
        self.amount = int(a)


@dataclass(frozen=True)
class Position:
    x: int
    y: int

    def __add__(self, other: "Position") -> "Position":
        return Position(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Position") -> "Position":
        return Position(self.x - other.x, self.y - other.y)

    def move(self, direction: Direction) -> "Position":
        DIRECTION_MAP = {
            Direction.UP: Position(0, 1),
            Direction.DOWN: Position(0, -1),
            Direction.LEFT: Position(-1, 0),
            Direction.RIGHT: Position(1, 0),
        }
        return self + DIRECTION_MAP[direction]

    def magnitude(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)

    @staticmethod
    def _sign(i: int) -> int:
        if i > 0:
            return 1
        if i < 0:
            return -1
        return 0

    def scale_to_direction(self) -> "Position":
        return Position(Position._sign(self.x), Position._sign(self.y))


@dataclass
class Bridge:
    head: Position
    tail: Position
    head_history: List[Position]
    tail_history: List[Position]

    def __init__(self):
        self.head = Position(0, 0)
        self.tail = Position(0, 0)
        self.head_history = []
        self.tail_history = []

    def execute_move(self, move: Move) -> None:
        for i in range(move.amount):
            self.head_history.append(copy(self.head))
            self.head = self.head.move(move.direction)

            diff = self.head - self.tail
            if math.floor(diff.magnitude()) > 1:
                self.tail_history.append(copy(self.tail))
                self.tail = self.tail + diff.scale_to_direction()


@dataclass
class BrokenBridge(Bridge):
    knots: List[Position]
    tail_history: List[Position]

    def __init__(self) -> None:
        self.knots = [
            Position(0, 0),
            Position(0, 0),
            Position(0, 0),
            Position(0, 0),
            Position(0, 0),
            Position(0, 0),
            Position(0, 0),
            Position(0, 0),
            Position(0, 0),
            Position(0, 0),
        ]
        self.tail_history = []

    def execute_move(self, move: Move) -> None:
        for i in range(move.amount):
            for j in range(10):
                if j == 0:
                    self.knots[0] = self.knots[0].move(move.direction)
                else:
                    diff = self.knots[j - 1] - self.knots[j]
                    if math.floor(diff.magnitude()) > 1:
                        if j == 9:
                            self.tail_history.append(copy(self.knots[j]))
                        self.knots[j] = self.knots[j] + diff.scale_to_direction()


def simulate_movements(moves: List[Move], bridge: Bridge) -> Bridge:
    for move in moves:
        bridge.execute_move(move)
    return bridge


def compute_first_star(input: List[str]) -> int:
    moves = [Move(i) for i in input]
    bridge = simulate_movements(moves, Bridge())
    tails = set(bridge.tail_history)
    tails.add(bridge.tail)
    return len(tails)


def compute_second_star(input: List[str]) -> int:
    moves = [Move(i) for i in input]
    bridge = simulate_movements(moves, BrokenBridge())
    tails = set(bridge.tail_history)
    tails.add(bridge.knots[9])
    return len(tails)


if __name__ == "__main__":
    input = get_input_for_day()
    print(compute_second_star(input))
