from random import randint

read_file = ""
write_file = ""
ind = 0
try:
    entries_number = int(input("Please enter number of values to generate: "))
    write_file = open("task5.txt", "w", encoding="utf-8")
    for _ in range(entries_number):
        print(str(randint(0,100)), end=" ", file=write_file)
    write_file.close()
    read_file = open("task5.txt", "r", encoding="utf-8")
    my_string = read_file.readlines()[0].split()
    my_num = [float(i) for i in my_string]
    print(f"The sequence is {my_num}")
    print(f"Total sum of list is {sum(my_num)}")
except IOError as error:
    print(f"An IOError has occurred! {error}")
except ValueError as error:
    print(f"An ValueError has occurred! {error}")
finally:
    write_file.close()
