import math
from typing import List


class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        self.explosed = set()
        self.answer = 0
        self.counter = 0
        self.bombsInRadius = {}

        def recursion(b):
            for bomb in b:
                if bomb in self.explosed:
                    pass
                else:
                    self.counter += 1
                    self.explosed.add(bomb)
                    recursion(self.bombsInRadius[bomb])
            return self.counter

        for i in range(len(bombs)):
            self.bombsInRadius[i] = []
            for j in range(len(bombs)):
                if i == j:
                    pass
                xDistance = abs(bombs[i][0] - bombs[j][0])
                yDistance = abs(bombs[i][1] - bombs[j][1])
                zDistance = math.sqrt(xDistance ** 2 + yDistance ** 2)
                if zDistance <= bombs[i][2]:
                    self.bombsInRadius[i].append(j)
        for k, v in self.bombsInRadius.items():
            counter = recursion(v)
            if counter > self.answer:
                self.answer = counter
            self.explosed = set()
            self.counter = 0
        return self.answer