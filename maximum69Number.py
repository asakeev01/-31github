class Solution:
    def maximum69Number (self, num: int) -> int:
        ans = ""
        changed = False
        numS = str(num)
        for i in numS:
            if i == "6" and not changed:
                ans += "9"
                changed = True
            else:
                ans += i
        return int(ans)