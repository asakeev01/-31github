from typing import List


def runningSum(self, nums: List[int]) -> List[int]:
    ans = []
    temp = 0
    for i in range(len(nums)):
        temp += nums[i]
        ans.append(temp)
    return ans