
class Scanner:

    pos = 0
    direction = 1

    def __init__(self, scan_range):
        self.scan_range = scan_range

    def advance(self):
        self.pos += self.direction
        if self.pos == self.scan_range:
            self.direction = -1
        elif self.pos == 0:
            self.direction = 1

    def is_at_pos(self, pos):
        return self.pos == pos;

    def __str__(self):
        return "pos: " + str(self.pos) + " direction: " + str(self.direction) + " scan_range: " + str(self.scan_range)


class ScannerMap:

    def __init__(self):
        self.scanner_map = {}

    def add_layer(self, layer, scan_range):
        self.scanner_map[layer] = Scanner(scan_range)

    def advance_scanners(self):
        for layer, scanner in self.scanner_map.items():
            scanner.advance()

    def scanner_at_layer(self, layer):
        if layer in self.scanner_map.keys():
            return self.scanner_map[layer]
        else:
            return None

    def clone_scanner_map(self):
        clone = ScannerMap()
        for layer, scanner in self.scanner_map.items():
            cloned_scanner = Scanner(scanner.scan_range)
            cloned_scanner.pos = scanner.pos
            cloned_scanner.direction = scanner.direction
            clone.scanner_map[layer] = cloned_scanner
        return clone

    def max_layer(self):
        return max(self.scanner_map.keys())


# Take the input string of the format
#  layer : range
#  layer : range etc
# And turn it into a dict of Scanners, layer : Scanner
def build_scanner_map(input_string):
    scanner_map = ScannerMap()
    for line in input_string.split("\n"):
        [l, r] = line.split(": ")
        scanner_map.add_layer(int(l), int(r) - 1)
    return scanner_map


def find_min_delay(scanner_map):

    severity = -1
    delay = 0

    while severity != 0:
        # clone scanner map, which is advanced delay number of steps
        severity = run_firewall(scanner_map.clone_scanner_map(), True)
        print("delay " + str(delay) + " results in severity " + str(severity))
        if severity == 0:
            return delay
        else:
            delay += 1
            scanner_map.advance_scanners()


def run_firewall(scanner_map, strict):

    max_layer = scanner_map.max_layer()

    print("max layers " + str(max_layer))

    current_packet_pos = -1

    severity = 0

    for i in range(max_layer+1):
        # print("loop " + str(i))

        # print("packet starts at " + str(current_packet_pos))

        # advance packet
        current_packet_pos += 1
        # print("packet moves to " + str(current_packet_pos))

        # do check
        scanner = scanner_map.scanner_at_layer(i)
        if scanner and 0 == scanner.pos:
            print("packet caught at " + str(i))
            if strict:
                return 100
            else:
                # print("range " + str(scanner.scan_range + 1))
                additional_severity = i * (scanner.scan_range + 1)
                # print("adding to severity " + str(additional_severity))
                severity += additional_severity

        scanner_map.advance_scanners()

    return severity


print(run_firewall(build_scanner_map('''0: 3
1: 2
2: 6
4: 4
6: 4
8: 8
10: 6
12: 8
14: 5
16: 6
18: 8
20: 8
22: 12
24: 6
26: 9
28: 8
30: 12
32: 12
34: 17
36: 12
38: 8
40: 12
42: 12
44: 10
46: 12
48: 12
50: 12
52: 14
54: 14
56: 10
58: 14
60: 12
62: 14
64: 14
66: 14
68: 14
70: 14
72: 14
74: 14
76: 14
86: 14
94: 20
96: 18'''), False))

