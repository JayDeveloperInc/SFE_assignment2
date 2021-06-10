#Expanded Form

userIn = input("Enter an Integer: ")

def expanded_form(inpNum):
    inString = ""
    _inpNum = str(inpNum)
    

    for i in range(len(_inpNum)):
        n = len(_inpNum)
        if _inpNum[i] != "0":
            inString += (" "+_inpNum[i]+"0"*(n-i-1)+" +")
    inString = inString[:len(inString)-1]
    return inString


print(expanded_form(userIn))
