def find_layer(i):
    l = 0
    while (2*l+1)**2 < i:
        l += 1

    return l


def start_num_of_layer(l):
    return (2*(l-1)+1)**2 + 1


def length_of_side(l):
    return 2*l + 1

# In layer l the square looks like:
# (-l,l) ... (l,l)
#   .           .
#   .           .
#   .           .
# (-l,-l) ... (l,-1)
# We find the position of the provided value by finding which side of the square the
# value is on, then using the diagram to compute the position.
def find_pos(i):
    layer = find_layer(i)
    print layer
    top_right_corner = start_num_of_layer(layer) + (length_of_side(layer)-1) - 1
    top_left_corner = top_right_corner + length_of_side(layer) - 1
    bottom_left_corner = top_left_corner + length_of_side(layer) - 1

    # right side of square
    if i <= top_right_corner:
        print "right side"
        x = layer
        y = -layer+1+i-start_num_of_layer(layer)
    # top side of square
    elif i <= top_left_corner:
        print "top"
        y = layer
        x = layer - (i - top_right_corner)
    # left side of square
    elif i <= bottom_left_corner:
        print "left side"
        x = -layer
        y = layer - (i - top_left_corner)
    # bottom side of square
    else:
        print "bottom"
        y = -layer
        x = -layer + (i - bottom_left_corner)

    return x, y


def find_dist(i):
    (x, y) = find_pos(i)
    return abs(x) + abs(y)
