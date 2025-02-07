from typing import List


class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        balls = {}
        colors = {}
        answer = []
        for i in range(len(queries)):
            if queries[i][0] not in balls:
                balls[queries[i][0]] = queries[i][1]
                if queries[i][1] in colors:
                    colors[queries[i][1]] += 1
                else:
                    colors[queries[i][1]] = 1
            else:
                colors[balls[queries[i][0]]] -= 1
                if colors[balls[queries[i][0]]] == 0:
                    del colors[balls[queries[i][0]]]
                balls[queries[i][0]] = queries[i][1]
                if queries[i][1] in colors:
                    colors[queries[i][1]] += 1
                else:
                    colors[queries[i][1]] = 1
            answer.append(len(colors))
        return answer