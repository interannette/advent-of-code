from collections import defaultdict
from day14 import Cave


def test_init_cave():
    input = ["498,4 -> 498,6 -> 496,6", "503,4 -> 502,4 -> 502,9 -> 494,9"]
    expected_rocks = [
        (494, 9),
        (495, 9),
        (496, 9),
        (496, 6),
        (497, 9),
        (497, 6),
        (498, 9),
        (498, 6),
        (498, 5),
        (498, 4),
        (499, 9),
        (500, 9),
        (501, 9),
        (502, 9),
        (502, 8),
        (502, 7),
        (502, 6),
        (502, 5),
        (502, 4),
        (503, 4),
    ]

    c = Cave(input)

    for (x, y) in expected_rocks:
        assert c.rocks[x][y]
    assert len(set([x for (x, y) in expected_rocks])) == len(c.rocks)
    assert c.max_y == 9


def test_cave_first_sand():
    input = ["498,4 -> 498,6 -> 496,6", "503,4 -> 502,4 -> 502,9 -> 494,9"]

    c = Cave(input)

    assert c.add_sand()
    assert c.sand[500][8]


def test_cave_fill_sand():
    input = ["498,4 -> 498,6 -> 496,6", "503,4 -> 502,4 -> 502,9 -> 494,9"]

    c = Cave(input)

    c.fill_sand()

    assert c.count_sand() == 24


def test_stop_with_floor():
    input = ["498,4 -> 498,6 -> 496,6", "503,4 -> 502,4 -> 502,9 -> 494,9"]

    c = Cave(input)
    c.rocks[499][1] = True
    c.rocks[500][1] = True
    c.rocks[501][1] = True

    r = c.add_sand(with_floor=True)
    assert not r


def test_cave_fill_sand_with_floor():
    input = ["498,4 -> 498,6 -> 496,6", "503,4 -> 502,4 -> 502,9 -> 494,9"]

    c = Cave(input)

    c.fill_sand(with_floor=True)

    assert c.count_sand() == 93
