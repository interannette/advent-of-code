from dataclasses import dataclass
import logging
from typing import Iterable

logger = logging.getLogger()
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.INFO)

ROBOT = "@"
WALL = "#"
BOX = "O"
EMPTY = "."


@dataclass(frozen=True)
class Coordinate:
    x: int
    y: int

    def __add__(self, other):
        return Coordinate(self.x + other.x, self.y + other.y)

    def __rmul__(self, other):
        return Coordinate(self.x * other, self.y * other)

    def move(self, d: str) -> "Coordinate":
        match d:
            case "<":
                return Coordinate(self.x - 1, self.y)
            case ">":
                return Coordinate(self.x + 1, self.y)
            case "^":
                return Coordinate(self.x, self.y - 1)
            case "v":
                return Coordinate(self.x, self.y + 1)

    def reverse(self, d: str) -> "Coordinate":
        match d:
            case "<":
                return self.move(">")
            case ">":
                return self.move("<")
            case "^":
                return self.move("v")
            case "v":
                return self.move("^")


class Day15Puzzle:

    grid: list[list[str]]
    moves: list[str]
    robot_pos: Coordinate
    current_move_index: int

    def __init__(self, input_lines: Iterable[str]):
        self.grid = []
        self.moves = []
        self.current_move_index = 0
        grid_done = False
        for l in input_lines:
            l = l.strip()
            if l == "":
                grid_done = True
            elif not grid_done:
                if ROBOT in l:
                    self.robot_pos = Coordinate(len(self.grid), l.index(ROBOT))
                self.grid.append(list(l))
            else:
                self.moves += list(l.strip())

    def __str__(self):
        s = f"Move {self.current_move_index}: before {self.moves[self.current_move_index]}\n"
        for l in self.grid:
            for c in l:
                s += c
            s += "\n"
        return s

    def _thing_at_coord(self, c: Coordinate) -> str:
        return self.grid[c.y][c.x]

    def _advance(self):
        next_direction = self.moves[self.current_move_index]
        next_pos = self.robot_pos.move(next_direction)
        logger.debug(f"Doing move {next_direction}. Next position to check {next_pos}")
        thing_in_next_pos = self._thing_at_coord(next_pos)
        if thing_in_next_pos is EMPTY:
            logger.debug(f"Next thing is empty. Simple move")
            self.grid[self.robot_pos.y][self.robot_pos.x] = EMPTY
            self.grid[next_pos.y][next_pos.x] = ROBOT
            self.robot_pos = next_pos
        elif thing_in_next_pos is BOX:
            logger.debug(f"Next thing is box. Complicated move")
            found_first = None
            adv_pos = next_pos
            while not found_first:
                adv_pos = adv_pos.move(next_direction)
                adv_thing = self._thing_at_coord(adv_pos)
                if adv_thing == WALL:
                    found_first = WALL
                elif adv_thing == EMPTY:
                    found_first = EMPTY

            if found_first == EMPTY:
                while adv_pos != next_pos:
                    rev_pos = adv_pos.reverse(next_direction)
                    self.grid[adv_pos.y][adv_pos.x] = self._thing_at_coord(rev_pos)
                    adv_pos = rev_pos
                self.grid[self.robot_pos.y][self.robot_pos.x] = EMPTY
                self.grid[next_pos.y][next_pos.x] = ROBOT
                self.robot_pos = next_pos
            # if we find a WALL first there is no where to go.
        else:
            logger.debug(f"Next thing is wall. No op")

        self.current_move_index += 1

    def _gps_score(self) -> int:
        score = 0
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j] == BOX:
                    score += 100 * i + j
        return score

    def star1(self) -> int:
        logger.debug(self)
        while self.current_move_index < len(self.moves) - 1:
            self._advance()
            logger.debug(self)

        return self._gps_score()


test_input1 = """########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<""".splitlines()
# test_puzzle1 = Day15Puzzle(test_input1)
# print(test_puzzle1.star1())
# expect 2028

test_input2 = """##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^""".splitlines()
# test_puzzle2 = Day15Puzzle(test_input2)
# print(test_puzzle2.star1())
# expect 10092

input = open("inputs/day15.txt").readlines()

puzzle = Day15Puzzle(input)
print(puzzle.star1())
