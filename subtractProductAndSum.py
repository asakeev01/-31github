class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        nS = str(n)
        pr = 1
        sm = 0
        for i in nS:
            sm += int(i)
            pr *= int(i)
        return pr - sm