import math


class Day06Puzzle:
    values:list[int]

    def __init__(self, input_lines: list[str]):
        values = []
        operations = []
        input_lines.reverse() # start with the operation
        for line in input_lines:
            if len(operations) == 0:
                operations = [o.strip() for o in line.split()]
                continue

            if len(values) == 0:
                values = [int(v.strip()) for v in line.split()]
                continue

            next_values = [int(v.strip()) for v in line.split()]
            for i in range(len(operations)):
                operation = operations[i]
                if operation == '*':
                    values[i] = values[i] * next_values[i]
                else:
                    values[i] = values[i] + next_values[i]

        self.values = values


    def star1(self) -> int:
        return sum(self.values)


class Day06Star2Puzzle:
    problems:list[list[str]]
    operations = list[str]

    @staticmethod
    def compute_dividing_indexes(operations_line:list[str])->tuple[list[int], list[str]]:
        indexes = []
        operations = []
        for i in range(len(operations_line)):
            c = operations_line[i]
            if c in {'*','+'}:
                indexes.append(i)
                operations.append(c)
        return indexes,operations


    @staticmethod
    def compute_problems(dividing_indexes:list[int], char_grid: list[list[str]]) -> list[list[str]]:
        problems = []
        previous_index = 0
        for i in dividing_indexes[1:]:
            problem = []
            for line in char_grid[:-1]:
                problem.append(line[previous_index:i-1])
            previous_index = i
            problems.append(problem)

        problem = []
        for line in char_grid[:-1]:
            problem.append(line[previous_index:])
        problems.append(problem)
        return problems

    def __init__(self, input_lines: list[str]):
        char_grid = []
        for line in input_lines:
            grid_line = []
            for c in line.rstrip("\n"):
                grid_line.append(c)
            char_grid.append(grid_line)

        dividing_indexes, operations = Day06Star2Puzzle.compute_dividing_indexes(char_grid[-1])

        self.problems = Day06Star2Puzzle.compute_problems(dividing_indexes,char_grid)
        self.operations = operations



    def solve_problem(self, problem_values: list[str], operation: str)-> int:
        num_values = []

        print(f"solving {problem_values}. op:{operation}")
        for i in range(len(problem_values[0])):
            s = ''
            for p in problem_values:
                s += p[i]
            num_values.append(int(s.strip()))

        if operation == '*':
            return math.prod(num_values)
        else:
            return sum(num_values)

    def star2(self) -> int:
        total = 0
        for i in range(len(self.operations)):
            total += self.solve_problem(self.problems[i], self.operations[i])

        return total


use_test_input = False
if use_test_input:
    input = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """.splitlines()
else:
    input = open("solutions/inputs/day06.txt").readlines()

puzzle = Day06Star2Puzzle(input)
#print(f"Test input: {use_test_input}. Star 1 result {puzzle.star1()}")
print(f"Test input: {use_test_input}. Star 2 result {puzzle.star2()}")
