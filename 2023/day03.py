from typing import List

sample = False

if sample:
    INPUT = \
        '''467..114..
        ...*......
        ..35..633.
        ......#...
        617*......
        .....+.58.
        ..592.....
        ......755.
        ...$.*....
        .664.598..'''.splitlines()
else:
    INPUT = open("inputs/day03.txt").readlines()
INPUT = [s.strip() for s in INPUT]


# region: part 1
def is_symbol(s: str) -> bool:
    return not s.isdigit() and s != '.'


def is_part_number(row: int, start: int, end: int) -> bool:
    left = max(0, start - 1)
    right = end if end == len(INPUT[row]) - 1 else end + 1

    adj = False
    print(f"checking row {row}. ({start},{end})")
    # previous row
    if row - 1 >= 0:
        for k in range(left, right + 1):
            if is_symbol(INPUT[row - 1][k]):
                adj = True
                break

    # this row
    if not adj:
        if is_symbol(INPUT[row][left]):
            adj = True
        elif is_symbol(INPUT[row][right]):
            adj = True

            # next row
    if not adj and row + 1 < len(INPUT):
        for k in range(left, right + 1):
            if is_symbol(INPUT[row + 1][k]):
                adj = True
                break

    return adj


def solve_part1() -> int:
    part_numbers = []
    for i in range(len(INPUT)):
        current_start = None
        current_end = None
        current = ''
        for j in range(len(INPUT[i])):
            if INPUT[i][j].isdigit():
                if current_start is None:
                    current_start = j
                current = current + INPUT[i][j]
                current_end = j
            else:
                if current_end == j-1:
                    if is_part_number(i, current_start, current_end):
                        part_numbers.append(current)

                    # either way, reset
                    current = ''
                    current_start = None
                    current_end = None

        if current:
            if is_part_number(i, current_start, current_end):
                part_numbers.append(current)

    print(part_numbers)
    return sum([int(i) for i in part_numbers])
# endregion: part 1


def find_numbers_in_row(row: int, j: int) -> List[int]:
    nums = []
    # center is digit expand out
    if INPUT[row][j].isdigit():
        left = j
        right = j + 1

        for k in range(j - 1, 0, -1):
            if not INPUT[row][k].isdigit():
                left = k + 1
                break
        for k in range(j + 1, len(INPUT[row])):
            if not INPUT[row][k].isdigit():
                right = k
                break
        nums.append(int(INPUT[row][left:right]))

    else:  # center is not digit, check left and right independently
        # left
        if INPUT[row][j - 1].isdigit():
            left = 0
            for k in range(j - 1, 0, -1):
                if not INPUT[row][k].isdigit():
                    left = k + 1
                    break
            nums.append(int(INPUT[row][left:j]))

        # right
        if INPUT[row][j + 1].isdigit():
            right = len(INPUT)
            for k in range(j + 1, len(INPUT[row])):
                if not INPUT[row][k].isdigit():
                    right = k
                    break
            nums.append(int(INPUT[row][j + 1:right]))

    return nums


def find_adjacent_numbers(i: int, j: int) -> List[int]:
    adj_num = []
    # above
    if i-1 >= 0:
        for num in find_numbers_in_row(i-1, j):
            adj_num.append(num)

    # same row
    for num in find_numbers_in_row(i, j):
        adj_num.append(num)

    # below
    if i+1 < len(INPUT):
        for num in find_numbers_in_row(i+1, j):
            adj_num.append(num)

    return adj_num


def check_gear(i: int, j: int) -> (bool, int):
    adj_nums = find_adjacent_numbers(i, j)
    if len(adj_nums) == 2:
        print(f"adding ({i},{j}) with nums {adj_nums[0]}, {adj_nums[1]}")
        return True, adj_nums[0] * adj_nums[1]
    else:
        print(f"skipping ({i},{j})")
        return False, -1


def solve_part2() -> int:
    gear_ratios = []
    for i in range(len(INPUT)):
        for j in range(len(INPUT[i])):
            if INPUT[i][j] == '*':
                is_gear, gear_ratio = check_gear(i, j)
                if is_gear:
                    gear_ratios.append(gear_ratio)
    return sum(gear_ratios)


# 71998335, too low
print(solve_part2())
