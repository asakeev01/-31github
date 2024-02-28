class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zeroPointer = 0
        lenNums = len(nums)
        for i in range(lenNums):
            if nums[i] != 0:
                temp = nums[zeroPointer]
                nums[zeroPointer] = nums[i]
                nums[i] = temp
                zeroPointer += 1
        return nums
