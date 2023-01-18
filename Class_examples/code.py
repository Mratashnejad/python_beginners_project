
import datetime

class parrot():
    #class attribute :
    name = ""
    lastname = ""
    age = 0
    year = 0
    month = 0
    day = 0

#create object1 from parrot
parrot1 = parrot()
parrot1.name = input("Please enter your name : ")
parrot1.lastname = input("Please Enter your last name : ")
parrot1.year = int(input("Please enter your year : "))
parrot1.month = int(input("Please enter your month : "))
parrot1.day =int(input("Please enter your day : "))

calcuteage = 0

def agecalcuter(y,m,d):
    year = datetime.date.today().year
    month = datetime.date.today().month
    day = datetime.date.today().day
    print ("we are in : " ,year,month,day)
    if y != 0 and m !=0 and d !=0:
        calcuteyear = year - y
        calcutemonth = m - month
        calcuteday = day - d
        return (calcuteyear , calcutemonth ,calcuteday)
    

if __name__ == '__main__':
    y = parrot1.year
    m = parrot1.month
    d = parrot1.day 
    total = agecalcuter(y,m,d)
#access attributes : 
    print(f"Dear {parrot1.name} {parrot1.lastname} , you born in  {total}")




