month = int(input("Please input month: "))
season_list = ("Зима", "Весна", "Лето", "Осень")

# Вывод месяца словарём
month_list = {1:"Январь", 2:"Февраль", 3:"Март", 4:"Апрель", 5:"Май", 6:"Июнь",
              7:"Июль", 8:"Август", 9:"Сентябрь", 10: "Октябрь", 11: "Ноябрь", 12: "Декабрь"}
if not month_list.get(month):
    print("Ошибочный месяц")
    exit()
print("Месяц " + month_list.get(month))

# Реализация с помощью списка
if month in (12,1,2):
    print(season_list[0])
elif month in (3,4,5):
    print(season_list[1])
elif month in (6,7,8):
    print(season_list[2])
elif month in (9,10,11):
    print(season_list[3])