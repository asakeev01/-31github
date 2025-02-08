import heapq


class NumberContainers:

    def __init__(self):
        self.nums = {}
        self.indexes = {}

    def change(self, index: int, number: int) -> None:
        if number not in self.nums:
            self.nums[number] = []
            heapq.heappush(self.nums[number], index)
        else:
            heapq.heappush(self.nums[number], index)

        self.indexes[index] = number

    def find(self, number: int) -> int:
        if number in self.nums:
            while self.nums[number] and self.indexes[self.nums[number][0]] != number:
                heapq.heappop(self.nums[number])
            if self.nums[number]:
                return self.nums[number][0]
            else:
                return -1
        else:
            return -1