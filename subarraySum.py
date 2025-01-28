from typing import List


class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        answer = 0
        dp = [nums[0]]
        for i in range(1, len(nums)):
            dp.append(dp[i-1]+nums[i])
        for j in range(len(nums)):
            if max(0, j - nums[j]) == 0:
                answer += dp[j]
            else:
                answer += dp[j] - dp[j-nums[j]-1]
        return answer