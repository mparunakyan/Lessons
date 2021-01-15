mynum = int(input("Input number: "))
sym = 0
while len(str(mynum)) > 1:
    mynum = mynum // 10
    if sym <= mynum % 10:
        sym = mynum % 10
print("Max number is: ", sym)