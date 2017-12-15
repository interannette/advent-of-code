partTwo = True


def diff_row(row):
    vals = row.split()
    minVal = None
    maxVal = None
    for val in vals:
        numVal = int(val)
        if minVal is None or numVal < minVal:
            minVal = numVal
        if maxVal is None or numVal > maxVal:
            maxVal = numVal
    return maxVal - minVal


def find_row_val(row):
    vals = row.split()
    for i in range(len(vals)):
        for j in range(len(vals)):
            if i == j:
                continue
            mod = int(vals[i]) % int(vals[j])
            if mod == 0:
                return int(vals[i]) / int(vals[j])


def checksum(spreadsheet):
    rows = spreadsheet.split("\n")
    total = 0
    for row in rows:
        if partTwo:
            total += find_row_val(row)
        else:
            total += diff_row(row)
    return total
