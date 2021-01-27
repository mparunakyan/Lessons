my_file = ""
try:
    my_file = open("task1.txt", "w", encoding="utf-8")
    while True:
        input_string = input("Enter strings. Empty will halt: ")
        if len(input_string) > 0:
            my_file.write(input_string + "\n")
        else:
            break
except IOError as error:
    print(f"An IOError has occurred! {error}")
finally:
    my_file.close()
