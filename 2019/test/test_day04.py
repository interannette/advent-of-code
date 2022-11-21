from day04 import meets_first_requirements, digits_list, meets_second_requirements


def test_digits_list_example1():
    assert [1, 1, 1, 1, 1, 1] == digits_list(111111)


def test_digits_list_example2():
    assert [2, 2, 3, 4, 5, 0] == digits_list(223450)


def test_digits_list_example3():
    assert [1, 2, 3, 7, 8, 9] == digits_list(123789)


def test_example1():
    assert meets_first_requirements(111111)


def test_example2():
    assert not meets_first_requirements(223450)


def test_example3():
    assert not meets_first_requirements(123789)


def test_second_example1():
    assert meets_second_requirements(112233)


def test_second_example2():
    assert not meets_second_requirements(123444)


def test_second_example3():
    assert meets_second_requirements(111122)
