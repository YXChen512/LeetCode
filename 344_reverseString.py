# reverse string

def reverseString(s):

    length = len(s)

    reverse = ""
    while (length >0):
        reverse = reverse + s[length-1]
        length = length -1

    return reverse

print("What's the string you want to flip over?")
inputString = input('>')
print(reverseString(inputString))
