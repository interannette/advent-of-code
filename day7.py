import re


def build_edge_map(input_string):
    regex = re.compile("([a-z]*) \(\d*\) -> ([a-z, ]*)")
    child_parent_map = {}
    for line in input_string.split("\n"):
        # padx (45) -> pbga, havc, qoyq
        re_result = regex.match(line)
        if re_result:
            parent = re_result.group(1)
            child_string = re_result.group(2)
            for child in child_string.split(", "):
                child_parent_map[child] = parent

    return child_parent_map


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

child_parent_edges = build_edge_map('''''')
print find_root(child_parent_edges)
