"""

Time:
    Best: O(n)
    Average: O(n^2)
    Worst: O(n^2)

Space:
    O(1)

Stable:
    Yes

Worst Case Scenario:
    Reverse Sorted Array

Algorithm Overview:

    This algorithm works like how a person would normally sort a hand of cards from left to right.
    You take the second card and compare with all the cards to the left, shifting over each card which is larger than
     the card you are trying to sort.

    The algorithm starts at the second element, and persists the element's index in a pointer. It then iterates over
     all the items to the left by moving the pointer back until either the index pointer is at 0 or it finds an element
     on the left hand side which is less than the current item. It then persists the element before that item.

"""


def insertion_sort(arr):
    pass


if __name__ == '__main__':
    arr = [8, 3, 1, 2]
    insertion_sort(arr)
    print(arr)
