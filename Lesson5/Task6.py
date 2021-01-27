def sum_function(element):
    new_str = element.replace('(пр)', '').replace('(лаб)', '').replace('(л)', '').replace('-', '0').split()
    name = new_str.pop(0).replace(":", "")
    # print(name)
    # print(sum(int(i) for i in new_str))
    new_dict = {name: sum(int(i) for i in new_str)}
    return new_dict


my_file = ""
my_dict = dict()
try:
    my_file = open("task6.txt", "r", encoding="utf-8")
    for el in my_file:
        my_str = sum_function(el)
        my_dict.update(my_str)
    print(my_dict)
except IOError as error:
    print(f"An IOError has occurred! {error}")
except ValueError as error:
    print(f"An ValueError has occurred! {error}")  # In case of salary will contain letters
finally:
    my_file.close()
