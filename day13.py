def build_scanner_map(input_string):
    scanner_map = {}
    for line in input_string.split("\n"):
        [l, r] = line.split(": ")
        scanner_map[int(l)] = int(r)-1
    return scanner_map


def run_firewall(input_string):
    scanner_range_map = build_scanner_map(input_string)
    scanner_pos_map = dict([(key, 0) for key in scanner_range_map.keys()])
    scanner_dir_map = dict([(key, 1) for key in scanner_range_map.keys()])

    max_layer = max(scanner_range_map.keys())

    print("scanner pos " + str(scanner_range_map))
    print("max layers " + str(max_layer))

    current_packet_pos = -1

    severity = 0

    for i in range(max_layer+1):
        print("loop " + str(i))

        print("packet starts at " + str(current_packet_pos))
        print("scanners start at " + str(scanner_pos_map))

        # advance packet
        current_packet_pos += 1
        print("packet moves to "+str(current_packet_pos))

        # do check
        if current_packet_pos in scanner_pos_map and scanner_pos_map[current_packet_pos] == 0:
            print("packet caught at " + str(i))
            print("range " + str(scanner_range_map[current_packet_pos] + 1))
            additional_severity = i * (scanner_range_map[current_packet_pos] + 1)
            print("adding to severity " + str(additional_severity))
            severity += additional_severity

        # advance scanners
        for layer, range_of_layer in scanner_range_map.iteritems():
            # print("advancing scanner layer " + str(layer))
            updated_pos = scanner_pos_map[layer] + scanner_dir_map[layer]
            # print("advanced to " + str(updated_pos))
            if updated_pos == scanner_range_map[layer]:
                scanner_dir_map[layer] = -1
            elif updated_pos == 0:
                scanner_dir_map[layer] = 1
            # print("corrected to " + str(updated_pos))
            scanner_pos_map[layer] = updated_pos

        print("current scanner pos " + str(scanner_pos_map))

    return severity


print(run_firewall('''0: 3
1: 2
4: 4
6: 4'''))
