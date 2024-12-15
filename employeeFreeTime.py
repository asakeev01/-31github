import heapq

class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        h = []
        ans = []
        for i in range(len(schedule)):
            heapq.heappush(h, [schedule[i][0].start, schedule[i][0].end, i, 0, len(schedule[i])])
        temp = start, end, emplId, currId, allIds = h[0]
        prevEnd = schedule[emplId][currId].end
        while h:
            start, end, emplId, currId, allIds = heapq.heappop(h)
            print(prevEnd)
            print(start)
            if prevEnd < start:
                interval = Interval(prevEnd, start)
                ans.append(interval)
            prevEnd = max(prevEnd, end)
            if currId + 1 < allIds:
                heapq.heappush(h, [schedule[emplId][currId+1].start, schedule[emplId][currId+1].end, emplId, currId+1, allIds])
        return ans