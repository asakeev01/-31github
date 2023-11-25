from typing import List


def trap(self, height: List[int]) -> int:
    leftLess = True
    water = 0
    left = 0
    while height[left] == 0 and left != len(height) - 1:
        left += 1
    leftBar = height[left]
    right = len(height) - 1
    while height[right] == 0 and right != 0:
        right -= 1
    rightBar = height[right]
    if rightBar < leftBar:
        leftLess = False
    while left < right:
        if leftLess:
            temp = leftBar - height[left + 1]
            if temp <= 0:
                leftBar = height[left + 1]
            else:
                water += temp
            if leftBar > rightBar:
                leftLess = False
            left += 1
        else:
            temp = rightBar - height[right - 1]
            if temp <= 0:
                rightBar = height[right - 1]
            else:
                water += temp
            if leftBar < rightBar:
                leftLess = True
            right -= 1
    return water