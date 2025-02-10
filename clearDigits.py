class Solution:
    def clearDigits(self, s: str) -> str:
        letters = []
        for i in range(len(s)):
            if s[i] in "0123456789":
                letters.pop()
            else:
                letters.append(s[i])
        return "".join(letters)