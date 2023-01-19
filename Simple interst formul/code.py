#Simple interest formula is given by: 
# Simple Interest = (P x T x R)/100 Where, P is the principal amount T is 
# the time and R is the rate
##
##
# alireza atashnejad - Python


def simpleintrest(p,t,r):
    print("####################################")
    print("## Principal : {}                  ##".format(p))
    print("## Time      : {}                  ##".format(t))
    print("## Rate      : {}                  ##".format(r))
    
    result = (p * t * r) % 100 
    print("####################################")
    print ("## the simple intrest is : {}     ##".format(result))
    print("####################################")


p = int(input("Please enter Principal: "))
t = int(input("Please enter Time: "))
r = int(input("Please enter Rate: "))

simpleintrest(p,t,r)

