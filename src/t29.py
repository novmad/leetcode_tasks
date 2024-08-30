"""
https://leetcode.com/problems/divide-two-integers/
"""

import sys


class Solution(object):

    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend == 0 or divisor == 0:
            return 0
        
        k = -1 if ((dividend > 0) != (divisor > 0)) else 1
        
        if dividend == -2**31:
            if divisor == 1:
                return -2**31
            if divisor == -1:
                return 2**31 - 1
            
        if dividend == 2**31:
            if divisor == 1:
                return 2**31 - 1
            if divisor == -1:
                return -2**31
        
        dividend = abs(dividend)
        divisor = abs(divisor)

        result = 0
        p = 32
        y_max = divisor << p

        while dividend >= divisor:
            while y_max > dividend:
                y_max >>= 1
                p -= 1

            result += 1 << p
            dividend -= y_max

        return result if k > 0 else -result


if __name__ == '__main__':

    dividend = int(sys.argv[1])
    divisor = int(sys.argv[2])
    print(dividend, divisor)
    s = Solution()
    k = s.divide(dividend, divisor)
    print(k)
