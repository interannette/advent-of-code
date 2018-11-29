import re


def build_maps(input_string):
    parent_regex = re.compile("([a-z]*) \((\d*)\) -> ([a-z, ]*)")
    child_regex = re.compile("([a-z]*) \((\d*)\)")
    child_parent_map = {}
    parent_child_map = {}
    node_weight_map = {}
    for line in input_string.split("\n"):
        # padx (45) -> pbga, havc, qoyq
        re_result = parent_regex.match(line)
        if re_result:
            parent = re_result.group(1)
            weight = int(re_result.group(2))
            node_weight_map[parent] = weight

            child_string = re_result.group(3)
            child_list = child_string.split(", ")
            parent_child_map[parent] = child_list
            for child in child_list:
                child_parent_map[child] = parent

        else:
            re_result = child_regex.match(line)
            if re_result:
                node = re_result.group(1)
                weight = int(re_result.group(2))
                node_weight_map[node] = weight

    return child_parent_map, parent_child_map, node_weight_map


def find_root(child_parent_map):
    root = None
    current_parent = child_parent_map.items()[0][1]
    while not root:
        # getting the current parent's parent
        next_parent = child_parent_map.get(current_parent)
        if not next_parent:
            root = current_parent
        else:
            current_parent = next_parent
    return root


def balance_subtree(parent_child_edges, node_weights, start_node):
    balanced = True
    correction_weight = None
    subtree_weight = node_weights.get(start_node)

    child_list = parent_child_edges.get(start_node)
    weights = {}
    if child_list:
        for child in child_list:
            this_balanced, this_weight, this_correction_weight = balance_subtree(parent_child_edges, node_weights, child)
            if not this_balanced:
                return False, None, this_correction_weight
            else:
                subtree_weight += this_weight
                if weights.get(this_weight):
                    weights.get(this_weight).append(child)
                else:
                    weights[this_weight] = [child]

    if len(weights.keys()) > 1:
        balanced = False
        subtree_weight = None  # Once we've found the correction, don't worry about subtree weights
        # Find correction weight
        common_weight = 0
        unique_weight = 0
        for weight, nodes in weights.items():
            if len(nodes) > 1:
                common_weight = weight
            else:
                unique_weight = weight

        weight_diff = common_weight - unique_weight
        correction_weight = node_weights[weights.get(unique_weight)[0]] + weight_diff

    return balanced, subtree_weight, correction_weight


def solve(input_tree):
    child_parent_edges, parent_child_edges, node_weight = build_maps(input_tree)
    root = find_root(child_parent_edges)
    balanced, subtree_weight, correction_weight = balance_subtree(parent_child_edges, node_weight, root)
    return correction_weight