import random
import math


#recive minimum and maximum number which is player want to guess
lower = int(input("Please Enter Lower Number :"))
higher = int(input("Please Enter Higher Number :"))


#found random number bettwin min and max
randnumber = random.randint(lower,higher)
# print("number is ", randnumber) #fot test


#get logaritm between min and max + 1 power 2
numbersug = round(math.log(higher - lower +1 ,2))
print(F"\n\t YOU HAVE ONLY {numbersug} CHANCE TO CHOOCE !")

#just a counter
count = 0

#
while count < numbersug:
    count +=1
    guess = int(input("Please Enter Guess Number :"))

#check validity of the guess number
    if randnumber == guess:
         print("Congratulations! your guess is Truly currect , you did it in ", count, " try")
         break
    elif randnumber > guess:
         print("you guessed too small")
    elif randnumber < guess:
         print("you guessed to high")
         
#for end project
if count >= math.log(higher - lower +1 , 2):
     print("\n\t The Number is :  " ,randnumber)
     print("\n\twish you good luck for the next time!!")
    