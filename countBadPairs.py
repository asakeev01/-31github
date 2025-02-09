from typing import List


class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        t = len(nums)-1
        counter = t*(t+1)/2
        d = {}
        for i in range(len(nums)):
            if nums[i] - i in d:
                d[nums[i] - i] += 1
            else:
                d[nums[i] - i] = 0
        for k, v in d.items():
            counter -= v*(v+1)//2
        return int(counter)
