from collections import deque
from typing import List


class Solution:
    def maxAmount(self, initialCurrency: str, pairs1: List[List[str]], rates1: List[float], pairs2: List[List[str]], rates2: List[float]) -> float:
        def bfs(maxDay, day, initCurr):
            q = deque()
            q.append(initCurr)
            while q:
                curr = q.popleft()
                if curr in day:
                    currs = day[curr]
                    for i in range(len(currs)):
                        exchanged = maxDay[curr] * currs[i][1]
                        if currs[i][0] not in maxDay or exchanged > maxDay[currs[i][0]]:
                            maxDay[currs[i][0]] = exchanged
                            q.append(currs[i][0])
            return maxDay
        day1 = defaultdict(list)
        for i,currs in enumerate(pairs1):
            day1[currs[0]].append([currs[1], rates1[i]])
            day1[currs[1]].append([currs[0], 1.0/rates1[i]])
        day2 = defaultdict(list)
        for i,currs in enumerate(pairs2):
            day2[currs[0]].append([currs[1], rates2[i]])
            day2[currs[1]].append([currs[0], 1.0/rates2[i]])
        maxDay1 = {}
        maxDay1[initialCurrency] = 1.0
        maxDay1 = bfs(maxDay1, day1, initialCurrency)
        print(maxDay1)
        maxAmount = 0.0
        for key, value in maxDay1.items():
            maxDay = {}
            maxDay[key] = value
            maxDay = bfs(maxDay, day2, key)
            maxAmount = max(maxAmount, maxDay.get(initialCurrency, 0.0))
        return maxAmount