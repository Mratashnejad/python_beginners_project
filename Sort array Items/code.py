#how to sort items in string array , and retun is this array sorted or not ?
# 
# ## it has issue 
# 
# 
# 

def issorted (s):
     for i in range(1,len(s)):
        if s[i] < s[i-1]:
            return False
        return True


if __name__ == '__main__':
    s= input("enter your array :")
    issorted(s)
    print(issorted(s))
