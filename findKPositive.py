from typing import List


def findKthPositive(self, arr: List[int], k: int) -> int:
    sp = 0
    fp = len(arr)
    while sp < fp:
        mid = (sp + fp) // 2
        diff = arr[mid] - mid - 1
        if diff < k:
            sp = mid + 1
        else:
            fp = mid
    return sp + k