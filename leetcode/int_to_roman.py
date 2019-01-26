def int_to_roman(num):
    numerals = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    result = ""
    for numeral, value in zip(numerals, values):
        div, mod, = divmod(num, value)
        result += numeral * div
        num = mod
    return result


if __name__ == '__main__':
    print(int_to_roman(1994))
