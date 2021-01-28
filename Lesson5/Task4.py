read_file = ""
write_file = ""
str_writer = ""
my_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
try:
    read_file = open("task41.txt", "r", encoding="utf-8")
    write_file = open("task42.txt", "w", encoding="utf-8")
    for el in read_file:
        print(el.replace(el.split()[0], my_dict.get(el.split()[0])), end="", file=write_file)
except IOError as error:
    print(f"An IOError has occurred! {error}")
finally:
    read_file.close()
    write_file.close()
