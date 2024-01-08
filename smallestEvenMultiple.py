class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        plus = 0
        while True:
            if (n + plus) % n == 0 and (n + plus) % 2 == 0:
                return n + plus
            else:
                plus += 1