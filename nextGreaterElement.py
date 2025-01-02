from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {}
        ans = []
        for i in range(len(nums2)):
            if nums2[i] not in d:
                d[nums2[i]] = i
        for j in range(len(nums1)):
            found = False
            startIndex = d[nums1[j]]
            for k in range(startIndex+1, len(nums2)):
                if nums2[k] > nums1[j]:
                    ans.append(nums2[k])
                    found = True
                    break
            if not found:
                ans.append(-1)
        return ans