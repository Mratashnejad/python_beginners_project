
import datetime

class parrot():
    #class attribute :
    name = ""
    lastname = ""
    age = 0

#create object1 from parrot
parrot1 = parrot()
parrot1.name = input("Please enter your name : ")
parrot1.lastname = input("Please Enter your last name : ")
parrot1.age = int(input("Please enter your Age : "))

calcuteage = 0

def agecalcuter(s):
    year = datetime.date.today().year
    print ("we are in : " ,year)
    if s != 0:
        calcuteage = year - s
        return (calcuteage)
    


if __name__ == '__main__':
    age = parrot1.age
    total = agecalcuter(age)
#access attributes : 
    print(f"Dear {parrot1.name} {parrot1.lastname} , you born in  {total}")




