class Solution:
    def numberOfMatches(self, n: int) -> int:
        games = 0
        while n != 1:
            if n % 2 == 0:
                n = n // 2
                games += n
            else:
                n = (n-1)//2+1
                games += n - 1
        return games