from typing import List


def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
    ans = []
    numbers = set(nums)
    for i in range(1, len(nums) + 1):
        if i not in numbers:
            ans.append(i)
    return ans