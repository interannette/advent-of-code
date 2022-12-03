from day02 import (
    FirstStarRound,
    Outcome,
    Shape,
    sum_first_star_rounds,
    SecondStarRound,
    sum_second_star_rounds,
)


def test_parse_first_star_round():
    r = "A Y"
    o = FirstStarRound.parse(r)
    assert FirstStarRound(Shape.ROCK, Shape.PAPER) == o


def test_first_star_example_sum():
    input = [
        "A Y",
        "B X",
        "C Z",
    ]

    output = sum_first_star_rounds(input)
    assert 15 == output


def test_parse_second_star_round():
    r = "A Y"
    o = SecondStarRound.parse(r)
    assert SecondStarRound(Shape.ROCK, Outcome.DRAW) == o


def test_second_star_example_sum():
    input = [
        "A Y",
        "B X",
        "C Z",
    ]

    output = sum_second_star_rounds(input)
    assert 12 == output
