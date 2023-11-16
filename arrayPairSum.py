from typing import List


def arrayPairSum(self, nums: List[int]) -> int:
    nums.sort()
    counter = 0
    for i in range(0, len(nums), 2):
        counter += nums[i]
    return counter