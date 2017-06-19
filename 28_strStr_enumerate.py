class Solution(object):
    def __init__(self):
        self.solution = None

    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if haystack == '' and needle == '':
            return 0
        elif needle == '':
            return 0
        elif haystack == '':
            return -1
        if len(needle) > len(haystack):
            return -1

        for i in xrange(len(haystack)-len(needle)+1):
            print("in outer loop: %d" % i)
            for j in xrange(len(needle)):
                print("in inner loop: %d" % j)
                if needle[j]!=haystack[i+j]:
                    break
                if j == len(needle)-1 and needle[j]==haystack[i+j]:
                    return i
        return -1


hay = '3'
needle = 'a'
#print(needle[0])
s = Solution()
s.solution = s.strStr(hay,needle)
print(s.solution)
