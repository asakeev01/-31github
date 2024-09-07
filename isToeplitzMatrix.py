from typing import List


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        d = len(matrix)
        h = 1
        same = True
        while d > -1:
            x = d
            y = 0
            num = -1
            while x < len(matrix) and y < len(matrix[0]):
                if num == -1:
                    num = matrix[x][y]
                elif matrix[x][y] != num:
                    same = False
                    break
                x += 1
                y += 1
            d -= 1
        while h < len(matrix[0])-1:
            x = 0
            y = h
            num = -1
            while x < len(matrix) and y < len(matrix[0]):
                if num == -1:
                    num = matrix[x][y]
                elif matrix[x][y] != num:
                    same = False
                    break
                x += 1
                y += 1
            h += 1
        return same