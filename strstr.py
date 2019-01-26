def strstr(haystack, needle):
    for i in range(0, len(haystack) - len(needle) + 1):
        temp = haystack[i: i + len(needle)]
        if temp == needle:
            return i
    return -1

if __name__ == '__main__':
    print(strstr('lll0', 'lll'))