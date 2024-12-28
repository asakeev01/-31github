from heapq import heapify, heappush, heappop
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxHeapQ = []
        minHeapQ = []
        heapify(maxHeapQ)
        heapify(minHeapQ)
        answer = 1
        left = 0
        for right in range(len(nums)):
            heappush(maxHeapQ, (nums[right], right))
            heappush(minHeapQ, (-nums[right], right))
            while maxHeapQ[0][1] < left:
                heappop(maxHeapQ)
            while minHeapQ[0][1] < left:
                heappop(minHeapQ)
            if abs(-minHeapQ[0][0] - maxHeapQ[0][0]) <= limit:
                print(abs(-minHeapQ[0][0] - maxHeapQ[0][0]))
                answer = max(answer, right - left + 1)
            else:
                left += 1
        return answer

