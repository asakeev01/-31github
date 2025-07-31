from typing import List


class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        m = min(nums)
        l = max(nums)
        d = l - m
        if d < 2*k:
            return 0
        else:
            return d - 2*k