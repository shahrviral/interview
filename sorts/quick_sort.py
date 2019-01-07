"""

Time:
    Best: O(nlogn)
    Average: O(nlogn)
    Worst: O(n^2)

Space:
    Worst: O(logn)

Stable:
    No

Worst Case Scenario:
    When pivot is largest or smallest value

Algorithm Overview:

    The crux of the algorithm is the selection of the pivot. The algorithm selects a pivot at random and moves all
     elements smaller than the pivot to the left of the pivot and all items larger than the pivot to the right. The
     algorithm then recursively calls quick sort on the items to the left and items to the right.

    The below algorithm arbitrarily selects the last item as the pivot

"""


def quick_sort_simple(arr):
    # Array is empty or has 1 item, it is by default sorted and can be returned
    if len(arr) < 2:
        return arr

    # Select the last element as the pivot
    pivot = arr[len(arr) - 1]

    return quick_sort_simple([i for i in arr if i < pivot]) + arr[pivot] + \
           quick_sort_simple([i for i in arr if i > pivot])


def quick_sort(arr):
    _quick_sort(arr, 0, len(arr) - 1)


def _quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        _quick_sort(arr, low, pivot_index - 1)
        _quick_sort(arr, pivot_index + 1, high)


# Array to be partitioned, index bounds for the partition
def partition(arr, low, high):
    """Take the last element as the pivot,
     and place that element in the correct sorted position by moving all smaller items to the left of the pivot
     and all larger items to the right of the pivot"""
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
    quick_sort(arr)
    print(arr)
