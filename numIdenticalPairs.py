from typing import List


def numIdenticalPairs(self, nums: List[int]) -> int:
    d = {}
    counter = 0
    for i in range(len(nums)):
        if nums[i] not in d:
            d[nums[i]] = 0
        else:
            d[nums[i]] = d[nums[i]] + 1
            counter += d[nums[i]]
    return counter