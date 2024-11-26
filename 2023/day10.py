from dataclasses import dataclass
from enum import Enum
from math import floor
from typing import List, Tuple

sample = True

if sample:
    INPUT = \
        '''.....
        .S-7.
        .|.|.
        .L-J.
        .....'''.splitlines()
else:
    INPUT = open("inputs/day10.txt").readlines()
INPUT = [s.strip() for s in INPUT]


class Pipe(Enum):
    '''
    | is a vertical pipe connecting north and south.
- is a horizontal pipe connecting east and west.
L is a 90-degree bend connecting north and east.
J is a 90-degree bend connecting north and west.
7 is a 90-degree bend connecting south and west.
F is a 90-degree bend connecting south and east.
. is ground; there is no pipe in this tile.
    '''

    NS = 1
    EW = 2
    NE = 3
    NW = 4
    SW = 5
    SE = 6
    G = 7
    START = 8

    @staticmethod
    def parse(s: str) -> "Pipe":
        if s == '|':
            return Pipe.NS
        elif s == '-':
            return Pipe.EW
        elif s == 'L':
            return Pipe.NE
        elif s == '7':
            return Pipe.SW
        elif s == 'F':
            return Pipe.SE
        elif s == 'S':
            return Pipe.START
        else:
            return Pipe.G


@dataclass
class Coordinate:
    i: int
    j: int






@dataclass
class Grid:
    pipes: List[List[Pipe]]
    path: List[Coordinate]
    start: Coordinate

    def get_adjacent(self, c: Coordinate) -> List["Coordinate"]:
        adj = []

        i = c.i
        j = c.j
        p = self.pipes[i][j]

        if p == Pipe.G:
            return adj

        if p == Pipe.NS:
            if i > 0:
                adj.append(Coordinate[i-1, j])
            if i < len(self.pipes):
                adj.append(Coordinate[i + 1, j])
            return adj

        if p == Pipe.EW:
            return [Coordinate(i, j-1), Coordinate(i, j+1)]

        if p == Pipe.NE:
            return [Coordinate(i-1, j), Coordinate(i, j+1)]

        if p == Pipe.NW:
            return [Coordinate(i-1, j), Coordinate(i, j-1)]

        if p == Pipe.SW:
            return [Coordinate(i+1, j), Coordinate(i, j-1)]

        if p == Pipe.SE:
            return [Coordinate(i+1, j), Coordinate(i, j+1)]

        if p == Pipe.START:
            # check all
            for x in i_range:
                for y in j_range:
                    adj.append(Coordinate(x, y))

            return adj


        '''
        | is a vertical pipe connecting north and south.
    - is a horizontal pipe connecting east and west.
    L is a 90-degree bend connecting north and east.
    J is a 90-degree bend connecting north and west.
    7 is a 90-degree bend connecting south and west.
    F is a 90-degree bend connecting south and east.
    . is ground; there is no pipe in this tile.
        '''

    def _find_next_step(self) -> Coordinate:
        c = self.path[-1]
        adj = self.get_adjacent(c)

        # find which is back and which is forward
        previous = self.path[-2] if len(self.path) > 1 else None

        return next([a for a in adj if not a == previous])

    def find_loop(self):
        # find next
        next_step = self._find_next_step()
        while next_step != self.start:
            self.path.append(next_step)
            next_step = self._find_next_step()




def solve_part1():
    pipes = []
    s_loc = None
    for line in INPUT:
        r = [Pipe.parse(j) for j in line.split()]
        pipes.append(r)
        try:
            j = r.index(Pipe.START)
            s_loc = Coordinate(len(pipes) - 1, j)
        except ValueError:
            continue

    grid = Grid(pipes=pipes, path=[s_loc], start=s_loc)

    grid.find_loop()

    return floor(len(grid.path)/2)


print(solve_part1())





