"""

Given an array arr and a number n, return indices of the two numbers which add up to n

Assume there is only one possible solution

arr = [2, 7, 8, 6, 3, 10] n = 11
[8, 3]

"""


def two_sum(nums, target):
    complement_map = {}
    for index, num in enumerate(nums):
        complement = target - num

        if complement in complement_map:
            return [index, complement_map[complement]]
        complement_map[num] = index
    return []


if __name__ == '__main__':
    print(two_sum([2, 211, 7, 6, 7, 4, 10], 8))
