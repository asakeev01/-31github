from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        answer = []
        counter = 0
        oneLeftCounter = 0
        oneRightCounter = 0
        for i in range(len(boxes)):
            if boxes[i] == "1":
                oneRightCounter += 1
                counter += i-0
        answer.append(counter)
        if boxes[0] == "1":
            oneLeftCounter += 1
            oneRightCounter -= 1
        for j in range(1, len(boxes)):
            steps = 0
            if boxes[j] == "1":
                oneRightCounter -= 1
                steps = answer[j-1] - oneRightCounter + oneLeftCounter - 1
                oneLeftCounter += 1
            else:
                steps = answer[j-1] - oneRightCounter + oneLeftCounter
            answer.append(steps)
        return answer