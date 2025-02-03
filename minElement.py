from typing import List


class Solution:
    def minElement(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            elem = 0
            for digit in str(num):
                elem += int(digit)
            nums[i] = elem
        return min(nums)