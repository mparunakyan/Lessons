my_file = ""
ind = 1
sum_average = 0
try:
    my_file = open("task3.txt", "r", encoding="utf-8")
    for el in my_file:
        if float(el.split()[1]) > 20000:  # Check for income more than 20k
            print(el, end="")
        sum_average += float(el.split()[1])  # Collects average of salary of all employees
        ind += 1
    print(f"\n\nAverage salary is: {round(sum_average / ind, 2)}")
except IOError as error:
    print(f"An IOError has occurred! {error}")
except ValueError as error:
    print(f"An ValueError has occurred in convert to float ! {error}")  # In case of salary will contain letters
finally:
    my_file.close()
