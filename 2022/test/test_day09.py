from day09 import (
    Position,
    compute_first_star,
    Bridge,
    Direction,
    Move,
    compute_second_star,
)


def test_execute_move():
    b = Bridge()
    b.execute_move(Move("R 4"))
    assert b.head == Position(4, 0)
    assert b.tail == Position(3, 0)
    assert b.head_history == [
        Position(0, 0),
        Position(1, 0),
        Position(2, 0),
        Position(3, 0),
    ]
    assert b.tail_history == [Position(0, 0), Position(1, 0), Position(2, 0)]

    b.execute_move(Move("U 4"))
    assert b.head == Position(4, 4)
    assert b.tail == Position(4, 3)
    assert b.head_history == [
        Position(0, 0),
        Position(1, 0),
        Position(2, 0),
        Position(3, 0),
        Position(4, 0),
        Position(4, 1),
        Position(4, 2),
        Position(4, 3),
    ]
    assert b.tail_history == [
        Position(0, 0),
        Position(1, 0),
        Position(2, 0),
        Position(3, 0),
        Position(4, 1),
        Position(4, 2),
    ]

    b.execute_move(Move("L 3"))
    assert b.head == Position(1, 4)
    assert b.tail == Position(2, 4)


def test_first_star_example():
    input = [
        "R 4",
        "U 4",
        "L 3",
        "D 1",
        "R 4",
        "D 1",
        "L 5",
        "R 2",
    ]
    assert 13 == compute_first_star(input)


def test_second_star_example1():
    input = [
        "R 4",
        "U 4",
        "L 3",
        "D 1",
        "R 4",
        "D 1",
        "L 5",
        "R 2",
    ]
    assert 1 == compute_second_star(input)


def test_second_star_example2():
    input = [
        "R 5",
        "U 8",
        "L 8",
        "D 3",
        "R 17",
        "D 10",
        "L 25",
        "U 20",
    ]
    assert 36 == compute_second_star(input)
