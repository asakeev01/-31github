from typing import List


class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        ans = [0, 0]
        for i in range(len(nums1)):
            if nums1[i] in set2:
                ans[0] += 1
        for j in range(len(nums2)):
            if nums2[j] in set1:
                ans[1] += 1
        return ans