from dataclasses import dataclass
from enum import Enum
from typing import List
import re
from utils.input_getter import get_input_for_day


class NodeType(Enum):
    FILE = 0
    DIR = 1


@dataclass
class Node:
    type: NodeType
    size: int
    name: str
    parent: "Node"
    children: List["Node"]


def parse_file_system(input: List[str]) -> Node:
    root = Node(NodeType.DIR, 0, "/", None, [])
    current_node = root

    for line in input:
        if "$ cd" in line:
            m = re.search("^\$ cd (\S*)$", line)
            if m:
                if m.group(1) == "/":
                    current_node = root
                elif m.group(1) == "..":
                    current_node = current_node.parent
                else:
                    current_node = next(
                        child
                        for child in current_node.children
                        if child.name == m.group(1)
                    )
        elif "$ ls" in line:
            continue
        elif "dir" in line:
            m = re.search("^dir (\S*)$", line)
            if m:
                child = Node(NodeType.DIR, 0, m.group(1), current_node, [])
                current_node.children.append(child)
        else:
            m = re.search("^(\d*) (\S*)$", line)
            if m:
                file = Node(
                    NodeType.FILE, int(m.group(1)), m.group(2), current_node, None
                )
                current_node.children.append(file)

    return root


def calculate_sizes(root: Node):
    for child in root.children:
        if child.type == NodeType.DIR:
            calculate_sizes(child)
            root.size += child.size
        else:
            root.size += child.size


def sum_small_directories(root: Node, limit: int) -> int:
    sum = 0
    for child in root.children:
        if child.type == NodeType.DIR:
            if child.size < limit:
                sum += child.size
            sum += sum_small_directories(child, limit)
    return sum


def find_smallest_dir(root: Node, needed_size: int) -> int:
    smallest = None
    for child in root.children:
        if child.type == NodeType.DIR:
            if child.size >= needed_size:
                if smallest is None:
                    smallest = child.size
                elif child.size < smallest:
                    smallest = child.size
            this_smallest = find_smallest_dir(child, needed_size)
            if this_smallest is not None:
                if smallest is None:
                    smallest = this_smallest
                elif this_smallest < smallest:
                    smallest = this_smallest
    return smallest


def first_star():
    input = get_input_for_day()
    root = parse_file_system(input)
    calculate_sizes(root)
    print(sum_small_directories(root, 100000))


def second_star():
    input = get_input_for_day()
    root = parse_file_system(input)
    calculate_sizes(root)

    current_free = 70000000 - root.size
    needed = 30000000 - current_free

    print(find_smallest_dir(root, needed))


if __name__ == "__main__":
    second_star()
