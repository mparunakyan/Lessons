import json


dict_companies = dict()
aver_sum = 0
diviation_value = 0
my_list = ""
ind = 0
main_dict = list()
try:
    my_file = open("task7.txt", "r", encoding="utf-8")
    for el in my_file:
        # print(el.split())
        my_list = el.split()
        diviation_value = float(my_list[2]) - float(my_list[3])
        if diviation_value > 0:
            aver_sum += diviation_value
            ind += 1
        # print(my_list[0], diviation_value)
        dict_companies.update({my_list[0]: round(diviation_value, 2)})
    main_dict.append(dict_companies)
    main_dict.append({"average_profit" : (aver_sum/ind)})
    print(main_dict)
    with open("task7.json", "w", encoding="utf-8") as write_file:
        json.dump(main_dict, write_file, ensure_ascii=False, indent=4 )

except IOError as error:
    print(f"An IOError has occurred! {error}")
except ValueError as error:
    print(f"An ValueError has occurred! {error}")  # In case of salary will contain letters
finally:
    my_file.close()