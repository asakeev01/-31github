from typing import List


class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        d = {}
        ans, f = 0, 0
        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]] += 1
            else:
                d[nums[i]] = 1
            if d[nums[i]] > f:
                ans = nums[i]
                f = d[nums[i]]
        return ans