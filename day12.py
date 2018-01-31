
def build_connections_dict(input_string):
    lines = input_string.split("\n")
    connections_dict = {}
    for line in lines:
        [lhs, rhs] = line.split(" <-> ")
        # assuming each row has unique lhs
        connections = rhs.split(", ")
        connections_dict[lhs] = set(connections)

    return connections_dict


def add_children_to_set(elem, zero_group, connections_dict):

    if elem in zero_group:
        return zero_group
    else:
        zero_group.add(elem)

    children_of_elem = connections_dict[elem]
    for child in children_of_elem:
        zero_group = add_children_to_set(child, zero_group, connections_dict)

    return zero_group


def find_zero_group(input_string):
    connections_dict = build_connections_dict(input_string)

    zero_group = set(['0'])

    for elem in list(connections_dict['0']):
        zero_group = add_children_to_set(elem, zero_group, connections_dict)

    return len(zero_group)
