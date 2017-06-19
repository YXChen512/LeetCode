class Solution(object):
    def __init__(self):
        self.solution = None

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # recursive solution
        def addOneParanthesis(n,string,nL,nR,storageList):
            if len(string) == 2*n:
                storageList.append(string)
                return
            if nL < n:
                addOneParanthesis(n,string + '(', nL + 1, nR, storageList)
            if nR < nL:
                addOneParanthesis(n, string + ')', nL, nR + 1, storageList)

        possibleParathesis = []
        addOneParanthesis(n,'',0,0,possibleParathesis)
        return possibleParathesis

s = Solution()
s.solution = s.generateParenthesis(4)
print(s.solution)
