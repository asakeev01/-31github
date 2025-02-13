class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        counter = 0
        while True:
            num1 = heappop(nums)
            if num1 >= k:
                break
            num2 = heappop(nums)
            num = (num1 * 2) + num2
            heappush(nums, num)
            counter += 1
        return counter