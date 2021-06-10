gnum = input("Enter a number from 0 - 15: ")
gvnString = input("Enter a string: ")

bval = bin(int(gnum)) 
binVal = bval[2:6]
strLen = len(gvnString)
binLen = len(binVal)


print("Strin Length = "+str(strLen))
print("Binary Length = "+str(binLen))