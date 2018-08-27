"""
Determine whether or not a given string contains no duplicate characters.
"""

import sys


def is_unique(s):
    """ TIME: O(N) SPACE: O(1) """

    if len(s) > 128: return False

    charset = [False] * 128

    for c in s:
        if charset[ord(c) - ord('a')]:
            return False
        else:
            charset[ord(c) - ord('a')] = True

    return True


if __name__ == '__main__':
    print(is_unique(sys.argv[-1]))

