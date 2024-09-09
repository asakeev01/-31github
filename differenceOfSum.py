class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        elSum = 0
        digSum = 0
        for i in range(len(nums)):
            elSum += nums[i]
            for c in str(nums[i]):
                digSum += int(c)
        return abs(elSum - digSum)