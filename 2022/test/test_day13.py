from day13 import (
    is_correct_order,
    compute_sum_packets,
    convert_to_list,
    build_pairs,
    order_packets,
    find_decoder_key,
)


def test_example1():
    f = "[1,1,3,1,1]"
    s = "[1,1,5,1,1]"

    assert is_correct_order(convert_to_list(f), convert_to_list(s))


def test_example2():
    f = convert_to_list("[[1],[2,3,4]]")
    s = convert_to_list("[[1],4]")
    assert is_correct_order(f, s)


def test_example3():
    f = "[9]"
    s = "[[8,7,6]]"

    assert not is_correct_order(convert_to_list(f), convert_to_list(s))


def test_example4():
    f = "[[4,4],4,4]"
    s = "[[4,4],4,4,4]"
    assert is_correct_order(convert_to_list(f), convert_to_list(s))


def test_example5():
    f = "[7,7,7,7]"
    s = "[7,7,7]"
    assert not is_correct_order(convert_to_list(f), convert_to_list(s))


def test_example6():
    f = "[]"
    s = "[3]"
    assert is_correct_order(convert_to_list(f), convert_to_list(s))


def test_example7():
    f = convert_to_list("[[[]]]")
    s = convert_to_list("[[]]")
    assert not is_correct_order(f, s)


def test_example8():
    f = "[1,[2,[3,[4,[5,6,7]]]],8,9]"
    s = "[1,[2,[3,[4,[5,6,0]]]],8,9]"
    assert not is_correct_order(convert_to_list(f), convert_to_list(s))


def test_full_set():
    inputs = [
        "[1,1,3,1,1]",
        "[1,1,5,1,1]",
        "",
        "[[1],[2,3,4]]",
        "[[1],4]",
        "",
        "[9]",
        "[[8,7,6]]",
        "",
        "[[4,4],4,4]",
        "[[4,4],4,4,4]",
        "",
        "[7,7,7,7]",
        "[7,7,7]",
        "",
        "[]",
        "[3]",
        "",
        "[[[]]]",
        "[[]]",
        "",
        "[1,[2,[3,[4,[5,6,7]]]],8,9]",
        "[1,[2,[3,[4,[5,6,0]]]],8,9]",
    ]

    pairs = build_pairs(inputs)

    assert 8 == len(pairs)

    sum = compute_sum_packets(pairs)
    assert 13 == sum


def test_input_example():
    f = convert_to_list("[[],[0],[[]]]")
    s = convert_to_list("[[0],[[4]]]")

    assert is_correct_order(f, s)


def test_convert_to_list():
    s = "[[[1, 3, 10, [1, 7, 7, 10]], 9], []]"
    expected = [[[1, 3, 10, [1, 7, 7, 10]], 9], []]
    assert convert_to_list(s) == expected


def test_order_packets():
    inputs = [
        "[1,1,3,1,1]",
        "[1,1,5,1,1]",
        "",
        "[[1],[2,3,4]]",
        "[[1],4]",
        "",
        "[9]",
        "[[8,7,6]]",
        "",
        "[[4,4],4,4]",
        "[[4,4],4,4,4]",
        "",
        "[7,7,7,7]",
        "[7,7,7]",
        "",
        "[]",
        "[3]",
        "",
        "[[[]]]",
        "[[]]",
        "",
        "[1,[2,[3,[4,[5,6,7]]]],8,9]",
        "[1,[2,[3,[4,[5,6,0]]]],8,9]",
    ]

    expected = [
        [],
        [[]],
        [[[]]],
        [1, 1, 3, 1, 1],
        [1, 1, 5, 1, 1],
        [[1], [2, 3, 4]],
        [1, [2, [3, [4, [5, 6, 0]]]], 8, 9],
        [1, [2, [3, [4, [5, 6, 7]]]], 8, 9],
        [[1], 4],
        [[2]],
        [3],
        [[4, 4], 4, 4],
        [[4, 4], 4, 4, 4],
        [[6]],
        [7, 7, 7],
        [7, 7, 7, 7],
        [[8, 7, 6]],
        [9],
    ]
    actual = order_packets(inputs)
    assert expected == actual


def test_order_packets():
    inputs = [
        "[1,1,3,1,1]",
        "[1,1,5,1,1]",
        "",
        "[[1],[2,3,4]]",
        "[[1],4]",
        "",
        "[9]",
        "[[8,7,6]]",
        "",
        "[[4,4],4,4]",
        "[[4,4],4,4,4]",
        "",
        "[7,7,7,7]",
        "[7,7,7]",
        "",
        "[]",
        "[3]",
        "",
        "[[[]]]",
        "[[]]",
        "",
        "[1,[2,[3,[4,[5,6,7]]]],8,9]",
        "[1,[2,[3,[4,[5,6,0]]]],8,9]",
    ]
    assert find_decoder_key(inputs) == 140
