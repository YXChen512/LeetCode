def singleNumber(nums):
    sortedList = sorted(nums)
    length = len(nums)

    if length == 1:
        return nums[0]

    i = 0
    while (i<(length-1))&(sortedList[i]==sortedList[i+1]):
        i = i+2

    return sortedList[i]

print('What\'s the input array?')
inputArray = input('>')
inputArray
print("The single number is:%d" % singleNumber(inputArray))
