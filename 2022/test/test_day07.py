from day07 import (
    parse_file_system,
    calculate_sizes,
    sum_small_directories,
    find_smallest_dir,
)


def test_sample():
    input = [
        "$ cd /",
        "$ ls",
        "dir a",
        "14848514 b.txt",
        "8504156 c.dat",
        "dir d",
        "$ cd a",
        "$ ls",
        "dir e",
        "29116 f",
        "2557 g",
        "62596 h.lst",
        "$ cd e",
        "$ ls",
        "584 i",
        "$ cd ..",
        "$ cd ..",
        "$ cd d",
        "$ ls",
        "4060174 j",
        "8033020 d.log",
        "5626152 d.ext",
        "7214296 k",
    ]
    root = parse_file_system(input)
    calculate_sizes(root)
    assert 48381165 == root.size

    sum = sum_small_directories(root, 100000)
    assert 95437 == sum

    current_free = 70000000 - root.size
    needed = 30000000 - current_free

    assert 24933642 == find_smallest_dir(root, needed)
