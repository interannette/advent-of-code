def find_max_index_and_value(mem_blocks):
    max_index = 0
    max_value = mem_blocks[0]
    for i in range(len(mem_blocks)):
        if mem_blocks[i] > max_value:
            max_index = i
            max_value = mem_blocks[i]
    return max_index, max_value


def build_next_state(mem_blocks):
    index, value = find_max_index_and_value(mem_blocks)
    next_state = list(mem_blocks)

    next_state[index] = 0
    l = len(next_state)

    while value > 0:
        next_index = (index + 1) % l
        next_state[next_index] += 1
        index = next_index
        value -= 1

    return next_state


def state_in_list(state, list_of_states):
    for i in range(len(list_of_states)):
        if state == list_of_states[i]:
            return i

    return -1


def find_cycle(start_state_as_string):

    start_state = map(int, start_state_as_string.split("\t"))

    states = list()
    current_state = start_state
    while state_in_list(current_state, states) < 0:
        states.append(current_state)
        current_state = build_next_state(current_state)

    return len(states), len(states) - state_in_list(current_state, states)