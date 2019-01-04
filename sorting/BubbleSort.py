"""

O(n^2)

"""


def bubble_sort(arr):
    # Number of passes equals number of elements (outer loop counts down)
    # Each pass bubbles the biggest element up
    for pass_number in range(len(arr)-1, 0, -1):
        # Iterate from start of array all the way up to last element sorted (biggest)
        for i in range(pass_number):
            # Compare each element with it's neighbor
            if arr[i] > arr[i+1]:
                # If neighbor is smaller, swap places
                arr[i], arr[i+1] = arr[i+1], arr[i]


if __name__ == '__main__':
    arr = [8, 3, 2, 1]
    bubble_sort(arr)
    print(arr)