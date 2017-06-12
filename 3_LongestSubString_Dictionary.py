def lengthOfLongestSubstring(s):
    """
    Input string s
    Output length of its longest substring
    Make use of Python dictionary
    """
    usedChar = {} # dictionary of <charactor:last position> pairs
    maxlength =0
    start = 0
    for i in range(len(s)):
        print("checking %dth character: %s" % (i,s[i]))
        print("start position at %d, which is a \'%s\'" % (start,s[start]))
        if s[i] in usedChar and start <=usedChar[s[i]]:
            print("a repeating found! and Move start:%d to the new position: %d" % (start,usedChar[s[i]]+1))
            start = usedChar[s[i]]+1 #position index where s[i] appeared last time
        else:
            maxlength = max(maxlength,i - start + 1)
            print("max length is %d" % maxlength)
        usedChar[s[i]]=i

    return maxlength

text = 'abcdefgagc'
print(lengthOfLongestSubstring(text))
