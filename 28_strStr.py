class Solution(object):
    def __init__(self):
        self.solution = None

    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # Use pytho dictionary
        if haystack == '' and needle == '':
            return 0
        elif needle == '':
            return 0
        elif haystack == '':
            return -1
        if len(needle) > len(haystack):
            return -1
        alphabet = {}
        for index in xrange(len(haystack)):
            if haystack[index] in alphabet.keys():
                alphabet[haystack[index]].append(index)
            else:
                alphabet[haystack[index]] = []
                alphabet[haystack[index]].append(index)
        for key in alphabet.keys():
            print("<%s,%r>" % (key, alphabet[key]))

        # Use needle[0] to search in the dictionary
        if needle[0] not in alphabet.keys():
            return -1
        for start in alphabet[needle[0]]:
            compare = True
            for i in xrange(len(needle)):
                if i+start >= len(haystack) or needle[i] != haystack[start + i]:
                    compare = False
                    break
            if compare:
                return start

        return -1

hay = 'Well, the problem does not aim for an advanced algorithm like KMP but only a clean brute-force algorithm. So we can traverse all the possible starting points of'
needle = 'algorithm'
print(needle[0])
s = Solution()
s.solution = s.strStr(hay,needle)
print(s.solution)
