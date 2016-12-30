'''
Arrays and Strings: Pg. 90 - 1.2

checkPermutations: Given two strings, write a method to decide if one is a
                permutation of the other.

Out Loud: Ok, so the first thing that I think needs to be clarified is the
definition of permutation...Going to assume white space matters and it is
case sensitive. (see tests for examples).  Ok, so now that we clarified what
a permutation is: we also decided that permutations in my solution will be
case + white space sensitive.  With this in mind we kalso know that word_one
can only be a permutation of word_two if they are the same length and vice
versa.  I think one slower but elgant + space conservative method would be
just sorting the two words and then comparing.

Tests:
word_one | word_two
dog | god --> True
dog  | god --> False (White space)
dog | God --> False (capitalization)
'''


def check_permutation(word_one, word_two):
    if len(word_one) != len(word_two):  # O(a) + O(b) for len
        return False

    # At this point we know they are the same length and will use n
    sorted_word_one = sorted(word_one)  # O(n log(n)) sorting
    sorted_word_two = sorted(word_two)  # O(n log(n)) sorting

    if sorted_word_one == sorted_word_two:  # O(1) constant
        return True

    return False
    # Overall the run time for this would be O(n log(n)) and would be
    # space conservative


def check_permutation_fast(word_one, word_two):
    len_word_one = len(word_one)  # O(a) to get length
    len_word_two = len(word_two)  # O(b) to get length

    if len_word_one != len_word_two:  # O(1)
        return False

    # At this point we know they are the same length and will use n
    # We now need to check that each char shows up in both words.  This is
    # to prevent only checking word_one and getting a false positive in a
    # case like word_one = aann and word_two = anba
    for i in range(0, len_word_one):  # O(n)
        if word_one[i] not in word_two or word_two[i] not in word_one:  # O(1)
            return False

    return True
    # Overall big O is O(n)
