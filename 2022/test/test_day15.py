from day15 import SenorGrid, Position, Range

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


def test_safe_range_on_row():
    s = Position(0, 2)
    distance = 2
    assert SenorGrid.safe_range_for_point_on_row(s, distance, 1) == Range(
        start=-1, end=1
    )


def test_excluded():
    s = SenorGrid(SAMPLE_INPUT)
    assert 26 == len(s.calculate_excluded_space(10))


def test_frequency():
    s = SenorGrid(SAMPLE_INPUT)
    f = s.calculate_tuning_frequence(limit=20)
    assert f == 56000011
