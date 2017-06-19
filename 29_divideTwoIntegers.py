class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor == 0:
            return sys.maxint
        if dividend == 0:
            return 0

        if (dividend>0 and divisor >0) or (dividend <0 and divisor <0):
            sign = 1
            print("positive answer")
        else:
            print("negative answer")
            sign = 0

        result = 0
        absDividend, absDivisor= abs(dividend), abs(divisor)
        if absDivisor == 1:
            result = absDividend
        else:
            remainder = absDividend
            while remainder >= absDivisor:
                remainder -= absDivisor
                result +=1
        if sign:
            if result< 2**31-1:
                return result
            else:
                return 2**31-1
        else:
            if result>-2**31:
                return -result
            else:
                return -2**31

s = Solution()
s.solution = s.divide(-1,1)
print(s.solution)
