from typing import List


class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        numsSet = set(nums)
        if len(numsSet) < 3:
            return -1
        numsSorted = sorted(list(numsSet))
        return numsSorted[1]