class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arrSorted = sorted(arr)
        arrSorted[0] = 1
        maxPoss = 1
        for i in range(len(arrSorted)-1):
            if arrSorted[i] == arrSorted[i+1]:
                pass
            elif abs(arrSorted[i+1] - arrSorted[i]) == 1:
                maxPoss = arrSorted[i+1]
            else:
                arrSorted[i+1] = arrSorted[i] + 1
                maxPoss = arrSorted[i+1]
        return maxPoss