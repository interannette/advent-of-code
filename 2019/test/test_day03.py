from day03 import build_path, Coordinate, solve_intersection, parse_path


def test_build_path():
    first_str = "R8,U5,L5,D3"
    path = build_path(first_str.split(","))
    assert Coordinate(0, 0) in path.keys()
    assert Coordinate(3, 2) in path.keys()


def test_build_path():
    first_str = "R8,U5,L5,D3"
    path = parse_path(first_str)
    assert Coordinate(0, 0) in path
    assert Coordinate(3, 2) in path


def test_solve_intersection_example1():
    first_str = "R8,U5,L5,D3"
    second_str = "U7,R6,D4,L4"
    distance = solve_intersection(first_str, second_str, False)
    assert distance == 6


def test_solve_intersection_example2():
    first_str = "R75,D30,R83,U83,L12,D49,R71,U7,L72"
    second_str = "U62,R66,U55,R34,D71,R55,D58,R83"
    distance = solve_intersection(first_str, second_str, False)
    assert distance == 159


def test_solve_intersection_example3():
    first_str = "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51"
    second_str = "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"
    distance = solve_intersection(first_str, second_str, False)
    assert distance == 135


def test_solve_intersection_step_example1():
    first_str = "R8,U5,L5,D3"
    second_str = "U7,R6,D4,L4"
    distance = solve_intersection(first_str, second_str, True)
    assert distance == 30


def test_solve_intersection_step_example2():
    first_str = "R75,D30,R83,U83,L12,D49,R71,U7,L72"
    second_str = "U62,R66,U55,R34,D71,R55,D58,R83"
    distance = solve_intersection(first_str, second_str, True)
    assert distance == 610


def test_solve_intersection_step_example3():
    first_str = "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51"
    second_str = "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"
    distance = solve_intersection(first_str, second_str, True)
    assert distance == 410
