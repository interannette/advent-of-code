def count_steps(maze):
    l = len(maze)
    i = 0
    count = 0
    while i < l:
        step = maze[i]
        maze[i] += 1
        i += step
        count += 1
    return count


def solve_maze(input_string):
    list_strings = input_string.split('\n')
    return count_steps(map(int, list_strings))

