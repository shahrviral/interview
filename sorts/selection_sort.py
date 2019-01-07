"""

Time:
    Best: O(n^2)
    Average: O(n^2)
    Worst: O(n^2)

Space:
    Worst: O(1)

Stable:
    No

Worst Case Scenario:
    Reverse Sorted Array

Algorithm Overview:

    For each element in the array, assume it is the minimum item and set the current_ in index to the element's index,
     iterate over each of its neighbors to the right, and if you encounter a smaller item, update the current minimum
     index with the smaller element's index.
    At the end of the inner iteration, swap the current element and the element at the current minimum index.

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
    arr = [6, 3, 9, 6, 7, 2]
    selection_sort(arr)
    print(arr)
