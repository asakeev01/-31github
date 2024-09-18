from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        ans = nums + nums
        return ans