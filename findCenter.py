from typing import List


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        node1 = edges[0][0]
        node2 = edges[0][1]
        if node1 in edges[1]:
            return node1
        if node2 in edges[1]:
            return node2