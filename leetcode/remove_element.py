def remove_duplicates_from_sorted_array(nums, val):
    current_pointer = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[current_pointer] = nums[i]
            current_pointer += 1

    return nums[0:current_pointer]


if __name__ == '__main__':
    print(remove_duplicates_from_sorted_array([0,1,2,2,3,0,4,2], 2))

