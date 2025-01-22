from typing import List


class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        counter = 0
        seats.sort()
        students.sort()
        for i in range(len(seats)):
            counter += abs(seats[i] - students[i])
        return counter