def length_of_longest_substringi(string):
    if not string:
        return 0

    char_map = {}

    start = 0
    max_sub = 0

    for i, c in enumerate(string):
        if c in char_map:
            start = max(start, char_map[c] + 1)
        else:
            start = max(start, 0)
        # start = max(start, char_map[c] + 1 if c in char_map else 0)
        max_sub = max(max_sub, i - start + 1)
        char_map[c] = i
    return max_sub


def length_of_longest_substring_set(string):
    s_set = set()

    max_sub = 0
    i = 0
    j = 0
    # i and j make a sliding window, start at an i and try to add each new char (j pointer)
    while i < len(string) and j < len(string):
        # if j has not been seen so far, add the char at j and increment j pointer,
        # update max to the max of current max and length of string from i to j since you added j
        if string[j] not in s_set:
            s_set.add(string[j])
            j += 1
            max_sub = max(max_sub, j - i)
        # If the char at j has been seen, you need to increment the i pointer (start of substring)
        # and remove the char from the string located at i
        else:
            s_set.remove(string[i])
            i += 1


def length_of_longest_substring(string):
    c_map = {}

    max_sub = 0
    i = 0
    j = 0
    # i and j make a sliding window, start at an i and try to add each new char (j pointer)
    while j < len(string):
        # if j has not been seen so far, add the char at j and increment j pointer,
        # update max to the max of current max and length of string from i to j since you added j
        if string[j] in c_map:
            i = max(c_map[string[j]], i)

        max_sub = max(max_sub, j - i + 1)
        c_map[string[j]] = j + 1
        j += 1
    return max_sub


if __name__ == '__main__':
    # print(length_of_longest_substring('abcabcabc'))
    # print(length_of_longest_substring('bbbbb'))
    print(length_of_longest_substring('pwwkew'))
