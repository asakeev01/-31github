class Solution:
    def removeStars(self, s: str) -> str:
        answer = []
        for i in range(len(s)):
            if s[i] != "*":
                answer.append(s[i])
            else:
                answer.pop()
        return "".join(answer)