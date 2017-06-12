class Solution(object):
    def __init__(self):
        self.solution = None

    def reverse(self, x):
        """
        :type x: int32
        :rtype: int32
        """
        if x == 0:
            return x

        isNegative = x < 0
        value = abs(x)
        digits = []
        while value >0:
            digits.append(value % 10)
            value = value / 10

        m = len(digits)
        digits = digits[::-1]
        reverse = 0
#        type(reverse) = int32

        for i in range(m):
            reverse +=  digits[i] * 10**i

        if isNegative:
            if reverse >2**31:
                print("Overflowed!")
                return 0
            else:
                return (-1)*reverse
        else: # input is positive
            if reverse > (2**31 -1):
                print('Overflowed')
                return 0
            else:
                return reverse



s = Solution()
s.solution = s.reverse(-2000000992)
#print(2**31)
print(s.solution)
