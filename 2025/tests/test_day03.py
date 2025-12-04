from solutions.day03 import BatteryBank


import unittest

class TestDay03Star2(unittest.TestCase):
    def test_line_1(self):
        b = BatteryBank("987654321111111")
        b.compute_max_joltage_star2()
        assert b.max_joltage_star2 == 987654321111

    def test_line_2(self):
        b = BatteryBank("811111111111119")
        b.compute_max_joltage_star2()
        assert b.max_joltage_star2 == 811111111119

    def test_line_3(self):
        b = BatteryBank("234234234234278")
        b.compute_max_joltage_star2()
        assert b.max_joltage_star2 == 434234234278

    def test_line_4(self):
        b = BatteryBank("818181911112111")
        b.compute_max_joltage_star2()
        assert b.max_joltage_star2 == 888911112111