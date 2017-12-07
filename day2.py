def diffrow(row):
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


def checksum(spreadsheet):
    rows = spreadsheet.split("\n")
    total = 0
    for row in rows:
        total += diffrow(row)
    return total
