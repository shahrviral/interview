"""

Time:
    Best: O(nlogn)
    Average: O(nlogn)
    Worst: O(nlogn)

Space:
    Worst: O(n)


Stable:
    Yes

Worst Case Scenario:
    N/A

Algorithm Overview:

    Algorithm recursively divides the array in half until it has arrays of 1 item each. At which point in time,
     the merge function is called which iterates over 2 arrays and picks the smallest item from each array and adds it
     to a result array. The merge function's result is passed up the recursion chain as the parameter to the merge
     function for that execution.

"""


def merge_sort(arr):
    pass


def merge(left, right):
    pass


if __name__ == '__main__':
    print(merge_sort([9, 7, 3, 10, 2, 7, 8]))
