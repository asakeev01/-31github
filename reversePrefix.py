class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        for i, letter in enumerate(word):
            if letter == ch:
                if i == len(word)-1:
                    word = word[i::-1]
                    break
                word = word[i::-1] + word[i+1:]
                break
        return word