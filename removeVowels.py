class Solution:
    def removeVowels(self, s: str) -> str:
        s = s.replace("a", "")
        s = s.replace("e", "")
        s = s.replace("i", "")
        s = s.replace("o", "")
        s = s.replace("u", "")
        return s