from typing import List


class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        strong = {j for j in range(n)}
        for i in range(len(edges)):
            if edges[i][1] in strong:
                strong.remove(edges[i][1])
        if len(strong) > 1:
            return -1
        else:
            return list(strong)[0]