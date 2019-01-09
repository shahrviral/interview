

def length_of_longest_substring(string):

    if not string:
        return 0

    char_map = {}

    start = 0
    max_sub = 0

    for i, c in enumerate(string):
        start = max(start, char_map[c] + 1 if c in char_map else 0)
        max_sub = max(max_sub, i - start + 1)
        char_map[c] = i
    return max_sub


if __name__ == '__main__':
    print(length_of_longest_substring('abcabcabc'))
    print(length_of_longest_substring('bbbbb'))
    print(length_of_longest_substring('pwwkew'))