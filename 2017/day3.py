import numpy as np

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
    top_right_corner = start_num_of_layer(layer) + (length_of_side(layer)-1) - 1
    top_left_corner = top_right_corner + length_of_side(layer) - 1
    bottom_left_corner = top_left_corner + length_of_side(layer) - 1

    # right side of square
    if i <= top_right_corner:
        x = layer
        y = -layer+1+i-start_num_of_layer(layer)
    # top side of square
    elif i <= top_left_corner:
        y = layer
        x = layer - (i - top_right_corner)
    # left side of square
    elif i <= bottom_left_corner:
        x = -layer
        y = layer - (i - top_left_corner)
    # bottom side of square
    else:
        y = -layer
        x = -layer + (i - bottom_left_corner)

    return x, y


def find_dist(i):
    (x, y) = find_pos(i)
    return abs(x) + abs(y)


#   (x-1,y+1)   (x,y+1) (x+1,y+1)
#   (x-1,y)     (x,y)   (x+1,y)
#   (x-1,y-1)   (x,y-1) (x+1,y-1)
def add_pos_to_array(i, two_d_space):
    x, y = find_pos(i)
    value = 0

    if i == 1:
        value = 1
    else:
        for j in [1, 0, -1]:
            for k in [1, 0, -1]:
                entry = two_d_space.get(x+j, y+k)
                if entry:
                    value += entry

    two_d_space.set(x, y, value)
    return value


def compute_array_up_to(input):
    i = 1
    value = 1
    two_d_space = TwoDSpace()
    while value < input:
        value = add_pos_to_array(i, two_d_space)
        i += 1
    return value


class TwoDSpace:
    # positive indexes are 2i
    # negative indexes are -2i+1
    def __init__(self):
        # assuming 100 will be big enough, could resize at get and set methods if needed
        self.space = np.zeros((100, 100), np.int)

    def convert_index(self, i):
        if i >= 0:
            return 2*i
        else:
            return -2*i+1

    def get(self, x, y):
        converted_x = self.convert_index(x)
        converted_y = self.convert_index(y)

        return self.space[converted_x, converted_y]

    def set(self, x, y, value):
        converted_x = self.convert_index(x)
        converted_y = self.convert_index(y)

        self.space[converted_x, converted_y] = value
