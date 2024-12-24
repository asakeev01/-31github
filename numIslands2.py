from typing import List


class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        parent = {}
        rank = {}
        count = 0
        result = []

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                if rank[rootX] > rank[rootY]:
                    parent[rootY] = rootX
                elif rank[rootX] < rank[rootY]:
                    parent[rootX] = rootY
                else:
                    parent[rootY] = rootX
                    rank[rootX] += 1
                return True
            return False

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for x, y in positions:
            if (x, y) in parent:
                result.append(count)
                continue

            parent[(x, y)] = (x, y)
            rank[(x, y)] = 0
            count += 1

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if (nx, ny) in parent:
                    if union((x, y), (nx, ny)):
                        count -= 1

            result.append(count)

        return result