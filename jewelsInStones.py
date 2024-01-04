class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        j = set()
        counter = 0
        for i in range(len(jewels)):
            j.add(jewels[i])
        for k in range(len(stones)):
            if stones[k] in j:
                counter += 1
        return counter