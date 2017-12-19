def reverse_length(current_list, start, length):

    end = (start + length - 1) % len(current_list)

    for i in range(length / 2):
        s = (start + i) % len(current_list)
        e = (end - i) % len(current_list)

        s_val = current_list[s]
        e_val = current_list[e]

        current_list[s] = e_val
        current_list[e] = s_val

    return current_list


def parse_lengths(length_strs):
    lengths = []
    for length_str in length_strs.split(","):
        lengths.append(int(length_str))
    return lengths


def perform_mutations(length_strs):
    current_list = range(256)
    pos = 0
    skip = 0
    lengths = parse_lengths(length_strs)

    for length in lengths:
        current_list = reverse_length(current_list, pos, length)
        pos = (pos + length + skip) % len(current_list)
        skip += 1

    print current_list[0] * current_list[1]
