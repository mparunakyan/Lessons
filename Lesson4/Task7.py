def factorial(num):
    f_factor = 1
    for i in range(1, num):
        f_factor = i * f_factor
        print(f"!{i} = ", end=" ")
        yield f_factor


try:
    my_number = int(input(f"Please enter iteration number: "))
    for i in factorial(my_number+1):
        print(i)

except ValueError as error:
    print(f"Error number or char entered with code {error}")
