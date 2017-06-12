def TwoSum(Array,targetInt):
    # both Array and targetInt should exist
    if Array is None:
        print("Array do NOT exist!!")
        return None
    if targetInt is None:
        print("Target Integer do NOT exist!!")
        return None

    # the elements of Array and targetInt should all be integers
    if type(targetInt) is not int:
        print("Target is NOT an integer")
        return None
    isInt = [type(x) is int for x in Array]
    if sum(isInt)!=len(Array):
        print("Not all elements of the input Array are integers")
        return None

    # if targetInt is too large or too small
    if targetInt > 2*max(Array):
        print("No such pair: target integer too large")
        return None
    if targetInt < 2*min(Array):
        print("No such pair: target integer too small")
        return None

    # enumerate
    for i in range(0,len(Array)):
        for j in range(i+1,len(Array)):
            print("examining [%d,%d]..." % (i,j))
            if (Array[i] + Array[j]) == targetInt:
                return (i,j)

    # if a solution not found
    print("A pair not found")
    return None

a = [-1,-2,-3,-4,-5]
b = [1,2,3,4,5]
target = -6
#print(len(a))
print(TwoSum(a,target))
