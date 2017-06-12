class Solution(object):
    def __init__(self):
        self.solution = None

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        romanNumerals = {
            'I':1,      'V':5,
            'X':10,     'L':50,
            'C':100,    'D':500,
            'M':1000}
        integer = 0
        for i in range(len(s)-1):
            if romanNumerals[s[i]] < romanNumerals[s[i+1]]:
                integer -= romanNumerals[s[i]]
            else:
                integer += romanNumerals[s[i]]

        return integer + romanNumerals[s[-1]]

s = Solution()
s.solution = s.romanToInt('XXXXXXX')
print(s.solution)
