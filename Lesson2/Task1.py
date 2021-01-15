my_list = ["comma", False, 5465, 434.3, (1,2)]

for i in my_list: #
    if type(i) == float:
        print(f"{i} is float")
    elif type(i) == int:
        print(f"{i} is int")
    elif type(i) == str:
        print(f"{i} is str")
    elif type(i) == str:
        print(f"{i} is list")
    elif type(i) == dict:
        print(f"{i} is dict")
    elif type(i) == tuple:
        print(f"{i} is tuple")
