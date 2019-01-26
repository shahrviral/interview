def roman_to_int(romanstr):
    # numerals = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    # values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    d = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}

    res = 0
    p = 'I'
    for c in romanstr[::-1]:
        if d[c] < d[p]:
            res -= d[c]
        else:
            res += d[c]
        p = c
    return res


if __name__ == '__main__':
    print(roman_to_int("MCMXCIV"))