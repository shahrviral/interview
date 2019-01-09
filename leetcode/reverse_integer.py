def reverse_integer(x):
    negate = x < 0
    temp = abs(x)
    reversed = 0
    while temp != 0:
        reversed = reversed * 10 + temp % 10
        temp //= 10
    if reversed > 2 ** 31 - 1:
        return 0
    return reversed if not negate else -reversed


if __name__ == '__main__':
    print(reverse_integer(-123))
