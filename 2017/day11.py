# Reference https://www.redblobgames.com/grids/hexagons/

# Summary think of hex as a cube:
# Directions equal:
# N := deltaX = 0, deltaY = +1, deltaZ = -1
# NE := deltaX = +1, deltaY = 0, deltaZ = -1
# SE := deltaX = +1, deltaY = -1, deltaZ = 0
# S := deltaX = 0, deltaY = -1, deltaZ = 1
# SW := deltaX = -1, deltaY = 0, deltaZ = 1
# NW := deltaX = -1, deltaY = 1, deltaZ = 0
# Distance = max dist in anyone direction


def handle_direction(direction, (x,y,z)):

    if direction == 'n':
        y += 1
        z -= 1
    elif direction == 'ne':
        x += 1
        z -= 1
    elif direction == 'se':
        x += 1
        y -= 1
    elif direction == 's':
        y -= 1
        z += 1
    elif direction == 'sw':
        x -= 1
        z += 1
    elif direction == 'nw':
        x -= 1
        y += 1
    else:
        print("unknown direction")

    return x, y, z


def distance_at_coord(coord):
    return max(map(abs, coord))


def find_distance(input_string):
    direction_list = input_string.split(",")
    coord = (0, 0, 0)

    max_distance = 0

    for direction in direction_list:
        coord = handle_direction(direction, coord)
        current_distance = distance_at_coord(coord)
        if current_distance > max_distance:
            max_distance = current_distance

    print "Final distance", current_distance
    print "Max distance ", max_distance

find_distance('''''')


