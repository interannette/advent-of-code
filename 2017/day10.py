part_two = True


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

    if part_two:
        for c in list(length_strs):
            lengths.append(ord(c))

        lengths.extend([17, 31, 73, 47, 23])
    else:
        for length_str in length_strs.split(","):
            lengths.append(int(length_str))

    return lengths


def convert_sparse_hash(sparse_hash):
    dense_hash = []
    for i in range(16):
        partial = 0
        start = i * 16
        for j in range(start, start+16):
            partial = partial ^ sparse_hash[j]

        dense_hash.append(partial)

    return dense_hash


def convert_to_hex(dense_hash):
    hex_string = ""
    for val in dense_hash:
        hex_string += format(val, 'x')
    return hex_string


def perform_mutations(length_strs):
    current_list = range(256)
    pos = 0
    skip = 0
    lengths = parse_lengths(length_strs)

    for i in range(64):
        for length in lengths:
            current_list = reverse_length(current_list, pos, length)
            pos = (pos + length + skip) % len(current_list)
            skip += 1

    dense_hash = convert_sparse_hash(current_list)

    return convert_to_hex(dense_hash)

print perform_mutations('''199,0,255,136,174,254,227,16,51,85,1,2,22,17,7,192''')