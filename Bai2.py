numbers = range(1, 101)
result = []
for number in numbers:
    if number % 3 == 0 and number % 5 == 0:
        result.append("FizzBuzz")
    elif (number % 3 == 0):
        result.append("Buzz")
    elif (number % 5 == 0):
        result.append("Fizz")
    else:
        result.append(number)
print(result)

'''
[1, 2, 'Buzz', 4, 'Fizz', 'Buzz', 7, 8, 'Buzz', 'Fizz', 11, 'Buzz', 13, 14, 'FizzBuzz',
16, 17, 'Buzz', 19, 'Fizz', 'Buzz', 22, 23, 'Buzz', 'Fizz', 26, 'Buzz', 28, 29,
'FizzBuzz', 31, 32, 'Buzz', 34, 'Fizz', 'Buzz', 37, 38, 'Buzz', 'Fizz', 41, 'Buzz',
43, 44, 'FizzBuzz', 46, 47, 'Buzz', 49, 'Fizz', 'Buzz', 52, 53, 'Buzz', 'Fizz', 56,
'Buzz', 58, 59, 'FizzBuzz', 61, 62, 'Buzz', 64, 'Fizz', 'Buzz', 67, 68, 'Buzz', 'Fizz',
71, 'Buzz', 73, 74, 'FizzBuzz', 76, 77, 'Buzz', 79, 'Fizz', 'Buzz', 82, 83, 'Buzz',
'Fizz', 86, 'Buzz', 88, 89, 'FizzBuzz', 91, 92, 'Buzz', 94, 'Fizz', 'Buzz', 97, 98,
'Buzz', 'Fizz']
'''