"""

O(nlogn)

The algorithm divides the array in half log n times and the merges the result n times

"""


def merge_sort(arr):

    print(f'Sorting: {arr}')

    # If the list is empty or has only one item, return it
    if len(arr) < 2:
        return arr

    # Else we need to split the list, extra elements would go to the right
    middle = len(arr) // 2

    left = arr[:middle]

    right = arr[middle:]

    print(f'Left: {left} | Right: {right}')

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
    print(f'Result: {result}')
    return result


if __name__ == '__main__':
    print(merge_sort([9, 7, 3, 10, 2, 7, 8]))
