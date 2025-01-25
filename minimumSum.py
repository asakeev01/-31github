class Solution:
    def minimumSum(self, num: int) -> int:
        l = list(str(num))
        l.sort()
        print(l)
        num1 = int(l[0] + l[2])
        num2 = int(l[1] + l[3])
        return num1 + num2