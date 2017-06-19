class Solution(object):
    def __init__(self):
        self.solution = None

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        paranthesisDict = { ')':'(',
                            ']':'[',
                            '}':'{'}
        for char in s:
            #print char
            if char in paranthesisDict.values():
                print('%s is a value' % char)
                stack.append(char)
            elif char in paranthesisDict.keys():
                print('%s is a key' % char)
                if stack == []:
                    return False
                if paranthesisDict[char] != stack.pop():
                    return False
            else:
                return False
        if stack !=[]:
            print len(stack)
        return stack == []


s = Solution()
s.solution = s.isValid('{[[()()()()][()][()]]}{[()()][]}')
print s.solution
