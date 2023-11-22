from typing import List


def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
    for i in range(len(image)):
        for j in range(len(image[i]) - 1, -1, -1):
            if image[i][j] == 0:
                image[i][j] = 1
            else:
                image[i][j] = 0
        image[i].reverse()
    return image