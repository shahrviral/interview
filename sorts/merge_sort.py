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
    # If the list is empty or has only one item, it is already sorted, so we return
    if len(arr) < 2:
        return arr

    # Else we need to split the list, extra elements would go to the right
    middle = len(arr) // 2

    left = arr[:middle]

    right = arr[middle:]

    return merge(merge_sort(left), merge_sort(right))


def merge(left, right):
    # initialize indices to 0 abd result to empty list
    i = 0
    j = 0
    result = []

    while i < len(left) and j < len(right):
        # if item in left is smaller than item in right
        if left[i] < right[j]:
            # add left item to the result and increment i index so it will compare right with next left
            result.append(left[i])
            i += 1
        else:
            # add right item to the result and increment j index so it will compare left with next right
            result.append(right[j])
            j += 1

    # one list is bound to finish before the other so we need to add in the rest of the unprocessed list
    # we add everything after the last processed index of both lists sorted or not
    result += left[i:]
    result += right[j:]
    return result


if __name__ == '__main__':
    print(merge_sort([9, 7, 3, 10, 2, 7, 8]))
