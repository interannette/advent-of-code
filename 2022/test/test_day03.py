from day03 import find_overlap, compute_priorities, find_badge, compute_badge_priorities


def test_overlap_line1():
    o = find_overlap("vJrwpWtwJgWrhcsFMMfFFhFp")
    assert o == "p"


def test_overlap_line2():
    o = find_overlap("jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL")
    assert o == "L"


def test_overlap_line3():
    o = find_overlap("PmmdzqPrVvPwwTWBwg")
    assert o == "P"


def test_overlap_line4():
    o = find_overlap("wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn")
    assert o == "v"


def test_overlap_line5():
    o = find_overlap("ttgJtRGJQctTZtZT")
    assert o == "t"


def test_overlap_line6():
    o = find_overlap("CrZsJsPPZsGzwwsLwLmpwMDw")
    assert o == "s"


def test_compute_priorities():
    inputs = "vJrwpWtwJgWrhcsFMMfFFhFp,jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL,PmmdzqPrVvPwwTWBwg,wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn,ttgJtRGJQctTZtZT,CrZsJsPPZsGzwwsLwLmpwMDw"
    assert 157 == compute_priorities(inputs.split(","))


def test_find_badge_example1():
    o = find_badge(
        "vJrwpWtwJgWrhcsFMMfFFhFp",
        "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
        "PmmdzqPrVvPwwTWBwg",
    )
    assert o == "r"


def test_find_badge_example2():
    o = find_badge(
        "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn", "ttgJtRGJQctTZtZT", "CrZsJsPPZsGzwwsLwLmpwMDw"
    )
    assert o == "Z"


def test_sum_badge_priorities():
    inputs = "vJrwpWtwJgWrhcsFMMfFFhFp,jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL,PmmdzqPrVvPwwTWBwg,wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn,ttgJtRGJQctTZtZT,CrZsJsPPZsGzwwsLwLmpwMDw"
    assert 70 == compute_badge_priorities(inputs.split(","))
