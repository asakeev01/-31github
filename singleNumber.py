from typing import List


def singleNumber(self, nums: List[int]) -> int:
    l = []
    for i in nums:
        if i in l:
            l.remove(i)
        else:
            l.append(i)
    return l[0]