from typing import List


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        answer = nums[0]
        current = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                current += nums[i]
                if current > answer:
                    answer = current
            else:
                if current > answer:
                    answer = current
                current = nums[i]

        return answer