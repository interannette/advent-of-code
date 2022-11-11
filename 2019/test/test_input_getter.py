from utils.input_getter import get_url_for_day, get_input_for_day


def test_get_url_for_1():
    assert get_url_for_day(1) == "https://adventofcode.com/2019/day/1/input"


def test_get_url_for_20():
    assert get_url_for_day(20) == "https://adventofcode.com/2019/day/20/input"


def test_get_input():
    input = get_input_for_day(1)
    assert input
