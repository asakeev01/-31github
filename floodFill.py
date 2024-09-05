from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        visited = set()

        def rec(x, y, c):
            if not x < 0 and not x > len(image) - 1 and not y < 0 and not y > len(image[0]) - 1 and (
            x, y) not in visited and image[x][y] == c:
                image[x][y] = color
                visited.add((x, y))
                rec(x + 1, y, c)
                rec(x, y + 1, c)
                rec(x - 1, y, c)
                rec(x, y - 1, c)

        rec(sr, sc, image[sr][sc])
        return image
