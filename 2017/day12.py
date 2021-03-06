
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


def find_n_group(n, connections_dict):
    n_group = set([n])
    for elem in list(connections_dict[n]):
        n_group = add_children_to_set(elem, n_group, connections_dict)

    return n_group


def find_size_zero_group(input_string):
    connections_dict = build_connections_dict(input_string)

    zero_group = find_n_group('0', connections_dict)

    return len(zero_group)


def find_num_groups(input_string):
    connections_dict = build_connections_dict(input_string)

    groups = []
    elems_in_groups = set()

    for elem in connections_dict.keys():
        if elem not in elems_in_groups:
            group_for_elem = find_n_group(elem, connections_dict)
            groups.append(group_for_elem)
            elems_in_groups = elems_in_groups.union(group_for_elem)

    return len(groups)

