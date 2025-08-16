class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        t = {}
        c = {}
        n = {}
        for i in range(len(items)):
            if items[i][0] in t:
                t[items[i][0]] += 1
            else:
                t[items[i][0]] = 1
            if items[i][1] in c:
                c[items[i][1]] += 1
            else:
                c[items[i][1]] = 1
            if items[i][2] in n:
                n[items[i][2]] += 1
            else:
                n[items[i][2]] = 1
        if ruleKey == "color":
            if ruleValue in c:
                return c[ruleValue]
            else:
                return 0
        elif ruleKey == "type":
            if ruleValue in t:
                return t[ruleValue]
            else:
                return 0
        elif ruleKey == "name":
            if ruleValue in n:
                return n[ruleValue]
            else:
                return 0