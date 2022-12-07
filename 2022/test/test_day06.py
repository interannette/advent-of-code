from day06 import find_marker, find_message


def test_example():
    assert 7 == find_marker("mjqjpqmgbljsphdztnvjfqwrcgsmlb")


def test_example1():
    assert 5 == find_marker("bvwbjplbgvbhsrlpgdmjqwftvncz")


def test_example2():
    assert 6 == find_marker("nppdvjthqldpwncqszvftbrmjlhg")


def test_example3():
    assert 10 == find_marker("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg")


def test_example4():
    assert 11 == find_marker("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw")


def test_message_example():
    assert 19 == find_message("mjqjpqmgbljsphdztnvjfqwrcgsmlb")


def test_message_example1():
    assert 23 == find_message("bvwbjplbgvbhsrlpgdmjqwftvncz")


def test_message_example2():
    assert 23 == find_message("nppdvjthqldpwncqszvftbrmjlhg")


def test_message_example3():
    assert 29 == find_message("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg")


def test_message_example4():
    assert 26 == find_message("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw")
