from functools import reduce


# Calculations function for multiplication values from list
def calculate(first, second):
    return first * second


my_list = [i for i in range(100, 1002, 2)]  # Generating list with step 2
new_value = reduce(calculate, my_list)  # Call function
print(my_list)
print(new_value)
