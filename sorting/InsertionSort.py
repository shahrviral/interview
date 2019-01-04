"""

Algorithm starts with second element and compares it with each of it's preceding elements,

swapping when element is smaller than previous elements

O(n^2)

"""


def insertion_sort(arr):

    # Assume that the first element in the list is sorted, begin iteration at second element, index 1
    for current_index in range(1, len(arr)):
        # get the value at the current element
        current_item = arr[current_index]
        # pointer to the previous element
        previous_index = current_index - 1
        # while your previous index does not go beyond the min index (0)
        # and the current item is smaller than the previous item
        while previous_index >= 0 and current_item < arr[previous_index]:
            # Copy the larger item before the current item to the current item's place
            arr[previous_index + 1] = arr[previous_index]
            # push your previous pointer back
            previous_index -= 1
            # Either your previous pointer will now be negative in which case you have reached the start of the array
            # or you reached an item smaller than the current item
            # This exists the loop
        # Now you can move the current item to the empty space created by moving the other items forward
        # and begin the next pass of the sorting algorithm
        arr[previous_index + 1] = current_item


if __name__ == '__main__':
    arr = [8, 3, 1, 2]
    insertion_sort(arr)
    print(arr)
