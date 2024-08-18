"""
https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
"""

import sys
import re


class Solution(object):

    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        r = re.search(needle, haystack)
        if r:
            return r.start()
        else:
            return -1


if __name__ == '__main__':

    haystack = sys.argv[1]
    needle = sys.argv[2]
    print(haystack, needle)
    s = Solution()
    k = s.strStr(haystack, needle)
    print(k)