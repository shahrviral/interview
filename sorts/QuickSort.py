"""

Average: O(nlogn)

Worst: O(n^2) When pivot is largest or smallest value

Below solution picks pivot as last element

"""


def quicksort(arr):
    _quicksort(arr, 0, len(arr) - 1)


def _quicksort(arr, low, high):
    if low < high:
        partition_index = partition(arr, low, high)
        _quicksort(arr, low, partition_index - 1)
        _quicksort(arr, partition_index + 1, high)


def partition(arr, low, high):

    # Set i to be index of smaller element
    i = low - 1

    # Assume last element as pivot
    pivot = arr[high]

    # Iterate over indices from low to high
    for j in range(low, high):

        # If you encounter an element smaller than the pivot
        if arr[j] <= pivot:
            # increment index of smaller element
            i += 1
            # swap the smaller and larger elements
            arr[i], arr[j] = arr[j], arr[i]
    # once you reach the end, swap the pivot with the index larger element
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    # return index of pivot
    return i + 1


if __name__ == '__main__':
    arr = [8, 3, 1, 2, 5]
    quicksort(arr)
    print(arr)
