#read text file from current directory and split word inside.


with open('readfileword/test.txt','r') as file:
    for line in file:
        for word in line.split():
            print(len(word)
            print(word)



