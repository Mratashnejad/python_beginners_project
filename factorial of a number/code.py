#Python Program for factorial of a number
#
#
#
#Alireza Atashnejad - Python

def factorial(number):

    return 1 if (number == 0 or number ==1) else number * factorial(number -1)


number = int(input('Please Enter Number :'))
result = factorial(number)

print("Factorial Number is :",result)