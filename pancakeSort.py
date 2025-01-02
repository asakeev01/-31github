from typing import List


class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans = []
        for size in range(len(arr), 1, -1):
            max_idx = arr.index(size)

            if max_idx != size - 1:
                if max_idx != 0:
                    ans.append(max_idx + 1)
                    arr[:max_idx + 1] = arr[:max_idx + 1][::-1]

                ans.append(size)
                arr[:size] = arr[:size][::-1]

        return ans