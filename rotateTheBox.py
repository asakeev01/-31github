from typing import List


class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        answer = []
        for i in range(len(boxGrid)):
            stones = []
            for j in range(len(boxGrid[i])):
                if boxGrid[i][j] == "#":
                    stones.append(j)
                elif boxGrid[i][j] == ".":
                    if stones:
                        oldStone = stones.pop(0)
                        stones.append(j)
                        boxGrid[i][oldStone] = "."
                        boxGrid[i][j] = "#"
                else:
                    stones = []
        print(boxGrid)
        for k in range(len(boxGrid[0])):
            answer.append([])
            for v in range(len(boxGrid)-1, -1, -1):
                answer[k].append(boxGrid[v][k])
        return answer