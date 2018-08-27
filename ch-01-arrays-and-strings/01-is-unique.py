"""
Determine whether or not a given string contains no duplicate characters.
"""

import sys


def is_unique(s):
    """ TIME: O(N) SPACE: O(1) """

    charset = {}
    for c in s:
        if c in charset:
            return False
        charset[c] = True
    return True


if __name__ == '__main__':
    print(is_unique(sys.argv[-1]))

