def fizzBuzz(n):
    answer = []
    for i in range(0,n,1):
        number = i+1
        print(i+1)
        if (number%3 == 0) & (number%5 == 0):
            answer.append("FizzBuzz")
        elif number%3 == 0:
            answer.append("Fizz")
        elif number%5 == 0:
            answer.append("Buzz")
        else:
            answer.append(str(number))
        print('\n')
    return answer

print('What\'s the number to exam\n')
num = input('>')
for someString in fizzBuzz(num):
    print(someString)
#    print('\n')
