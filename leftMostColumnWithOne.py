# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
# class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        dimensions = binaryMatrix.dimensions()
        answerRow = -1
        current = [i for i in range(dimensions[0])]
        left = 0
        right = dimensions[1] - 1
        mid = left + (right - left) // 2
        isHave = False
        print(mid)
        while left <= right:
            temp = []
            for i in current:
                if binaryMatrix.get(i, mid) == 1:
                    temp.append(i)
            if temp:
                current = temp
                right = mid - 1
                mid = left + (right - left) // 2
                isHave = True
            else:
                left = mid + 1
                mid = left + (right - left) // 2
            print(left, right)
        return left if isHave else -1


