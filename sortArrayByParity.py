class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        ans = deque()
        for i in nums:
            if i % 2 == 0:
                ans.appendleft(i)
            else:
                ans.append(i)
        return ans