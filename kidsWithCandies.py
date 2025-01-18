class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCan = max(candies)
        ans = []
        for candy in candies:
            if candy + extraCandies >= maxCan:
                ans.append(True)
            else:
                ans.append(False)
        return ans