def search(self, nums: List[int], target: int) -> int:
    min_ind = 0
    max_ind = len(nums) - 1
    nums_len = len(nums)
    left = 0
    right = nums_len - 1
    while min_ind < max_ind:
        mid1 = (min_ind + max_ind) // 2
        if nums[mid1] > nums[max_ind]:
            min_ind = mid1 + 1
        else:
            max_ind = mid1
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