from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxNum = 0
        for i in range(len(accounts)):
            temp = 0
            for j in range(len(accounts[i])):
                temp += accounts[i][j]
            if temp > maxNum:
                maxNum = temp
        return maxNum