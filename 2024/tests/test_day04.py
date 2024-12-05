from day04 import Day04Star1Puzzle


def test_count_instances():
    assert 1 == Day04Star1Puzzle._count_instances_for_string("XMAS")
    assert 1 == Day04Star1Puzzle._count_instances_for_string("SAMX")
    assert 2 == Day04Star1Puzzle._count_instances_for_string("XMASXXMAS")
    assert 2 == Day04Star1Puzzle._count_instances_for_string("XMASXSSAMX")
