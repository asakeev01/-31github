from typing import List


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        word_1 = ""
        for i in range(len(word1)):
            word_1 += word1[i]
        word_2 = ""
        for j in range(len(word2)):
            word_2 += word2[j]
        return True if word_1 == word_2 else False