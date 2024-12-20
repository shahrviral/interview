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
    pass


def quick_sort(arr):
    pass


def _quick_sort(arr, low, high):
    pass


# Array to be partitioned, index bounds for the partition
def partition(arr, low, high):
    """Take the last element as the pivot,
     and place that element in the correct sorted position by moving all smaller items to the left of the pivot
     and all larger items to the right of the pivot"""
     pass


if __name__ == '__main__':
    arr = [8, 3, 1, 2, 5]
    quick_sort(arr)
    print(arr)
