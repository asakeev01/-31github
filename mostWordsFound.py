from typing import List


class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        counter = 0
        for i in range(len(sentences)):
            current = 0
            sentence = sentences[i].split(" ")
            for j in range(len(sentence)):
                current += 1
            if counter < current:
                counter = current
        return counter