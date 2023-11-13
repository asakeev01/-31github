from typing import List


def longestOnes(self, nums: List[int], k: int) -> int:
    zeros = []
    sp = 0
    p = 0
    used = 0
    counter_max = 0
    counter = 0
    fp = len(nums)
    while p < fp:
        if nums[p] == 0:
            if used < k:
                zeros.append(p)
                counter += 1
                p += 1
                used += 1
            else:
                if zeros:
                    counter_max = max(counter_max, counter)
                    sp = zeros[0] + 1
                    counter = p - sp + 1
                    zeros.pop(0)
                    zeros.append(p)
                    p += 1
                else:
                    counter_max = max(counter_max, counter)
                    counter = 0
                    p += 1
        else:
            p += 1
            counter += 1
    counter_max = max(counter_max, counter)
    return counter_max