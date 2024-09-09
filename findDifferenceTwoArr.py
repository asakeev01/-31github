from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        a = set()
        b = set()
        answer = [a, b]
        for d in nums1:
            if d not in nums2:
                answer[0].add(d)
        for d in nums2:
            if d not in nums1:
                answer[1].add(d)
        answer[0] = list(answer[0])
        answer[1] = list(answer[1])
        return answer