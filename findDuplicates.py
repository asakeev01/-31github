from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        answer = []
        n = len(nums)
        for i in range(n):
            num = abs(nums[i])
            idx = num - 1
            if nums[idx] < 0:
                answer.append(num)
            nums[idx] *= -1
        return answer