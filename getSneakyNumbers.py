class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        s = set()
        for num in nums:
            if num in s:
                ans.append(num)
            else:
                s.add(num)
        return ans