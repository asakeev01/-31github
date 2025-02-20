from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        s = set(nums)
        def bt(temp):
            if len(temp) == len(nums[0]):
                if temp not in s:
                    return temp
                else:
                    return None
            for i in range(2):
                result = bt(temp + str(i))
                if result:
                    return result
            return None
        return bt("")