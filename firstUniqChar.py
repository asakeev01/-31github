class Solution:
    def firstUniqChar(self, s: str) -> int:
        notUniqueSet = set()
        for i in range(len(s)):
            if s[i] in notUniqueSet:
                continue
            isUnique = True
            for j in range(i+1, len(s)):
                if s[i] == s[j]:
                    isUnique = False
                    notUniqueSet.add(s[i])
                    break
            if isUnique:
                 return i
        return -1