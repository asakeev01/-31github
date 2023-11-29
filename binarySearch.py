from typing import List


def search(self, nums: List[int], target: int) -> int:
    startPointer = 0
    finalPointer = len(nums) - 1
    while startPointer < finalPointer:
        middle = (startPointer + finalPointer) // 2
        if target == nums[middle]:
            return middle
        elif target > nums[middle]:
            startPointer = middle + 1
        elif target < nums[middle]:
            finalPointer = middle - 1
    if nums[startPointer] == target:
        return startPointer
    else:
        return -1