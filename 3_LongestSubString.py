def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    ## Brutal force O(n^2) time complexity
    if s == '':
        return 0
    if len(s) == 1:
        return 1

    mask = [True for x in range(0,len(s))]
    length = 1
    while sum(mask):
        #print(mask)
        #print("l = %d" % length)
        index = 0
        while index < len(s):
            if (index + length) < len(s):
        #        print("check if \'%s\' is included in \'%s\'"
        #                    % (s[index+length],s[index:(index+length)]))
                if s[index+length] in s[index:(index+length)]:
        #            print("remove %d" % index)
                    mask[index] = False
            else:
        #        print("remove %d" % index)
                mask[index] = False
            index +=1
        length += 1
        #print(sum(mask))
    return length-1

print(lengthOfLongestSubstring(
'whata;slkdjf[weurz;xncvajfopawethpoasbfk]019487@#$E@#!@#!SADGASDFasdf;lkjqwertpoiuyzxcvbnm,./1234567890'))
