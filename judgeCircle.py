class Solution:
    def judgeCircle(self, moves: str) -> bool:
        d = { "U" : 0,
            "D" : 0,
            "L" : 0,
            "R" : 0}
        for i in range(len(moves)):
            d[moves[i]] += 1
        if d["U"] == d["D"] and d["L"] == d["R"]:
            return True
        else:
            return False