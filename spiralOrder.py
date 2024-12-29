from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        xUp = 0
        xDown = len(matrix)
        yRight = len(matrix[0])
        yLeft = 0
        while xUp < xDown or yRight > yLeft:
            for i in range(yLeft, yRight):
                ans.append(matrix[xUp][i])
            xUp += 1
            if xUp >= xDown : break
            for j in range(xUp, xDown):
                ans.append(matrix[j][yRight-1])
            yRight -= 1
            if yRight <= yLeft : break
            for k in range(yRight-1, yLeft-1, -1):
                ans.append(matrix[xDown-1][k])
            xDown -= 1
            if xUp >= xDown : break
            for n in range(xDown-1, xUp-1, -1):
                ans.append(matrix[n][yLeft])
            yLeft += 1
            if yRight <= yLeft : break
        return ans