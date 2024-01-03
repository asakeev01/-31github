from typing import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        pointer1 = 0
        pointer2 = n
        ans = []
        while pointer1 < n:
            ans.append(nums[pointer1])
            ans.append(nums[pointer2])
            pointer1 += 1
            pointer2 += 1
        return ans