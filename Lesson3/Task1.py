def divider (arg1, arg2):
    try:
        print(f"Result is {arg1/arg2}")
    except ZeroDivisionError as error:
        print(f"Деление на ноль - {error}")
try:
    a = int(input("Введите делимое: "))
    b = int(input("Введите делитель: "))
except ValueError as error:
    print(f"Введен не числовой аргумент - {error}")
    exit()
divider(a,b)