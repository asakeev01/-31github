
def searchMatrix(matrix, target) -> bool:
    i, j = len(matrix), len(matrix[0])
    left = [0, 0]
    right = [i - 1, j - 1]
    while left[1] <= (right[0] - left[0]) * j + right[1]:
        mid = [((left[1] + (right[0] - left[0]) * j + right[1]) // 2 // j) + left[0], ((left[1] + (right[0] - left[0]) * j + right[1]) // 2 % j)]
        if matrix[mid[0]][mid[1]] == target:
            return True
        elif matrix[mid[0]][mid[1]] < target:
            left = [mid[0] + 1, 0] if mid[1] + 1 == j else [mid[0], mid[1] + 1]
        elif matrix[mid[0]][mid[1]] > target:
            right = [mid[0] - 1, j - 1] if mid[1] - 1 == -1 else [mid[0], mid[1] - 1]
    return False

print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))