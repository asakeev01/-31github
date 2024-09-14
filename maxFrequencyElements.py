from typing import List


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        d = {}
        m = 1
        counter = 0
        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]] += 1
                if d[nums[i]] > m:
                    m = d[nums[i]]
            else:
                d[nums[i]] = 1
        for v in d.values():
            if v == m:
                counter += v
        return counter