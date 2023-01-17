

def palindromic(text):
    n = len(text)
    for i in range(n//2):
        if text[i] != text[n-1-i]:
            return False

    return True


    

if __name__ == '__main__':
    text = input("Please enter your text :")
    print(palindromic(text))

