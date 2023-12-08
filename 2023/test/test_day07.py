from day07 import Part2Card, part2_parse_hand, part2_find_type, Type


def test_sort_part2():
    assert Part2Card.J < Part2Card.ONE
    assert Part2Card.ONE < Part2Card.A
    assert [Part2Card.ONE, Part2Card.J] < [Part2Card.ONE, Part2Card.ONE]


def test_type_part2():
    h = part2_parse_hand('JKTKK')
    t = part2_find_type(h)
    assert Type.FOUR_OF_A_KIND == t

    h = part2_parse_hand('8JT83')
    t = part2_find_type(h)
    assert Type.THREE_OF_A_KIND == t

    h = part2_parse_hand('7KJJK')
    t = part2_find_type(h)
    assert Type.FOUR_OF_A_KIND == t

    h = part2_parse_hand('JTTKK')
    t = part2_find_type(h)
    assert Type.FULL_HOUSE == t