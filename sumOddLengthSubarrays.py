from typing import List


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        total = 0
        for i, x in enumerate(arr):
            left = i
            right = n - i - 1
            evenL = left // 2 + 1
            oddL  = (left + 1) // 2
            evenR = right // 2 + 1
            oddR  = (right + 1) // 2
            total += x * (evenL * evenR + oddL * oddR)
        return total