def binary_search(arr, value):
    # If the input array is empty the array only has one element and that element
    # does not match the value return False
    if len(arr) == 0 or len(arr) == 1 and arr[0] != value:
        return False

    # Find the middle value of the array
    midpoint = arr[len(arr) // 2]

    if midpoint == value:
        return True
    # If the value is smaller than midpoint, send slice of array smaller than midpoint
    elif value < midpoint:
        return binary_search(arr[:len(arr) // 2], value)
    # If the value of the array is larger than the midpoint, send slice of arrays larger than midpoint
    else:
        # We need to add 1 to the slice start so it does not include midpoint
        return binary_search(arr[len(arr) // 2 + 1:], value)


if __name__ == '__main__':
    arr = [2, 5, 7, 19, 22, 38, 46, 59, 64, 73]
    print(binary_search(arr, 46))
    print(binary_search(arr, 74))
