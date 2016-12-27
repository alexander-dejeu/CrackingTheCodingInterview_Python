"""
Is Unique: Implement an algorithm to determine if a string has all unique
        characters.  What if you cannot use additional data structures?

Tests:  '' -> True
        'a' -> True
        'ab' -> True
        'Aa' -> True
        'a!!b' -> False
        '  ' -> False
        'abcdcba' -> False

Outloud: Yeah so one way we could brute force would be itterate over each char
and then see if it comes up?  This would be a double for loop, but mad slow
O(n^2).  But one quick fix to speed it up would be by having the outer loop
go from 0 to n (with an index var) and then the inner loop go from index + 1 to
n.

But lets try to do this a bit faster by using a dict()
"""


def is_unique(word):
    # Solution using a set for an optimal time complexity but high space
    # Used a set instead of dict because no need to store a key value pair
    # when we just need to track keys
    seen_chars = set()
    for c in word:  # O(n) have to go over every char
        if c in seen_chars:  # O(1) constant to look up
            return False
        seen_chars.add(c)
    return True
    # Overal time complexity : O(n)


def is_unique_nds_v1(word):
    # Brute force solution - first attempt for no data structures
    length = len(word)
    for i in xrange(0, length - 1):
        for j in xrange(i + 1, length):
            if word[i] == word[j]:
                return False
    return True
    # BigO: O(n^2) -  some stuff see written example


def is_unique_nds_v2(word):
    # Solution that sorts and then compares
    sorted_str = sorted(word)  # O(n log(n))
    # Sorting will destory the input so check with interviewer if it is ok
    for index in xrange(0, len(sorted_str)-1):  # O(n)
        if sorted_str[index] == sorted_str[index+1]:
            return False
    return True
    # BigO: O(nlog(n))


# print is_unique('')
# print is_unique_nds_v1('')
# print is_unique_nds_v2('')
#
# print is_unique('a')
# print is_unique_nds_v1('a')
# print is_unique_nds_v2('a')
#
# print is_unique('Aa')
# print is_unique_nds_v1('Aa')
# print is_unique_nds_v2('Aa')
#
# print is_unique('aba')
# print is_unique_nds_v1('aba')
# print is_unique_nds_v2('aba')
