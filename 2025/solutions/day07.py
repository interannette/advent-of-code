from collections.abc import Iterable


class Day07Puzzle:
    grid: list[list[str]]
    active_row: int
    num_splits: int
    beams: list[int]
    timeline_results: dict[tuple[int, int], int]

    def __init__(self, input_lines: Iterable[str]):
        grid = []
        start_pos = -1
        for line in input_lines:
            if start_pos == -1:
                start_pos = line.index("S")
            grid.append([c for c in line.strip()])

        self.grid = grid
        self.active_row = 0
        self.num_splits = 0
        self.beams = [start_pos]
        self.timeline_results = {}
        return

    def advance(self) -> None:
        current_row = self.grid[self.active_row]
        next_row = self.grid[self.active_row + 1]

        new_beams = []
        for beam_index in self.beams:
            next_spot = next_row[beam_index]
            if next_spot == '.':
                current_row[beam_index] = '|'
                next_row[beam_index] = 'S'
                new_beams.append(beam_index)
            elif next_spot == 'S':
                current_row[beam_index] = '|'
            elif next_spot == '^':
                if beam_index - 1 >= 0:
                    next_row[beam_index - 1] = 'S'
                    new_beams.append(beam_index - 1)
                if beam_index + 1 < len(next_row):
                    next_row[beam_index + 1] = 'S'
                    new_beams.append(beam_index + 1)
                current_row[beam_index] = '|'
                self.num_splits += 1
            elif next_spot == '|':
                raise Exception("should be |")

        self.grid[self.active_row] = current_row
        self.grid[self.active_row + 1] = next_row
        self.beams = new_beams
        self.active_row += 1
        return

    def star1(self) -> int:
        while self.active_row < len(self.grid) - 1:
            self.advance()
        return self.num_splits

    def quantum_advance(self, current_pos: tuple[int, int]) -> int:
        if current_pos in self.timeline_results:
            return self.timeline_results.get(current_pos)

        if current_pos[0] + 1 > len(self.grid) - 1:
            self.timeline_results[current_pos] = 1
            return 1
        next_char = self.grid[current_pos[0] + 1][current_pos[1]]
        if next_char == '.':
            result = self.quantum_advance((current_pos[0] + 1, current_pos[1]))
            self.timeline_results[current_pos] = result
            return result
        elif next_char == '^':
            left_timelines = 0
            if current_pos[1] - 1 >= 0:
                left_timelines = self.quantum_advance((current_pos[0] + 1, current_pos[1] - 1))

            right_timelines = 0
            if current_pos[1] + 1 < len(self.grid[0]):
                right_timelines = self.quantum_advance((current_pos[0] + 1, current_pos[1] + 1))
            results = left_timelines + right_timelines
            self.timeline_results[current_pos] = results
            return results
        else:
            raise Exception("unexpected char")

    def star2(self) -> int:
        return self.quantum_advance((0, self.beams[0]))


use_test_input = False
if use_test_input:
    input = """.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............""".splitlines()
else:
    input = open("solutions/inputs/day07.txt").readlines()

puzzle = Day07Puzzle(input)
# print(f"Test input: {use_test_input}. Star 1 result {puzzle.star1()}")
print(f"Test input: {use_test_input}. Star 2 result {puzzle.star2()}")
