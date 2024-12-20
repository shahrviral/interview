"""

Time:
    Best: O(n)
    Average: O(n^2)
    Worst: O(n^2)

Space:
    Worst: O(1)

Stable:
    Yes

Worst Case Scenario:
    Reverse Sorted Array

Algorithm Overview:

    Pass over the list comparing each item with its neighbor to the right, if the item is larger than the neighbor,
     swap the neighbor and the current item.

    This effectively bubbles the largest item to the end of the list.

    You have to have n passes of the algorithm

    The inner loop though shrinks since after every pass the last sorted item will be in the correct position so we no
     longer have to compare new items with it

"""


def bubble_sort(arr):
    pass


if __name__ == '__main__':
    arr = [8, 3, 2, 1]
    bubble_sort(arr)
    print(arr)