class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        prev = {}
        curr = {}
        for k in range(len(words[0])):
            if words[0][k] not in prev:
                prev[words[0][k]] = 1
            else:
                prev[words[0][k]] += 1
        for i in range(1, len(words)):
            for j in range(len(words[i])):
                if words[i][j] in prev:
                    if words[i][j] not in curr:
                        curr[words[i][j]] = 1
                    else:
                        if curr[words[i][j]] < prev[words[i][j]]:
                            curr[words[i][j]] += 1
            prev = curr
            curr = {}
        ans = []
        for k, v in prev.items():
            ans.extend([k]*v)
        return ans