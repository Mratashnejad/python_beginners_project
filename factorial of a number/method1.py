#Python Program for factorial of a number with numpy 
#
#
#
#Alireza Atashnejad - Python


import numpy as np

number = int(input('Please Enter your number :'))
factorial = np.prod([i for i in range(1 , number+1)])

print("Factorial is :",factorial)