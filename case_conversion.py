gnum = input("Enter a number from 0 - 15: ")
inpLine = input("Enter a string: ")


def swap(inpLine, gnum):
    gvnString = str(inpLine)
    bval = bin(int(gnum)) 
    binVal = bval[2:6]
    strLen = len(gvnString)
    binLen = len(binVal)
    numArr = []
    numArr = [0 for i in range(strLen)]

    binIndex = 0
    overflow = False
    for i in range(strLen):
        if binIndex < 3:
            if overflow == False:
                binIndex = i 
            else:
                binIndex+=1 
        else:
            binIndex=0
            overflow = True
        numArr[i] = binVal[binIndex]
        if numArr[i] == "1":
            if gvnString[i].isupper():
                gvnString = gvnString.replace(gvnString[i], gvnString[i].lower(), 1)
            else:
                gvnString = gvnString.replace(gvnString[i], gvnString[i].upper(), 1)
    return gvnString    

    
print("New string: "+ swap(inpLine, gnum))
