class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        initials = [0]*len(target)
        dp = [0]*len(target)
        dp[0] = target[0]
        for i in range(1,len(target)):
            if target[i-1] >= target[i]:
                dp[i] = dp[i-1]
            else:
                dp[i] = dp[i-1] + target[i] - target[i-1]
        print(dp)
        return dp[len(target)-1]