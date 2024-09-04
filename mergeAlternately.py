class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word = ""
        pointer1 = 0
        pointer2 = 0
        while pointer1 < len(word1):
            word += word1[pointer1]
            if pointer2 < len(word2):
                word += word2[pointer2]
                pointer2 += 1
            pointer1 += 1
        while pointer2 < len(word2):
            word += word2[pointer2]
            pointer2 += 1
        return word