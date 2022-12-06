from day04 import Range, sum_contains


def test_parse():
    output = Range.parse("4-6")
    assert output == Range(4, 6)


def test_contains_true():
    assert Range(2, 8).contains(Range(3, 7))


def test_contains_false():
    assert not Range(5, 7).contains(Range(7, 9))


def test_sum_contians():
    inputs = ["2-4,6-8", "2-3,4-5", "5-7,7-9", "2-8,3-7", "6-6,4-6", "2-6,4-8"]
    output = sum_contains(inputs)
    assert 2 == output
