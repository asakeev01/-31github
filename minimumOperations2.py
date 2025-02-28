from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        answer = 0
        for i in range(len(nums)):
            counter1 = 0
            temp1 = nums[i]
            while temp1 % 3 != 0:
                temp1 += 1
                counter1 += 1
            counter2 = 0
            temp2 = nums[i]
            while temp2 % 3 != 0:
                temp2 -= 1
                counter2 += 1
            answer += min(counter1, counter2)
        return answer