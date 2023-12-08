from typing import Optional

sample = False
part_2 = True

if sample:
    if not part_2:
        races = [(7, 9), (15, 40), (30,200)]
    else:
        races = [(71530, 940200)]
else:
    if not part_2:
        races = [(40, 233), (82, 1011), (84, 1110), (92, 1487)]
    else:
        races = [(40828492, 233101111101487)]

# For each whole millisecond you spend at the beginning of the race holding down the button,
# the boat's speed increases by one millimeter per millisecond.


def compute_race_options(time: int, record_distance: int) -> Optional[int]:
    shortest = None
    for i in range(time):
        time_to_run = time - i
        speed = i
        distance = speed * time_to_run
        if distance > record_distance:
            shortest = i
            break

    if not shortest:
        return

    longest = None
    for i in range(time):
        time_to_charge = time - i
        distance = time_to_charge * i
        if distance > record_distance:
            longest = i

    print(f"shortest {shortest}. longest {longest}. total {longest-shortest}")
    return longest - shortest + 1


def solve() -> int:
    product = None
    for race in races:
        options = compute_race_options(race[0], race[1])
        if options:
            product = product * options if product else options

    return product


print(solve())

