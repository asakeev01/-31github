from typing import List


def selfDividingNumbers(self, left: int, right: int) -> List[int]:
    dividing = []
    for i in range(left, right + 1):
        isDividing = True
        for j in str(i):
            if j == "0":
                isDividing = False
                break
            if i % int(j) != 0:
                isDividing = False
                break
        if isDividing:
            dividing.append(i)
    return dividing
