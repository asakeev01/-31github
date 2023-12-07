from typing import List


def minimumOperations(self, nums: List[int]) -> int:
    counter = 0
    while max(nums) != 0:
        m = min(nums)
        while len(nums) > 1 and m == 0:
            nums.remove(min(nums))
            m = min(nums)
        for i in range(len(nums)):
            if nums[i] - m <= 0:
                nums[i] = 0
            else:
                nums[i] = nums[i] - m
        counter += 1
    return counter