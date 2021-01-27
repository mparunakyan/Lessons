my_file = ""
ind = ""
try:
    my_file = open("task2.txt", "r", encoding="utf-8")
    for ind, el in enumerate(my_file):
        print(f"{el.strip()} (word count is: {len(el.split())})")
    print(10 * "*")
    print(f"Total lines number is {ind + 1}")
except IOError as error:
    print(f"An IOError has occurred! {error}")
finally:
    my_file.close()
