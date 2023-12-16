def gcdOfStrings(self, str1: str, str2: str) -> str:
    str1L = True
    ans = []
    lower = 0
    if len(str1) > len(str2):
        lower = len(str2)
        str1L = False
    else:
        lower = len(str1)
    for i in range(1, lower + 1):
        if len(str1) % i == 0 and len(str2) % i == 0:
            temp = ""
            if str1L:
                temp = str1[:i]
            else:
                temp = str2[:i]
            if temp * (len(str1) // i) == str1 and temp * (len(str2) // i) == str2:
                ans.append(temp)
    ans.sort()
    return ans[-1] if ans else ""