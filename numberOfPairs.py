class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        counter = 0
        for i in nums1:
            for j in nums2:
                if i % (j * k) == 0:
                    counter += 1
        return counter