from dataclasses import dataclass
from typing import List
import re

# INPUT = \
#     '''Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
#     Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
#     Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
#     Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
#     Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'''.splitlines()
INPUT = open("inputs/day02.txt").readlines()


@dataclass
class Draw:
    blue: int
    red: int
    green: int

    @staticmethod
    def get_digit(s: str) -> int:
        m = re.match('\\d+', s.strip())
        if m:
            return int(m.group(0))
        else:
            return -1

    @staticmethod
    def parse(s: str) -> "Draw":
        parts = s.split(',')
        b, r, g = 0, 0, 0
        for p in parts:
            d = Draw.get_digit(p)
            if 'blue' in p:
                b = d
            elif 'red' in p:
                r = d
            else:
                g = d
        return Draw(b, r, g)


@dataclass
class Game:
    id: int
    draws: List[Draw]

    @staticmethod
    def parse(s: str) -> "Game":
        m = re.match('Game (\\d+): (.*)', s)
        if not m:
            raise ValueError(f"Invalid game line. {s}")

        game_id = int(m.group(1))

        draws = [Draw.parse(d) for d in m.group(2).split(';')]

        return Game(game_id, draws)

    def max_possible_draw(self) -> Draw:
        max_red = max([d.red for d in self.draws])
        max_blue = max([d.blue for d in self.draws])
        max_green = max([d.green for d in self.draws])
        return Draw(blue=max_blue, red=max_red, green=max_green)


def parse_games() -> List[Game]:
    games = []
    for line in INPUT:
        line = line.strip()
        if line:
            games.append(Game.parse(line))
    return games


def solve_part1():
    games = parse_games()
    total = 0
    for g in games:
        d = g.max_possible_draw()
        #12 red cubes, 13 green cubes, and 14 blue cubes
        if d.red > 12:
            continue
        elif d.green > 13:
            continue
        elif d.blue > 14:
            continue
        else:
            print(f"game {g.id} is possible")
            total = total + g.id
    return total


def solve_part2():
    games = parse_games()
    total = 0
    for g in games:
        d = g.max_possible_draw()
        total = total + (d.red * d.blue * d.green)
    return total


print(solve_part2())
