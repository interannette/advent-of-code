part_two = True


def transform_value(i):
    if part_two:
        if i >= 3:
            return i - 1
        else:
            return i + 1
    else:
        return i + 1


def count_steps(maze):
    l = len(maze)
    i = 0
    count = 0
    while i < l:
        step = maze[i]
        maze[i] = transform_value(maze[i])
        i += step
        count += 1
    return count


def solve_maze(input_string):
    list_strings = input_string.split('\n')
    return count_steps(map(int, list_strings))