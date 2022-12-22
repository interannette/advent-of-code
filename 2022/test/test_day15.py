from day15 import SenorGrid, Position

SAMPLE_INPUT = [
    "Sensor at x=2, y=18: closest beacon is at x=-2, y=15",
    "Sensor at x=9, y=16: closest beacon is at x=10, y=16",
    "Sensor at x=13, y=2: closest beacon is at x=15, y=3",
    "Sensor at x=12, y=14: closest beacon is at x=10, y=16",
    "Sensor at x=10, y=20: closest beacon is at x=10, y=16",
    "Sensor at x=14, y=17: closest beacon is at x=10, y=16",
    "Sensor at x=8, y=7: closest beacon is at x=2, y=10",
    "Sensor at x=2, y=0: closest beacon is at x=2, y=10",
    "Sensor at x=0, y=11: closest beacon is at x=2, y=10",
    "Sensor at x=20, y=14: closest beacon is at x=25, y=17",
    "Sensor at x=17, y=20: closest beacon is at x=21, y=22",
    "Sensor at x=16, y=7: closest beacon is at x=15, y=3",
    "Sensor at x=14, y=3: closest beacon is at x=15, y=3",
    "Sensor at x=20, y=1: closest beacon is at x=15, y=3",
]


def test_init():
    s = SenorGrid(SAMPLE_INPUT)

    expected_sensors = [
        (2, 18),
        (9, 16),
        (13, 2),
        (12, 14),
        (10, 20),
        (14, 17),
        (8, 7),
        (2, 0),
        (0, 11),
        (20, 14),
        (17, 20),
        (16, 7),
        (14, 3),
        (20, 1),
    ]

    expected_beacons = [
        (-2, 15),
        (10, 16),
        (15, 3),
        (10, 16),
        (10, 16),
        (10, 16),
        (2, 10),
        (2, 10),
        (2, 10),
        (25, 17),
        (21, 22),
        (15, 3),
        (15, 3),
        (15, 3),
    ]
    assert s
    for sensor in expected_sensors:
        assert Position(sensor[0], sensor[1]) in s.sensors
    for beacon in expected_beacons:
        assert Position(beacon[0], beacon[1]) in s.detected_beacons


def test_safe_range():
    s = Position(0, 2)
    distance = 2
    expected_range = set(
        [
            Position(0, 0),
            Position(0, 1),
            Position(0, 2),
            Position(0, 3),
            Position(0, 4),
            Position(1, 1),
            Position(1, 2),
            Position(1, 3),
            Position(2, 2),
            Position(-1, 1),
            Position(-1, 3),
            Position(-1, 2),
            Position(-2, 2),
        ]
    )

    computed_range = SenorGrid.safe_range_for_point(s, distance)
    for c in computed_range:
        d = abs(s.x - c.x) + abs(s.y - c.y)
        assert d <= distance
    assert computed_range == expected_range


def test_excluded():
    s = SenorGrid(SAMPLE_INPUT)
    s.calculate_excluded_space()

    assert s

    row = [p.x for p in s.excluded_space if p.y == 10]
    assert 26 == len(row)
