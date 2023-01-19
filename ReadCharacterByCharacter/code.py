#open file with new way and split characters to each line
#
#
#
# Alireza Atashnejad - Python

file = open('ReadCharacterByCharacter/test.txt' , 'r')

while 1:
    char = file.read(1)
    if not char :
        break
    print(char)

file.close()
