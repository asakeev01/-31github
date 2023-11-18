def hammingDistance(self, x: int, y: int) -> int:
    binX = format(x, 'b')
    binY = format(y, 'b')
    while len(binX) > len(binY):
        binY = '0' + binY
    while len(binY) > len(binX):
        binX = '0' + binX
    pointer = 0
    counter = 0
    while pointer < len(binX):
        if binX[pointer] != binY[pointer]:
            counter += 1
        pointer += 1
    return counter