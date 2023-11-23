from typing import List


def countPairs(self, nums: List[int], target: int) -> int:
    sp = 0
    fp = len(nums) - 1
    nums.sort()
    counter = 0
    while sp < fp:
        if nums[sp] + nums[fp] < target:
            counter += fp - sp
            sp += 1
        else:
            fp -= 1
    return counter