def remove_duplicates_from_sorted_array(nums):
    new_element_pointer = 0

    # begin from processing the second element
    for i in range(1, len(nums)):
        if nums[i] != nums[new_element_pointer]:
            # Found new element so need to put it in the next slot
            new_element_pointer += 1
            nums[new_element_pointer] = nums[i]
    return new_element_pointer + 1


if __name__ == '__main__':
    print(remove_duplicates_from_sorted_array([1, 1, 2, 4, 4, 5, 5, 5, 6, 7, 8]))

