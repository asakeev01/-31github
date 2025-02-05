class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        first = ""
        second = ""
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                first = first + s1[i]
                second = s2[i] + second
            if len(first) > 2:
                return False
        return False if first != second else True