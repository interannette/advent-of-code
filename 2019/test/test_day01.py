from day01.day01 import calculate_fuel, calculate_fuel_including_fuel


def test_example1():
    assert calculate_fuel(12) == 2


def test_example2():

    assert calculate_fuel(14) == 2


def test_example3():
    assert calculate_fuel(1969) == 654


def test_example4():
    assert calculate_fuel(100756) == 33583


def test_star2_example1():
    assert calculate_fuel_including_fuel(14) == 2


def test_star2_example2():
    assert calculate_fuel_including_fuel(1969) == 966


def test_star2_example3():
    assert calculate_fuel_including_fuel(100756) == 50346
