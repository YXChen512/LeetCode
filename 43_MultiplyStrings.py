class Solution(object):
    def __init__(self):
        self.solution = None

    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == '' or num2== '':
            return None
        if num1 == '0' or num2== '0':
            return '0'
        if num1 == '1':
            return num2
        if num2 == '1':
            return num1

        if len(num1)>=len(num2):
            Long,Short = num1,num2
        else:
            Long,Short = num2,num1

        return strMultiReversed(Short,Long)[::-1]

def strMultiReversed(Short,Long):
    '''
    type rShort: str
    type rLong: str
    rtype: str
    rShort rLong represent non-negative integers where their digits are in reversed order
    the length of rShort is smaller than that of rLong
    '''
    #Product = '0'
    if len(Short) == 1:
        rLong = Long[::-1]
        product = ''
        carry = 0
        index = 0
        for j in xrange(len(Long)):
            intProduct = int(Short)*int(rLong[j]) + carry
            product = product + str(intProduct % 10)
            carry = intProduct / 10
        if carry:
            product = product + str(carry)
        return product

    else:
        product = '0'
        rShort = Short[::-1]
        i= 0
        while i< len(rShort):
            digitProduct = strMultiReversed(rShort[i],Long)
            if i>0:
                shift = i;
                while shift:
                    digitProduct = '0'+digitProduct
                    shift -=1
            product = strAddReversed(product,digitProduct)
            i += 1
        return product

def strAddReversed(rnum1,rnum2):
    '''
    rnum1 is the reversed string of num1, same for num2
    return also the reversed order string
    '''
    Longer = max(len(rnum1),len(rnum2))
    i = 0
    carry = 0
    addition = ''
    while i< Longer or carry:
        if i < len(rnum1):
            digit1 = int(rnum1[i])
        else:
            digit1 = 0
        if i < len(rnum2):
            digit2 = int(rnum2[i])
        else:
            digit2 = 0
        intAdd = digit1 + digit2 + carry
        addition = addition + str(intAdd % 10)
        carry = intAdd / 10
        i += 1
    return addition

print(strAddReversed('2','15'))
s = Solution()
s.solution = s.multiply('21','401')
print(s.solution)
