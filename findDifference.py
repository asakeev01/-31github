def findTheDifference(self, s: str, t: str) -> str:
    s = sorted(s)
    t = sorted(t)
    position = 0
    while position < len(s):
        one = s[position]
        two = t[position]
        if one != two:
            return two
        position += 1
    return t[-1]