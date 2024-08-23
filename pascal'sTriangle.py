class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for i in range(1, numRows+1):
            currRow = []
            for j in range(i):
                if j == 0:
                    currRow.append(1)
                elif j == i-1:
                    currRow.append(1)
                else:
                    num = ans[i-2][j-1] + ans[i-2][j]
                    currRow.append(num)
            ans.append(currRow)
        return ans