"""

O(n^2)

"""


def selection_sort(arr):

    # For each element in array
    for i in range(len(arr)):
        # assume current element is smallest
        current_min_index = i
        # compare current element with all elements to the right
        for j in range(i + 1, len(arr)):
            # if you find a smaller element
            if arr[current_min_index] > arr[j]:
                # store it's index
                current_min_index = j
        # swap the current element with the smallest based off of index you found
        arr[current_min_index], arr[i] = arr[i], arr[current_min_index]


if __name__ == '__main__':
    arr = [6,3,9,6,7,2]
    selection_sort(arr)
    print(arr)