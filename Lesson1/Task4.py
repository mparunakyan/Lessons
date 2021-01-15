mynum = int(input("Input number: "))
sym = 0
while len(str(mynum)) > 1:
    if sym <= mynum % 10:
        sym = mynum % 10
    mynum = mynum // 10
    #print(mynum)
    #print(sym)
    #print(len(str(mynum)))
print("Max number is: ", sym)