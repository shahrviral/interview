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
    pass


if __name__ == '__main__':
    arr = [6, 3, 9, 6, 7, 2]
    selection_sort(arr)
    print(arr)
