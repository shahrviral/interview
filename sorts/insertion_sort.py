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

    # Assume that the first element in the list is sorted, begin iteration at second element, index 1
    for current_index in range(1, len(arr)):
        # current item is the  not sorted item we want to put in the correct place in the sorted array
        # Everything to the left of this item is sorted, and this item and everything to the right is not sorted
        current_item = arr[current_index]
        # pointer to the index where the above item should go, initialized at the current item's current position
        insert_index = current_index
        # while your previous index does not go beyond the min index (0)
        # and the current item is smaller than the previous item
        while insert_index > 0 and current_item < arr[insert_index - 1]:
            # Copy the larger item before the current item to the current item's place
            arr[insert_index] = arr[insert_index - 1]
            # push your insert pointer back
            insert_index -= 1
            # Either your previous pointer will now be 0 in which case you have reached the start of the array
            # or you reached an item smaller than the current item
            # This exists the loop
        # Now you can move the current item to the empty space created by moving the other items forward
        # and begin the next pass of the sorting algorithm
        arr[insert_index] = current_item


if __name__ == '__main__':
    arr = [8, 3, 1, 2]
    insertion_sort(arr)
    print(arr)
