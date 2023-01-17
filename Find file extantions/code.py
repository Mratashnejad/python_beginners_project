
def find_extention(text):
    dot = text.find('.')
    filename = text[:dot]
    fileextention = text[dot+1:]
    return filename , fileextention

if __name__ == '__main__':
    text = input("Please enter your file name Plus extention :")
    # find_extention(text)

    

    print(f"Your File Name is {0} , And your File extentions is : {1} ", find_extention(text))
