from day01 import Elf, build_elves, find_max_elf, find_top_three_elves


def test_parse_elves():
    input = [
        "1000",
        "2000",
        "3000",
        "",
        "4000",
        "",
        "5000",
        "6000",
        "",
        "7000",
        "8000",
        "9000",
        "",
        "10000",
    ]

    expected_output = [
        Elf(1, 6000),
        Elf(2, 4000),
        Elf(3, 11000),
        Elf(4, 24000),
        Elf(5, 10000),
    ]

    actual_output = build_elves(input)
    assert expected_output == actual_output


def test_find_max_elf():
    input = [
        "1000",
        "2000",
        "3000",
        "",
        "4000",
        "",
        "5000",
        "6000",
        "",
        "7000",
        "8000",
        "9000",
        "",
        "10000",
    ]
    found_max = find_max_elf(input)
    assert Elf(4, 24000) == found_max


def test_find_top_three_elves():
    input = [
        "1000",
        "2000",
        "3000",
        "",
        "4000",
        "",
        "5000",
        "6000",
        "",
        "7000",
        "8000",
        "9000",
        "",
        "10000",
    ]
    top_three = find_top_three_elves(input)
    assert [Elf(4, 24000), Elf(3, 11000), Elf(5, 10000)] == top_three
