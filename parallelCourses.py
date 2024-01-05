from collections import defaultdict
import collections
from typing import List


class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        courses = defaultdict(list)
        inStudy = defaultdict(int)
        for i in range(len(relations)):
            courses[relations[i][0]].append(relations[i][1])
            inStudy[relations[i][1]] += 1
        queue = collections.deque([i for i in range(1, n + 1) if i not in inStudy])
        counter = 0
        coursesTook = 0
        while queue:
            counter += 1

            for k in range(len(queue)):
                first = queue.popleft()
                coursesTook += 1
                for item in courses[first]:
                    inStudy[item] -= 1

                    if inStudy[item] == 0:
                        queue.append(item)
        return counter if coursesTook == n else -1