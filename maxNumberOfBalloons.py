class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        chars = {"b":0, "a":0, "l":0, "o":0, "n":0}
        for c in text:
            if c in chars:
                chars[c] += 1
        m = 10000
        for k,v in chars.items():
            if k == "l":
                v = v // 2
            elif k == "o":
                v = v // 2
            if v < m:
                m = v
        return m