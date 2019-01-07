"""

Given an array arr and a number n, return indices of the two numbers which add up to n

Assume there is only one possible solution

arr = [2, 7, 8, 6, 3, 10] n = 11
[8, 3]

"""


def two_sum(arr, n):
    complement_map = {}
    for index, number in enumerate(arr):
        complement = n - number

        if complement in complement_map:
            return [index, complement_map[complement]]
        complement_map[number] = index
    return []


if __name__ == '__main__':
    arr = [2, 2, 7, 8, 7, 4, 10]
    n = 4
    res = two_sum(arr, n)
    print(res)
