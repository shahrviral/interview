# Find if 2 strings are anagrams


# Assume strings are all lowercase and are made up of 26 letters of alphabet

def is_anagram_n(s1, s2):
    '''
    Find if 2  strings are anagrams of each other in O(n) time complexity
    :param s1: string containing lowercase letters of the 26 letter alphabet (a-z)
    :param s2: string containing lowercase letters of the 26 letter alphabet (a-z)
    :return: boolean telling if strings are anagrams of each other
    '''
    charArray1 = [0] * 26 # Array of 0 for each unique letter in alphabet
    charArray2 = [0] * 26


    # Count occurrence of each char and update the count in the respective charArray for each string

    for i in range(len(s1)): # iterate over the string indices

        pos = ord(s1[i]) - ord('a') # find index in char array of characters

        # This works because whatever the ord of the char is if I subtract the ord of 'a'
        # then it will return a number between 0 and 26

        charArray1[pos] += 1

    for i in range(len(s2)):
        pos = ord(s2[i]) - ord('a')
        charArray2[pos] += 1

    # Iterate over both charArrays to see if counts of each letter are the same

    index = 0  # Counter from 0 to 26
    still_valid = True # Flag to see if strings are still an anagram

    # while index < 26 and still_valid:
    #     if charArray1[index] == charArray2[index]:
    #         index += 1
    #     else:
    #         still_valid = False

    for charArray1L, charArray2L in zip(charArray1, charArray2):
        if charArray1L != charArray2L:
            still_valid = False
            break
    return still_valid


def is_anagram_nlogn(s1, s2):
    '''
    Find if 2 strings are anagrams of each other in O(nlogn) time complexity
    :param s1: string containing lowercase letters of the 26 letter alphabet (a-z)
    :param s2: string containing lowercase letters of the 26 letter alphabet (a-z)
    :return: boolean telling if strings are anagrams of each other
    '''

    charArray1 = list(s1)
    charArray2 = list(s2)

    # nlogn sorting
    charArray1.sort()
    charArray2.sort()

    still_valid = True

    for c1, c2 in zip(charArray1, charArray2):
        if c1 != c2:
            still_valid = False
            break
    return still_valid



if __name__ == '__main__':
    print(is_anagram_n("apple", "paple"))
    print(is_anagram_n("orange", "apple"))

    print(is_anagram_nlogn("apple", "paple"))
    print(is_anagram_nlogn("orange", "apple"))
