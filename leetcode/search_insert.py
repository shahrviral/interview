def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """

    def bs(left, right):
        if left > right:
            return left
        else:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return bs(left, mid - 1)
            else:
                return bs(mid + 1, right)

    return bs(0, len(nums) - 1)


if __name__ == '__main__':
    print(searchInsert([1, 3, 4, 6], 5))