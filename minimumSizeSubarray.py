from typing import List


def minSubArrayLen(self, target: int, nums: List[int]) -> int:
    sp = 0
    fp = 0
    counter = 0
    sub = 2 ** 31
    while fp < len(nums):
        counter += nums[fp]
        fp += 1
        while counter >= target:
            sub = min(sub, fp - sp)
            counter -= nums[sp]
            sp += 1
    return 0 if sub == 2 ** 31 else sub