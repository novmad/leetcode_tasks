"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
"""

import sys

class Solution(object):

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0

        while i < len(nums):
            if nums[i] in nums[:i]:
                nums.pop(i)
                i -= 1
            else:
                i += 1

        print(nums)
        return len(nums)


if __name__ == '__main__':

    nums = eval(sys.argv[1])
    print(nums)
    s = Solution()
    k = s.removeDuplicates(nums)
