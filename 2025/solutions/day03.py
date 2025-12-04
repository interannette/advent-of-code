
class BatteryBank:
    batteries: list[int]
    max_joltage_star1: int | None
    max_joltage_star2: int | None

    def __init__(self, b:str):
        self.batteries = [int(i) for i in b]
        self.compute_max_joltage_star2()

    def compute_max_joltage_star1(self):
        max_battery = max(self.batteries[:-1])
        idx_max = self.batteries.index(max_battery)

        second_max = max(self.batteries[idx_max+1:])
        self.max_joltage_star1 = max_battery * 10 + second_max

    @staticmethod
    def recursive_star2(remaining_batteries: list[int], num_spots_to_fill: int)->list[int]:
        if num_spots_to_fill == len(remaining_batteries):
            return remaining_batteries
        elif num_spots_to_fill == 1:
            return [max(remaining_batteries)]
        else:
            num_to_add = max(remaining_batteries[:len(remaining_batteries) -num_spots_to_fill+1])
            idx = remaining_batteries.index(num_to_add)
            return [num_to_add,*BatteryBank.recursive_star2(remaining_batteries[idx+1:],num_spots_to_fill-1)]

    def compute_max_joltage_star2(self):
        seq = BatteryBank.recursive_star2(self.batteries, 12)
        self.max_joltage_star2 = int("".join([str(s) for s in seq]))


test_input = False
if test_input:
    input = """987654321111111
811111111111119
234234234234278
818181911112111""".splitlines()
else:
    input = open("../inputs/day03.txt").readlines()


bank = [BatteryBank(b.strip()) for b in input]
print(sum([b.max_joltage_star2 for b in bank]))