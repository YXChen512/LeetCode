class Solution(object):
    def __init__(self):
        self.solution = None
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits is None:
            return []
        if len(digits) == 0:
            return []
#        print(digits)
        digitToLetters = {
            '2':['a','b','c'], '3':['d','e','f'], '4':['g','h','i'],
            '5':['j','k','l'], '6':['m','n','o'], '7':['p','q','r','s'],
            '8':['t','u','v'], '9':['w','x','y','z']
        }

        combination = ['']
        i = 0
        while i<len(digits):
            combination = [x+y for x in combination for  y in digitToLetters[digits[i]]]
            i += 1

        return combination


s = Solution()
s.solution = s.letterCombinations('')
print(s.solution)
#print(len(s.solution))
