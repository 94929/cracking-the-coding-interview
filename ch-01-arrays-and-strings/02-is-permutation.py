"""
Determine whether or not one string is a permutation of another.
"""


import sys


def is_permutation(s1, s2):
    """ TIME: O(N), SPACE: O(1) """

    # assume that 1. lower chars only 2. no white spaces
    s1 = s1.lower().replace(' ', '')
    s2 = s2.lower().replace(' ', '')

    return sorted(s1) == sorted(s2)


if __name__ == '__main__':
    print(is_permutation(sys.argv[-2], sys.argv[-1]))

