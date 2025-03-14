from typing import List


class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for i in range(k):
            nums[nums.index(min(nums))] = min(nums) * multiplier
        return nums