class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        s = ["a", "b", "c"]
        answer = []
        def bt(temp):
            for i in range(len(s)):
                if len(temp) == n:
                    answer.append(temp)
                    break
                if temp:
                    if temp[-1] == s[i]:
                        continue
                temp += s[i]
                bt(temp)
                temp = temp[:-1]
        bt("")
        return answer[k-1] if len(answer) > k-1 else ""