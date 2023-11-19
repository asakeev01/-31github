from typing import List


def productExceptSelf(self, nums: List[int]) -> List[int]:
    left = [0] * len(nums)
    right = [0] * len(nums)
    for i in range(len(nums)):
        if i == 0:
            left[i] = nums[i]
        else:
            left[i] = left[i - 1] * nums[i]
    for j in range(len(nums) - 1, -1, -1):
        if j == len(nums) - 1:
            right[j] = nums[j]
        else:
            right[j] = right[j + 1] * nums[j]
    for k in range(len(nums)):
        if k == 0:
            nums[k] = right[k + 1]
        elif k == len(nums) - 1:
            nums[k] = left[k - 1]
        else:
            nums[k] = right[k + 1] * left[k - 1]
    return nums