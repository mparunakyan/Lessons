my_str = [21, 33, "dfd", 234, True, 34.3, "end"]
ind = 1
my_str_len = len(my_str)
while ind < my_str_len :
    my_str[ind], my_str[ind-1] = my_str[ind-1],my_str[ind]
    ind +=2
print(my_str)


