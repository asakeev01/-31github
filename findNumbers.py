from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        counter = 0
        for i in range(len(nums)):
            if len(str(nums[i])) % 2 == 0:
                counter += 1
        return counter