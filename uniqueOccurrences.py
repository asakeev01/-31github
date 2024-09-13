from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        s = set()
        d = {}
        for i in range(len(arr)):
            if arr[i] in d:
                d[arr[i]] += 1
            else:
                d[arr[i]] = 1
        for v in d.values():
            s.add(v)
        return True if len(s) == len(d) else False