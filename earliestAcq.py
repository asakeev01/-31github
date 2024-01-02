from typing import List


class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        friends = []
        timestamp = 0
        pointer = 0
        logs.sort(key=lambda x:x[0])
        for i in range(len(logs)):
            timestamp = logs[i][0]
            pos1 = -1
            pos2 = -1
            for j in range(len(friends)):
                if logs[i][1] in friends[j]:
                    pos1 = j
                elif logs[i][2] in friends[j]:
                    pos2 = j
            if pos1 != -1 and pos2 != -1:
                friends[pos1].update(friends[pos2])
                if len(friends[pos1]) == n:
                    return timestamp
                friends.pop(pos2)
            elif pos1 != -1:
                friends[pos1].add(logs[i][2])
                if len(friends[pos1]) == n:
                    return timestamp
            elif pos2 != -1:
                friends[pos2].add(logs[i][1])
                if len(friends[pos2]) == n:
                    return timestamp
            else:
                friends.append({logs[i][1], logs[i][2]})
        return -1