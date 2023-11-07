def search(self, nums: List[int], target: int) -> int:
    min_num = target
    min_ind = 0
    nums_len = len(nums)
    for i in range(nums_len):
        if min_num >= nums[i]:
            min_num = nums[i]
            min_ind = i
    left = 0
    right = nums_len - 1
    while left <= right:
        mid = (right + left) // 2
        mid_pivoted = (mid + min_ind) % nums_len
        if nums[mid_pivoted] == target:
            return mid_pivoted
        elif nums[mid_pivoted] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1