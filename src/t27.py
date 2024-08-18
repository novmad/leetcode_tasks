"""
https://leetcode.com/problems/remove-element/description/
"""

import sys


class Solution(object):

    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        while val in nums:
            nums.pop(nums.index(val))

        print(nums)
        return len(nums)


if __name__ == '__main__':

    nums = eval(sys.argv[1])
    val = eval(sys.argv[2])
    print(nums, val)
    s = Solution()
    k = s.removeElement(nums, val)
